"""周易族回书核：把各 skill 的 R 节引文逐字比回三本源文件（归一化只留汉字）。

覆盖：周易这一维的全部 skill（13 个既有 ＋ 9 个新增）。
处理两种 R 节写法：
  A) 既有成员：`> 屯：元亨利贞。…（第三卦）（已据公版原文核）`
  B) 新增成员：`1. 引文（《周易》卦名·爻题）`
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SK = ROOT / "skills"
SOURCES = ["zhouyi-jing.txt", "zhouyi-benyi.txt", "zhouyi-zhengyi.txt"]

MEMBERS = [
    "zhouyi", "advance-retreat-boundary", "hexagram-situation-diagnosis", "line-position-timing",
    "reversal-cycle", "observation-judgment", "relationship-assembly", "repair-renewal-cycle",
    "response-action", "scale-and-restraint-control", "conflict-coalition-diagnosis",
    "humility-overreach-check", "auspicious-risk-language",
    "zhouyi-jing-shang", "zhouyi-jing-xia", "zhouyi-tuan-zhuan", "zhouyi-xiang-zhuan",
    "zhouyi-wenyan-zhuan", "zhouyi-xici-shang", "zhouyi-xici-xia",
    "zhouyi-shuogua-xugua-zagua", "zhouyi-zhu-shu-du-fa",
]

# 引文里不属于原文的部分：出处、核验标记、卦次标记、层标记
CITE = [
    re.compile(r"（[^）]*）"),          # 任何全角括注（出处/卦次/层标记/行内说明）都不属原文
    re.compile(r"\([^)]*\)"),
]
# 形如「乾：…」「坤·六四：…」「屯(卦三)：…」的前缀也不属原文
PREFIX = re.compile(r"^《[^》]*》?\s*")
SKIP_LINE = ("引文说明", "逐字抄自", "以下逐条", "下面每条", "说明：", "出处：")


def norm(s):
    """只留汉字，并做繁简归一（源文件是繁体、老成员的引文是简体，不归一就全对不上）。"""
    s = "".join(ch for ch in s if "\u4e00" <= ch <= "\u9fff")
    if _CC is not None:
        s = _CC.convert(s)
    return s


try:
    from opencc import OpenCC

    _CC = OpenCC("t2s")
except Exception:                                                 # noqa: BLE001
    _CC = None
    print("（没装 opencc，繁简不归一——命中率会偏低；装法：pip install -i "
          "https://pypi.tuna.tsinghua.edu.cn/simple opencc-python-reimplemented）")


src = {}
for fn in SOURCES:
    p = ROOT / "sources" / fn
    if p.exists():
        src[fn] = norm(p.read_text(encoding="utf-8"))
print("源文件：%s" % "、".join("%s(%.1f 万字)" % (k, len(v) / 10000) for k, v in src.items()))


def _one(t):
    """把一行里的一条引文洗干净：去前缀（卦名／爻题）、去括注、去标记。"""
    t = PREFIX.sub("", t).strip()
    t = re.sub(r"^\s*(?:\d+\s*[\.、)）]|[-*·>]\s*)", "", t).strip()
    # 形如「乾：…」「坤·六四：…」「屯（卦三）：…」的前缀
    m = re.match(r"^([^：，。；、]{1,10})[:：]\s*(.+)$", t)
    if m and len(m.group(1)) <= 10:
        t = m.group(2).strip()
    for pat in CITE:
        t = pat.sub("", t)
    t = t.replace("**", "").strip(" 　「」『』*_—－-")
    return t.strip()


def quotes_of(text):
    """R 节里逐条引文。两种写法都认：
       A) `> 屯：元亨利贞。勿用有攸往，利建侯。（第三卦）（已据公版原文核）`
       B) `1. 引文（《周易》卦名·爻题）`
    一行里塞了多条（「师：…。师·初六：…。」）时**按句拆开分别核**。
    """
    sec = text.split("## R：原文锚点")
    if len(sec) < 2:
        return []
    sec = sec[1].split("\n## ")[0]
    out = []
    for line in sec.split("\n"):
        t = line.strip()
        if not t or t.startswith(("#", "|")):
            continue
        if any(k in t for k in SKIP_LINE):
            continue
        t = re.sub(r"^[>\s]*", "", t)
        t = re.sub(r"^\s*(?:\d+\s*[\.、)）]|[-*·])\s*", "", t)
        for chunk in re.split(r"(?<=。)", t):
            if chunk.lstrip().startswith(("—", "－", "-", "→", "–")):
                continue            # 「…（原文）— 白话说明」里的说明不是引文
            q = _one(chunk)
            if len("".join(c for c in q if "\u4e00" <= c <= "\u9fff")) >= 4:
                out.append(q)
    return out


total = hit = miss = 0
misses = []
for slug in MEMBERS:
    f = SK / slug / "SKILL.md"
    if not f.exists():
        print("  ✗ 缺 skill：%s" % slug)
        continue
    qs = quotes_of(f.read_text(encoding="utf-8"))
    h = 0
    for q in qs:
        total += 1
        nq = norm(q)
        where = [k for k, v in src.items() if nq and nq in v]
        if where:
            h += 1
            hit += 1
        else:
            miss += 1
            misses.append((slug, q[:52]))
    print("  %-38s R %3d 条，命中 %3d" % (slug, len(qs), h))

print("\n共 %d 个 skill｜可核引文 %d 条：命中 %d，未命中 %d" % (len(MEMBERS), total, hit, miss))
for s, q in misses[:25]:
    print("  未命中 %-32s %s" % (s, q))
sys.exit(0 if miss == 0 else 1)
