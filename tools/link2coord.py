"""把「地图 App 的分享链接」解成坐标。

支持（实测）：
  · 高德：`https://surl.amap.com/xxxx` → 302 到 `https://wb.amap.com/?p=<POI>,<纬度>,<经度>,<名称>,<地址>`
          也支持 `amap.com`/`m.amap.com` 上带 `longitude=`/`latitude=` 或 `q=纬度,经度,名称` 的形态。
  · 百度：`https://j.map.baidu.com/xxxx` → 跳到 `map.baidu.com` 上的 `@经度,纬度` 或 `latlng=`/`location=`。
  · 通用兜底：任何链接文本里出现 `纬度,经度` 或 `lat=`/`lng=` 参数都试着认。

**只做「链接 → 坐标 + 名称」，不做判读。** 坐标系按域名判定：
高德系 = GCJ-02，百度系 = BD-09，其余按 WGS-84（见 tools/crs.py）。
"""
import re
import urllib.parse
import urllib.request

UA = {"User-Agent": ("Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) "
                     "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1")}

AMAP_HOSTS = ("amap.com",)
BAIDU_HOSTS = ("baidu.com",)


def _host_crs(url):
    h = urllib.parse.urlparse(url).netloc.lower()
    if any(h.endswith(x) or h == x for x in AMAP_HOSTS) or "amap" in h:
        return "gcj02"
    if any(h.endswith(x) or h == x for x in BAIDU_HOSTS) or "baidu" in h:
        return "bd09"
    return "wgs84"


def _get(url, timeout=20):
    req = urllib.request.Request(url, headers=UA)
    try:
        r = urllib.request.urlopen(req, timeout=timeout)
        return r.geturl(), r.read().decode("utf-8", "replace"), r.status
    except urllib.error.HTTPError as e:
        return url, "", e.code


def _chain(url, max_hops=6, timeout=20):
    """手动跟踪跳转，把每一跳的 URL 都收集起来（坐标常藏在中途的 Location 里）。"""
    seen, urls = set(), [url]
    cur = url
    for _ in range(max_hops):
        if cur in seen:
            break
        seen.add(cur)
        req = urllib.request.Request(cur, headers=UA)
        try:
            op = urllib.request.build_opener(_NoRedirect)
            try:
                r = op.open(req, timeout=timeout)
                break
            except urllib.error.HTTPError as e:
                loc = e.headers.get("Location")
                if not loc:
                    break
                nxt = urllib.parse.urljoin(cur, loc)
                urls.append(nxt)
                cur = nxt
            except _Redirect as red:
                nxt = urllib.parse.urljoin(cur, red.loc)
                urls.append(nxt)
                cur = nxt
        except Exception:                                     # noqa: BLE001
            break
    # 最后一跳抓一次正文，坐标也可能在 HTML/JS 里
    body = ""
    try:
        final, body, _ = _get(cur, timeout=timeout)
        if final and final not in urls:
            urls.append(final)
    except Exception:                                         # noqa: BLE001
        pass
    return urls, body


class _Redirect(Exception):
    def __init__(self, loc):
        self.loc = loc


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise _Redirect(newurl)


NUM = r"-?\d{1,3}\.\d{3,}"


def _try(lat, lon):
    """范围校验：经纬度要对得上（避免把版本号、面积当成坐标）。"""
    try:
        la, lo = float(lat), float(lon)
    except (TypeError, ValueError):
        return None
    if not (-90 <= la <= 90 and -180 <= lo <= 180):
        return None
    if abs(la) < 1 and abs(lo) < 1:                # 赤道/本初子午线附近基本不是这类场景
        return None
    return la, lo


def parse_from_urls(urls, body=""):
    """从一串 URL/正文里抽 (lat, lon, name)。返回 (lat, lon, name, 证据串) 或 None。"""
    text_all = "\n".join(urls) + "\n" + body

    # 1) 高德 poi 形态： p=POIID,纬度,经度,名称[,地址]
    for u in urls:
        q = urllib.parse.parse_qs(urllib.parse.urlparse(u).query)
        for key in ("p",):
            for v in q.get(key, []):
                parts = v.split(",")
                if len(parts) >= 3:
                    got = _try(parts[1], parts[2])
                    if got:
                        return got[0], got[1], (parts[3] if len(parts) > 3 else ""), "amap:p"
        # 高德 long/lat 参数
        lat = (q.get("latitude") or q.get("lat") or [None])[0]
        lon = (q.get("longitude") or q.get("lng") or [None])[0]
        got = _try(lat, lon)
        if got:
            return got[0], got[1], (q.get("name") or [""])[0], "amap:param"
        # 高德 q=纬度,经度,名称
        for v in q.get("q", []):
            parts = urllib.parse.unquote(v).split(",")
            if len(parts) >= 2:
                got = _try(parts[0], parts[1])
                if got:
                    return got[0], got[1], (parts[2] if len(parts) > 2 else ""), "amap:q"

    # 2) 百度 @经度,纬度 / latlng=纬度,经度 / location=
    for u in urls:
        m = re.search(r"@(%s),(%s)" % (NUM, NUM), u)
        if m:
            got = _try(m.group(2), m.group(1))       # @lon,lat
            if got:
                return got[0], got[1], "", "baidu:@lng,lat"
        q = urllib.parse.parse_qs(urllib.parse.urlparse(u).query)
        for key in ("latlng", "location", "center"):
            for v in q.get(key, []):
                parts = re.split(r"[,|]", v)
                if len(parts) >= 2:
                    got = _try(parts[0], parts[1])   # 百度这个参数一般是 lat,lng
                    if got:
                        return got[0], got[1], (q.get("name") or [""])[0], "baidu:%s" % key

    # 3) 通用兜底：正文里找 lat/lng 或 uid/坐标对
    for pat, swap in ((r'"?lat"?\s*[:=]\s*"?(' + NUM + r')"?[^\d-]{0,20}"?l(?:ng|on)"?\s*[:=]\s*"?(' + NUM + r')"?', False),
                      (r'"?l(?:ng|on)"?\s*[:=]\s*"?(' + NUM + r')"?[^\d-]{0,20}"?lat"?\s*[:=]\s*"?(' + NUM + r')"?', True)):
        m = re.search(pat, text_all)
        if m:
            got = _try(m.group(1), m.group(2)) if not swap else _try(m.group(2), m.group(1))
            if got:
                return got[0], got[1], "", "generic"
    return None


def resolve(link_or_text):
    """主入口。返回 dict：lat/lon（原坐标系）/crs/name/evidence/hops。解不出抛错。"""
    m = re.search(r"https?://[^\s，。；、）)】\"']+", link_or_text)
    if not m:
        raise ValueError("这段文字里没找到链接（把地图 App 里「复制链接」得到的那条发我）")
    url = m.group(0)
    urls, body = _chain(url)
    hit = parse_from_urls(urls, body)
    if not hit:
        raise ValueError("链接能打开，但里面没找到坐标（可能这条分享的是「路线」而不是「一个点」，"
                         "或者链接已失效）。可以退一步：直接给我地名，我来解析并列出候选让你核对。")
    lat, lon, name, ev = hit
    # 名称在跳转链里常是 URL 编码的，解一层
    try:
        name = urllib.parse.unquote(name)
    except Exception:                                         # noqa: BLE001
        pass
    return {"lat": lat, "lon": lon, "name": name.strip(),
            "crs": _host_crs(url), "evidence": ev, "hops": len(urls)}
