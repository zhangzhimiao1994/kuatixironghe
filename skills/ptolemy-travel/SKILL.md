---
name: ptolemy-travel
description: 出行与迁居的星盘推演。当用户给出出生信息、问"我会不会去外地 / 出国""要不要搬家迁居""出行顺不顺利"时使用。以日月相对角宫的位置、尤其以月，判行程与迁居的倾向，以福点与吉凶星判出行得失；只在象征层做倾向性推演，不替用户做搬迁 / 出行决定、不断言吉凶事件。
input_schema:
  required: [birth_data, travel_question]
  optional: [destination, planned_timing, life_context]
output_schema:
  primary: {travel_tendency: string, direction_tendency: string, quality_tendency: string}
  secondary: [luminary_condition, benefic_or_malefic_note, cautions]
requires:
  pip: [pymeeus]
  commands: [python3]
---

# 出行与迁居：从日月与福点看行程倾向

**来源**：《Tetrabiblos（四书 / Quadripartite）》BOOK THE FOURTH 第 VIII 章（TRAVELLING）｜ 证据等级：firsthand

## 触发条件

**应该触发**：
- 用户给了出生信息，问"我会不会离开家乡 / 去外地 / 出国"
- 用户问"要不要搬家 / 迁居，盘里怎么说"
- 用户问"我这一趟出行顺不顺 / 有没有波折"（作象征层参照）
- 用户在纠结"留下还是走"，想加一层参照

**不应触发**：
- 用户要一个"该不该搬 / 该不该去"的决定 → 本 skill 只推倾向，**不替用户做搬迁 / 出行决定**
- 用户问的是**工作机会在哪** → 走 `ptolemy-vocation`
- 用户问"什么时候出行最合适" → 时点走 `ptolemy-periods-of-life`
- 用户没给出出生信息 → 先索取，信息不全不推

## R：原文锚点

> "The circumstances indicative of travel are to be considered by means of the situation held by both the luminaries, in respect to the angles, and especially, by means of that held by the Moon."（BOOK THE FOURTH, CHAPTER VIII: TRAVELLING）（已据公版原文核）

> "should she be descending, or cadent from the angles, she will cause journeys and changes of residence"（同上，CHAPTER VIII: TRAVELLING）（已据公版原文核）

> "if the part of Fortune, also, should happen to be placed in signs which produce travelling, the course and practice of the whole life will be engaged in foreign lands."（同上，CHAPTER VIII: TRAVELLING）（已据公版原文核）

> "if the luminaries be posited in the cadent houses of the oriental quadrants, the travel will take place in the eastern or southern quarters of the world"（同上，CHAPTER VIII: TRAVELLING）（已据公版原文核）

> "when Jupiter and Venus may be in dominion over the luminaries, and over the places producing travel, they will render the journeys agreeable, as well as free from danger"（同上，CHAPTER VIII: TRAVELLING）（已据公版原文核）

> "Saturn and Mars, if controlling the luminaries, and, especially, if placed distant from each other, will produce great dangers, and at the same time render the journey fruitless and unavailing."（同上，CHAPTER VIII: TRAVELLING）（已据公版原文核）

> "if the said signs be bicorporeal, or double in form or figure, travel will be constantly repeated and continued."（同上，CHAPTER VIII: TRAVELLING）（已据公版原文核）

## I：核心解释

1. **看日月、尤其看月**：出行由两个光体相对角宫的位置指示，尤其以月为主。（R1）
2. **月落 / 离角 → 有行程与迁居**：月若"descending, or cadent from the angles"（下行或离角），会带来journeys与迁居；火星若也下行或离天顶，且与光体成刑或冲，有时同样如此。（R2）
3. **福点在"主出行"的星座 → 一生在异地**：若福点落在产生出行的星座里，"the course and practice of the whole life will be engaged in foreign lands"。（R3）
4. **吉凶星定行程的性质**：吉星主管这些位置或随后上升到它们 → 在外的际遇体面、有利，归途也顺；凶星主管或随后升到它们 → 外行有险、归途多阻。（R 附带）
5. **方位**：光体落在东方象限的"落宫"（cadent houses）→ 出行朝向世界的东或南方；落在西方位置或西方象限 → 朝北或西方。（R4）
6. **频次**：主出行的星座是单形、或主星单一位 → 出行相隔较久、偶一为之；双体 / 双形 → "travel will be constantly repeated and continued"。（R7）
7. **行程的顺逆**：木、金主管光体与主出行的位置 → 行程愉快、无险，沿途受地方长官与友人的助，天气也顺；土、火主管光体（尤其彼此远离时）→ 大险、无功。书里再按星座属性细分险从何来：水象 → 船难或荒野；固定象 → 崖坠与逆风；回归 / 二分象 → 缺粮与瘴气；人形象 → 劫掠、背叛；陆象 → 野兽或地震。（R5、R6）

## A1：来源应用 — 书里给的具体做法

- **看日月相对角宫**：尤其看月是否下行、离角。
- **看福点**：是否落在"主出行"的星座里（判一生是否在异地）。
- **看吉凶星**：木、金主管 → 行程愉快无险、归途顺；土、火主管（尤其二者远隔）→ 大险无功。
- **判方位**：光体在东方象限的落宫 → 东 / 南；在西方 → 北 / 西。
- **判频次**：单形星座 / 单一位主星 → 偶尔；双体 / 双形 → 频繁而持续。
- **细分险源**（书里原样）：水象 → 船难、荒野；固定象 → 崖坠、逆风；回归 / 二分象 → 缺粮、瘴气；人形象 → 劫掠、背叛、掠夺；陆象 → 野兽、地震。若水星也参与，则还有因被指控、以及爬虫毒咬而来的危险。
- **判得失质量**：再看主职业 / 财富 / 身体 / 地位之星的所在位置的属性（书里说照前面已述的形式）。**时段**由五星的过境推。

## A2：典型触发场景

- 面临"留家乡还是去外地 / 出国"的选择，想加一层参照
- 已在异地，想理解"为什么我总在移动"
- 计划一趟长途，想知道象征层的顺逆（而非买保险式的判断）
- 想理解"迁移"在自己人生里的位置

## E：执行步骤

### 步骤1：确认出生信息

**输入**：出生日期、时间、地点。
**输出**：日、月相对角宫的位置，尤其月的状态；福点位置。
🔴 **CHECKPOINT — 触发条件：缺出生信息**：停在索取，不硬推。

### 步骤2：读"是否出行 / 迁居"的倾向

**输入**：月是否下行 / 离角；福点是否在"主出行"的星座。
**输出**：出行 / 迁居的倾向强度 ＋ 是否倾向一生在异地。
照 R2、R3。
🔴 **CHECKPOINT — 触发条件：用户把"一生在异地"当成命运**：守边界——这是倾向性表述，不是命定；选择权在人。

### 步骤3：读方位与频次

**输入**：光体所在象限；主出行星座的形态。
**输出**：大致方位（东 / 南 / 西 / 北）与"偶尔 / 频繁"的倾向。
照 R4、R7。
🔴 **CHECKPOINT — 触发条件：用户拿方位去决定"该去哪个城市"**：说明这只是书里的象限对应，不是对具体地点的指引。

### 步骤4：读行程顺逆的倾向

**输入**：主管光体与主出行位置的是吉星还是凶星。
**输出**：行程"愉快无险 / 有险无功"的定性倾向（细分险源可列，但只作象征层）。
照 R5、R6。
🔴 **CHECKPOINT — 触发条件：用户据此决定"要不要搬 / 要不要去"**：退回——**不替用户做搬迁 / 出行决定**，只作倾向性推演。

## B：边界与失败模式

| 情况 | 表现 | 怎么处理 |
|------|------|---------|
| 拿盘决定该不该搬 / 去 | "盘说我有险，那我别去了" | 🛑 **不替用户做搬迁 / 出行决定**，选择权在人。 |
| 用方位当"去哪座城市"的指引 | "东边好，那我去上海" | 🛑 象限对应只是象征层，不是地点指引。 |
| 把"一生在外"当命运 | "那我注定漂泊了" | 🛑 倾向不是命定；选择与经营在人。 |
| 把"险源清单"当预言 | "我会遇到地震 / 船难" | 🛑 那是象征层的分类，不是对具体灾难的预言。 |
| 借出行问时点 | "什么时候走最好" | 🛑 时点走 `ptolemy-periods-of-life`。 |
| 缺出生信息 | 无出生时间 | 🛑 停在索取。 |

**边界规则**：
1. 本 skill 只做象征层的**倾向性推演**，不是命定论，也不是对具体事件的预言。
2. **只作倾向性推演，选择权在人**：不替用户做搬迁 / 出行 / 人生决定。
3. 方位、频次、顺逆与险源一律用书里的条目；不自行添加地点或事件。
4. 与相邻 skill 分工：职业走 `ptolemy-vocation`；时点走 `ptolemy-periods-of-life`。
5. 需要出生信息才能触发；缺信息不推。

**自查清单**：
- [ ] 我确认了完整出生信息
- [ ] 我以日月、尤其以月为主来读出行
- [ ] 我用了福点与吉凶星读得失
- [ ] 我用倾向性语言说顺逆，没有预言具体事件
- [ ] 我说明了不替用户做搬迁 / 出行决定、选择权在用户

**安全兜底**：
- **不是命定论**。书里原话："the fulfilment of events thus indicated must not be ascribed solely to the vigour of the cause producing them, nor to any inevitable fate, but rather to the absence of any opposing influence capable of prevention."（BOOK THE FIRST, CHAPTER III: THAT PRESCIENCE IS USEFUL）
- **只作倾向性推演，选择权在人**：不替用户做搬迁 / 出行 / 人生决定。
- **不做健康 / 寿命断言（🏥）**：涉及身体、疾病、寿数时只做提醒与陪伴，指向专业资源；真实出行安全以官方信息与专业渠道为准。
- 触发需出生信息；没有出生信息不推。

## 📖 练习手册

**象限标注**：在纸上画出东 / 南 / 西 / 北，把光体所在象限标出来，写上"书里说朝向 X / Y"，再问自己：这真的等于我该去那儿吗？

**去除预言**：把盘里得到的"险源"（船难 / 地震等）改写成"象征层的风险意象"，练"意象 ≠ 事件"。

## 🚫 反例黑名单

1. **拿盘替用户决定搬 / 不搬** → 🛑 越界，选择权在人。
2. **把象限方位当地点指引** → 🛑 只是象征层。
3. **把险源清单当灾难预言** → 🛑 意象不是事件。
4. **自创出行判法** → 🛑 A1/E 只用书里的条目。
5. **借出行话题引向健康 / 寿命** → 🏥 拒绝并转出。

### 灰色地带

- **用户已经有明确的搬迁计划，只是想要个"吉利确认"**：可以给象征层的描述，但要一句点明这是文化参照，不是事实预测。
- **"一生在外"与"偶尔出行"两种表述同时出现**：以书里的条件为准分主次，如实说明，不强行统一。
- **用户拿"有险"去阻断自己**：把话题从"盘说危险"拉回"你想不想、能不能做好准备"。
