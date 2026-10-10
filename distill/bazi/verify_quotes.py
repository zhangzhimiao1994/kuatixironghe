#!/usr/bin/env python3
"""回书核 · 子平八字（bazi）

把 skills/bazi-*/SKILL.md 的 R 节引文逐条回三本源文件比对。
规矩（distill/bazi/STYLE.md 第二节）：引文必须是原书原话、逐字；归一化时只留汉字字形。

用法（包根目录）：
    python distill/bazi/verify_quotes.py                 # 核全部 bazi-*
    python distill/bazi/verify_quotes.py bazi-sanming-* bazi-ditian-gan-zhi
退出码：0 = R 节齐全且全部命中；1 = 有未命中或 R 条数不足。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SKILLS = ROOT / "skills"
SRC = ROOT / "sources"
BOOKS = ["sanmingtonghui", "ditianxu", "qiongtongbaojian", "zipingzhenquan"]
MIN_LEN = 8          # 归一化后短于此长度的片段不单独判（避免常见短语误判）
MIN_QUOTES = 3

CJK = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")
NOISE = [
    re.compile(r"[（(][^（()）]*《[^》]*》[^（()）]*[）)]"),        # （《书名》卷次·篇名）
    re.compile(r"[（(][^（()）]*(?:原注|任注|經注|经注|经文|經文|補充|补充|注)[^（()）]*[）)]"),
]


def norm(s):
    """只留汉字字形（忽略空白、标点、数字、拉丁、括号）。"""
    return "".join(CJK.findall(s))


def load_sources():
    out = {}
    for b in BOOKS:
        p = SRC / ("%s.txt" % b)
        if p.exists():
            out[b] = norm(p.read_text(encoding="utf-8"))
    return out


def r_section(text):
    m = re.search(r"(?m)^##\s*R[^\n]*$", text)
    if not m:
        return None
    rest = text[m.end():]
    m2 = re.search(r"(?m)^##\s", rest)
    return rest[: m2.start()] if m2 else rest


def quotes_of(sec):
    """R 节里每条引文一行，形如「N. 引文（《书》卷次·篇名）」。

    注意：R 节开头常有一行斜体**说明**（「*引文说明：下面每条逐字抄自 …*」），
    那是写给人看的交代，不是引文——必须跳过，否则会被当成"核不过"。
    """
    SKIP = ("引文说明", "逐字抄自", "以下逐条", "下面每条", "说明：")
    out = []
    for line in sec.split("\n"):
        t = line.strip()
        if not t or t.startswith(("#", ">", "|")):
            continue
        if any(k in t for k in SKIP):
            continue
        t = re.sub(r"^\s*(?:\d+\s*[\.、)）]|[-*·])\s*", "", t)
        for pat in NOISE:
            t = pat.sub("", t)
        t = t.replace("**", "").strip(" 　「」『』*_")
        if t:
            out.append(t)
    return out


def main(argv):
    srcs = load_sources()
    if not srcs:
        sys.exit("sources/ 下找不到源文本")
    pats = argv[1:] or ["bazi-*"]
    dirs, seen = [], set()
    for p in pats:
        for d in sorted(SKILLS.glob(p)):
            if d.is_dir() and d.name not in seen:
                seen.add(d.name); dirs.append(d)

    total = hit = miss = 0
    bad, thin, norq = [], [], []
    print("%-42s %-7s %-6s %s" % ("skill", "R条数", "核过", "问题"))
    for d in dirs:
        f = d / "SKILL.md"
        if not f.exists():
            norq.append((d.name, "没有 SKILL.md")); continue
        sec = r_section(f.read_text(encoding="utf-8"))
        if sec is None:
            norq.append((d.name, "没有 R 节")); continue
        qs = quotes_of(sec)
        okc = 0
        for q in qs:
            nq = norm(q)
            if len(nq) < MIN_LEN:
                continue
            total += 1
            if any(nq in t for t in srcs.values()):
                hit += 1; okc += 1
            else:
                miss += 1
                bad.append((d.name, q[:70]))
        note = ""
        if len(qs) < MIN_QUOTES:
            thin.append(d.name); note = "R 条数不足 %d" % MIN_QUOTES
        print("%-42s %-7d %-6d %s" % (d.name, len(qs), okc, note))

    print("\n共 %d 个 skill｜可核引文 %d 条：命中 %d，未命中 %d" % (len(dirs), total, hit, miss))
    if norq:
        print("\n没有 R 节／文件：")
        for n, why in norq:
            print("  %-40s %s" % (n, why))
    if thin:
        print("\nR 条数不足 %d：%s" % (MIN_QUOTES, "、".join(thin)))
    if bad:
        print("\n未命中（引文与源文件对不上，必须删或改）：")
        for n, q in bad[:80]:
            print("  %-40s %s" % (n, q))
    return 1 if (miss or norq) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
