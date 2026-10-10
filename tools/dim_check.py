#!/usr/bin/env python3
"""维度一致性自检：注册表 ↔ skills/ 目录 ↔ hub 的维度概览表与 H 节名单 ↔ 计数。

用法（包根目录）：python tools/dim_check.py
退出码：0 = 全对；1 = 有硬错误。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
HUB = SKILLS / "cross-system-hub/SKILL.md"
REG = SKILLS / "cross-system-hub/dimensions.registry.md"
# 不属于任何维度、只作工具用的 skill（不算漏登记）
UNMETA_UTIL = {"cross-system-hub"}

errors, warnings = [], []


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")] if line.strip().startswith("|") else None


# ---- 注册表 ----
# 元工具（不是维度）：从注册表的「元工具」表读
META = {c[0].strip("*") for c in (cells(l) for l in REG.read_text(encoding="utf-8").split("\n"))
        if c and len(c) == 5 and c[0].startswith("**")}
UTIL = UNMETA_UTIL | META   # skills/ 只放：总入口 + 分析维度 + 元工具

reg_rows = []
for line in REG.read_text(encoding="utf-8").split("\n"):
    c = cells(line)
    if c and len(c) == 8 and re.match(r"^\d", c[0]):
        reg_rows.append({"order": c[0], "name": c[1], "layer": c[2], "entry": c[3].strip("`"),
                         "signals": c[4], "count": c[7]})
if not reg_rows:
    sys.exit("注册表没解析出维度行（检查 dimensions.registry.md 的表格）")

# ---- hub 的维度概览表 / H 节 ----
hub_lines = HUB.read_text(encoding="utf-8").split("\n")
overview, hgroups, cur = [], {}, None
for i, line in enumerate(hub_lines):
    c = cells(line)
    if c and len(c) == 6 and c[0].isdigit() and c[2] in ("观察", "象征", "校准"):
        overview.append({"name": c[1].strip("*"), "layer": c[2], "signals": c[4], "count": c[5]})
    m = re.match(r"^###\s+(.*?)\s*\((\d+)个\)\s*$", line)
    if m:
        cur = m.group(1)
        hgroups[cur] = {"count": int(m.group(2)), "slugs": []}
        continue
    if cur:
        if line.startswith("###") or line.startswith("## "):
            cur = None
            continue
        c2 = cells(line)
        if c2 and c2[0].startswith("`"):
            hgroups[cur]["slugs"].append(c2[0].strip("`"))

dirs = {p.name for p in SKILLS.iterdir() if p.is_dir()}

# 1) 注册表 ↔ hub 概览表
if len(reg_rows) != len(overview):
    errors.append(f"注册表 {len(reg_rows)} 行 vs hub 概览表 {len(overview)} 行，数量不一致")
for r, o in zip(reg_rows, overview):
    rn = r["name"].replace(" ", "")
    if rn != o["name"].replace(" ", ""):
        errors.append(f"注册表维度 {r['name']!r} 与 hub 概览表 {o['name']!r} 顺序/名称不一致")
    if r["layer"] != o["layer"]:
        errors.append(f"{r['name']}: 层不一致（注册表 {r['layer']} / hub {o['layer']}）")
    if r["count"] != o["count"]:
        errors.append(f"{r['name']}: skill 数不一致（注册表 {r['count']} / hub {o['count']}）")

# 2) 每个维度的目录/名单
matched = set()
for r in reg_rows:
    name, entry, cnt = r["name"], r["entry"], r["count"]
    if cnt == "待接入":
        warnings.append(f"{name}: 标为待接入，跳过（{entry}）")
        continue
    try:
        want = int(cnt)
    except ValueError:
        errors.append(f"{name}: skill 数列不是数字也不是'待接入'：{cnt!r}")
        continue
    if entry.endswith("*"):
        pre = entry[:-1]
        hit = sorted(d for d in dirs if d.startswith(pre))
        matched |= set(hit)
        if len(hit) != want:
            errors.append(f"{name}: 目录里有 {len(hit)} 个 `{pre}*`，注册表写 {want}")
        for s in hit:
            if not any(s in g["slugs"] for g in hgroups.values()):
                warnings.append(f"{name}: {s} 在 skills/ 里但 H 节没列")
    else:
        # 目录归属：以 H 节名单为准
        KEY = {"毛选": "毛泽东思想", "黄帝内经": "黄帝内经", "周易": "周易", "决策框架": "决策框架"}
        kw = KEY.get(name, name)
        grp = next((g for t, g in hgroups.items() if kw in t), None)
        if grp is None:
            errors.append(f"{name}: H 节找不到对应分组（入口写的是'{entry}'，需要人工归属）")
            continue
        if grp["count"] != want or len(grp["slugs"]) != want:
            errors.append(f"{name}: H 节写 {grp['count']} 个、列了 {len(grp['slugs'])} 个，注册表写 {want}")
        for s in grp["slugs"]:
            matched.add(s)
            if s not in dirs:
                errors.append(f"{name}: H 节列的 {s} 在 skills/ 里不存在")

# 2.5) 描述行里的层计数（"观察 N / 象征 M / 校准 K"）与实际是否一致
from collections import Counter
cnt = Counter(r["layer"] for r in reg_rows)   # 含"待接入"，因为描述里的总数把待接入也算进去了
for path, label in ((HUB, "hub 描述"), (ROOT / "README.md", "README 导语")):
    t = path.read_text(encoding="utf-8")[:2000]
    m = re.search(r"观察\s*(\d+)\s*/\s*象征\s*(\d+)\s*/\s*校准\s*(\d+)", t)
    if m:
        got = {"观察": int(m.group(1)), "象征": int(m.group(2)), "校准": int(m.group(3))}
        for k in got:
            if got[k] != cnt.get(k, 0):
                errors.append(f"{label}: 写 {k} {got[k]} 个，注册表实际 {cnt.get(k, 0)} 个")

# 2.8) 元工具目录存在性
for m in sorted(META):
    if m not in dirs:
        errors.append(f"元工具 {m}: 注册表登记了，但 skills/ 里没有这个目录")

# 3) 有没有漏登记的目录
for d in sorted(dirs - matched - UTIL):
    warnings.append(f"{d}: 在 skills/ 里，但没有任何维度登记它")

# 4) 骨架完备性：frontmatter 四字段 + 正文十节 + test-prompts 三类用例。
#    老体系（旧骨架）尚未补齐，默认只作警告；STRICT_SKELETON=1 时计为硬错误。
import json as _json
import os as _os

SKELETON_SKIP = {"cross-system-hub", "darwin-skill", "zhengliu"}   # 总入口 + 元工具不按子 skill 骨架要求
# 十节（节名不统一的旧写法也需归一到同一套；这里按标题关键字判定）
SKELETON_SECTIONS = (
    ("触发条件", lambda h: "触发条件" in h),
    ("R：原文锚点", lambda h: h == "R" or bool(re.match(r"^R[\s:：\-—]", h))),
    ("I：核心解释", lambda h: "核心解释" in h or bool(re.match(r"^I[\s:：\-—]", h))),
    ("A1：来源应用", lambda h: "来源应用" in h or bool(re.match(r"^A1[\s:：\-—]", h))),
    ("A2：典型触发场景", lambda h: "典型触发场景" in h or bool(re.match(r"^A2[\s:：\-—]", h))),
    ("E：执行步骤", lambda h: "执行步骤" in h or bool(re.match(r"^E[\s:：\-—]", h))),
    ("B：边界与失败模式", lambda h: "边界" in h or "失败模式" in h or bool(re.match(r"^B[\s:：\-—]", h))),
    ("练习手册", lambda h: "练习" in h),
    ("反例", lambda h: "反例" in h),
    ("灰色地带", lambda h: "灰色地带" in h),
)
FM_FIELDS = ("name", "description")


def _headings(text):
    hs = []
    for line in text.split("\n"):
        m = re.match(r"^#{1,6}\s+(.*?)\s*$", line)
        if m:
            hs.append(re.sub(r"^[^0-9A-Za-z\u4e00-\u9fff]+", "", m.group(1)))  # 去掉 emoji/符号前缀
    return hs


def _frontmatter(text):
    if not text.startswith("---"):
        return None, None
    end = text.find("\n---", 3)
    raw = text[3:end] if end != -1 else None
    obj = None
    if raw is not None:
        try:
            import yaml
            obj = yaml.safe_load(raw)
        except Exception:
            obj = None
    return (obj if isinstance(obj, dict) else None), raw


def _fm_has(obj, raw, key):
    if isinstance(obj, dict):
        return key in obj and obj[key] not in (None, "", [], {})
    return bool(raw and re.search(rf"(?m)^{re.escape(key)}\s*:", raw))


def _schema_bad(fm, raw, parent, subs):
    """父字段(parent)下的子字段(subs)是否缺失；YAML 解析失败时退化为文本匹配。"""
    if isinstance(fm, dict) and isinstance(fm.get(parent), dict):
        return [s for s in subs if fm[parent].get(s) is None]
    if raw and re.search(rf"(?m)^{parent}\s*:", raw):
        return [s for s in subs if not re.search(rf"(?m)^[ \t]+{re.escape(s)}\s*:", raw)]
    return list(subs)


def _test_classes(obj, out):
    """递归收集测试用例标记，归一到 should_trigger / should_not_trigger / boundary。"""
    def cls(s):
        t = str(s).lower().replace("-", "_")
        if "not_trigger" in t or "no_trigger" in t or "不应触发" in str(s) or "不应该触发" in str(s):
            return "should_not_trigger"
        if "trigger" in t or "触发" in str(s) or "激活" in str(s):
            return "should_trigger"
        if "edge" in t or "boundary" in t or "边界" in str(s) or "边缘" in str(s):
            return "boundary"
        return None
    if isinstance(obj, dict):
        if "type" in obj:
            c = cls(obj["type"])
            if c:
                out.add(c)
        for k, v in obj.items():
            if isinstance(v, (list, dict)) and v and cls(k):
                out.add(cls(k))
            _test_classes(v, out)
    elif isinstance(obj, list):
        for v in obj:
            _test_classes(v, out)
    return out


def _skeleton_missing(d):
    miss = []
    sk = SKILLS / d / "SKILL.md"
    if not sk.exists():
        return ["SKILL.md"]
    text = sk.read_text(encoding="utf-8")
    fm, raw = _frontmatter(text)
    for f in FM_FIELDS:
        if not _fm_has(fm, raw, f):
            miss.append(f"frontmatter.{f}")
    if _schema_bad(fm, raw, "input_schema", ("required", "optional")):
        miss.append("frontmatter.input_schema(required/optional)")
    if _schema_bad(fm, raw, "output_schema", ("primary", "secondary")):
        miss.append("frontmatter.output_schema(primary/secondary)")
    heads = _headings(text)
    for label, pred in SKELETON_SECTIONS:
        if not any(pred(h) for h in heads):
            miss.append("节 " + label)
    tp = SKILLS / d / "test-prompts.json"
    if not tp.exists():
        miss.append("test-prompts.json")
    else:
        try:
            got = _test_classes(_json.loads(tp.read_text(encoding="utf-8")), set())
        except Exception:
            got = set()
        for need, tag in (("should_trigger", "应该触发"), ("should_not_trigger", "不应触发"), ("boundary", "边界")):
            if need not in got:
                miss.append("test-prompts 缺" + tag)
    return miss


# 2) 硬闸门（显式请求才激活）：注册表标了闸门 ↔ 入口 skill 的触发条件里必须有闸门
#    依据：AGENTS.md 硬规矩 12、docs/扩展手册.md 情形 B「新维度要不要设硬闸门」
GATE_MARK = "硬闸门"


def _gated(sig):
    return bool(sig) and (GATE_MARK in sig or "⛔" in sig)


for idx, r in enumerate(reg_rows):
    entry = r["entry"]

    def _resolve_entry(r, entry=entry):
        """把注册表的「入口」解析成一个真实 skill 目录（入口列可能是 `kanyu-*` 这种前缀）。"""
        if entry in dirs:
            return entry
        pre = entry.rstrip("*").rstrip("-")
        if not pre:
            return None
        cands = sorted(s for s in dirs if s == pre or s.startswith(pre + "-"))
        for s in cands:
            if s.endswith("-hub"):
                return s
        for gname, g in hgroups.items():
            if r["name"] and r["name"] in gname:
                for s in g["slugs"]:
                    if s in cands:
                        return s
        return cands[0] if cands else None

    edir = _resolve_entry(r)
    reg_gated = _gated(r.get("signals", ""))
    hub_gated = _gated(overview[idx].get("signals", "")) if idx < len(overview) else False
    if edir is None:
        if reg_gated:
            errors.append(f"{r['name']}: 注册表标了硬闸门，但入口 {entry} 解析不出具体 skill 目录")
        continue
    text = (SKILLS / edir / "SKILL.md").read_text(encoding="utf-8")
    sk_gated = GATE_MARK in text
    if reg_gated and not sk_gated:
        errors.append(f"{r['name']}: 注册表标了硬闸门，但入口 {edir}/SKILL.md 的触发条件里没有闸门说明")
    if sk_gated and not reg_gated:
        errors.append(f"{r['name']}: 入口 {edir}/SKILL.md 写了硬闸门，但注册表这一行没标（两处不一致）")
    if reg_gated and not hub_gated:
        errors.append(f"{r['name']}: 注册表标了硬闸门，但 hub 维度概览表这一行没标（⛔/硬闸门）")
    if reg_gated and sk_gated and "不显示" not in text:
        warnings.append(f"{r['name']}: 入口 {edir} 的闸门没写明「不显示」（闸门没过应整行不出现）")

skel_dirs = sorted(dirs - SKELETON_SKIP)
skel_missing = {d: m for d in skel_dirs if (m := _skeleton_missing(d))}
skel_strict = _os.environ.get("STRICT_SKELETON") == "1"
for d in sorted(skel_missing):
    (errors if skel_strict else warnings).append("骨架 " + d + ": 缺 " + "，".join(skel_missing[d]))
skel_complete = len(skel_dirs) - len(skel_missing)
skel_tally = Counter(m for ms in skel_missing.values() for m in ms)

print(f"注册表 {len(reg_rows)} 维 + 元工具 {len(META)} 个；skills/ 里 {len(dirs)} 个目录；H 节 {len(hgroups)} 组")
print(f"骨架完备 {skel_complete}/{len(skel_dirs)}")
for m, n in skel_tally.most_common(5):
    print(f"  缺项 top：{m} × {n}")
for w in warnings:
    print("WARN", w)
for e in errors:
    print("ERROR", e)
print(f"\n{len(errors)} 个错误，{len(warnings)} 个警告")
sys.exit(1 if errors else 0)
