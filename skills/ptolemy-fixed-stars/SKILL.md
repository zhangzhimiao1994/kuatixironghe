---
name: ptolemy-fixed-stars
description: 恒星（黄道内外）的性质取用。当用户报了出生信息，问某颗恒星/星团（如角宿一、心宿二、毕宿五、轩辕十四、昴星团、大角星）对某主题的作用，或想按《四书》给恒星"像哪颗行星"的脾性时使用。需要出生信息；没有出生信息不激活。
input_schema:
  required: [birth_info, fixed_star_or_constellation, topic]
  optional: [zodiac_sign, aspect_to_planet, chart_context]
output_schema:
  primary: {star_nature: string, planetary_analogue: string, topic_read: string}
  secondary: [constellation_position, intensity_note, caveats]
requires:
  pip: [pymeeus]
  commands: [python3]
---

# 恒星的性质：像哪颗行星，管哪个部位

**来源**：《Tetrabiblos（四书）》BOOK THE FIRST，CHAPTER IX THE INFLUENCE OF THE FIXED STARS / CHAPTER X CONSTELLATIONS NORTH OF THE ZODIAC / CHAPTER XI CONSTELLATIONS SOUTH OF THE ZODIAC ｜ 证据等级：firsthand

## 触发条件

**应该触发**：
- 用户给了出生信息，问"我盘里那颗恒星（如心宿二、轩辕十四、角宿一、毕宿五）意味着什么"
- 用户要按《四书》的对照法，给某颗恒星或某个星座内的亮星找"像哪颗行星"的脾性
- 用户问黄道十二宫内部的某个部位（如白羊头部、金牛的昂宿、天蝎之身、狮子之心）带什么性质
- 用户问黄道以北或以南的某个星座（如天鹰、猎户、大犬、南鱼）起什么作用
- 用户要把恒星的脾性并进它对某主题（性格、事业、身体倾向）的读法里

**不应触发**：
- 用户没给出生信息 → 不激活，先索取
- 用户要的是行星本身的性质 → 走 `ptolemy-planet-natures`
- 用户要的是星座（白羊/金牛……整个宫）的性质 → 走 `ptolemy-sign-natures`
- 用户要的是行星之间、星座之间的相位 → 走 `ptolemy-aspects`
- 用户问"是不是命中注定" → 走 `ptolemy-prescience-frame`

## R：原文锚点

> "Next in succession, it is necessary to detail the natures and properties of the fixed stars; all of which have their respective influences, analogous to the influences of the planets"（BOOK THE FIRST・CHAPTER IX「THE INFLUENCE OF THE FIXED STARS」）（已据公版原文核）

> "The stars in the head of Aries possess an influence similar in its effects to that of Mars and Saturn"（BOOK THE FIRST・CHAPTER IX）（已据公版原文核）

> "Those stars in Taurus, which are in the abscission of the sign, resemble in their temperament the influence of Venus"（BOOK THE FIRST・CHAPTER IX）（已据公版原文核）

> "Those in the loins, and the bright one in the tail, are like Saturn and Venus"（BOOK THE FIRST・CHAPTER IX）（已据公版原文核）

> "The bright stars in the front of the body of Scorpio have an effect similar to that produced by the influence of Mars, and partly to that produced by Saturn"（BOOK THE FIRST・CHAPTER IX）（已据公版原文核）

> "The constellations north of the zodiac have their respective influences, analogous to those of the planets"（BOOK THE FIRST・CHAPTER X「CONSTELLATIONS NORTH OF THE ZODIAC」）（已据公版原文核）

> "The influences of the constellations south of the zodiac, existing in a similar mode, are as follows"（BOOK THE FIRST・CHAPTER XI「CONSTELLATIONS SOUTH OF THE ZODIAC」）（已据公版原文核）

> "The bright star in the mouth is like Jupiter, and partly like Mars"（BOOK THE FIRST・CHAPTER XI）（已据公版原文核）

## I：核心解释

1. **恒星的读法是"类比行星"**：书里说恒星各有其影响，且这些影响与行星的影响相类比；所以读恒星的办法，就是找出它"像哪颗（或哪两颗）行星"，再借用那颗行星的脾性。（R1）
2. **黄道十二宫要逐宫逐部位看**：同一个星座的不同部位（头、口、足、尾、角、心、腰、爪……）对应的行星类比可以不同。例如白羊头部像火星与土星；金牛被切割处像金星；狮子之心（轩辕十四）同于火星与木星；天蝎之身（含心宿二）像火星并略似木星。（R2–R5）
3. **黄道以北、以南的星座同样各有所像**：书里给出北方星座表（如小熊像土星、天龙像土星与火星、天鹰像火星与木星等）与南方星座表（如鲸鱼像土星、大犬之口的亮星像木星而略似火星、南鱼之口像金星与水星等）。（R6–R8）
4. **恒星的强度还受"外因"影响**：书里的注解说，恒星中越大的越有力；越靠近黄道带的越强；北纬北赤纬的、处于天顶的、与某行星部分同度或共同升起/落下/上中天的，power 都增大；而恒星本身并不发光（只是位置与同度关系带来影响）。
5. **所以一颗恒星的读法 = 类比的主星脾性 × 它在哪个宫/部位 × 它有多强 × 与哪颗行星同度**。

## A1：来源应用

书里给的具体做法（不是我的发挥）：

- **查表定性**：按 CHAPTER IX 的十二宫逐部位表、CHAPTER X 的北方星座表、CHAPTER XI 的南方星座表，给目标恒星/部位找到"像哪颗（哪几颗）行星"。（R2–R8）
- **两星叠加**：多数条目是"像 A，且部分像 B"，读时把两颗行星的脾性叠起来（如"像火星与土星"＝干热叠加干冷）。
- **按部位取用**：同一星座不同部位可有不同类比，务必读到用户所指的那个部位（如"狮子之心"与"狮子之颈"不同）。
- **看强度**：越大、越近黄道、越靠天顶、与行星同度或共升落/上中天的恒星越有力；据此调整影响权重（书里注解所述）。
- **记得恒星本身不发光**：其作用来自位置与同度关系，不来自自身辐射。

## A2：典型触发场景

- 用户问"我盘里那颗心宿二是好是坏"，想按古书读
- 用户想知道毕宿五/轩辕十四/角宿一分别像哪颗行星、带什么性质
- 用户问"狮子座的心和脖子部位性质一样吗"
- 用户要查黄道以外某个星座（猎户、大犬、天鹰）的含义
- 用户要把恒星的性质并进它对性格或某主题的读法

## E：执行步骤

1. **确认出生信息与目标恒星/部位**　输入：出生信息 + 具体恒星名或"星座+部位"。→ 输出：一个精确到部位的查询对象。
   🔴 **CHECKPOINT — 触发条件：无出生信息**：不激活，先索取。
   🔴 **CHECKPOINT — 触发条件：用户只给星座名（如"我白羊座"）**：追问是哪个部位/哪颗星，因为不同部位类比不同（R2）。

2. **查类比**　输入：目标。→ 输出：一句"像哪颗（哪几颗）行星"。
   照 R2–R8：黄道内的查 CHAPTER IX，北方查 CHAPTER X，南方查 CHAPTER XI。
   🔴 **CHECKPOINT — 触发条件：目标不在书表内**：如实说书里未列，不杜撰类比。

3. **叠加主星脾性**　输入：类比行星。→ 输出：该部位的热/冷/湿/干与吉凶主调（转引 `ptolemy-planet-natures` 的性质表）。
   🔴 **CHECKPOINT — 触发条件：涉及身体部位**：转安全兜底 🆘/🏥，不作健康判断。

4. **估强度**　输入：星等、与黄道的距离、纬度、是否与行星同度或共升落/上中天。→ 输出：影响权重（强/中/弱）。
   照书里注解所述的强度规则。

5. **并入主题读**　输入：前面的性质与强度 + 用户要看的主题。→ 输出：一句"倾向"读法。
   🔴 **CHECKPOINT — 触发条件：读法滑向"必然/注定"**：转 `ptolemy-prescience-frame` 改写成倾向+条件。

## B：边界与失败模式

| 失败模式 | 长什么样 | 怎么退回去 |
|---|---|---|
| 杜撰类比 | 书表里没有的星也给出"像木星" | 🛑 回到步骤2 的 CHECKPOINT，书里未列就说未列。 |
| 只看星座不看部位 | 拿"白羊"整体套一个类比 | 🛑 回到步骤1，精确到部位（R2）。 |
| 把恒星当发光体 | 说"它发出某种射线" | 🛑 书里明确恒星本身不发光，作用来自位置与同度。 |
| 忽略强度 | 把一颗暗星与一等亮星等同 | 🛑 回到步骤4 估强度。 |
| 拿恒星下健康断语 | "这颗星在你某某宫，你要得某病" | 🛑 走安全兜底，不作医疗判断。 |
| 写成命定论 | "命中带这颗星，所以必然……" | 🛑 转 `ptolemy-prescience-frame` 改写。 |

**边界规则**：
1. 本 skill 只处理恒星，不处理行星性质与星座性质（分别走 `ptolemy-planet-natures`、`ptolemy-sign-natures`）。
2. 书表之外的星不硬套类比。
3. 需要出生信息才能用；没有出生信息不激活。
4. 涉及身体部位时只谈倾向，不作诊断、不替代就医。

**自查清单**：
- [ ] 我确认过出生信息
- [ ] 我把目标精确到了星座的哪个部位/哪颗星
- [ ] 我给出的类比能在 R 节或书表里找到出处
- [ ] 我按"越大越近黄道越强"估了强度
- [ ] 我的结论是倾向，不是必然

**安全兜底**：🆘/🏥 恒星条目里出现身体部位时，只谈性质倾向，不作医疗判断、不做寿命断言、不替代就医（急救 120、心理援助 12356）。

## 📖 练习手册

1. **部位对照**：挑一个星座，把书里它各部位的行星类比抄成一张小表，体会同宫不同部位怎么不同。
2. **两星叠加**：任选一条"像 A 且部分像 B"的条目，写出叠加后的热冷湿干。
3. **强度排序**：给你盘里的两颗恒星，按"星等、离黄道远近、是否与行星同度"排出强弱。

## 🚫 反例黑名单（不要做的事）

1. 给书表外的星编一个类比。
2. 只报星座名就下整体类比。
3. 说恒星自己发光/放射能量。
4. 把恒星条目直接翻成病症或寿数。
5. 用恒星读法下"必然"结论。

## 灰色地带

- **同一部位两处说法不一致**：以 CHAPTER IX 十二宫表为准，本书内部冲突时优先采用正文章节表，并把分歧如实标出。
- **星名古今不同**（如 Facula / 毕宿五、Regulus / 轩辕十四、Antares / 心宿二）：先对齐古今星名再查类比，拿不准就说明对应关系存疑。
- **恒星与行星同度**：此时两者影响会叠加，强度也上升；读法上以"恒星加彩、行星为主"处理，别让恒星喧宾夺主。
