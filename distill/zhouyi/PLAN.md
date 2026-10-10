# 蒸馏计划 · 周易（并入第二批，9 个）

维度：**周易**（象征层，注册表顺序 **4**）｜本批前缀 `zhouyi-`
来源（包内相对路径，只准从这里抄引文）：
- `sources/zhouyi-jing.txt` — 周易（經文，維基文庫本，4.9 万字）
- `sources/zhouyi-benyi.txt` — 周易本義（宋朱熹，四庫全書本，14.9 万字）
- `sources/zhouyi-zhengyi.txt` — 周易正義（唐孔穎達等，十三經注疏本，30.0 万字）

规矩：`distill/zhouyi/STYLE.md`；骨架：`templates/skill-template/SKILL.md`。

**定位口径：一律按篇名/卦名定，不按行号**（三本的卷次标记与正文交错，行号会错位；上一族已踩过）。
**先勘定再取引**：某一句到底在哪一本里，先在三本里搜到再抄，抄完由 `verify_quotes.py` 回书核。

**已有 13 个**（不动）：`zhouyi`（入口）＋ 12 个处境路由成员（`advance-retreat-boundary`、`hexagram-situation-diagnosis`、`line-position-timing`、`reversal-cycle`、`observation-judgment`、`relationship-assembly`、`repair-renewal-cycle`、`response-action`、`scale-and-restraint-control`、`conflict-coalition-diagnosis`、`humility-overreach-check`、`auspicious-risk-language`）。

## 本批 9 个

| # | slug | 标题 | 盖的范围（出处按「篇／卦」写） |
|---|---|---|---|
| 1 | `zhouyi-jing-shang` | 上經卦爻辭（卦一–卦三十） | 乾、坤、屯、蒙、需、訟、師、比、小畜、履、泰、否、同人、大有、謙、豫、隨、蠱、臨、觀、噬嗑、賁、剝、復、无妄、大畜、頤、大過、坎、離 —— **卦辞＋爻辞**逐卦抄，每卦带卦次 |
| 2 | `zhouyi-jing-xia` | 下經卦爻辭（卦三十一–卦六十四） | 咸、恆、遯、大壯、晉、明夷、家人、睽、蹇、解、損、益、夬、姤、萃、升、困、井、革、鼎、震、艮、漸、歸妹、豐、旅、巽、兌、渙、節、中孚、小過、既濟、未濟 —— 同上 |
| 3 | `zhouyi-tuan-zhuan` | 彖傳（上下） | 彖传释卦辞者：乾坤…未濟各卦的「彖曰」；重点在**卦体、卦德、卦时、卦用**的释法 |
| 4 | `zhouyi-xiang-zhuan` | 象傳（大象／小象） | 大象释卦（「天行健，君子以自强不息」这类），小象释爻；**大象的「君子以…」句式**是本 skill 的主料 |
| 5 | `zhouyi-wenyan-zhuan` | 文言傳 | 只乾坤两卦的「文言曰」，含四德说与爻位说 |
| 6 | `zhouyi-xici-shang` | 繫辭上傳 | 「繫辭焉而明吉凶」这一路的通论：乾坤易简、设卦观象、筮法大衍之数 |
| 7 | `zhouyi-xici-xia` | 繫辭下傳 | 通论下半：作易者其有忧患、天地设位圣人成能、爻位与吉凶之动 |
| 8 | `zhouyi-shuogua-xugua-zagua` | 說卦·序卦·雜卦 | 說卦（八卦取象、帝出乎震）、序卦（六十四卦次序之理）、雜卦（错杂而论，多从**卦德对照**） |
| 9 | `zhouyi-zhu-shu-du-fa` | 朱子本義與孔疏的讀法 | 两家**体例层**：本義（筮法、卦变、图说、其对经传的取舍）＋正義（卷首八论与注疏体例），**两家对同一处的不同取法要并陈** |

## 收尾顺序（不可颠倒）

1. 9 个 skill 的 `SKILL.md` ＋ `test-prompts.json` 写完
2. 注册表 `| 4 | 周易 …| 13 |` → **22**、hub 概览表计数、hub H 节分组计数与名单 → 全部对齐 22
3. `zhouyi` 入口的路由表：12 个成员 → 21 个（补 9 条），并说明新增的是「十翼与注疏」一组
4. `python tools/install_deps.py`（本批不加新依赖，跑一遍确认没坏）
5. `STRICT_SKELETON=1 python tools/dim_check.py`（0 错）
6. 回书核：`python distill/zhouyi/verify_quotes.py`（逐字命中，核不过就删改）
7. 版本号 +1 ＋ 打包

## 已知要当心的坑

- **三本各自对同一句的用字不同**（无／無、系／繫、说／說）——**照本抄**，别统一。
- **`周易正義` 里「经＋注＋疏」是混排的**：抄之前先认准哪一段是经、哪一段是王弼注、哪一段是孔疏，R 节要标清；**不许把疏文当经文**。
- **`周易本義` 的四庫本有图说与附录**：只取与经传直接相关的注，图说类只在第 9 个 skill 里用。
- **别把现代流派的说法（各种「象数」「卦变」的当代化简）冒充古法**；本義与疏怎么讲就怎么引。
