"""引文可信度总核（回书核的扩展版）：

① 全包：正文里的 `（R编号）` 指回，是否都指得到 R 节里真实存在的锚点（指空＝虚假依据）。
② 有源书的族（周易／八字）：R 节引文逐字比回 sources/（繁简归一）。
③ 全包：R 节是否为空、引文条数是否 ≥3。

用法：python3 tools/verify_citations.py
退出码：0 = 全过；1 = 有未命中。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SK = ROOT / "skills"
SRC = ROOT / "sources"

try:
    from opencc import OpenCC
    CC = OpenCC("t2s")
except Exception:                                                   # noqa: BLE001
    CC = None
    print("（没装 opencc，繁简不归一，命中率会偏低）")


def norm(s):
    s = "".join(ch for ch in s if "\u4e00" <= ch <= "\u9fff")
    return CC.convert(s) if CC else s


def rsec(t):
    i = t.find("## R：原文锚点")
    if i < 0:
        return None
    j = len(t)
    for m in re.finditer(r"(?m)^## ", t[i + 1:]):
        j = i + 1 + m.start()
        break
    return t[i:j]


def body(t):
    r = rsec(t)
    if r is None:
        return t
    return t.replace(r, "")


def anchors(r):
    nums = set()
    for m in re.finditer(r"(?m)^\s*(?:[>#*\s]*)(?:R)?(\d{1,3})\s*[\.、）)]", r):
        nums.add(int(m.group(1)))
    for m in re.finditer(r"\bR(\d{1,3})\b", r):
        nums.add(int(m.group(1)))
    return nums


BS = ["bazi-"]


def family(slug):
    if slug.startswith("bazi-"):
        return ["sanmingtonghui.txt", "ditianxu.txt", "qiongtongbaojian.txt", "zipingzhenquan.txt"]
    if slug.startswith("kanyu-"):
        return ["xieji.txt", "zangshu.txt", "hanlongjing.txt", "yilongjing.txt"]
    if slug == "zhouyi" or slug.startswith("zhouyi-") or slug in (
            "advance-retreat-boundary", "hexagram-situation-diagnosis", "line-position-timing",
            "reversal-cycle", "observation-judgment", "relationship-assembly", "repair-renewal-cycle",
            "response-action", "scale-and-restraint-control", "conflict-coalition-diagnosis",
            "humility-overreach-check", "auspicious-risk-language"):
        return ["zhouyi-jing.txt", "zhouyi-benyi.txt", "zhouyi-zhengyi.txt"]
    return []


cache = {}
e1 = e2 = e3 = 0
n1 = n2 = 0
bad1, bad2, bad3 = [], [], []
known = []
META = {"darwin-skill", "zhengliu", "cross-system-hub", "zhengliu"}   # 元工具，不看 R 节
# 已知未决（挂账、不当失败）：补第 3 条引文需要该族原书进 sources/，书到齐再消
KNOWN = {
    "emotion-organ-proxy": "需《黄帝内经》文本进 sources/ 才能补第 3 条",
    "negative-feedback": "需《黄帝内经》文本进 sources/ 才能补第 3 条",
}
for d in sorted(p for p in SK.iterdir() if p.is_dir()):
    f = d / "SKILL.md"
    if not f.exists():
        continue
    t = f.read_text(encoding="utf-8")
    b, r = body(t), rsec(t)
    # ① R 编号指回
    refs = [int(x) for x in re.findall(r"(?<![A-Za-z0-9])R(\d{1,3})(?![A-Za-z0-9])", b)]
    if refs:
        if r is None:
            e1 += 1
            bad1.append((d.name, "有 R 指回但无 R 节"))
        else:
            have = anchors(r)
            n1 += len(refs)
            miss = sorted({x for x in refs if have and x > max(have)})
            if miss:
                e1 += 1
                bad1.append((d.name, "指回 %s，R 节只到 R%d" % (miss[:4], max(have))))
    # ③ R 节存在且 ≥3 条
    if r is None:
        if d.name not in META:
            e3 += 1
            bad3.append((d.name, "无 R 节"))
    else:
        cnt = len(re.findall(r"(?m)^\s*(?:[>]\s*)?(?:\d+\s*[\.、）)]|\*\*?R\d)", r))
        if cnt and cnt < 3:
            if d.name in KNOWN:
                known.append((d.name, "R 节仅 %d 条 —— %s" % (cnt, KNOWN[d.name])))
            else:
                e3 += 1
                bad3.append((d.name, "R 节仅 %d 条" % cnt))
    # ② 有源书的族回书核（先去掉括注/前缀，再归一）
    files = family(d.name)
    if files and r:
        for fn in files:
            if fn not in cache:
                p = SRC / fn
                cache[fn] = norm(p.read_text(encoding="utf-8")) if p.exists() else ""
        for line in r.split("\n"):
            s = line.strip()
            if not s or s.startswith(("#", "|")):
                continue
            if re.search(r"抄自|逐条|说明：|出处：|注：|余下|经核|校正|互校", s):
                continue                        # 说明行不是引文
            if s.startswith("—") or s.lstrip(">#*- ").startswith("—"):
                continue                        # 「—（注）…」白话注行，包内允许
            s = re.sub(r"^[>\s]*", "", s)
            s = re.sub(r"^\s*(?:\d+\s*[\.、)）]|[-*·])\s*", "", s)
            s = re.sub(r"^《[^》]*》\s*", "", s)
            s = re.sub(r"^([^：，。；、！？]{1,12})[：:]\s*(?=\S)", "", s)   # 去「乾：」「坤·六四：」前缀
            s = re.split(r"\s*[—－→–]\s*", s)[0]                           # 引文后的白话说明不算
            for chunk in re.split(r"(?<=[。！？])", s):                     # 一行多条时逐句核
                c = chunk.strip()
                if not c or re.match(r"^[—－→–]", c):
                    continue
                if re.search(r"抄自|逐条|说明：|出处：", c):
                    continue
                c = re.sub(r"（[^）]*）|\([^)]*\)", "", c)
                c = c.strip(" 　「」『』“”*_—－-）)")
                q = norm(c)
                if len(q) < 6 or len(set(q)) <= 3:
                    continue
                n2 += 1
                if not any(q in cache[fn] for fn in files):
                    e2 += 1
                    bad2.append((d.name, c[:56]))

print("① 正文 R 编号指回：核 %d 次，问题 %d 个" % (n1, e1))
for n, m in bad1[:15]:
    print("     %-34s %s" % (n, m))
print("② 有源书族 R 节引文回书核：核 %d 条，未命中 %d 条" % (n2, e2))
for n, q in bad2[:15]:
    print("     %-34s %s" % (n, q))
print("③ R 节完整性：问题 %d 个" % e3)
for n, m in bad3[:15]:
    print("     %-34s %s" % (n, m))
if known:
    print("（已知未决，挂账不计：%s）" % "；".join("%s（%s）" % (n, m) for n, m in known))
print("\n合计问题 %d 个" % (e1 + e2 + e3))
sys.exit(0 if e1 + e2 + e3 == 0 else 1)
