---
name: ptolemy-wealth-and-rank
description: 财富与地位的星盘推演。当用户给出出生信息、想知道"我这辈子会不会有钱""财从哪来、稳不稳""能不能有像样的地位或成就"时使用。以福点（Part of Fortune）及其主星判财富的来源与持续，以日月及其护卫星（doryphory）判地位的高低与种类；只在象征层做倾向性推演，不预判金额、不替用户做财务或人生决定。
input_schema:
  required: [birth_data, fortune_question]
  optional: [current_stage, focus_area, work_context]
output_schema:
  primary: {wealth_reading: string, rank_reading: string, tendency_summary: string}
  secondary: [wealth_source_planet, doryphory_note, stability_note, cautions]
requires:
  pip: [pymeeus]
  commands: [python3]
---

# 财富与地位：从福点与日月护卫看外在际遇

**来源**：《Tetrabiblos（四书 / Quadripartite）》BOOK THE FOURTH 第 I–III 章（PROEM / THE FORTUNE OF WEALTH / THE FORTUNE OF RANK）｜ 证据等级：firsthand

## 触发条件

**应该触发**：
- 用户报了出生信息，问"我这辈子会不会有钱""财运怎么样""钱从哪来"
- 用户问"我能不能有地位 / 有成就 / 当领导"
- 用户想知道"我的财稳不稳、会不会破财""这条路能不能攒下东西"
- 用户在做人生阶段盘点，想从"外在际遇（财、位）"这个象征角度加一层参照

**不应触发**：
- 用户问的是"我适合做什么工作 / 干什么职业" → 走 `ptolemy-vocation`
- 用户要的是一个具体决定（该不该投资、该不该辞职），本 skill 只推倾向、不做决定
- 用户只想听"我一定发财"的保证 → 本 skill 明确不给保证
- 用户没给出出生信息 → 先索取，信息不全不推

## R：原文锚点

> "Each of these fortunes has a distinct relationship; for instance, that of wealth relates to the body, and that of rank to the mind."（BOOK THE FOURTH, CHAPTER I: PROEM）（已据公版原文核）

> "The circumstances regulating the fortune of wealth are to be judged of from that part alone, which is expressly denominated the Part of Fortune"（BOOK THE FOURTH, CHAPTER II: THE FORTUNE OF WEALTH）（已据公版原文核）

> "if the planets which assume dominion of the Part of Fortune be in full force, they will create much wealth, and especially should the luminaries also give them suitable testimony in addition."（同上，CHAPTER II: THE FORTUNE OF WEALTH）（已据公版原文核）

> "Saturn will effect the acquirement of wealth by means of buildings, agriculture, or navigation; Jupiter, by holding some government, or office of trust, or by the priesthood; Mars, by the army and military command; Venus by means of friends, by the dowry of wives, or by other gifts proceeding from women; and Mercury by the sciences and by trade."（同上，CHAPTER II: THE FORTUNE OF WEALTH）（已据公版原文核）

> "if stars of an adverse condition should either be in elevation above the ruling places, or ascend in succession to them, the wealth will not continue."（同上，CHAPTER II: THE FORTUNE OF WEALTH）（已据公版原文核）

> "The disposition of the luminaries and the respective familiarities, exercised by the stars attending them, are to be considered as indicative of the degree of rank or dignity."（BOOK THE FOURTH, CHAPTER III: THE FORTUNE OF RANK）（已据公版原文核）

> "if the chief dominion be claimed by the malefics, or by stars of an adverse condition, the dignities will be more subordinate, and more dangerous and evanescent."（同上，CHAPTER III: THE FORTUNE OF RANK）（已据公版原文核）

> "if Saturn have chief dominion of the doryphory, the power and authority derived therefrom will lead to wealth and profit: authority proceeding from Jupiter and Venus will be pleasurable, and attended by presents and honours: that proceeding from Mars will consist in commanding armies, in obtaining victories, and in overawing the vanquished: and that proceeding from Mercury will be intellectual, superintending education and study, and directing the management of business."（同上，CHAPTER III: THE FORTUNE OF RANK）（已据公版原文核）

## I：核心解释

1. **财与位是两条不同的线**：财富牵连"身"（外在条件、可积累之物），地位牵连"心智所显"（被承认的高度）。同一张盘要分开看，不能用一个"命好"糊过去。（R1）
2. **财单看福点**：判财富只看"福点"这一个点——它与上升点的距离，等于太阳与月亮之间的距离；由此定出它的位置。（R2）
3. **财看主星的力量与连接**：谁主福点，就决定了财的来路；主星"in full force"（有力量、庙旺居角）、再得日月作证，则财厚；主星无力则财薄。财的**来源种类**由主星是土 / 木 / 火 / 金 / 水而定。（R3、R4）
4. **财的持续看制衡**：同条件的星助它，财可持续；反之，若不同条件的星高踞其上、或依次升到这些位置，财就不长久——书里说"the wealth will not continue"。（R5）
5. **地位看日月与护卫星**：位阶的高低，看两个光体（日、月）的状态，以及"随侍"它们的星（护卫星 / doryphory）各自的力量与亲疏。（R6）
6. **地位有层级，不是有 / 无**：护卫星整体有力则显赫；若只有一部分入角或与天顶有相位，则只到"有限的高位"；若都不成相位，则"altogether undistinguished"。书里给的是**从帝王、诸侯、长官一路到完全默默无闻的分层**。（R6、R7）
7. **种类的差异由护卫主星决定**：土星主护卫 → 权力带来财与利；木、金主 → 愉悦、馈赠与荣誉；火 → 统军、克敌；水 → 学业、文字与经管。（R8）

## A1：来源应用 — 书里给的具体做法

- **定福点**：福点的位置，"always as far removed from the ascendant as the Sun is distant from the Moon"——不论昼生夜生都这样定。
- **判财的来路**（书里原样给的对照）：土星 → 建筑、农业、航运；木星 → 政府的官职、受托的职位、祭司之职；火星 → 军旅与统帅；金星 → 朋友、妻的嫁资、来自女性的馈赠；水星 → 科学与贸易。
- **土星兼与木星成相位** → 由继承得财；若两者在"上位的角"、木星又在双体星座且得月的应用，则"will also be adopted by persons unallied to him, and will become heir to their property"（被无亲缘者收养而承其财产）。
- **判财的稳固**：与主福点之星同条件的星也主事，则财持久；不同条件之星高踞或依次上升，则财不继。**持续的时间**以"造成损失的星在角与后续宫上的赤纬弧"来算。
- **判地位**：日月在阳性星座且入角，再得全部五星组成的护卫（日在东、月在西方）→ 帝王诸侯；护卫星亦入角或与天顶成相位 → 更显赫；若只有一日或一月入角、护卫星不入角也不给天顶作证 → 只到"delegated governor, or commander of an army, or dignitary of the priesthood"这样的有限高位；若两光体都不入角、护卫星多数入角或与角成相位 → 只在"ordinary civil and municipal affairs"里居首；全不成相位 → 无名；既无阳性星座、又无角、又无吉星 → 默默与逆境。
- **判种类的差别**：吉星或同条件星掌握主导 → 所获之位不仅重要且"more securely established"；凶星或异条件星主导 → 位分较低、危险且易逝。

## A2：典型触发场景

- 刚拿到星盘，最关心"这辈子财富能到什么程度"
- 正站在"稳定工作"与"下海博一把"之间，想听一个象征层的参照
- 家族里对"名声 / 地位"看得很重，用户想知道自己有没有
- 经历了破财或事业受挫，想回头看盘里有没有对应的线索
- 做长期人生规划，把"财"和"位"分开来盘一盘

## E：执行步骤

### 步骤1：确认出生信息，定出基本要素

**输入**：出生日期、时间、地点。
**输出**：上升点、日 / 月所在、福点位置（福点＝从上升量出与日月距离相等的点）。
🔴 **CHECKPOINT — 触发条件：用户没给全出生信息（只给日期没给时间 / 地点）**：停在这里索取，缺时间地点就不硬推，并说明这类象征层推演对出生信息的依赖。

### 步骤2：读福点与主财之星

**输入**：步骤1 的福点。
**输出**：财富来路（对应五星之一或多）＋ 财的力量强弱 ＋ 是否可得继承 / 承接他人财产。
照 R2–R5：先定福点的显主，再看其力量与同 / 异条件之星的高低先后。
🔴 **CHECKPOINT — 触发条件：用户想拿这一步的结论去做投资、借贷或大额消费决定**：退回边界——本 skill 只给倾向，**不替用户做财务决定**；选择与责任在人。

### 步骤3：读日月与护卫星，定地位层级

**输入**：步骤1 的日 / 月状态 ＋ 与之相随的星。
**输出**：位阶从"显赫"到"默默"的定性分层 ＋ 种类（由护卫主星定）。
照 R6–R8：日月是否在阳性星座、是否入角、护卫星是否入角或与天顶成相位，决定层级；护卫主星决定"哪一种"地位。
🔴 **CHECKPOINT — 触发条件：用户把"帝王 / 显赫"当成承诺或当成炫耀**：守边界——书里给的是分层，多数人落在中间层次；不许把最高档说成保证。

### 步骤4：合成倾向小结

**输入**：步骤2、3 的输出。
**输出**：一段"财的来路与稳固度 + 地位的大致层级与种类"的**倾向性**小结，并注明这只是象征层推演。
🔴 **CHECKPOINT — 触发条件：用户追问"具体能赚多少 / 几岁发迹 / 一定是哪种结局"**：明确书里只给来路、强度与层级，不给金额与年份；不编具体数字。

## B：边界与失败模式

| 情况 | 表现 | 怎么处理 |
|------|------|---------|
| 要具体金额 / 发迹年份 | "我几岁能赚到多少万" | 🛑 书里只给来源、强弱与分层；不给数字与年份，如实说明。 |
| 要一个保证 | "你就说我会不会发财" | 🛑 不做保证，只作倾向性推演。 |
| 拿结论去做财务决定 | "那我是不是该把房子抵押去创业" | 🛑 **不替用户做财务决定**；只提供一种象征视角，选择权与责任在人。 |
| 断章取义吓人 | "书里说我的财不长久，完了" | 🛑 退回全书立场：这是"倾向"，不是命定（见安全兜底）。 |
| 出生信息不全 | 只有生日没有时间 | 🛑 停在步骤1，索取信息。 |
| 借财位话题问健康 / 寿命 | "我财运这样，是不是也活不长" | 🏥 明确不做健康 / 寿命断言，转出该话题。 |

**边界规则**：
1. 本 skill 只做象征层的**倾向性推演**，不是命定论，也不是预言。
2. **只作倾向性推演，选择权在人**：不替用户做婚姻 / 职业 / 财务 / 人生决定。
3. 财的"来源种类"来自书的五星对照，"持续 / 层级"来自书的分层——不自行添加书里没有的判法。
4. 与相邻 skill 分工：职业走 `ptolemy-vocation`；婚姻走 `ptolemy-marriage`；只做"财 / 位"两线。
5. 需要出生信息才能触发；缺信息不推。

**自查清单**：
- [ ] 我确认了用户给了完整的出生信息（日期＋时间＋地点）
- [ ] 我把"财"与"位"分开看，没有用一个笼统的"命好 / 命差"糊过去
- [ ] 财的来路对应到了书里的五星对照之一
- [ ] 地位用的是分层语言，没有把某一档说成保证
- [ ] 我说明了这只是倾向性推演、选择权在用户自己

**安全兜底**：
- **不是命定论**。书里原话："the fulfilment of events thus indicated must not be ascribed solely to the vigour of the cause producing them, nor to any inevitable fate, but rather to the absence of any opposing influence capable of prevention."（BOOK THE FIRST, CHAPTER III: THAT PRESCIENCE IS USEFUL）
- **只作倾向性推演，选择权在人**：不替用户做财务 / 职业 / 人生决定，最终选择与责任在用户自己。
- **不做健康 / 寿命断言（🏥）**：涉及身体、疾病、寿数时只做提醒与陪伴，指向专业资源，不做诊断。
- 触发需出生信息；没有出生信息不推。

## 📖 练习手册

**分两栏写盘记**：左边写"财"（福点、主星、来路、稳固），右边写"位"（日月、护卫星、层级、种类）。两栏各写三行以内，练"财位分明"。

**对照现实**：把盘里的"财的来源种类"与你过去真正赚到钱的路径对照，看看是印证、是补充、还是无关——只做参照，不做结论。

## 🚫 反例黑名单

1. **把"帝王 / 显赫"当承诺** → 🛑 书里是分层，最高档极少数，不许当保证给出。
2. **拿"财不长久"去吓人或劝人放弃** → 🛑 那是倾向，不是判决。
3. **替用户做投资 / 辞职 / 借贷决定** → 🛑 越界，选择权在人。
4. **编造书里没有的判法**（自创星曜吉凶、加数字预测） → 🛑 A1/E 只用书里的对照与分层。
5. **把财位话题引到健康 / 寿命** → 🏥 明确拒绝并转出。

### 灰色地带

- **用户只是想"听个吉利"，并不真做分析**：可以给象征层的倾向，但要一句话点明这是文化 / 象征参照，不是事实预测。
- **多颗星同主福点、来路互相矛盾**：书里让"看哪一颗权利更大、更占主导"来定优先，照此判断，不必强行统一成一个来源。
- **用户拿盘里的话去评价别人（家人 / 合作者）**：只描述盘本身的倾向，不替用户给别人下判断。
