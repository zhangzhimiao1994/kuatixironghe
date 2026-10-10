#!/usr/bin/env python3
"""回书核：把 kanyu-* 各 SKILL.md 的 R 节引文回源文件核对（归一化只留字形）。

用法（包根目录）：python3 distill/kanyu/verify_quotes.py [--fix-report out.md]
判据：归一化后（去掉空白、标点、常见异体差异）引文必须是源文件的子串。
      核不过的条目全部列出来，供人工删改——不自动改包。
"""
import re, sys, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
SRC = ROOT / "sources"
SKILLS = ROOT / "skills"

SRC_FILES = {"zangshu": SRC / "zangshu.txt", "hanlongjing": SRC / "hanlongjing.txt",
             "yilongjing": SRC / "yilongjing.txt", "xieji": SRC / "xieji.txt"}

CJK = re.compile(r"[\u3000-\u303f\u4e00-\u9fff\uff00-\uffef]")
DROP = set(" \t\r\n，。、；：？！〈〉《》「」『』（）()·．,.;:?!\"'“”‘’—－-…〈〉【】[]")


def norm(s: str) -> str:
    return "".join(ch for ch in s if ch not in DROP and not ch.isspace())


NORM = {k: norm(v.read_text(encoding="utf-8")) for k, v in SRC_FILES.items()}

QUOTE_RE = re.compile(r"[「『“\"《]([^」』”\"》]{4,})[」』”\"》]")


def quotes_of(text: str):
    out = []
    for m in QUOTE_RE.finditer(text):
        q = m.group(1).strip()
        # 去掉出处尾巴里的书卷名（引文一般不带书名号）
        if len(norm(q)) < 6:
            continue
        if q.startswith("《") or "卷" in q[:3]:
            continue
        out.append(q)
    # 也收 > 引用块
    for line in text.split("\n"):
        if line.strip().startswith(">") and "（" in line and "《" in line:
            body = line.strip().lstrip(">").strip()
            body = re.split(r"（(?:《|卷)", body)[0].strip()
            if len(norm(body)) >= 6:
                out.append(body)
    return out


def main():
    report, total, ok = [], 0, 0
    for d in sorted(p for p in SKILLS.iterdir() if p.is_dir() and p.name.startswith("kanyu-")):
        sk = d / "SKILL.md"
        if not sk.exists():
            report.append(f"!! {d.name}: 没有 SKILL.md")
            continue
        text = sk.read_text(encoding="utf-8")
        # 只核 R 节
        m = re.search(r"(?m)^##\s*R[\s:：\-—]", text)
        r_sec = text[m.start():] if m else ""
        m2 = re.search(r"(?m)^##\s*[IA1-2E B]", r_sec[4:])
        if m2:
            r_sec = r_sec[: m2.start() + 4]
        qs = quotes_of(r_sec)
        bad = []
        for q in qs:
            n = norm(q)
            total += 1
            if any(n in nf for nf in NORM.values()):
                ok += 1
            else:
                bad.append(q[:60])
        if bad:
            report.append(f"## {d.name}  （{len(bad)}/{len(qs)} 条核不过）")
            for b in bad:
                report.append(f"  - 核不过: {b}")
    head = f"引文核验：{ok}/{total} 条命中；{len(report)} 个 skill 有未核过条目"
    print(head)
    print("\n".join(report[:120]))
    return 0 if not report else 1


if __name__ == "__main__":
    sys.exit(main())
