---
name: ptolemy-aspects
description: 星座间关系（相位）读法。当用户报了出生信息，要问两个星座/两颗行星之间是什么关系——对冲、三分、四分、六分，哪种和谐哪种冲突；或问"命宫/服从宫""互视等力""隔绝"这类星宫关系时使用。需要出生信息；没有出生信息不激活。
input_schema:
  required: [birth_info, two_points, aspect_or_relation]
  optional: [sign_pair, orb_or_distance, topic]
output_schema:
  primary: {aspect_name: string, harmony_or_discord: string, relation_read: string}
  secondary: [commanding_obeying, beholding_equal, inconjunct_flag]
requires:
  pip: [pymeeus]
  commands: [python3]
---

# 星座间的关系：四个相位与命从、互视、隔绝

**来源**：《Tetrabiblos（四书）》BOOK THE FIRST，CHAPTER XVI MUTUAL CONFIGURATIONS OF THE SIGNS / CHAPTER XVII SIGNS COMMANDING AND OBEYING / CHAPTER XVIII SIGNS BEHOLDING EACH OTHER, AND OF EQUAL POWER / CHAPTER XIX SIGNS INCONJUNCT ｜ 证据等级：firsthand

## 触发条件

**应该触发**：
- 用户给了出生信息，问两颗行星（或两个星座）之间是"对冲、三分、四分、六分"哪一种
- 用户问某个相位是和谐还是冲突
- 用户问"这两处隔了几个宫，算不算有关系"
- 用户问"命宫/服从宫（commanding and obeying）""互视且等力""隔绝（inconjunct）"是什么意思
- 用户要把星座/行星之间的关系并进某个主题（关系、合作、冲突）的读法

**不应触发**：
- 用户没给出生信息 → 不激活，先索取
- 用户要的是行星本身的性质 → 走 `ptolemy-planet-natures`
- 用户要的是单个星座的性质或四轴 → 走 `ptolemy-sign-natures`
- 用户要的是行星在某星座的庙旺 → 走 `ptolemy-dignities`
- 用户要的是行星在盘中强不强（入相位出相位、速度、方位） → 走 `ptolemy-planet-condition`
- 用户问"是不是命中注定" → 走 `ptolemy-prescience-frame`

## R：原文锚点

> "This mutual configuration attaches to all parts diametrically distant from each other, containing between them two right angles, or six signs, or a hundred and eighty degrees"（BOOK THE FIRST・CHAPTER XVI「MUTUAL CONFIGURATIONS OF THE SIGNS」）（已据公版原文核）

> "it also exists in all parts at the triangular distance from each other, containing between them one right angle and a third, or four signs, or a hundred and twenty degrees"（BOOK THE FIRST・CHAPTER XVI）（已据公版原文核）

> "Of these configurations, the trine and the sextile are each called harmonious, because they are constituted between signs of the same kind"（BOOK THE FIRST・CHAPTER XVI）（已据公版原文核）

> "The opposition and quartile are considered to be discordant, because they are configurations made between signs not of the same kind, but of different natures and sexes."（BOOK THE FIRST・CHAPTER XVI）（已据公版原文核）

> "Any two signs configurated with each other at an equal distance from the same, or from either equinoctial point, are termed commanding and obeying"（BOOK THE FIRST・CHAPTER XVII「SIGNS COMMANDING AND OBEYING」）（已据公版原文核）

> "The signs in the summer semicircle are commanding; those in the winter semicircle, obeying"（BOOK THE FIRST・CHAPTER XVII）（已据公版原文核）

> "Any two signs, equally distant from either tropical sign, are equal to each other in power"（BOOK THE FIRST・CHAPTER XVIII「SIGNS BEHOLDING EACH OTHER, AND OF EQUAL POWER」）（已据公版原文核）

> "All signs, between which there does not exist any familiarity in any of the modes above specified, are inconjunct and separated."（BOOK THE FIRST・CHAPTER XIX「SIGNS INCONJUNCT」）（已据公版原文核）

> "All parts which are distant from each other in the space of one sign only are considered inconjunct"（BOOK THE FIRST・CHAPTER XIX）（已据公版原文核）

## I：核心解释

1. **关系由距离决定，共四种主要相位**：正对（对冲）＝相距六个宫 / 180 度（两个直角）；三分＝相距四个宫 / 120 度（一个半直角）；四分＝相距三个宫 / 90 度（一个直角）；六分＝相距两个宫 / 60 度（三分之二个直角）。（R1、R2）
2. **按"同类/异类"分和谐与不和**：三分与六分是在同类的宫之间构成的（同为阴或同为阳），故称和谐；对冲与四分是在不同类、不同性质与性别的宫之间构成的，故称不和。（R3、R4）
3. **除相位外还有"命从"关系**：任何两个宫，若距同一点（或距任一平分点）相等，则称命宫与服从宫——因为二者的上升与下降时间相等、走相等的纬圈；夏季半圆内的宫为命（主），冬季半圆内的为从（R5、R6）。
4. **还有"互视且等力"**：任何两个距任一至点相等的宫，彼此力量相等，且从地平同一处升起、在相同处落下，故称互视。（R7）
5. **其余都是"隔绝"**：凡彼此之间不存在上述任何一种关系的宫，都是隔绝的、分离的。特别是只相隔一个宫、或相隔五个宫的情形——前者被彼此避开，后者把整圆分成不等份，而四种相位都产生整除的分割，故被排除在关系之外。（R8、R9）
6. **所以两张盘/两个点之间先量距离 → 定相位或命从/互视/隔绝 → 再定和谐与否，这是关系读法的固定顺序。**

## A1：来源应用

书里给的具体做法（不是我的发挥）：

- **量距离定相位**：把两点间的宫数/度数换算成 180、120、90、60 四种之一，不在其列就归入命从/互视/隔绝范畴。（R1、R2）
- **判和谐或不和**：三分、六分判和谐（同类）；对冲、四分判不和（异类）。（R3、R4）
- **判命从**：两点距同一点等距时，定谁是命宫、谁是服从宫，夏季半圆的为命、冬季半圆的为从。（R5、R6）
- **判互视等力**：两点距任一至点等距时，判为力量相等、彼此互视。（R7）
- **判隔绝**：不在上述任何关系内、尤其只隔一宫或隔五宫的，判为隔绝、分离，两者之间"没有关系"。（R8、R9）

## A2：典型触发场景

- 用户问"我太阳和月亮是不是对冲，这意味着什么"
- 用户问"三分和六分是不是都是好相位，四分和对冲都是坏相位"
- 用户问"我们两个星座哪一个是主导、哪一个是配合"
- 用户问"我这两点隔得远，是不是就没关系了"
- 用户要把两处关系并进关系/合作/冲突的主题读法

## E：执行步骤

1. **确认出生信息与两个目标点**　输入：出生信息 + 两个星座/两颗行星。→ 输出：明确的两个点。
   🔴 **CHECKPOINT — 触发条件：无出生信息**：不激活，先索取。

2. **量距离，定关系类别**　输入：两点间的宫数/度数。→ 输出：对冲 / 三分 / 四分 / 六分 / 命从 / 互视 / 隔绝。
   照 R1、R2、R5、R7、R8：逐条比对。
   🔴 **CHECKPOINT — 触发条件：距离落在两者之间、难以归类**：按书里"取整"的四种相位判断，若落在整除之外即归隔绝或命从/互视，不硬造新相位（书里明确不承认后来新增的相位）。

3. **判和谐或不和**　输入：上一步的类别。→ 输出：和谐（三分/六分）或 不和（对冲/四分）。
   照 R3、R4：以"同类/异类"为据。
   🔴 **CHECKPOINT — 触发条件：用户把"不和"等同"灾难"**：说明这只是宫的性质相异、倾向不易调和，转 `ptolemy-prescience-frame` 校准。

4. **（如需）判命从或互视**　输入：两点是否等距于同一平分点或至点。→ 输出：命宫/服从宫，或 互视等力。
   照 R5–R7。

5. **并入主题读**　输入：类别 + 和谐与否 + 用户要看的主题。→ 输出：一句"倾向"读法。
   🔴 **CHECKPOINT — 触发条件：读法涉及身体/寿命**：转安全兜底 🆘/🏥，只谈倾向。

## B：边界与失败模式

| 失败模式 | 长什么样 | 怎么退回去 |
|---|---|---|
| 硬造书里没有的相位 | 用半四分、五分等新相位 | 🛑 书里明确只认四种；其余归隔绝或命从/互视（R8、R9）。 |
| 只看相位不看同类异类 | 说不出三分六分为何和谐 | 🛑 回到步骤3，按同类/异类判（R3、R4）。 |
| 把"不和"读成灾难 | "四分相，所以你必出事" | 🛑 只是性质相异、倾向难调，转 `ptolemy-prescience-frame`。 |
| 缺出生信息硬算 | 没出生信息也定关系 | 🛑 回到步骤1，不激活。 |
| 忽略隔绝 | 对相距一宫/五宫的两点也硬读出关系 | 🛑 照 R8、R9 判为隔绝、分离。 |
| 命从/互视与相位混淆 | 把命从关系当相位读 | 🛑 分开两类：相位是距离关系，命从/互视是等距关系。 |

**边界规则**：
1. 本 skill 只管"点与点之间的关系"，不管单点自身性质（走 `ptolemy-planet-natures`、`ptolemy-sign-natures`）。
2. 只承认书里的四种主要相位；新增相位不采用。
3. 需要出生信息才能用；没有出生信息不激活。
4. 一切结论写"倾向"，不写"必然"。

**自查清单**：
- [ ] 我确认过出生信息
- [ ] 我量出了两点间的距离并归入四种相位之一或命从/互视/隔绝
- [ ] 我按同类/异类判了和谐或不和
- [ ] 我没有引入书里没有的相位
- [ ] 我的结论是倾向，不是必然

**安全兜底**：🆘/🏥 关系读法若被用来推断身体、疾病或寿命，一律只谈倾向，不作医疗判断、不做寿命断言、不替代就医（急救 120、心理援助 12356）。

## 📖 练习手册

1. **相位换算**：把 180/120/90/60 度分别换成"相隔几个宫"，再写上对应名称。
2. **和谐判定**：任取两个星座，先量距离，再判它是同类还是异类，最后判和谐与否。
3. **命从/互视练习**：给两个距平分点等距的星座，判谁为命、谁为从；再给两个距至点等距的，判互视等力。

## 🚫 反例黑名单（不要做的事）

1. 采用书里没有的现代相位。
2. 只报相位名，不判同类异类。
3. 把"不和"直接翻成灾祸。
4. 无出生信息也硬定关系。
5. 把命从、互视当成相位来读。

## 灰色地带

- **同宫相合（conjunction）**：书里本章只讲"彼此构成相位的宫之间"，故未列相合；相合在后面的篇章里另有处理。遇到相合，说明它不属于本章的四种相位，另行对待。
- **同宫与命从的分界**：同宫/相邻一宫归隔绝，注意别和"距平分点等距"的命从关系搞混。
- **现代新增相位的请求**：书里对这个分歧是明确否定的；若用户坚持要用，先说明古书立场，再按其自选体系另读，不混用。
