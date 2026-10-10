---
name: ptolemy-periods-of-life
description: 人生阶段与时段的星盘推演。当用户给出出生信息、问"我现在是什么人生阶段""这个阶段会怎样""什么时候会发生某件事"时使用。以七行星对应的年龄段分人生时期，以各"时刻点"（prorogation）管不同主题，再按年 / 月 / 日的"进度"（一年一星座等）定当时的主星；只在象征层做倾向性推演，不替用户做人生决定、不给确切日期。
input_schema:
  required: [birth_data, timing_question]
  optional: [age_or_period, life_area, current_events]
output_schema:
  primary: {life_stage_reading: string, period_lord: string, tendency_summary: string}
  secondary: [prorogation_topic, annual_profile_note, cautions]
requires:
  pip: [pymeeus]
  commands: [python3]
---

# 人生阶段与时段：从七行星与"进度"看当下的主题

**来源**：《Tetrabiblos（四书 / Quadripartite）》BOOK THE FOURTH 第 X 章（THE PERIODICAL DIVISIONS OF TIME）｜ 证据等级：firsthand

## 触发条件

**应该触发**：
- 用户给了出生信息，问"我现在处在什么人生阶段""这个年纪该是什么主题"
- 用户问"这几年 / 今年 / 这个月会怎样"（作象征层参照）
- 用户想知道"什么时候适合做某件事"（不替代现实规划）
- 用户在做人生阶段的复盘，想加一层时间结构

**不应触发**：
- 用户要一个确切的日期 / 死线 / 吉日 → 本 skill 只给时段结构，**不给确切日期**
- 用户问的是某一具体题目本身（财 / 婚 / 业） → 走对应的 `ptolemy-*` skill
- 用户问健康 / 寿命 → 🏥 不做
- 用户没给出出生信息 → 先索取，信息不全不推

## R：原文锚点

> "the general divisions of time must be considered by means of the spheres, as a primary arrangement"（BOOK THE FOURTH, CHAPTER X: THE PERIODICAL DIVISIONS OF TIME）（已据公版原文核）

> "the first age of infancy, which endures for four years, agreeing in number with the quadrennial period of the Moon, is consequently adapted to her"（同上，CHAPTER X: THE PERIODICAL DIVISIONS OF TIME）（已据公版原文核）

> "The age after this continues for ten years, and accommodates itself to the second sphere, that of Mercury."（同上，CHAPTER X: THE PERIODICAL DIVISIONS OF TIME）（已据公版原文核）

> "The fourth and adult age next succeeds, and is subject to the fourth sphere, that of the Sun: it endures for nineteen years, according to the Sun’s number."（同上，CHAPTER X: THE PERIODICAL DIVISIONS OF TIME）（已据公版原文核）

> "prorogation made from the ascendant is to be applied to events affecting the body, and to travelling, or change of residence; that from the part of Fortune, to incidents affecting the substance or wealth; that from the Moon, to actions of the mind, and to communion and cohabitation; that from the Sun, to dignities and glory; and that from the mid-heaven, to other particular circumstances of life, such as employment, friendship, and the possession of children."（同上，CHAPTER X: THE PERIODICAL DIVISIONS OF TIME）（已据公版原文核）

> "at one and the same time any single planet, whether benefic or malefic, will not possess the sole dominion; for many conflicting events frequently occur at the same period"（同上，CHAPTER X: THE PERIODICAL DIVISIONS OF TIME）（已据公版原文核）

> "human nature in general is not subjected to the extremity either of good or evil, but rather to their moderate alteration and counter-change."（同上，CHAPTER X: THE PERIODICAL DIVISIONS OF TIME）（已据公版原文核）

> "the number of years which have elapsed since the birth has been ascertained, the amount is to be projected from each place of prorogation, in the succession of the signs, at the rate of one sign for a year, and the lord of the last sign is to be assumed as arbiter."（同上，CHAPTER X: THE PERIODICAL DIVISIONS OF TIME）（已据公版原文核）

## I：核心解释

1. **先把"大背景"放在前面**：书里说，判任何个人都要先顾及"地区 / 种族"这一层更普遍、更占先的原因，不可脱离它去断言——否则会闹出"埃塞俄比亚人生出白皮肤直头发"的笑话。（R 前置条件）
2. **人生阶段对应七行星的球层**：从月的球层（最初的年龄）到土的球层（最后的老年），每一段年龄受一层支配；先从球层做大分，再按各盘的差异做小分。（R1）
3. **各年龄段与年限**（书里原样）：幼儿 → 月，四年（湿软、速长、善变、心识未全）；此后十年 → 水星（理智与推理开始、学之胚芽）；再八年 → 金星（情欲之动与莽撞）；壮年 → 太阳，十九年（事功与荣名之志、弃幼态而求名誉）；成年 → 火星，十五年（生活更严、烦扰与忧劳）；成熟 → 木星，十二年（舍劳作与险业，更庄重、远见、审慎）；老年 → 土星（心识与嗜欲转钝）。（R2、R3）
4. **"时刻点"分管不同主题**：从上升起算的时刻点 → 身体与出行 / 迁居；从福点起算 → 财物；从月起算 → 心智与交合 / 同居；从太阳起算 → 尊荣；从天顶起算 → 职业、友情、子女等。（R4）
5. **同一时刻不会只有一个主星**：书里说"任何单一星，无论吉凶，都不独占支配"——因为同一时段常有互相冲突的事件；同一个人可能一边丧亲一边继承其财、一边抱病一边得利。（R5）
6. **因此常态是"中道"**：人性一般并不落在极好或极坏的极端，而多在其中间的起落与互换之间。（R7）
7. **进度（profection）算法**：由出生起算的年数，从每个时刻点按星座次序推进，一年一星座；最后落在的那个星座的显主，就是该年的主星（arbiter）。月按 28 天一个星座推，日按 2 又 1/3 天一个星座推。（R8）
8. **各周期的主星与"过境"**：一般时段的显主为要；木星管年度、日月火金水管月度、月管日度；过境（ingress）会加强或减弱事件的力度。

## A1：来源应用 — 书里给的具体做法

- **先立"地区 / 种族"的大前提**，再谈个人。
- **读人生阶段**：月（幼儿，4 年）→ 水星（10 年）→ 金星（8 年）→ 太阳（壮年，19 年）→ 火星（15 年）→ 木星（12 年）→ 土星（老年）。
- **读主题**：上升 → 身体 / 出行；福点 → 财物；月 → 心智 / 同居；太阳 → 尊荣；天顶 → 职业 / 友情 / 子女。
- **读年 / 月 / 日的主星**：从时刻点按"一年一星座"推年；按"28 天一个星座"推月；按"2 又 1/3 天一个星座"推日；取落在末位的星座之显主为该时段的 arbiter。
- **看主星的好坏**：主星依其本性吉 / 凶、以及它与自己当初所主位置的亲疏，给出该时段"好或坏"的倾向；时段中事件何时更明显，由年 / 月星座相对"因之所在"的位置、以及行星过境来显示。
- **看日月与时段星座的关系**：日月若自出生起就与"运作的位置"和谐，并在过境时保持和谐 → 出好；反之 → 出坏。
- **强弱**：若同一批星既是一般时段之主、又是过境之主 → 效果极端而纯粹（吉则极吉，凶则极凶）。

## A2：典型触发场景

- "我今年三十出头，感觉在换阶段，盘里怎么说？"
- "我想知道这几年是不是我的关键期"
- 做年度复盘 / 生日前后的自省
- 想理解"为什么同一件事在我人生不同阶段意义不同"

## E：执行步骤

### 步骤1：确认出生信息与所求时段

**输入**：出生日期、时间、地点；用户关心的时段（年龄 / 年 / 月）。
**输出**：定出各"时刻点"（上升、福点、日月、天顶）与所求时段。
🔴 **CHECKPOINT — 触发条件：缺出生信息**：停在索取，不硬推。

### 步骤2：读人生阶段的大图

**输入**：用户的年龄。
**输出**：当前落在哪一球层 / 年龄段，以及该段的书里描述（如"金星段：情欲之动"）。
照 R1–R3。
🔴 **CHECKPOINT — 触发条件：用户把"年龄段 = 一定发生什么"当成判决**：守边界——那是该段的一般倾向，不是命定事件。

### 步骤3：读该时段的主题与主星

**输入**：所求时段的"时刻点"（管哪个主题）＋ 按"一年一星座"推出的星座。
**输出**：该时段的主题（身体 / 财 / 心智 / 尊荣 / 职业）＋ 主星（末位星座的显主）。
照 R4、R8。
🔴 **CHECKPOINT — 触发条件：用户把主星当成"这个月一定发生好事 / 坏事"**：退回——书里说同一时段常有互相冲突的事件、单星不独占支配；只作倾向。

### 步骤4：合成"中道"的时段小结

**输入**：前几步输出。
**输出**：一段"阶段主题 + 时段主星 + 可能的中道起落"的小结，并注明：不落在极好 / 极坏，多在中间互换。
照 R5–R7。
🔴 **CHECKPOINT — 触发条件：用户要确切日期 / 要据此做重大决定（结婚 / 辞职 / 生育）**：退回——**不给确切日期，不替用户做人生决定**；时段结构只作象征层参照。

## B：边界与失败模式

| 情况 | 表现 | 怎么处理 |
|------|------|---------|
| 要确切日期 / 吉日 | "几月几号最好" | 🛑 书里给的是时段结构，不给确切日期。 |
| 拿"关键期"当命运 | "这年是我的大限" | 🛑 常态是"中道"；单星不独占支配。 |
| 拿时段去替用户做决定 | "今年主星好，那我辞职吧" | 🛑 **不替用户做人生决定**，选择权在人。 |
| 脱离环境泛推 | "不管他在哪儿，星说了算" | 🛑 书里先立"地区 / 种族"的大前提，不可脱离。 |
| 借时段问健康 / 寿命 | "这段时间会不会出大事" | 🏥 不做健康 / 寿命断言，转出。 |
| 缺出生信息 | 无出生时间 | 🛑 停在索取。 |

**边界规则**：
1. 本 skill 只做象征层的**倾向性推演**，不是命定论，也不给确切日期。
2. **只作倾向性推演，选择权在人**：不替用户做婚姻 / 职业 / 财务 / 人生决定。
3. 阶段年限、主题对应、进度算法一律用书里的条目；不自行添加判法。
4. 与相邻 skill 分工：具体主题（财 / 婚 / 业 / 子女）走对应的 `ptolemy-*` skill；本 skill 只给时间结构。
5. 需要出生信息才能触发；缺信息不推。

**自查清单**：
- [ ] 我确认了完整出生信息
- [ ] 我按七行星球层读了人生阶段
- [ ] 我用"时刻点"对应了主题，并按"一年一星座"推出时段主星
- [ ] 我重复了"单星不独占支配、常态是中道"的提醒
- [ ] 我没有给确切日期，也没替用户做决定

**安全兜底**：
- **不是命定论**。书里原话："the fulfilment of events thus indicated must not be ascribed solely to the vigour of the cause producing them, nor to any inevitable fate, but rather to the absence of any opposing influence capable of prevention."（BOOK THE FIRST, CHAPTER III: THAT PRESCIENCE IS USEFUL）
- **只作倾向性推演，选择权在人**：不替用户做人生决定，最终选择与责任在用户自己。
- **不做健康 / 寿命断言（🏥）**：涉及身体、疾病、寿数时只做提醒与陪伴，指向专业资源。
- 触发需出生信息；没有出生信息不推。

## 📖 练习手册

**阶段自述**：按七球层的段落，写下你现在这一段"书里怎么说"，再写一句"我实际在经历什么"，两相对照，练"结构"与"生活"的区分。

**中道提醒**：把"这一时段可能有互冲的事"写进你的年度复盘模板，提醒自己不要期待极好或极坏的单一剧本。

## 🚫 反例黑名单

1. **给确切日期 / 吉日** → 🛑 书里只给时段结构。
2. **把"关键期 / 主星"当命运判决** → 🛑 单星不独占支配，常态是中道。
3. **替用户做婚姻 / 职业 / 生育决定** → 🛑 越界，选择权在人。
4. **脱离地区 / 环境泛推** → 🛑 书里先立大前提。
5. **把时段话题引向健康 / 寿命** → 🏥 拒绝并转出。

### 灰色地带

- **用户只想知道"今年大概什么调子"**：可以按年进度给一个中道的倾向描述，但强调这是象征层。
- **多个主题在同一时段同时活跃**：书里说这正是常态——如实并列几个方向，不强行统一成一个结论。
- **用户拿时段来"等一个时机"而不是行动**：把话题从"等星象"拉回"你能做什么准备"。
