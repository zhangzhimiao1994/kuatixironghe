---
name: ptolemy-vocation
description: 职业与事业的星盘推演。当用户给出出生信息、问"我适合做什么工作""干哪一行""事业能不能做起来"时使用。以太阳前最近东出之星与天顶所在定"职业之主"，以火 / 金 / 水三星与所在星座定职业的种类；只在象征层做倾向性推演，不替用户做职业决定、不给收入承诺。
input_schema:
  required: [birth_data, work_question]
  optional: [current_job, skills_and_interests, career_dilemma]
output_schema:
  primary: {vocation_lord: string, vocation_species: string, tendency_summary: string}
  secondary: [planet_signature, magnitude_note, cautions]
requires:
  pip: [pymeeus]
  commands: [python3]
---

# 职业与事业：从"职业之主"与三星种类看从业倾向

**来源**：《Tetrabiblos（四书 / Quadripartite）》BOOK THE FOURTH 第 IV 章（THE QUALITY OF EMPLOYMENT）｜ 证据等级：firsthand

## 触发条件

**应该触发**：
- 用户给了出生信息，问"我适合做什么职业 / 干什么行业"
- 用户问"我的事业能不能做起来、能不能做到有地位"
- 用户在做转行 / 择业的纠结，想从象征层加一层参照
- 用户想理解"为什么我总被某类工作吸引"

**不应触发**：
- 用户问"我这辈子会不会有钱 / 有没有地位" → 走 `ptolemy-wealth-and-rank`
- 用户要的是具体 offer 的取舍、薪酬谈判、要不要裸辞 → 本 skill 不做决定
- 用户问的是"我现在该不该走 / 什么时候跳槽"这类时点问题 → 走 `ptolemy-periods-of-life`
- 用户没给出出生信息 → 先索取，信息不全不推

## R：原文锚点

> "The dominion of the employment, or profession, is claimed in two quarters; viz. by the Sun, and by the sign on the mid-heaven."（BOOK THE FOURTH, CHAPTER IV: THE QUALITY OF EMPLOYMENT）（已据公版原文核）

> "It is, therefore, necessary to observe whether any planet may be making its oriental appearance nearest to the Sun, and whether any be posited in the mid-heaven; especially, when also receiving the application of the Moon."（同上，CHAPTER IV: THE QUALITY OF EMPLOYMENT）（已据公版原文核）

> "the species of the employment will be distinguished by means of the respective properties of the three planets, Mars, Venus, and Mercury, and of the signs in which they may be posited."（同上，CHAPTER IV: THE QUALITY OF EMPLOYMENT）（已据公版原文核）

> "Mercury, for instance, produces writers, superintendents of business, accountants, teachers in the sciences, merchants and bankers"（同上，CHAPTER IV: THE QUALITY OF EMPLOYMENT）（已据公版原文核）

> "the signs of human shape promote all scientific pursuits, and such as are of utility to mankind; the quadrupedal signs contribute to produce employment among metals, in business and trade, in house-building, and in the work of smiths and mechanics"（同上，CHAPTER IV: THE QUALITY OF EMPLOYMENT）（已据公版原文核）

> "if the said planets be oriental, or in angles, they will give the person eminence and authority in his employment; but, if occidental or cadent, they will render him subordinate."（同上，CHAPTER IV: THE QUALITY OF EMPLOYMENT）（已据公版原文核）

> "if the malefics be in elevation above the lords of the employment, it will then be mean, disreputable, unprofitable, and insecure"（同上，CHAPTER IV: THE QUALITY OF EMPLOYMENT）（已据公版原文核）

## I：核心解释

1. **"职业之主"有两位候选**：一由太阳（谁在太阳之前最近东出），一由天顶所在星座。两个位置都点到的星，单取它；只点到一位也取它；两位各点一星，则取"权利更大"的那一颗。（R1、R2）
2. **若两者都空**：则取天顶的显主为职业之主，但书里提醒——这种情况多半只是"偶有的营生"，人往往闲居无业。（R2）
3. **种类由火 / 金 / 水三星定**：主职业之星在什么状态、落在什么星座，决定了"做什么"。书里把三颗星各自的职业清单列得很细（水 → 文字、经管、账目、教学、商贾、钱庄；金 → 香、酒、染料、香料、织物、饰物；火 → 与火、金属、器械、军旅相关的行当）。（R3、R4）
4. **星座进一步细分**：人形星座 → 科学与实用之学；四足星座 → 金属、商贸、营建、工匠；回归 / 二分星座 → 转译、交换、度量、农事、宗教职分；陆生 / 水生星座 → 与水有关的一切（养植物、造船、殡殓、防腐、盐）。（R5）
5. **两颗星同主时会"合成"新行当**：水＋金 → 音乐、诗歌、演艺；水＋火 → 雕塑、军械、外科、亦含告密与伪造；金＋火 → 染匠、香料、金属加工、医者；火＋水再加土 → 盗匪、刺客一类。（R3 附带清单）
6. **事业的大小看主星之力**：主星在东、入角 → 有权威；在西、落宫 → 居下位。吉星高踞 → 事业重要、有利、稳当；凶星高踞 → 卑微、无利、不稳。（R6、R7）
7. **兴起 / 衰退的时段**同样由星在东西角的态势决定。

## A1：来源应用 — 书里给的具体做法

- **选职业之主**：先看"哪颗星离太阳最近、在东出"，再看"哪颗星在天顶"，两者交叉定主；同时看是否得月的应用。
- **读种类**（书里原样给的对照）：水星主 → writers, superintendents of business, accountants, teachers in the sciences, merchants and bankers，以及占卜、占星、祭祀之属；水＋土 → 代人管事、解梦、庙中占卜；水＋木 → 画师、演说家、辩士；金星主 → 花香、油膏、酒、颜色、染料、香料、织造、画师、成衣；金＋土 → 娱乐装饰、幻术与江湖一类；金＋木 → 竞技与获冠、借女性之势显达；火主（与太阳成相位）→ 用火的行当（厨、熔铸金属）；火（离太阳）→ 造船、铁匠、农人、石匠、木匠、劳力者；火＋土 → 水手、井 / 窖 / 矿工、看护牲畜、屠夫、浴场与展演侍从；火＋木 → 士兵、机匠、收税、客栈、祭祀侍从。
- **看事业大小**：主星在东或入角 → 显达；在西或落宫 → 居下；吉星在上 → 事业重要、有利、安稳、荣耀；凶星在上 → 卑微、无利、不稳，土星带来迟滞与"颜色之别"，火星带来莽撞与张扬。
- **看时段**：由星在东西角的态势推"事业的增减在何时"。

## A2：典型触发场景

- 刚毕业或要填志愿，想从星盘找一个方向做参照
- 干了很多年不对味的活，想看看盘里"本该是什么行当"
- 手上有两份 offer，想加一层象征视角（但不做决定）
- 想理解自己为什么反复被某一类工作吸引
- 做副业 / 转行前的人生盘点

## E：执行步骤

### 步骤1：确认出生信息，定太阳、天顶与月相

**输入**：出生日期、时间、地点。
**输出**：太阳位置、天顶所在星座、月的位置。
🔴 **CHECKPOINT — 触发条件：缺出生时间 / 地点（天顶与月位定不出）**：停在索取；职业之主依赖天顶，缺时间不硬推。

### 步骤2：选出"职业之主"

**输入**：步骤1 的太阳、天顶、月。
**输出**：一颗（或两颗）主职业之星。
按 R1、R2 的优先顺序：双点 → 单取；单点 → 取之；两星分点 → 取权利更大者；两者皆空 → 取天顶显主，并注明"这多主偶有营生 / 闲居"的书里提醒。
🔴 **CHECKPOINT — 触发条件：用户问"那我是不是就注定只能干这个"**：守边界——书里是倾向与种类，不是宿命；人的选择与努力仍在。

### 步骤3：读职业的种类

**输入**：步骤2 的主星 ＋ 其所在星座 ＋ 与之同辉的其他星。
**输出**：一到三类具体行当（用书里的对照，不自行发明）。
照 R3–R5：三星属性给大类，星座属性给细分，另星同辉做合成。
🔴 **CHECKPOINT — 触发条件：用户把"书里列的行当"当成唯一答案**：说明这是**倾向的种类**，不是限定；书里给的是一份行业谱式的列举（某颗星主某事，则生出某类行当），不是职业判决。

### 步骤4：判事业的大小与时段倾向

**输入**：主星的东西 / 角宫状态、吉凶星高低。
**输出**：事业大致"显达 / 居下 / 重要 / 卑微"的定性 ＋ 增减时段的倾向。
🔴 **CHECKPOINT — 触发条件：用户据此要做具体的转行 / 辞职决定**：退回——**不替用户做职业决定**，只给倾向，选择权在人。

## B：边界与失败模式

| 情况 | 表现 | 怎么处理 |
|------|------|---------|
| 把行当清单当唯一答案 | "书里说我是木匠，那我只能当木匠" | 🛑 那是倾向的种类，不是限定；结合现实禀赋与机会。 |
| 要收入 / 职位承诺 | "这行能挣多少、我能当多大官" | 🛑 书里给种类与层级，不给数字；如实说明。 |
| 拿结论替用户做决定 | "那我明天就辞职去做音乐" | 🛑 **不替用户做职业决定**；只提供象征视角。 |
| 借职业话题问时点 | "我几岁能发达" | 🛑 时点走 `ptolemy-periods-of-life`。 |
| 出生时间缺失 | 定不出天顶 | 🛑 停在步骤1，索取。 |
| 借机问健康 / 寿命 | "这行是不是伤身" | 🏥 不做健康 / 寿命断言，转出。 |

**边界规则**：
1. 本 skill 只做象征层的**倾向性推演**，不是命定论。
2. **只作倾向性推演，选择权在人**：不替用户做职业 / 财务 / 人生决定。
3. 种类一律用书里的三星与星座对照；不自行添加行业、不编收入。
4. 与相邻 skill 分工：财与位走 `ptolemy-wealth-and-rank`；时点走 `ptolemy-periods-of-life`。
5. 需要出生信息才能触发；缺时间地点不推。

**自查清单**：
- [ ] 我确认了完整的出生信息（尤其出生时间）
- [ ] 我按"太阳前最近东出 + 天顶"两条线选出了职业之主
- [ ] 职业种类落到了书里三星 / 星座对照之内
- [ ] 我用定性语言说事业大小，没有承诺收入与职位
- [ ] 我说明了这只是倾向、选择权在用户

**安全兜底**：
- **不是命定论**。书里原话："the fulfilment of events thus indicated must not be ascribed solely to the vigour of the cause producing them, nor to any inevitable fate, but rather to the absence of any opposing influence capable of prevention."（BOOK THE FIRST, CHAPTER III: THAT PRESCIENCE IS USEFUL）
- **只作倾向性推演，选择权在人**：不替用户做职业 / 财务 / 人生决定。
- **不做健康 / 寿命断言（🏥）**：涉及身体、疾病、寿数时只做提醒与陪伴，指向专业资源。
- 触发需出生信息；没有出生信息不推。

## 📖 练习手册

**职业谱对照**：把盘里得到的"职业之主"与它的星座，翻回书里的三星 / 星座对照，列出 3–5 个具体行当，再拿它们与你真实做过的事对照，看重合与差异。

**一句话命名**：用书里的语言给这条倾向起个短名（如"以文字与经管为业"），写完再问自己：这是我想要的，还是盘说我要的？

## 🚫 反例黑名单

1. **拿行当清单当唯一出路** → 🛑 倾向不等于限定。
2. **替用户做转行 / 辞职决定** → 🛑 越界，选择权在人。
3. **承诺收入、职位、出名** → 🛑 书里不给这些。
4. **自创职业对照**（书里没写的行业） → 🛑 A1/E 只用书里的对照。
5. **把职业话题引到健康 / 寿命** → 🏥 拒绝并转出。

### 灰色地带

- **主星与时下热门行业对不上**：以书里的"种类"为准去理解，不必硬塞到某个具体岗位。
- **两颗星分主、都说得通**：书里让取"权利更大者"为优先，但可以把第二颗当作补充视角，主次分明即可。
- **用户先问职业、后滑到时点**：先答种类，再把时点问题转到 `ptolemy-periods-of-life`。
