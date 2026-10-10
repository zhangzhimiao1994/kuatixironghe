#!/usr/bin/env python3
"""形势取数器：把一个地点变成一份「形势描述」交给相地类 skill 判读。

用法（包根目录）：
    python tools/xingshi.py --place 婺源县江湾镇
    python tools/xingshi.py --lat 28.4546 --lon 117.9686 --radius 3 --out xingshi.json

它做什么：地名→经纬度 → 抓 DEM 瓦片(30m 级) → 算高差/坡度/坡向/脊谷/八向遮护 →
查 OSM 水系 → 输出①一段中文形势描述 ②一份取数日志 ③明确的「（补充）」标注。

它**不做什么**：不下吉凶断语、不点穴、不给葬法、不替代现场踏勘。
把地理量翻成书里术语（干枝、过峡、水口、明堂）的那几步是**现代补充**，不是原书原文，
输出里逐条标了「（补充）」，判读必须回到 skill 的 R 节原文。

依赖：Pillow、numpy（见 requirements.txt）。联网走公开只读接口：
    photon.komoot.io（地名）、elevation-tiles-prod.s3.amazonaws.com（地形）、
    overpass.osm.ch（水系）。
"""
import argparse, json, math, os, sys, time, urllib.parse, urllib.request
from datetime import datetime, timezone

UA = {"User-Agent": "cross-system-kanyu/1.0 (research; contact: local)"}
TILE_URL = "https://elevation-tiles-prod.s3.amazonaws.com/terrarium/{z}/{x}/{y}.png"
# 2026-10-08 实测（西湖 1km，retry 2 次）：z.overpass-api.de ✓、maps.mail.ru ✓（需重试）、
# overpass-api.de / lz4.overpass-api.de 常返回「too busy」（实例可用但忙，要重试）、
# kumi / private.coffee 500、openstreetmap.fr 403、osm.jp / rambler / openstreetmap.ru 超时。
# **overpass.osm.ch 是坏实例**：HTTP 200，但数据时间戳为 "117583"（非法）、对任何地点都返回 0——
# 必须靠时间戳校验挡掉，光看状态码会误判成"通"。
OVERPASS_URLS = [
    "https://z.overpass-api.de/api/interpreter",
    "https://lz4.overpass-api.de/api/interpreter",
    "https://overpass-api.de/api/interpreter",
    "https://maps.mail.ru/osm/tools/overpass/api/interpreter",
    "https://overpass.kumi.systems/api/interpreter",
    "https://overpass.private.coffee/api/interpreter",
    "https://overpass.osm.ch/api/interpreter",   # 坏实例；靠时间戳校验挡
]
PHOTON_URL = "https://photon.komoot.io/api/"

# 本包取数源一律吃 WGS-84；从百度/高德抄来的坐标要先转（见 tools/crs.py）
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crs import to_wgs84, offset_meters, CRS_ALIAS  # noqa: E402

BEARINGS = [("北", 0), ("东北", 45), ("东", 90), ("东南", 135),
            ("南", 180), ("西南", 225), ("西", 270), ("西北", 315)]

# 本工具实际要用的数据源（名字与 tools/install_deps.py 的 DATA_SOURCES 一致）
NEEDED_SOURCES = ["terrain_terrarium", "geocode_photon", "water_overpass"]


def _load_source_registry():
    """复用 tools/install_deps.py 里的数据源登记表，避免两处各写一份。"""
    import importlib.util
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "install_deps.py")
    spec = importlib.util.spec_from_file_location("_pkg_install_deps", p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def preflight(verbose=True):
    """跑数据前的依赖体检：**先查再跑**，缺什么就停，不许跑到一半才发现。

    返回 (ok, 明细列表)。每项 (源名, 标签, 是否可用, 说明)。
    """
    try:
        mod = _load_source_registry()
    except Exception as e:                                    # noqa: BLE001
        return False, [("install_deps", "依赖登记表", False, "读不到 tools/install_deps.py：%s" % e)]
    rows = []
    for nm in NEEDED_SOURCES:
        if nm not in getattr(mod, "DATA_SOURCES", {}):
            rows.append((nm, nm, False, "未登记的数据源名（先在 install_deps.py 的 DATA_SOURCES 里登记）"))
            continue
        label = mod.DATA_SOURCES[nm]["label"]
        ok, why = mod.probe_data_source(nm)
        rows.append((nm, label, ok, why))
        if verbose:
            print("  %s %s：%s" % ("✓" if ok else "✗", label, why))
    # 离线河网是本地文件、不联网：缺了不拦（只是水系少一层兜底），但要说清
    if verbose:
        if os.path.exists(HYDRO_SHAPEFILE):
            print("  ✓ 离线河网 HydroRIVERS（本地）：已就位（乡野水系缺漏时可兜底）")
        else:
            print("  ! 离线河网 HydroRIVERS（本地）：未下载——水系只剩 OSM 一层，"
                  "乡野缺漏会更明显（下载说明见 docs/形势取数与映射表.md）")
    return all(r[2] for r in rows), rows


def get(url, data=None, timeout=45, tries=3):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, data=data, headers=UA)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except Exception as e:                     # noqa: BLE001
            last = e
            time.sleep(1.5 * (i + 1))
    raise RuntimeError("取数失败 %s：%s" % (url.split("?")[0], last))


def geocode_place(place, limit=5):
    """返回候选列表 [{'lat','lon','name','type'}...]，按相关度排序。

    注意两点（都实测过）：① photon 不认 lang 参数，带上会 400；② **同名地名会被解错**——
    查「杭州西湖」会先命中台湾高雄的「杭州西湖」。所以这里多取几个候选、把候选原样打出来
    让调用者核对，而不是默默取第一个。
    """
    q = urllib.parse.urlencode({"q": place, "limit": limit})
    d = json.loads(get(PHOTON_URL + "?" + q))
    out = []
    for f in d.get("features", []):
        p = f.get("properties", {})
        loc = f["geometry"]["coordinates"][:2]
        nm = " ".join(x for x in [p.get("country"), p.get("state"), p.get("city"),
                                  p.get("district"), p.get("name")] if x)
        out.append({"lat": loc[1], "lon": loc[0], "name": nm or place,
                    "type": p.get("type", ""), "osm_value": p.get("osm_value", "")})
    if not out:
        raise RuntimeError("地名没解析出来：%s（换个写法，或直接给 --lat/--lon）" % place)
    return out


# ---------- DEM（Terrarium PNG） ----------
def lonlat_to_tile(lon, lat, z):
    n = 2 ** z
    x = (lon + 180.0) / 360.0 * n
    y = (1.0 - math.asinh(math.tan(math.radians(lat))) / math.pi) / 2.0 * n
    return x, y


def fetch_dem(lat, lon, z, span):
    """span=半宽（瓦片数）：取 (2*span+1)^2 张瓦片拼成高程网格。"""
    import numpy as np
    from PIL import Image
    import io
    fx, fy = lonlat_to_tile(lon, lat, z)
    x0, y0 = int(fx), int(fy)
    rows = []
    tiles = []
    for ty in range(y0 - span, y0 + span + 1):
        row = []
        for tx in range(x0 - span, x0 + span + 1):
            raw = get(TILE_URL.format(z=z, x=tx, y=ty), timeout=60)
            im = Image.open(io.BytesIO(raw)).convert("RGB")
            a = np.asarray(im).astype(np.float32)
            h = (a[:, :, 0] * 256.0 + a[:, :, 1] + a[:, :, 2] / 256.0) - 32768.0
            row.append(h)
            tiles.append({"z": z, "x": tx, "y": ty, "bytes": len(raw)})
        rows.append(np.concatenate(row, axis=1))
    grid = np.concatenate(rows, axis=0)
    # 中心点在这块网格里的像素坐标
    px = (fx - (x0 - span)) * 256.0
    py = (fy - (y0 - span)) * 256.0
    return grid, (px, py), tiles, z


def mpp(z, lat):
    """每像素地面米数（近似）。"""
    return (2 * math.pi * 6378137.0 / (256 * 2 ** z)) * math.cos(math.radians(lat))


# ---------- 水系 ----------
def fetch_water(lat, lon, radius_m):
    # 轻查询 + 多镜像留痕：nwr 一条覆盖 node/way/relation；round 取 100m 降负载
    q = ("[out:json][timeout:25];("
         'nwr(around:%d,%f,%f)["waterway"];'
         'nwr(around:%d,%f,%f)["natural"="water"];'
         ");out center tags;" % (radius_m, lat, lon, radius_m, lat, lon))
    body = urllib.parse.urlencode({"data": q}).encode()
    errs = []
    for url in OVERPASS_URLS:
        for attempt in (1, 2):
            try:
                raw = get(url, data=body, timeout=75, tries=1)
                if b"too busy" in raw[:2000] or b"<strong" in raw[:2000]:
                    errs.append("%s 忙（第 %d 次）" % (url.split("/")[2], attempt))
                    time.sleep(2)
                    continue
                d = json.loads(raw)
                # 数据时间戳合法性校验：坏实例会返回 "117583" 这种非法值并对一切地点返回空
                ts = d.get("osm3s", {}).get("timestamp_osm_base", "")
                if not (len(ts) >= 10 and ts[4] == "-" and ts[:4].isdigit() and int(ts[:4]) >= 2020):
                    errs.append("%s 数据时间戳不可信：%r" % (url.split("/")[2], ts))
                    break
                items = []
                for e in d.get("elements", []):
                    c = e.get("center") or {"lat": e.get("lat"), "lon": e.get("lon")}
                    if not c.get("lat"):
                        continue
                    tags = e.get("tags", {})
                    items.append({"kind": tags.get("waterway") or tags.get("natural") or "water",
                                  "name": tags.get("name", ""), "lat": c["lat"], "lon": c["lon"]})
                return items, {"source": url.split("/")[2], "timestamp": ts}
            except Exception as e:                            # noqa: BLE001
                errs.append("%s: %s" % (url.split("/")[2], str(e)[:50]))
                break
    raise RuntimeError("水系接口都不可用（换时间再试）：" + "；".join(errs))


def haversine_bearing(lat1, lon1, lat2, lon2):
    R = 6371000.0
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dp, dl = p2 - p1, math.radians(lon2 - lon1)
    a = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    d = 2 * R * math.asin(math.sqrt(a))
    br = (math.degrees(math.atan2(math.sin(dl) * math.cos(p2),
                                  math.cos(p1) * math.sin(p2) - math.sin(p1) * math.cos(p2) * math.cos(dl))) + 360) % 360
    return d, br


def compass(br):
    names = ["北", "东北", "东", "东南", "南", "西南", "西", "西北"]
    return names[int((br + 22.5) // 45) % 8]


# ---------- 主流程 ----------
def analyse(lat, lon, radius_m):
    import numpy as np
    z = 13
    span = 1 if radius_m <= 4000 else 2
    grid, (px, py), tiles, z = fetch_dem(lat, lon, z, span)
    res = mpp(z, lat)
    h, w = grid.shape
    cx, cy = int(round(px)), int(round(py))
    out = {"input": {"lat": lat, "lon": lon, "radius_m": radius_m},
           "crs_note": "",
           "dem": {"zoom": z, "metres_per_pixel": round(res, 1), "grid": [w, h],
                   "tiles_fetched": len(tiles),
                   "window_km": round(w * res / 1000, 2), "tiles": tiles}}

    def sample(la, lo):
        fx, fy = lonlat_to_tile(lo, la, z)
        x = int(round((fx - (int(lonlat_to_tile(lon, lat, z)[0]) - span)) * 256))
        y = int(round((fy - (int(lonlat_to_tile(lon, lat, z)[1]) - span)) * 256))
        if 0 <= x < w and 0 <= y < h:
            return float(grid[y, x])
        return None

    centre = float(grid[cy, cx])
    out["centre"] = {"elevation_m": round(centre, 1),
                     "pixel": [cx, cy]}
    ring_r = int(max(3, radius_m / res))
    y0, y1 = max(0, cy - ring_r), min(h, cy + ring_r)
    x0, x1 = max(0, cx - ring_r), min(w, cx + ring_r)
    win = grid[y0:y1, x0:x1]
    out["window"] = {"elevation_min_m": round(float(win.min()), 1),
                     "elevation_max_m": round(float(win.max()), 1),
                     "relief_m": round(float(win.max() - win.min()), 1),
                     "mean_m": round(float(win.mean()), 1)}

    # 坡度 / 坡向（中心 5x5）
    k = 2
    sub = grid[max(0, cy - k):cy + k + 1, max(0, cx - k):cx + k + 1]
    gy, gx = np.gradient(sub)
    slope = math.degrees(math.atan(math.hypot(float(gx.mean()), float(gy.mean())))) if sub.size else 0.0
    aspect = (math.degrees(math.atan2(-float(gx.mean()), float(gy.mean()))) + 360) % 360 if sub.size else 0.0
    out["slope_aspect"] = {"slope_deg": round(slope, 1), "aspect_deg": round(aspect, 1),
                           "aspect_compass": compass(aspect)}

    # 八向剖面 + 遮护角
    prof = {}
    for nm, br in BEARINGS:
        dh_r, dh_f = None, None
        for frac, key in ((0.25, "near"), (1.0, "far")):
            la = lat + (radius_m * frac / 111320.0) * math.cos(math.radians(br))
            lo = lon + (radius_m * frac / (111320.0 * math.cos(math.radians(lat)))) * math.sin(math.radians(br))
            v = sample(la, lo)
            if v is not None:
                if key == "near":
                    dh_r = v
                else:
                    dh_f = v
        s = {}
        if dh_r is not None:
            s["near_dh_m"] = round(dh_r - centre, 1)
        if dh_f is not None:
            s["far_dh_m"] = round(dh_f - centre, 1)
        angs = []
        for i in range(1, 6):
            f = i / 5.0
            la = lat + (radius_m * f / 111320.0) * math.cos(math.radians(br))
            lo = lon + (radius_m * f / (111320.0 * math.cos(math.radians(lat)))) * math.sin(math.radians(br))
            v = sample(la, lo)
            if v is not None:
                angs.append(math.degrees(math.atan2(v - centre, radius_m * f)))
        if angs:
            s["shelter_deg"] = round(max(angs), 1)
        prof[nm] = s
    out["bearings"] = prof

    rising = sorted(((v.get("far_dh_m"), k) for k, v in prof.items() if v.get("far_dh_m") is not None),
                    reverse=True)
    out["derived"] = {
        "highest_bearings": [k for _, k in rising[:3]],
        "lowest_bearings": [k for _, k in rising[-3:]],
        "max_shelter": max(((v.get("shelter_deg", -99), k) for k, v in prof.items()))[1],
        "min_shelter": min(((v.get("shelter_deg", 99), k) for k, v in prof.items()))[1],
    }

    # 水系
    try:
        water, meta = fetch_water(lat, lon, radius_m)
        near = []
        for it in water:
            d, br = haversine_bearing(lat, lon, it["lat"], it["lon"])
            it = dict(it); it["distance_m"] = round(d, 1); it["bearing_deg"] = round(br, 1)
            it["bearing_compass"] = compass(br)
            near.append(it)
        near.sort(key=lambda x: x["distance_m"])
        out["water"] = {"count": len(near), "nearest": near[:12], "source": meta}
    except Exception as e:                                    # noqa: BLE001
        out["water"] = {"error": str(e), "count": 0, "nearest": []}

    # 水系（离线河网，补 OSM 乡野缺漏）：只有级别与流域面积，没有河名
    try:
        loc, lmeta = fetch_water_local(lat, lon, radius_m)
        out["water_local"] = {"count": len(loc), "nearest": loc, "source": lmeta}
    except Exception as e:                                    # noqa: BLE001
        out["water_local"] = {"error": str(e), "count": 0, "nearest": []}

    out["fetched_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    return out


# ---------- 离线河网（HydroRIVERS 亚洲）：补 OSM 在乡野的缺漏 ----------
HYDRO_SHAPEFILE = os.path.expanduser(
    "~/.hermes/cache/hydrorivers/HydroRIVERS_v10_as_shp/HydroRIVERS_v10_as.shp")


def fetch_water_local(lat, lon, radius_m, max_items=12):
    """查离线河网。**没有河名**，但带 ORD_FLOW（河流级别，越小越是干流）与
    UPLAND_SKM（上游流域面积），因此能排「干流／支流」。约 10–15 秒（扫全亚洲 142.9 万条）。

    目录里没有这个数据集时抛错——照实说「离线河网未下载」，不假装查过。
    """
    if not os.path.exists(HYDRO_SHAPEFILE):
        raise RuntimeError("离线河网未就绪：%s 不存在（下载说明见 docs/形势取数与映射表.md）"
                           % HYDRO_SHAPEFILE)
    import shapefile
    dlat = radius_m / 111000.0
    dlon = radius_m / (111000.0 * max(0.2, math.cos(math.radians(lat))))
    sf = shapefile.Reader(HYDRO_SHAPEFILE)
    fields = [f[0] for f in sf.fields[1:]]
    best = {}
    for sr in sf.iterShapeRecords():
        b = sr.shape.bbox                      # [xmin, ymin, xmax, ymax] = [lon, lat, ...]
        if b[2] < lon - dlon or b[0] > lon + dlon or b[3] < lat - dlat or b[1] > lat + dlat:
            continue
        rec = dict(zip(fields, sr.record))
        rid = rec.get("HYRIV_ID")
        for i in range(0, len(sr.shape.points), 3):
            x, y = sr.shape.points[i]
            dist, br = haversine_bearing(lat, lon, y, x)
            if dist > radius_m:
                continue
            if rid not in best or dist < best[rid]["distance_m"]:
                best[rid] = {"distance_m": round(dist, 1), "bearing_deg": round(br, 1),
                             "bearing_compass": compass(br),
                             "ord_flow": rec.get("ORD_FLOW"),
                             "upstream_km2": (round(float(rec["UPLAND_SKM"]), 1)
                                              if rec.get("UPLAND_SKM") is not None else None),
                             "length_km": (round(float(rec["LENGTH_KM"]), 1)
                                           if rec.get("LENGTH_KM") is not None else None)}
    items = sorted(best.values(), key=lambda v: v["distance_m"])
    return items[:max_items], {"source": "HydroRIVERS v10 亚洲（离线）", "scanned": len(sf.shapes())}


# ---------- 区域大势（--area）：粗读，回答「大势往哪走、水大致往哪去」 ----------
AREA_AZ = [0, 45, 90, 135, 180, 225, 270, 315]   # 八向，与 compass() 命名一致
TOPK = 3             # 八向里升高最多的前几名算「高带」


def _pick_area_zoom(lat, half_km, max_span=3):
    """挑 zoom 与半宽瓦片数：尽量贴近请求的半径，别为了凑格数把窗口撑得过大。
       实测教训：固定 span=3 时，请求 30 km 会被撑到 108 km 的窗口——
       在这个尺度上「每个方向都向外升高」，「高带」判据直接失效。"""
    for z in (13, 12, 11, 10, 9, 8):
        m = mpp(z, lat)
        span = int(math.ceil(half_km * 1000.0 / (256.0 * m)))
        if span <= max_span:
            return z, max(1, span)
    return 8, max_span


def _ray(grid, px, py, bearing, max_px):
    """自中心沿方位角（0=北，顺时针）逐像素向外采样，返回 [(像素距, 高程 m)]。"""
    h, w = grid.shape
    th = math.radians(bearing)
    dx, dy = math.sin(th), -math.cos(th)            # 图像 y 向下，方位角自北顺时针
    out = []
    for i in range(1, max_px + 1):
        x, y = int(round(px + dx * i)), int(round(py + dy * i))
        if not (0 <= x < w and 0 <= y < h):
            break
        out.append((i, float(grid[y, x])))
    return out


def _bands(az_hits):
    """把命中的方位合成连续弧段（跨 0° 要接起来），返回 [(起始, 终止), ...]。"""
    if not az_hits:
        return []
    s = sorted(az_hits)
    groups, cur = [], [s[0]]
    for a in s[1:]:
        if a - cur[-1] <= 22:
            cur.append(a)
        else:
            groups.append(cur); cur = [a]
    groups.append(cur)
    # 首尾相接（跨北）合并
    if len(groups) > 1 and groups[0][0] == 0 and groups[-1][-1] == 352:
        groups[0] = groups.pop() + groups[0]
    return [(g[0], g[-1]) for g in groups]


def _fmt_band(b):
    a, z2 = b
    return "%d°–%d°" % (a, z2) if a != z2 else "%d°" % a


def analyse_area(lat, lon, half_km):
    """区域粗读：区域倾斜方向 ＋ 各方位上的高带（脊）与低带（谷）。"""
    import numpy as np
    z, span = _pick_area_zoom(lat, half_km)
    grid, (px, py), tiles, z = fetch_dem(lat, lon, z, span)
    m = mpp(z, lat)
    h, w = grid.shape
    cx, cy = int(round(px)), int(round(py))
    centre = float(grid[cy, cx])
    max_px = int(min(px, py, w - 1 - px, h - 1 - py))
    eff_km = max_px * m / 1000.0

    # 各方位：向外最高／最低
    rays = {}
    for az in AREA_AZ:
        prof = _ray(grid, px, py, az, max_px)
        if not prof:
            continue
        hi = max(prof, key=lambda t: t[1])
        lo = min(prof, key=lambda t: t[1])
        rays[az] = {"rise_m": round(hi[1] - centre, 1), "rise_km": round(hi[0] * m / 1000, 2),
                    "drop_m": round(centre - lo[1], 1), "drop_km": round(lo[0] * m / 1000, 2),
                    "far_m": round(prof[-1][1] - centre, 1)}

    # 高低带改成**相对排序**（尺度无关）：八向里升高最多的前几名 vs 最少的几名。
    # 绝对阈值在百公里尺度上必失效——那个跨度里每个方向都有比中心高的地方。
    by_rise = sorted(rays.items(), key=lambda kv: -kv[1]["rise_m"])
    ridge = [a for a, _ in by_rise[:TOPK]]
    valley = [a for a, _ in by_rise[-TOPK:]]

    # 区域整体倾斜（最小二乘平面）：水大致往哪边去
    step = max(1, int((2 * span + 1) * 256 / 220))
    sub = grid[cy - max_px:cy + max_px + 1:step, cx - max_px:cx + max_px + 1:step]
    hs, ws = sub.shape
    yy, xx = np.mgrid[0:hs, 0:ws]
    A = np.column_stack([np.ones(hs * ws), xx.ravel(), yy.ravel()])
    try:
        coef, *_ = np.linalg.lstsq(A, sub.ravel(), rcond=None)
    except Exception:                                          # noqa: BLE001
        coef = None
    trend = None
    if coef is not None:
        a0, bx, by = coef
        glon, glat = bx / m, -by / m                    # 每米的变化
        mag = math.hypot(glon, glat) * 1000.0           # m/km
        # 最陡下降方向（水走的候选）＝ 负梯度
        desc_bearing = (math.degrees(math.atan2(-glon, -glat))) % 360
        trend = {"mag_m_per_km": round(mag, 1), "down_bearing": round(desc_bearing, 1),
                 "down_compass": compass(desc_bearing),
                 "up_compass": compass((desc_bearing + 180) % 360),
                 "window_km": round(2 * max_px * m / 1000, 1)}

    out = {"input": {"lat": lat, "lon": lon, "half_km": half_km, "mode": "area"},
           "crs_note": "",
           "area": {"zoom": z, "metres_per_pixel": round(m, 1), "tiles_fetched": len(tiles),
                    "effective_radius_km": round(eff_km, 1),
                    "centre_elevation_m": round(centre, 1),
                    "min_m": round(float(grid[cy - max_px:cy + max_px + 1,
                                              cx - max_px:cx + max_px + 1].min()), 1),
                    "max_m": round(float(grid[cy - max_px:cy + max_px + 1,
                                              cx - max_px:cx + max_px + 1].max()), 1)},
           "rays": {str(k): v for k, v in sorted(rays.items())},
           "ridge_az": ridge, "valley_az": valley,
           "ridge_bands": [_fmt_band(b) for b in _bands(ridge)],
           "valley_bands": [_fmt_band(b) for b in _bands(valley)],
           "trend": trend,
           "fetched_at": time.strftime("%Y-%m-%dT%H:%M:%S%z")}
    return out


def describe_area(a, place=""):
    L = []
    ar = a["area"]
    L.append("【取数对象】%s（经度 %.5f, 纬度 %.5f）｜**区域粗读**｜取数于 %s"
             % (place or "未名地点", a["input"]["lon"], a["input"]["lat"], a["fetched_at"]))
    if a.get("crs_note"):
        L.append(a["crs_note"])
    L.append("【区域网格】有效半径 %.1f km（约 %.0f m/像素，%.0f 张瓦片）；"
             "中心高程 %.1f m；范围内 %.1f–%.1f m（高差 %.1f m）"
             % (ar["effective_radius_km"], ar["metres_per_pixel"], ar["tiles_fetched"],
                ar["centre_elevation_m"], ar["min_m"], ar["max_m"], ar["max_m"] - ar["min_m"]))
    if a.get("trend"):
        t = a["trend"]
        L.append("【区域整体倾斜】**最陡下降方向 %s（%s）／相反一侧 %s 为高侧**；"
                 "平均坡度 %.1f m/km（窗口 %.1f km）——这是「水大致往哪边走」的候选"
                 % (t["down_compass"], t["down_bearing"], t["up_compass"],
                    t["mag_m_per_km"], t["window_km"]))
    L.append("【高带（向外升高最多的三个方位）】%s"
             % ("、".join(a["ridge_bands"]) if a["ridge_bands"]
                else "无"))
    L.append("【低带（向外升高最少／最能走出去的三个方位）】%s"
             % ("、".join(a["valley_bands"]) if a["valley_bands"]
                else "无"))
    L.append("【各方位向外高／低】（方位：在外多远处升高多少 m ｜ 在外多远处降低多少 m）")
    for az, v in sorted(a["rays"].items(), key=lambda kv: int(kv[0])):
        L.append("    %-5s：升 %6.1f m（%.1f km 处）｜降 %6.1f m（%.1f km 处）"
                 % (compass(float(az)), v["rise_m"], v["rise_km"], v["drop_m"], v["drop_km"]))
    L.append("【标注（补充）】把上面这些量叫作「脊／谷／汇水方向」是**现代粗读**，不是原书原文；"
             "书里判大势要看**连续的走势（过峡、剥换、入首、星峰形态）**，"
             "这份粗读给不出这些——它只回答「哪几边高、哪几边低、水大致往哪边去」。")
    L.append("【必须说明的局限】粗读：分辨率只有 %.0f m/像素，比近身那一级粗得多；"
             "DEM 是公开数据非实测；半径 %.1f km 之外未取；方位以真北为准、未做磁偏角校正；"
             "**不能替代现场踏勘**；不点穴、不给葬法、不接阴宅实地作业指导。"
             % (ar["metres_per_pixel"], ar["effective_radius_km"]))
    return "\n".join(L)


def describe(a, place=""):
    """把取数结果写成一段中文形势描述（只描述，不断吉凶）。"""
    L = []
    L.append("【取数对象】%s（经度 %.5f, 纬度 %.5f）｜取数于 %s"
             % (place or "未名地点", a["input"]["lon"], a["input"]["lat"], a["fetched_at"]))
    if a.get("crs_note"):
        L.append(a["crs_note"])
    L.append("【地形网格】中心高程 %.1f m；半径 %.1f km 窗口内最低 %.1f m、最高 %.1f m、高差 %.1f m；"
             "分辨率约 %.1f m/像素（%d 张瓦片）"
             % (a["centre"]["elevation_m"], a["input"]["radius_m"] / 1000,
                a["window"]["elevation_min_m"], a["window"]["elevation_max_m"],
                a["window"]["relief_m"], a["dem"]["metres_per_pixel"], a["dem"]["tiles_fetched"]))
    L.append("【中心点坡度／坡向】坡度约 %.1f°；坡向约 %.0f°（朝%s）"
             % (a["slope_aspect"]["slope_deg"], a["slope_aspect"]["aspect_deg"],
                a["slope_aspect"]["aspect_compass"]))
    L.append("【八方相对高差与遮护角】（正数为高于中心，单位 m / °）")
    for nm, _ in BEARINGS:
        s = a["bearings"].get(nm, {})
        L.append("    %s：近 %.1f / 远 %.1f / 最大仰角 %.1f"
                 % (nm, s.get("near_dh_m", float("nan")), s.get("far_dh_m", float("nan")),
                    s.get("shelter_deg", float("nan"))))
    d = a["derived"]
    L.append("【由此得到的三件事｜标注（补充）：把地理量对应到书里术语的这一步是**现代补充**，不是原书原文】")
    L.append("    ① 相对最高／最开阔（来势侧候选）：%s；相对最低（去势侧候选）：%s"
             % ("、".join(d["highest_bearings"]), "、".join(d["lowest_bearings"])))
    L.append("    ② 遮护最强方向 %s、最弱方向 %s" % (d["max_shelter"], d["min_shelter"]))
    w = a.get("water", {})
    if w.get("error"):
        L.append("【水系】取数失败：%s" % w["error"])
    elif w.get("count"):
        n = w["nearest"][0]
        L.append("【水系】半径内 %d 处水体／水道；最近一处：%s%s，约 %.0f m，位于%s方"
                 % (w["count"], (n.get("kind") or ""), ("「%s」" % n["name"]) if n.get("name") else "",
                    n["distance_m"], n["bearing_compass"]))
    else:
        L.append("【水系】半径内未取到水体／水道（可能是数据缺失，不表示现场无水）")
    wl = a.get("water_local", {})
    if wl.get("error"):
        L.append("【水系·离线河网】不可用：%s" % wl["error"])
    elif wl.get("count"):
        L.append("【水系·离线河网（补乡野缺漏；**无河名**，按河流级别排干枝）】半径内 %d 条河道，最近几条："
                 % wl["count"])
        for it in wl["nearest"][:6]:
            L.append("    约 %6.0f m %s方｜级别 ORD_FLOW=%s（越小越是干流）｜上游流域 %s km²"
                     % (it["distance_m"], it["bearing_compass"], it["ord_flow"],
                        ("%.0f" % it["upstream_km2"]) if it["upstream_km2"] is not None else "?"))
    else:
        L.append("【水系·离线河网】半径内没有达到收录阈值的河道（该数据只收流域面积 ≥10 km² 的河道；"
                 "小沟渠不在其中，**不等于现场无水**）")
    L.append("【下一步交给谁】把上面这段交给相地类 skill（藏风得水 / 支垄之辨 / 势来形止 / "
             "形势品类 / 疑龙经下篇 / 倒杖十二法）；取数**不等于**判读，本工具不给吉凶、不点穴。")
    L.append("【必须说明的局限】DEM 为公开 30m 级数据，非实测；半径 %.1f km 之外未取；"
             "OSM 水系在乡野常有缺漏（离线河网可补一部分，但它只收流域面积 ≥10 km² 的河道、且无河名）；"
             "方位以真北为准但未做磁偏角校正；"
             "**不能替代现场踏勘**，阴宅实地作业指导不在本包范围内。"
             % (a["input"]["radius_m"] / 1000))
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description="形势取数器：地点 → 形势描述")
    g = ap.add_mutually_exclusive_group(required=False)
    g.add_argument("--place", help="地名（走 photon.komoot.io 解析；会列出候选让你核对）")
    g.add_argument("--lat", type=float, help="纬度（与 --lon 同用）")
    g.add_argument("--url", help="地图 App 的分享链接（高德 surl.amap.com / 百度 j.map.baidu.com）——"
                                "会自动解析出坐标、地名，并按其坐标系转成 WGS-84")
    ap.add_argument("--lon", type=float)
    ap.add_argument("--crs", default="wgs84",
                    help="你给的经纬度是哪家地图读的：wgs84（默认；GPS·OSM）/ "
                         "gcj02（高德·腾讯·微信）/ bd09（百度）。会给转成 WGS-84 再取数")
    ap.add_argument("--pick", type=int, default=1, help="地名命中多个时取第几个候选（默认 1）")
    ap.add_argument("--radius", type=float, default=2.0, help="近身半径（公里），默认 2")
    ap.add_argument("--area", type=float, metavar="KM",
                    help="改跑**区域大势粗读**：以该点为中心、半径 KM 公里，"
                         "出区域倾斜方向与高带（脊）／低带（谷）方位。建议 15–40")
    ap.add_argument("--out", help="把原始结果写成 JSON")
    ap.add_argument("--check", action="store_true",
                    help="只做依赖体检（pre-flight），不取数（此时不需要 --place/--lat）")
    ap.add_argument("--force", action="store_true",
                    help="体检不过也照跑（不建议：会把已经拿不到的那一项写成取数失败）")
    a = ap.parse_args()
    if not a.check and a.place is None and a.lat is None and a.url is None:
        ap.error("要么给 --place，要么给 --lat/--lon，要么给 --url；只想查依赖就加 --check")
    # 分享链接：先解坐标与坐标系，再走下面的同一套校验与转换
    url_name = ""
    if a.url:
        from link2coord import resolve as _resolve
        try:
            r = _resolve(a.url)
        except Exception as e:                                # noqa: BLE001
            sys.exit("链接解析失败：%s" % e)
        a.lat, a.lon, a.crs = r["lat"], r["lon"], r["crs"]
        url_name = r["name"]
        print("# 链接解析（依据 %s，%d 跳）：%s → 纬度 %.6f、经度 %.6f｜坐标系 %s"
              % (r["evidence"], r["hops"], r["name"] or "(无名)", r["lat"], r["lon"], r["crs"]))
    if a.lat is not None and a.lon is None:
        sys.exit("给了 --lat 就要给 --lon")
    # 经纬度范围校验：写反是最常见的错，绝不能静默算出垃圾
    if a.lat is not None:
        if abs(a.lat) > 90:
            sys.exit("纬度 %.6f 超过 ±90 —— 你大概把经纬度写反了"
                     "（经度范围是 ±180，纬度才是 ±90）；也可能是把东经/西经或北纬/南纬写错。" % a.lat)
        if not -180.0 <= a.lon <= 180.0:
            sys.exit("经度 %.6f 超出 ±180。" % a.lon)
        if abs(a.lon) < 60 and abs(a.lat) > 10:
            sys.exit("这组数字看着像「纬度在前、经度在后」（%.6f, %.6f），请核对：" 
                     "--lat 是纬度（南北，如 28.45），--lon 是经度（东西，如 117.97）。" % (a.lat, a.lon))
    crs_note = ""
    if a.lat is not None:
        c = CRS_ALIAS.get(str(a.crs).strip().lower())
        if c is None:
            sys.exit("不认识的 --crs %r；可用：wgs84 / gcj02（高德·腾讯·微信）/ bd09（百度）" % a.crs)
        if c != "wgs84":
            olng, olat = a.lon, a.lat
            a.lon, a.lat = to_wgs84(a.lon, a.lat, c)
            crs_note = ("【坐标系】输入按 %s 解读（%s），已转成 WGS-84："
                        "经度 %.6f、纬度 %.6f → 经度 %.6f、纬度 %.6f，折合偏移 %.0f m"
                        % (c, {"gcj02": "高德/腾讯/微信", "bd09": "百度"}[c],
                           olng, olat, a.lon, a.lat, offset_meters(olng, olat, a.lon, a.lat)))
        else:
            crs_note = "【坐标系】按 WGS-84 原样使用（GPS / OpenStreetMap 口径）"

    print("# 依赖体检（跑数据前必查：先查再跑，不跑到一半才发现缺）")
    ok, rows = preflight()
    if a.check:
        print("\n体检结论：%s" % ("全部可用" if ok else "有不可用项——先解决再跑，别硬跑"))
        sys.exit(0 if ok else 1)
    if not ok and not a.force:
        bad = [r[1] for r in rows if not r[2]]
        print("\n× 依赖不齐：%s" % "、".join(bad))
        print("  本工具**没有开始取数**。可选：①过一会儿重试 ②换镜像（见 tools/install_deps.py 的 DATA_SOURCES）"
              " ③只跑能用的那部分（--force，取数失败的那项会在输出里照实写明）")
        sys.exit(1)
    if not ok:
        print("\n! --force：带着不可用的数据源继续，失败项会照实写进输出。")

    if a.place:
        cands = geocode_place(a.place)
        print("# 地名候选（**同名地名会被解错，请核对该位置对不对**）：")
        for i, c in enumerate(cands, 1):
            print("   %d) %s  → %.5f, %.5f  [%s/%s]" % (i, c["name"], c["lat"], c["lon"],
                                                        c["type"], c["osm_value"]))
        if len(cands) > 1:
            print("# 取第 %d 个；不对就换 --pick N，或直接用 --lat/--lon 给准确坐标。" % a.pick)
        if not 1 <= a.pick <= len(cands):
            sys.exit("--pick 超出范围（1–%d）" % len(cands))
        c = cands[a.pick - 1]
        lat, lon, name = c["lat"], c["lon"], c["name"]
    else:
        lat, lon, name = a.lat, a.lon, url_name

    if a.area:
        res = analyse_area(lat, lon, a.area)
        res["crs_note"] = crs_note
        print()
        print(describe_area(res, name))
    else:
        res = analyse(lat, lon, a.radius * 1000.0)
        res["crs_note"] = crs_note
        print()
        print(describe(res, name))
    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            json.dump(res, f, ensure_ascii=False, indent=1)
        print("\n# 原始取数结果已写入 %s" % a.out)


if __name__ == "__main__":
    main()
