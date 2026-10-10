"""四柱排盘器：出生信息 → 四柱、藏干、十神、五行计数。

**只做可核的历法与规则计算**（四柱、纳音、藏干、十神、五行计数、真太阳时、时辰边界）；
**旺衰、格局、用神、吉凶属判读**，要回到原书条文上（见 skills/bazi-*），本工具不下断语。

依赖：lunar_python（pip，国内源可装）、pymeeus（可选的均时差精算，缺失时用内置低精度公式）。

用法：
    python tools/bazi.py --date 2004-09-10 --time 11:00 --tz 8
    python tools/bazi.py --date 2004-09-10 --time 11:00 --tz 8 --lat 38.30 --lon 116.84 --place 河北沧州
    python tools/bazi.py --date 2004-09-10 --time 11:00 --tz 8 --lat 38.30 --lon 116.84 --json
说明：给了 --lat/--lon 就会同时给出**真太阳时**与**时辰翻转点**（记录时间早于翻转点才是该时柱）。
"""
import argparse
import json
import math
import sys
from collections import Counter
from datetime import datetime, timedelta

WX_GAN = {"甲": "木", "乙": "木", "丙": "火", "丁": "火", "戊": "土",
          "己": "土", "庚": "金", "辛": "金", "壬": "水", "癸": "水"}
WX_ZHI = {"子": "水", "丑": "土", "寅": "木", "卯": "木", "辰": "土", "巳": "火",
          "午": "火", "未": "土", "申": "金", "酉": "金", "戌": "土", "亥": "水"}
YANG = set("甲丙戊庚壬")
# 地支藏干（本气在前），通行表
CANG = {"子": "癸", "丑": "己癸辛", "寅": "甲丙戊", "卯": "乙", "辰": "戊乙癸",
        "巳": "丙庚戊", "午": "丁己", "未": "己丁乙", "申": "庚壬戊", "酉": "辛",
        "戌": "戊辛丁", "亥": "壬甲"}
SHENG = {"木": "火", "火": "土", "土": "金", "金": "水", "水": "木"}   # 我生
KE = {"木": "土", "土": "水", "水": "火", "火": "金", "金": "木"}       # 我克
ORDER = ["木", "火", "土", "金", "水"]


def shishen(g, ri):
    wg, wr = WX_GAN[g], WX_GAN[ri]
    same = (g in YANG) == (ri in YANG)
    if wg == wr:
        return "比肩" if same else "劫财"
    if SHENG[wr] == wg:
        return "食神" if same else "伤官"
    if KE[wr] == wg:
        return "偏财" if same else "正财"
    if KE[wg] == wr:
        return "七杀" if same else "正官"
    if SHENG[wg] == wr:
        return "偏印" if same else "正印"
    return "?"


def eot_minutes(dt_utc):
    """均时差（分钟）＝ 真太阳时 − 平太阳时。低精度公式，误差约 ±0.2 分。"""
    try:
        import ephem
        d = ephem.Date(dt_utc)
        jd = ephem.julian_date(d)
        ra_deg = math.degrees(float(ephem.Sun(d).ra))
    except Exception:                                          # noqa: BLE001
        days = (dt_utc - datetime(2000, 1, 1, 12, tzinfo=dt_utc.tzinfo)).total_seconds() / 86400.0
        jd = 2451545.0 + days
        T = (jd - 2451545.0) / 36525.0
        L = math.radians((280.460 + 36000.771 * T) % 360)
        g = math.radians((357.529 + 35999.050 * T) % 360)
        lam = L + math.radians(1.915) * math.sin(g) + math.radians(0.020) * math.sin(2 * g)
        eps = math.radians(23.439 - 0.0000004 * (jd - 2451545.0))
        ra_deg = math.degrees(math.atan2(math.cos(eps) * math.sin(lam), math.cos(lam))) % 360
    T = (jd - 2451545.0) / 36525.0
    L0 = 280.46646 + 36000.76983 * T + 0.0003032 * T * T
    diff = (L0 - ra_deg) % 360.0
    if diff > 180:
        diff -= 360.0
    return diff * 4.0


def main():
    ap = argparse.ArgumentParser(description="四柱排盘器（只做可核计算，不下断语）")
    ap.add_argument("--date", required=True, help="出生日期 YYYY-MM-DD（公历）")
    ap.add_argument("--time", required=True, help="出生时刻 HH:MM（所在时区的钟表时间）")
    ap.add_argument("--tz", type=float, default=8.0, help="时区偏移，默认 8（东八区）")
    ap.add_argument("--lat", type=float, help="纬度（与 --lon 同用；给了才算真太阳时）")
    ap.add_argument("--lon", type=float)
    ap.add_argument("--place", default="", help="出生地（只用于显示）")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    try:
        from lunar_python import Solar
    except Exception:                                          # noqa: BLE001
        sys.exit("缺 lunar_python：python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple lunar_python")

    y, m, d = (int(x) for x in a.date.replace("/", "-").split("-"))
    hh, mm = (int(x) for x in a.time.replace("：", ":").split(":"))

    def pillars(h, mi, dd=None):
        yy, mm2, dd2 = dd or (y, m, d)
        return Solar.fromYmdHms(yy, mm2, dd2, h, mi, 0).getLunar().getEightChar()

    # 先算钟表时间口径（参考）
    e_clock = pillars(hh, mm)

    # 给了经纬度就按真太阳时排（八字通行做法）；没给就按钟表时间排
    ts = None
    if a.lat is not None and a.lon is not None:
        utc = datetime(y, m, d, hh, mm) - timedelta(hours=a.tz)
        eot = eot_minutes(utc.replace(tzinfo=utc.tzinfo))
        drift = (a.lon - 15.0 * a.tz) * 4.0                     # 经度差（分钟）
        tst = datetime(y, m, d, hh, mm) + timedelta(minutes=drift + eot)
        # 时辰界在奇数点（子 23、丑 1、寅 3…）；找真太阳时之后的第一个奇数点
        nb = ((tst.hour + 1) // 2) * 2 + 1
        wrap = nb > 23
        nb_h = (nb % 24)
        # 翻转点＝钟表时间多少分时真太阳时正好到 nb
        anchor = (nb_h + (24 if nb_h < tst.hour else 0)) * 60
        flip = anchor - (drift + eot)
        prev_dt = datetime(y, m, d) + timedelta(minutes=anchor - 1)
        next_dt = datetime(y, m, d) + timedelta(minutes=anchor + 1)
        ts = {
            "eot_minutes": round(eot, 1), "lon_drift_minutes": round(drift, 1),
            "true_solar_time": tst.strftime("%H:%M:%S"),
            "prev_time_pillar": pillars(prev_dt.hour, prev_dt.minute, (prev_dt.year, prev_dt.month, prev_dt.day)).getTime(),
            "next_time_pillar": pillars(next_dt.hour, next_dt.minute, (next_dt.year, next_dt.month, next_dt.day)).getTime(),
            "flip_point_clock": ("次日 %02d:%02d" % (int(flip // 60), int(round(flip % 60))))
                                if wrap else ("%02d:%02d" % (int(flip // 60), int(round(flip % 60)))),
        }
        e = pillars(tst.hour, tst.minute, (tst.year, tst.month, tst.day))
    else:
        e = e_clock

    gan = [e.getYearGan(), e.getMonthGan(), e.getDayGan(), e.getTimeGan()]
    zhi = [e.getYearZhi(), e.getMonthZhi(), e.getDayZhi(), e.getTimeZhi()]
    ri = e.getDayGan()

    c_gan = Counter(WX_GAN[g] for g in gan)
    c_ben = c_gan + Counter(WX_ZHI[b] for b in zhi)
    c_all = c_gan + Counter(WX_GAN[c] for b in zhi for c in CANG[b])
    ss = Counter(shishen(g, ri) for g in gan) + Counter(shishen(c, ri) for b in zhi for c in CANG[b])

    out = {
        "input": {"date": a.date, "time": a.time, "tz": a.tz, "lat": a.lat, "lon": a.lon,
                  "place": a.place},
        "pillars": {"年": e.getYear(), "月": e.getMonth(), "日": e.getDay(), "时": e.getTime()},
        "nayin": {"年": e.getYearNaYin(), "月": e.getMonthNaYin(),
                  "日": e.getDayNaYin(), "时": e.getTimeNaYin()},
        "day_master": {"gan": ri, "element": WX_GAN[ri], "yin_yang": "阳" if ri in YANG else "阴"},
        "month_order": {"zhi": zhi[1], "element": WX_ZHI[zhi[1]], "shishen": shishen(CANG[zhi[1]][0], ri)},
        "canggan": {b: [{"gan": c, "element": WX_GAN[c], "shishen": shishen(c, ri)} for c in CANG[b]]
                    for b in zhi},
        "wuxing": {"只天干": {k: c_gan.get(k, 0) for k in ORDER},
                   "天干_地支本气": {k: c_ben.get(k, 0) for k in ORDER},
                   "天干_含藏干": {k: c_all.get(k, 0) for k in ORDER}},
        "shishen_count": {k: ss.get(k, 0) for k in
                          ["比肩", "劫财", "食神", "伤官", "偏财", "正财", "七杀", "正官", "偏印", "正印"]},
    }

    # 真太阳时与时辰翻转点（上面已算好，这里只挂进结果；翻转点算在奇数时辰界上）
    if ts:
        out["true_solar"] = ts
        out["time_pillar_clock"] = e_clock.getTime()

    if a.json:
        print(json.dumps(out, ensure_ascii=False, indent=1))
        return
    p = out["pillars"]
    print("四柱：%s %s %s %s%s" % (p["年"], p["月"], p["日"], p["时"],
                                 ("　（%s）" % a.place) if a.place else ""))
    print("纳音：年 %s｜月 %s｜日 %s｜时 %s"
          % (out["nayin"]["年"], out["nayin"]["月"], out["nayin"]["日"], out["nayin"]["时"]))
    dm = out["day_master"]
    print("日主：%s（%s%s）｜月令：%s（%s）→ 对日主是「%s」"
          % (dm["gan"], dm["element"], dm["yin_yang"], out["month_order"]["zhi"],
             out["month_order"]["element"], out["month_order"]["shishen"]))
    print("\n天干十神：%s" % "｜".join("%s %s" % (g, shishen(g, ri)) for g in gan))
    print("地支藏干：")
    for label, b in zip(("年", "月", "日", "时"), zhi):
        print("  %s支 %s（%s）：%s" % (label, b, WX_ZHI[b],
              "、".join("%s%s" % (c, shishen(c, ri)) for c in CANG[b])))
    w = out["wuxing"]
    print("\n五行计数：")
    for k, name in (("只天干", "只看天干        "), ("天干_地支本气", "天干＋地支本气  "),
                    ("天干_含藏干", "天干＋含藏干    ")):
        print("  %s（共 %2d）：%s" % (name, sum(w[k].values()),
              "  ".join("%s %d" % (e2, w[k][e2]) for e2 in ORDER)))
    print("  缺（本气口径）：%s" % ("、".join(e2 for e2 in ORDER if w["天干_地支本气"][e2] == 0) or "无（五行俱全）"))
    print("\n十神计数（天干＋藏干，共 %d）：%s"
          % (sum(out["shishen_count"].values()),
             "｜".join("%s %d" % (k, v) for k, v in out["shishen_count"].items())))
    if "true_solar" in out:
        t = out["true_solar"]
        print("\n真太阳时口径（**本工具默认用这个排**）：%s（均时差 %+.1f 分、经度差 %+.1f 分）"
              % (t["true_solar_time"], t["eot_minutes"], t["lon_drift_minutes"]))
        print("  时柱 = %s；**钟表时间口径**的时柱是 %s（未做真太阳时校正，作对照）"
              % (out["pillars"]["时"], out.get("time_pillar_clock", "?")))
        print("  时辰翻转点：钟表时间 %s 起才算下一时辰；前一柱 %s、后一柱 %s"
              % (t["flip_point_clock"], t["prev_time_pillar"], t["next_time_pillar"]))
        print("  说明：只要记录的钟表时间早于翻转点，时柱就按上面那个；晚于它则用后一柱。")
    print("\n> 本工具只给**可核的历法与规则计算**。旺衰、格局、用神、吉凶属判读——"
          "回到原书条文上读（`skills/bazi-*`），本工具不下断语。")


if __name__ == "__main__":
    main()
