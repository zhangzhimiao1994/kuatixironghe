# -*- coding: utf-8 -*-
"""排盘工具（象征层前置）：用纯 Python 的 Meeus 算法算出七政黄经与上升/中天。

依赖：pymeeus（纯 Python，无需星历数据文件；国内镜像可装）
    python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pymeeus

用法：
    python tools/paipan.py --date 1994-11-10 --time 07:30 --tz 8 \
        --lat 28.4546 --lon 117.9686 --place 江西上饶

说明与限制：
  * 本脚本只用标准库 + pymeeus；不联网、不需要 .se1/.bsp 星历文件。
  * 精度：太阳/行星黄经约角秒—角分（Meeus 算法），对星座、宫位、相位的判读足够。
  * 「辰时」这类只知道两小时时段的输入：**上升/中天在该时段内会大幅移动**，
    脚本照给定时刻算，但使用者必须把不确定度写进判读（见 docs/排盘与星历.md）。
  * 东出/西没（oriental / occidental）按与太阳的黄经差判定：
    黄经差（行星 − 太阳，取模 360）落在 0–180° → 行星在太阳之东 → 昏见/西没（vespertine）；
    落在 180–360° → 行星在太阳之西 → 晨见/东出（matutine / oriental）。
  * 本工具只给数据，不下断语；判读照《Tetrabiblos》取用链走。
"""

import argparse
import math
from datetime import datetime, timedelta

SIGNS = ["白羊", "金牛", "双子", "巨蟹", "狮子", "处女",
         "天秤", "天蝎", "射手", "摩羯", "水瓶", "双鱼"]
SIGN_EN = ["Ari", "Tau", "Gem", "Can", "Leo", "Vir", "Lib", "Sco", "Sag", "Cap", "Aqu", "Pis"]
ELEMENT = {"火": ["白羊", "狮子", "射手"], "土": ["金牛", "处女", "摩羯"],
           "风": ["双子", "天秤", "水瓶"], "水": ["巨蟹", "天蝎", "双鱼"]}
TRIPLICITY = {  # 三重性主星（火/土/风/水，按昼/夜）
    "火": ("太阳", "木星"), "土": ("金星", "月亮"),
    "风": ("土星", "水星"), "水": ("金星", "火星"),
}


def dms(x, unit="°"):
    d = int(x)
    m = int(round((x - d) * 60))
    if m == 60:
        d, m = d + 1, 0
    return f"{d:02d}{unit}{m:02d}′"


def fmt(lon):
    lon %= 360.0
    s = int(lon // 30)
    d = lon - s * 30
    return f"{SIGNS[s]}{dms(d)}"


def sign_of(lon):
    return SIGNS[int((lon % 360) // 30)]


def elem_of(lon):
    s = sign_of(lon)
    for e, signs in ELEMENT.items():
        if s in signs:
            return e
    return "?"


def asc_mc(eps_deg, lst_hours, lat_deg):
    """上升与中天黄经。标准球面三角公式。"""
    ramc = (lst_hours * 15.0) % 360.0
    eps = math.radians(eps_deg)
    lam_mc = math.degrees(math.atan2(math.sin(math.radians(ramc)),
                                     math.cos(math.radians(ramc)) * math.cos(eps))) % 360
    phi = math.radians(lat_deg)
    lam_asc = math.degrees(math.atan2(
        math.cos(math.radians(ramc)),
        -(math.sin(math.radians(ramc)) * math.cos(eps)
          + math.tan(phi) * math.sin(eps)))) % 360
    return ramc, lam_mc, lam_asc


ASPECTS = [(0, "合"), (60, "六分"), (90, "四分"), (120, "三分"), (180, "对冲")]
ORB = 6.0


def aspects(positions, lum_only=False):
    out = []
    keys = list(positions)
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            a, b = keys[i], keys[j]
            if lum_only and not ({"太阳", "月亮"} & {a} or {"太阳", "月亮"} & {b}):
                continue
            diff = abs(positions[a] - positions[b]) % 360
            if diff > 180:
                diff = 360 - diff
            for ang, nm in ASPECTS:
                if abs(diff - ang) <= ORB:
                    out.append(f"{a}—{b} {nm}（差 {diff:.1f}°，容许 {ORB:g}）")
                    break
    return out


def compute(place, dt_local, tz, lat, lon):
    from pymeeus.Epoch import Epoch
    from pymeeus.Sun import Sun, true_obliquity
    from pymeeus.Moon import Moon
    from pymeeus.Mercury import Mercury
    from pymeeus.Venus import Venus
    from pymeeus.Mars import Mars
    from pymeeus.Jupiter import Jupiter
    from pymeeus.Saturn import Saturn

    ut = dt_local - timedelta(hours=tz)
    e = Epoch(ut.year, ut.month, ut.day + (ut.hour + ut.minute / 60.0 + ut.second / 3600.0) / 24.0)
    pos = {}
    pos["太阳"] = float(Sun.apparent_geocentric_position(e)[0]) % 360
    pos["月亮"] = float(Moon.apparent_ecliptical_pos(e)[0]) % 360
    for nm, cls in (("水星", Mercury), ("金星", Venus), ("火星", Mars),
                    ("木星", Jupiter), ("土星", Saturn)):
        pos[nm] = float(cls.geocentric_position(e)[0]) % 360
    eps = float(true_obliquity(e))
    lst = (float(e.mean_sidereal_time()) * 24.0 + lon / 15.0) % 24.0
    ramc, mc, asc = asc_mc(eps, lst, lat)
    return {"ut": ut, "pos": pos, "eps": eps, "lst": lst, "ramc": ramc, "mc": mc, "asc": asc}


def report(place, dt_local, tz, lat, lon):
    d = compute(place, dt_local, tz, lat, lon)
    pos, asc, mc = d["pos"], d["asc"], d["mc"]
    print(f"# 排盘：{place}  本地 {dt_local:%Y-%m-%d %H:%M} (UTC{tz:+g})  "
          f"= UT {d['ut']:%Y-%m-%d %H:%M}")
    print(f"# 地理 {lat:.4f}N {lon:.4f}E | 黄赤交角 {d['eps']:.4f}° | "
          f"本地恒星时 {d['lst']:.4f}h | RAMC {d['ramc']:.3f}°")
    print()
    print("| 点 | 黄经 | 星座 | 元素 | 距上升(整宫) | 东出/西没 |")
    print("|---|---|---|---|---|---|")
    asc_sign = int((asc % 360) // 30)
    delta_sun = lambda l: (l - pos["太阳"]) % 360
    rows = [("上升", asc), ("中天", mc)] + list(pos.items())
    for nm, l in rows:
        if nm in ("上升", "中天"):
            extra = ("—", "—")
        else:
            house = (int((l % 360) // 30) - asc_sign) % 12 + 1
            dd = delta_sun(l)
            extra = (f"第{house}宫",
                     "昏见/西没" if dd < 180 else "晨见/东出")
        print(f"| {nm} | {l % 360:.4f}° | {fmt(l)} | {elem_of(l)} | {extra[0]} | {extra[1]} |")
    print()
    print("日月角距（月 − 日，取模 360）：%.2f°" % delta_sun(pos["月亮"]))
    print()
    print("## 主要相位（容许 %.0f°）" % ORB)
    for a in aspects(pos):
        print("- " + a)
    lum = aspects(pos, lum_only=True)
    if lum:
        print()
        print("## 与日月成相位的项（合婚、婚姻线要用的）")
        for a in lum:
            print("- " + a)
    print()
    print("> 别把上表当结论：星座、宫位、相位的判读照《Tetrabiblos》的取用链走；")
    print("> 出生时刻若只精确到时段（如「辰时」），上升/中天在时段内会大幅移动，必须标注未校正。")


def main():
    p = argparse.ArgumentParser(description="用 Meeus 算法排一张盘（七政黄经 + 上升/中天）")
    p.add_argument("--date", required=True, help="本地出生日期 YYYY-MM-DD")
    p.add_argument("--time", required=True, help="本地出生时间 HH:MM（取时段中点也行，但要说明）")
    p.add_argument("--tz", type=float, default=8.0, help="时区偏移（小时），默认 8（北京时间）")
    p.add_argument("--lat", type=float, required=True, help="纬度（北为正）")
    p.add_argument("--lon", type=float, required=True, help="经度（东为正）")
    p.add_argument("--place", default="", help="出生地名称（只用于显示）")
    a = p.parse_args()
    dt = datetime.strptime(f"{a.date} {a.time}", "%Y-%m-%d %H:%M")
    report(a.place or "(未填)", dt, a.tz, a.lat, a.lon)


if __name__ == "__main__":
    main()
