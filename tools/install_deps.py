#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""依赖体检 / 安装（默认走国内源）。

口径（AGENTS.md 硬规矩 11）：
  * Python 依赖**一律走国内镜像**（默认清华，备选阿里云）；官方 pypi.org 在本环境拉不动。
  * **加 skill / 加维度 / 从新书蒸馏之前，先把依赖装完**——装完再登记、再自检。

依赖来源（三处合并去重）：
  1. 包根目录 `requirements.txt`（逐行，支持 `#` 注释与 `-e`/`-r` 除外）
  2. 每个 `skills/*/SKILL.md` frontmatter 里可选的 `requires`：
         requires:
           pip: [pymeeus]                    # 需要 import 的 Python 包（pip 名）
           commands: [python3]               # 需要存在的可执行命令
           data: [geocode_photon, terrain_terrarium, water_overpass]
                                             # 需要联网取数的数据源（登记在下面 DATA_SOURCES）
  3. 数据源连通探针：**pip 包缺了能装；数据源缺了装不了**，所以「跑数据前先查」——
     声明了 `data:` 的 skill，本脚本会在跑数前做最小探针（超时 12s），
     并且能分辨「通但内容是坏的」（例：某些 Overpass 实例返回非法时间戳、对任何地点都是 0 条）。

用法：
    python tools/install_deps.py                 # 只体检（默认，不装）；含数据源连通
    python tools/install_deps.py --install       # 缺什么装什么（国内源）
    python tools/install_deps.py --install --mirror https://mirrors.aliyun.com/pypi/simple/
    python tools/install_deps.py --no-probe      # 离线场景：跳过数据源探针
    python tools/install_deps.py --json
退出码：0 = 依赖齐备（或已装好）；1 = 有缺失（pip / 命令 / 数据源 / 未登记的数据源名）。
"""

import argparse
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"

MIRRORS = ["https://pypi.tuna.tsinghua.edu.cn/simple",
           "https://mirrors.aliyun.com/pypi/simple/"]

# ---- 数据源（网络依赖）体检表 ----
# 口径：缺 pip 包能装；**数据源装不了**，所以只能"跑数据前先查"，查不通就停下报清楚。
# 每个源给一条最小探针；探针要快（超时 20s）且能分辨"通但内容是坏的"（见 water_overpass）。
def _ok_overpass_status(b):
    """Overpass 的 /api/status 探针：健康实例返回纯文本
       'Connected as: ... | Current time: ... | ... | N slots available now. |'
    实测的好坏判别（比解释器查询轻得多，且能一次分干净）：
      好：z. / lz4. / overpass-api.de → 200 + Connected as + 有 slots
      坏：osm.ch → 返回的是 XML 错误文档（没有 'Connected as'）
          kumi  → Rate limit: 0，没有 'slots available now'
          private.coffee → 500
    """
    if b"Connected as:" not in b:
        return False, "不是健康实例（没有 Connected as 状态文本）"
    import re as _re
    m = _re.search(rb"(\d+)\s+slots available now", b)
    if not m:
        return False, "没有空闲槽位（实例在满负荷）"
    return True, "%s 个空闲槽位" % m.group(1).decode()


def _ok_png(b):
    return b[:4] == b"\x89PNG"


def _ok_features(b):
    return b'"features"' in b


DATA_SOURCES = {
    "geocode_photon": {
        "label": "地名解析 photon.komoot.io",
        "urls": ["https://photon.komoot.io/api/?q=Shangrao&limit=1"],
        "method": "GET",
        "expect": _ok_features,
        "note": "带 lang 参数会 400；同名地名会解错，取数器会列候选供核对",
    },
    "terrain_terrarium": {
        "label": "地形瓦片 AWS Terrarium（30m 级）",
        "urls": ["https://elevation-tiles-prod.s3.amazonaws.com/terrarium/13/6739/3444.png"],
        "method": "GET",
        "expect": _ok_png,
        "note": "主力地形源；单点高程备选 api.opentopodata.org / api.open-elevation.com",
    },
    "water_overpass": {
        "label": "水系 Overpass（多镜像）",
        "urls": ["https://z.overpass-api.de/api/status",
                 "https://lz4.overpass-api.de/api/status",
                 "https://overpass-api.de/api/status",
                 "https://maps.mail.ru/osm/tools/overpass/api/status",
                 "https://overpass.kumi.systems/api/status",
                 "https://overpass.private.coffee/api/status",
                 "https://overpass.osm.ch/api/status"],
        "method": "OVERPASS_STATUS",
        "expect": _ok_overpass_status,
        "note": "探针走 /api/status（比解释器查询轻得多）：z / lz4 实测**真查询也通**，de 有槽位但常瞬时 too busy（要重试）。"
                "**osm.ch 是坏实例**：/api/status 返回的是错误文档、不是状态文本，本探针直接判它不健康——"
                "而它的 HTTP 状态码是 200、解释器还对任何地点返回 0 条，光看状态码会误判。"
                "区域大势的离线替代：`water_hydrorivers`（HydroRIVERS 亚洲河网 86MB）",
    },
    "water_hydrorivers": {
        "label": "水系 HydroRIVERS 亚洲河网（离线，区域大势用）",
        "urls": ["https://data.hydrosheds.org/file/HydroRIVERS/HydroRIVERS_v10_as_shp.zip"],
        "method": "HEAD_SIZE",
        "expect": lambda b: True,
        "min_bytes": 50 * 1024 * 1024,
        "note": "86MB，一次性下载后本地查（缓存目录 `~/.hermes/cache/hydrorivers/`，**不入包**）；"
                "比 OSM 粗（约 500m、只收流域面积 ≥10km² 的河道），且**没有河名字段**（河名只能从 OSM 取），"
                "但**离线、不受实例波动影响**，适合「水从哪来到哪去」的区域粗读；"
                "带 ORD_FLOW（河流级别）与 UPLAND_SKM（上游流域面积），可据此排干流/支流",
    },
}


def probe_data_source(name, timeout=20):
    """返回 (ok, 说明)。只做最小探针，不拉数据。"""
    import urllib.request
    import urllib.error
    import urllib.parse
    spec = DATA_SOURCES[name]
    tries = []
    for url in spec["urls"]:
        for attempt in (1, 2):
            try:
                if spec["method"] == "HEAD_SIZE":
                    req = urllib.request.Request(url, method="HEAD",
                                                 headers={"User-Agent": "cross-system-deps/1.0"})
                    r = urllib.request.urlopen(req, timeout=timeout)
                    size = int(r.headers.get("Content-Length", 0) or 0)
                    ok = r.status == 200 and size >= spec.get("min_bytes", 0)
                    tries.append("%s → %s" % (url.split("/")[2],
                                              "%s（%.1f MB）" % (r.status, size / 1048576) if size else str(r.status)))
                    if ok:
                        return True, "；".join(tries)
                    break
                if spec["method"] == "OVERPASS_STATUS":
                    req = urllib.request.Request(url, headers={"User-Agent": "cross-system-deps/1.0"})
                    raw = urllib.request.urlopen(req, timeout=timeout).read()
                    ok, why = spec["expect"](raw)
                    tries.append("%s → %s" % (url.split("/")[2], why))
                    if ok:
                        return True, "；".join(tries)
                    break
                if spec["method"] == "POST_STATUS":
                    q = urllib.parse.urlencode(
                        {"data": '[out:json][timeout:10];node(1);out count;'}).encode()
                    req = urllib.request.Request(url, data=q,
                                                 headers={"User-Agent": "cross-system-deps/1.0"})
                    raw = urllib.request.urlopen(req, timeout=timeout).read()
                    if b"too busy" in raw[:2000] or b"<strong" in raw[:2000]:
                        tries.append("%s → 忙（第 %d 次）" % (url.split("/")[2], attempt))
                        time.sleep(2)
                        continue
                    ok = _ok_overpass(raw)
                    tries.append("%s → %s" % (url.split("/")[2], "时间戳有效" if ok else "时间戳非法/内容异常"))
                    if ok:
                        return True, "；".join(tries)
                    break
                req = urllib.request.Request(url, headers={"User-Agent": "cross-system-deps/1.0"})
                raw = urllib.request.urlopen(req, timeout=timeout).read()
                ok = spec["expect"](raw)
                tries.append("%s → %s" % (url.split("/")[2], "ok" if ok else "内容不符"))
                if ok:
                    return True, "；".join(tries)
                break
            except Exception as e:                            # noqa: BLE001
                tries.append("%s → %s" % (url.split("/")[2], str(e)[:60]))
                break
    return False, "；".join(tries)

# pip 名 → import 名（不一样的那些）
IMPORT_NAME = {
    "pyswisseph": "swisseph",
    "pyyaml": "yaml",
    "pillow": "PIL",
    "pyshp": "shapefile",
    "lunar_python": "lunar_python",
    "ephem": "ephem",
    "beautifulsoup4": "bs4",
    "python-dateutil": "dateutil",
    "scikit-learn": "sklearn",
    "opencv-python": "cv2",
    "pymupdf": "fitz",
    "rapidocr-onnxruntime": "rapidocr_onnxruntime",
}


def pkg_name(spec):
    """'pymeeus>=0.5.12' → 'pymeeus'"""
    for sep in (">=", "<=", "==", "~=", "!=", ">", "<", "[", " ", ";"):
        spec = spec.split(sep)[0]
    return spec.strip()


def import_name(pip_name):
    return IMPORT_NAME.get(pip_name.lower(), pip_name.lower().replace("-", "_"))


def installed(pip_name):
    return importlib.util.find_spec(import_name(pip_name)) is not None


def read_requirements(path):
    out = []
    if not path.exists():
        return out
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.split("#")[0].strip()
        if not line or line.startswith("-"):
            continue
        out.append(line)
    return out


def read_skill_requires():
    """{slug: {"pip": [...], "commands": [...], "data": [...]}}"""
    out = {}
    try:
        import yaml
    except Exception:
        yaml = None
    for d in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        sk = d / "SKILL.md"
        if not sk.exists():
            continue
        text = sk.read_text(encoding="utf-8")
        if not text.startswith("---"):
            continue
        end = text.find("\n---", 3)
        if end == -1:
            continue
        raw = text[3:end]
        obj = None
        if yaml:
            try:
                obj = yaml.safe_load(raw)
            except Exception:
                obj = None
        req = (obj or {}).get("requires") if isinstance(obj, dict) else None
        if isinstance(req, dict):
            pip = [str(x) for x in (req.get("pip") or [])]
            cmds = [str(x) for x in (req.get("commands") or [])]
            data = [str(x) for x in (req.get("data") or [])]
            if pip or cmds or data:
                out[d.name] = {"pip": pip, "commands": cmds, "data": data}
    return out


def command_exists(cmd):
    from shutil import which
    return which(cmd) is not None


def main():
    ap = argparse.ArgumentParser(description="依赖体检 / 安装（默认国内源）")
    ap.add_argument("--install", action="store_true", help="缺失时自动安装（国内源）")
    ap.add_argument("--mirror", default=None, help="指定镜像 index-url（默认清华，失败自动换阿里云）")
    ap.add_argument("--requirements", default=str(ROOT / "requirements.txt"))
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--no-probe", action="store_true",
                    help="跳过数据源连通探针（离线场景）；默认会探")
    a = ap.parse_args()

    reqs = read_requirements(Path(a.requirements))
    skill_req = read_skill_requires()

    missing_pip, ok_pip = [], []
    for spec in reqs:
        nm = pkg_name(spec)
        (ok_pip if installed(nm) else missing_pip).append((nm, "requirements.txt"))
    for slug, r in skill_req.items():
        for nm in r["pip"]:
            if not installed(nm):
                missing_pip.append((nm, f"skill:{slug}"))
            else:
                ok_pip.append((nm, f"skill:{slug}"))
    missing_cmd = [(c, s) for s, r in skill_req.items() for c in r["commands"] if not command_exists(c)]

    # ---- 数据源连通（网络依赖）----
    declared = sorted({d for r in skill_req.values() for d in r.get("data", [])})
    unknown = [d for d in declared if d not in DATA_SOURCES]
    data_status = {}
    if declared and not a.no_probe:
        for nm in declared:
            if nm in DATA_SOURCES:
                ok, why = probe_data_source(nm)
                data_status[nm] = {"ok": ok, "why": why, "label": DATA_SOURCES[nm]["label"]}
    missing_data = sorted(n for n, v in data_status.items() if not v["ok"])

    result = {
        "requirements_file": str(a.requirements),
        "skills_with_requires": {k: v for k, v in skill_req.items()},
        "ok": sorted(set(n for n, _ in ok_pip)),
        "missing_pip": sorted(set(n for n, _ in missing_pip)),
        "missing_commands": sorted(set(c for c, _ in missing_cmd)),
        "data_sources_declared": declared,
        "data_sources_unknown": unknown,
        "data_sources": data_status,
        "missing_data_sources": missing_data,
        "probe_skipped": bool(a.no_probe),
        "installed_now": [],
    }

    if not a.install:
        if a.json:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            print(f"依赖来源：{a.requirements}"
                  + (f"；声明了 requires 的 skill：{', '.join(skill_req) or '无'}" if skill_req else ""))
            print(f"已具备：{', '.join(result['ok']) or '（无）'}")
            print(f"缺失 pip 包：{', '.join(result['missing_pip']) or '（无）'}")
            print(f"缺失命令：{', '.join(result['missing_commands']) or '（无）'}")
            if declared:
                if a.no_probe:
                    print(f"数据源（已跳过探针，--no-probe）：{', '.join(declared)}")
                else:
                    print("数据源连通（跑数据前必查）:")
                    for nm in declared:
                        v = data_status.get(nm)
                        if not v:
                            print(f"  ✗ {nm}：**未登记的数据源名**（DATA_SOURCES 里没有）")
                            continue
                        print(f"  {'✓' if v['ok'] else '✗'} {v['label']}：{v['why']}")
            if result["missing_pip"] or result["missing_commands"] or missing_data or unknown:
                print()
                if result["missing_pip"] or result["missing_commands"]:
                    print("装法（国内源）：python tools/install_deps.py --install")
                if missing_data:
                    print("数据源装不了，只能：① 等一会重试 ② 换镜像（见 DATA_SOURCES）"
                          " ③ 缺的那一项照实写进回答（别说没取到就是没有）")
                if unknown:
                    print("未登记的数据源名：%s —— 先把它登记进 tools/install_deps.py 的 DATA_SOURCES"
                          % ", ".join(unknown))
        sys.exit(1 if (result["missing_pip"] or result["missing_commands"]
                       or missing_data or unknown) else 0)

    # ---- 安装 ----
    if not result["missing_pip"]:
        print("没有缺失的 pip 包，无需安装。")
    else:
        mirrors = [a.mirror] if a.mirror else MIRRORS
        got = False
        for m in mirrors:
            cmd = [sys.executable, "-m", "pip", "install", "-i", m] + result["missing_pip"]
            print("$ " + " ".join(cmd))
            if subprocess.call(cmd) == 0:
                result["installed_now"] = result["missing_pip"]
                print(f"已从 {m} 装好：{', '.join(result['installed_now'])}")
                got = True
                break
            print(f"[{m} 装失败，换下一个镜像]")
        if not got:
            print("所有镜像都没装上——先别往下走（登记/自检前把依赖补齐）。", file=sys.stderr)
            sys.exit(1)

    if a.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    sys.exit(0)


if __name__ == "__main__":
    main()
