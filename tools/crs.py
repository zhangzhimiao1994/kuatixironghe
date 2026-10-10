"""坐标系互转（相地取数用）。

为什么要它：**同一处地方，各家地图显示的数字不一样**。
  · WGS-84  —— 真实经纬度。GPS 原始输出、OpenStreetMap、Google、本包取数源（photon / DEM）都用它。
  · GCJ-02  —— 中国官方加密坐标（俗称「火星坐标」）。**高德、腾讯、微信内置地图**显示的是它。
  · BD-09   —— 百度在 GCJ-02 上再偏移一次。**百度地图**显示的是它。
境内 GCJ-02 与 WGS-84 一般差 **100–700 米**，BD-09 又多一重偏移。
所以：**从百度/高德抄来的数字，必须说明是哪一家，否则点位会系统性挪几百米。**

算法为公开实现（Krasovsky 椭球参数的标准做法，与各家 SDK 一致到厘米级）。
"""
import math

A = 6378245.0                     # Krasovsky 1940 长半轴
EE = 0.00669342162296594323       # 第一偏心率平方


def out_of_china(lng, lat):
    """境外不做偏移（各家实现一致：境外返回原值）。"""
    return not (73.66 < lng < 135.05 and 3.86 < lat < 53.55)


def _tlat(x, y):
    r = (-100.0 + 2.0 * x + 3.0 * y + 0.2 * y * y + 0.1 * x * y
         + 0.2 * math.sqrt(abs(x)))
    r += (20.0 * math.sin(6.0 * x * math.pi) + 20.0 * math.sin(2.0 * x * math.pi)) * 2.0 / 3.0
    r += (20.0 * math.sin(y * math.pi) + 40.0 * math.sin(y / 3.0 * math.pi)) * 2.0 / 3.0
    r += (160.0 * math.sin(y / 12.0 * math.pi) + 320 * math.sin(y * math.pi / 30.0)) * 2.0 / 3.0
    return r


def _tlng(x, y):
    r = (300.0 + x + 2.0 * y + 0.1 * x * x + 0.1 * x * y
         + 0.1 * math.sqrt(abs(x)))
    r += (20.0 * math.sin(6.0 * x * math.pi) + 20.0 * math.sin(2.0 * x * math.pi)) * 2.0 / 3.0
    r += (20.0 * math.sin(x * math.pi) + 40.0 * math.sin(x / 3.0 * math.pi)) * 2.0 / 3.0
    r += (150.0 * math.sin(x / 12.0 * math.pi) + 300.0 * math.sin(x / 30.0 * math.pi)) * 2.0 / 3.0
    return r


def wgs2gcj(lng, lat):
    if out_of_china(lng, lat):
        return lng, lat
    dlat = _tlat(lng - 105.0, lat - 35.0)
    dlng = _tlng(lng - 105.0, lat - 35.0)
    rad = lat / 180.0 * math.pi
    m = 1 - EE * math.sin(rad) ** 2
    sm = math.sqrt(m)
    dlat = (dlat * 180.0) / ((A * (1 - EE)) / (m * sm) * math.pi)
    dlng = (dlng * 180.0) / (A / sm * math.cos(rad) * math.pi)
    return lng + dlng, lat + dlat


def gcj2wgs(gcj_lng, gcj_lat, iters=8):
    """反解：WGS ≈ GCJ 减去该处偏移，迭代收敛到厘米级。"""
    lng, lat = gcj_lng, gcj_lat
    for _ in range(iters):
        tl, tt = wgs2gcj(lng, lat)
        lng += gcj_lng - tl
        lat += gcj_lat - tt
    return lng, lat


X_PI = math.pi * 3000.0 / 180.0


def gcj2bd(gcj_lng, gcj_lat):
    z = math.sqrt(gcj_lng * gcj_lng + gcj_lat * gcj_lat) + 0.00002 * math.sin(gcj_lat * X_PI)
    th = math.atan2(gcj_lat, gcj_lng) + 0.000003 * math.cos(gcj_lng * X_PI)
    return z * math.cos(th) + 0.0065, z * math.sin(th) + 0.006


def bd2gcj(bd_lng, bd_lat):
    x, y = bd_lng - 0.0065, bd_lat - 0.006
    z = math.sqrt(x * x + y * y) - 0.00002 * math.sin(y * X_PI)
    th = math.atan2(y, x) - 0.000003 * math.cos(x * X_PI)
    return z * math.cos(th), z * math.sin(th)


# ---- 对外统一入口 ----
CRS_ALIAS = {
    "wgs84": "wgs84", "wgs": "wgs84", "gps": "wgs84", "osm": "wgs84",
    "gcj02": "gcj02", "gcj": "gcj02", "amap": "gcj02", "gaode": "gcj02",
    "tencent": "gcj02", "qq": "gcj02", "wechat": "gcj02", "weixin": "gcj02",
    "bd09": "bd09", "bd": "bd09", "baidu": "bd09",
}


def to_wgs84(lng, lat, crs="wgs84"):
    """把任意坐标系的一对经纬度转成 WGS-84（本包取数源用的坐标）。返回 (lng, lat)。"""
    c = CRS_ALIAS.get(str(crs).strip().lower())
    if c is None:
        raise ValueError("不认识的坐标系 %r；可用：wgs84 / gcj02（高德·腾讯·微信）/ bd09（百度）" % crs)
    if c == "wgs84":
        return lng, lat
    if c == "gcj02":
        return gcj2wgs(lng, lat)
    return gcj2wgs(*bd2gcj(lng, lat))


def offset_meters(lng1, lat1, lng2, lat2):
    """两点相差多少米（小范围近似，够用于报「偏了多少米」）。"""
    dx = (lng2 - lng1) * 111320.0 * math.cos(math.radians(lat1))
    dy = (lat2 - lat1) * 110540.0
    return math.hypot(dx, dy)
