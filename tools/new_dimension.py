#!/usr/bin/env python3
"""一条命令加一个维度 —— 这个包的扩展入口。

用法（包根目录下）：
  python tools/new_dimension.py --prefix ptolemy --name 托勒密星盘 --layer 象征 \
      --signals "点名星盘、出生信息、行星状态、主题取用" --data 出生信息 \
      --source "Tetrabiblos (Ptolemy)" --skill ptolemy-natal-chart --skill-title "出生盘解读" \
      --emoji "♈"

它会做四件事，然后自检：
  1 建 skills/<skill>/{SKILL.md,test-prompts.json}（从 templates/skill-template/ 复制并填占位符）
  2 在 dimensions.registry.md 正表末尾加一行（顺序默认 = 现有最大 + 1）
  3 在 hub 的「维度概览与触发信号」表追加一行、在 H 节追加一个分组块
  4 跑 tools/dim_check.py，四处对齐才算完

之后自己填空：R 原文锚点必须回书抄原话；test-prompts.json 三类用例写全。
只依赖标准库，Python 3.8+。
"""
import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
HUB = SKILLS / "cross-system-hub/SKILL.md"
REG = SKILLS / "cross-system-hub/dimensions.registry.md"
TPL = ROOT / "templates/skill-template"
LAYERS = ("观察", "象征", "校准")


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")] if line.strip().startswith("|") else None


def main():
    ap = argparse.ArgumentParser(description="加一个维度（建 skill + 登记注册表 + 补 hub + 自检）")
    ap.add_argument("--prefix", required=True,
                    help="skill 目录前缀本体，如 ptolemy（写成 `ptolemy-*`；结尾别带 - 或 *，带了也会自动去掉）")
    ap.add_argument("--name", required=True, help="维度中文名，如 托勒密星盘")
    ap.add_argument("--layer", required=True, choices=LAYERS, help="层：观察 / 象征 / 校准")
    ap.add_argument("--signals", required=True, help="触发信号关键词，顿号分隔")
    ap.add_argument("--data", default="—", help="数据依赖：— / 心态或状态 / 一件具体的事 / 出生信息")
    ap.add_argument("--source", required=True, help="来源，如 Tetrabiblos (Ptolemy)")
    ap.add_argument("--skill", required=True, help="入口 skill 的目录名/slug，如 ptolemy-natal-chart")
    ap.add_argument("--skill-title", default="", help="入口 skill 的一句话标题")
    ap.add_argument("--desc", default="", help="frontmatter description（默认按维度名生成）")
    ap.add_argument("--emoji", default="🧩", help="hub 概览表与 H 节的图标")
    ap.add_argument("--order", default="", help="顺序号（默认 = 现有最大 + 1）")
    ap.add_argument("--dry-run", action="store_true", help="只打印要做什么，不落盘")
    a = ap.parse_args()
    # 容错：前缀末尾多写连字符/星号是常见手滑，会登记出 `testflow--*` 这种坏入口
    a.prefix = a.prefix.strip().rstrip("-*_").strip()
    a.skill = a.skill.strip().strip("/")
    if not a.prefix:
        sys.exit("× --prefix 不能为空（只要前缀本体，如 ptolemy；工具会自动补 -*) ")

    # ---- 前置校验 ----
    reg_txt = REG.read_text(encoding="utf-8")
    hub_txt = HUB.read_text(encoding="utf-8")
    if f"`{a.prefix}-*`" in reg_txt or re.search(rf"^\|\s*[\d.]+\s*\|\s*{re.escape(a.name)}\s*\|", reg_txt, re.M):
        sys.exit(f"× 注册表里已经有 {a.name} / `{a.prefix}-*` 了；改维度请直接编辑注册表那一行。")
    if (SKILLS / a.skill).exists():
        sys.exit(f"× skills/{a.skill} 已存在，换个 --skill。")
    if not shutil.which("python3") and not shutil.which("python"):
        print("! 没找到 python3，第 4 步自检需要它（其余步骤不需要）")

    rows = [cells(l) for l in reg_txt.split("\n")]
    rows = [c for c in rows if c and len(c) == 8 and re.match(r"^\d", c[0])]
    order = a.order or str(max([float(c[0]) for c in rows], default=0) + 1)
    order = order.rstrip("0").rstrip(".") if "." in order else order

    new_reg_row = (f"| {order} | {a.name} | {a.layer} | `{a.prefix}-*` | {a.signals} | {a.data} | "
                   f"{a.source} | 1 |")
    new_ov_row = (f"| {len(rows) + 1} | **{a.name}** | {a.layer} | {a.emoji} | {a.signals} | 1 |")
    h_block = (f"\n### {a.emoji} {a.name} (1个)\n"
               f"| Skill | 核心功能 |\n|-------|---------|\n"
               f"| `{a.skill}` | {a.skill_title or a.name} |\n")

    print(f"将新建：skills/{a.skill}/{{SKILL.md,test-prompts.json}}")
    print(f"注册表加行：{new_reg_row}")
    print(f"hub 概览加行：{new_ov_row}")
    print(f"hub H 节加块：### {a.emoji} {a.name} (1个)")
    if a.dry_run:
        print("\n（--dry-run，什么都没写）")
        return

    # ---- 1 建 skill ----
    (SKILLS / a.skill).mkdir(parents=True)
    desc = a.desc or f"当用户提到{a.signals.split('、')[0]}等与{a.name}有关的处境时使用；按原文锚点给出视角、洞察与行动。"
    tpl = (TPL / "SKILL.md").read_text(encoding="utf-8")
    for k, v in {"{{SKILL_NAME}}": a.skill, "{{TITLE}}": a.skill_title or a.name,
                 "{{SOURCE}}": a.source, "{{DESCRIPTION}}": desc,
                 "{{REQ_FIELDS}}": "\"user_message\"", "{{OPT_FIELDS}}": "\"context\""}.items():
        tpl = tpl.replace(k, v)
    (SKILLS / a.skill / "SKILL.md").write_text(tpl, encoding="utf-8")
    shutil.copy2(TPL / "test-prompts.json", SKILLS / a.skill / "test-prompts.json")

    # ---- 2 注册表 ----
    lines = reg_txt.split("\n")
    last = max(i for i, l in enumerate(lines)
               if (c := cells(l)) and len(c) == 8 and re.match(r"^\d", c[0]))
    lines.insert(last + 1, new_reg_row)
    REG.write_text("\n".join(lines), encoding="utf-8")

    # ---- 3 hub：概览表 + H 节 ----
    lines = HUB.read_text(encoding="utf-8").split("\n")
    last = max(i for i, l in enumerate(lines)
               if (c := cells(l)) and len(c) == 6 and c[0].isdigit() and c[2] in LAYERS)
    lines.insert(last + 1, new_ov_row)
    hub_txt = "\n".join(lines)
    anchor = "\n---\n\n## J："
    if anchor not in hub_txt:
        an = re.search(r"\n---\n\n## J[：:]", hub_txt)
        anchor = an.group(0) if an else None
    if not anchor:
        sys.exit("× 找不到 hub 的 J 节锚点，H 节块没加；请手动补 H 节名单后再跑自检。")
    HUB.write_text(hub_txt.replace(anchor, h_block + anchor), encoding="utf-8")

    # ---- 3.5 同步描述行里的层计数（"观察 N / 象征 M / 校准 K"）----
    from collections import Counter
    cnt = Counter()
    for l in REG.read_text(encoding="utf-8").split("\n"):
        c = cells(l)
        if c and len(c) == 8 and re.match(r"^\d", c[0]):
            cnt[c[2]] += 1
    line = f"观察 {cnt['观察']} / 象征 {cnt['象征']} / 校准 {cnt['校准']}"
    for path in (HUB, ROOT / "README.md"):
        txt = path.read_text(encoding="utf-8")
        txt2 = re.sub(r"观察\s*\d+\s*/\s*象征\s*\d+\s*/\s*校准\s*\d+", line, txt, count=1)
        if txt2 != txt:
            path.write_text(txt2, encoding="utf-8")
            print(f"  描述行层计数 → {line}（{path.name}）")

    # ---- 4 自检 ----
    print("\n--- dim_check ---")
    r = subprocess.run([sys.executable, str(ROOT / "tools/dim_check.py")], capture_output=True, text=True)
    print(r.stdout.strip() or r.stderr.strip())
    print("\n下一步：① 在 skills/%s/SKILL.md 填 R 原文锚点（回书抄原话）与 I/A/E/B；"
          "② 把 test-prompts.json 三类用例写全；③ 再跑一次 tools/dim_check.py。" % a.skill)
    sys.exit(r.returncode)


if __name__ == "__main__":
    main()
