---
name: ptolemy-planet-condition
description: 行星的"处境与强弱"读法。当用户报了出生信息，要问某颗行星在盘里"强不强"——是否入相位/出相位、"面"与"车（御座）"、是否同气相喜（rejoice）、向东向西、顺行逆行速度快慢、落在中天或地平附近还是地平下——时使用。需要出生信息；没有出生信息不激活。
input_schema:
  required: [birth_info, planet, chart_placement]
  optional: [application_or_separation, motion_state, horizon_position]
output_schema:
  primary: {condition_reading: string, strength_score: string, phase_relation: string}
  secondary: [face_chariot_rejoice, motion_modifier, caveats]
requires:
  pip: [pymeeus]
  commands: [python3]
---

# 行星的处境：入出相位、面与车、同气相喜、方位快慢

**来源**：《Tetrabiblos（四书）》BOOK THE FIRST，CHAPTER XXVI FACES, CHARIOTS, AND OTHER SIMILAR ATTRIBUTES OF THE PLANETS / CHAPTER XXVII APPLICATION, SEPARATION, AND OTHER FACULTIES ｜ 证据等级：firsthand

## 触发条件

**应该触发**：
- 用户给了出生信息，问某颗行星在盘里"强不强、有没有力"
- 用户问两颗行星是"入相位"还是"出相位"、谁去就谁
- 用户问某行星是否"在它的面里""在它的车/御座里""同气相喜（rejoice）"
- 用户问某行星向东还是向西、顺行还是逆行、快还是慢，对强弱有什么影响
- 用户问某行星落在中天、地平附近，还是在地平之下，哪个更有力
- 用户要把行星处境并入某主题的强弱判断

**不应触发**：
- 用户没给出生信息 → 不激活，先索取
- 用户要的是行星本身的热冷湿干/吉凶 → 走 `ptolemy-planet-natures`
- 用户要的是入庙入旺三分性界这套权柄 → 走 `ptolemy-dignities`
- 用户要的是两颗星/两宫的相位关系 → 走 `ptolemy-aspects`
- 用户问"是不是命中注定" → 走 `ptolemy-prescience-frame`

## R：原文锚点

> "Each is said to be in its proper face, when the aspect it holds to the Sun, or Moon, is similar to that which its own house bears to their houses"（BOOK THE FIRST・CHAPTER XXVI「FACES, CHARIOTS, AND OTHER SIMILAR ATTRIBUTES OF THE PLANETS」）（已据公版原文核）

> "Each planet is also said to be in its proper chariot, or throne, or otherwise triumphantly situated, when it holds familiarity with the place which it actually occupies by two, or more, of the prescribed modes of connection"（BOOK THE FIRST・CHAPTER XXVI）（已据公版原文核）

> "each planet (although it may possess no familiarity with the sign encompassing it) is said to rejoice, when any connection subsists between itself and other stars of the same condition"（BOOK THE FIRST・CHAPTER XXVI）（已据公版原文核）

> "when a planet occupies a place adverse and dissimilar in condition to itself, much of its influence is dissipated and lost"（BOOK THE FIRST・CHAPTER XXVI）（已据公版原文核）

> "the planet which precedes is said to apply to that which follows; and that which follows to be separating from that which precedes."（BOOK THE FIRST・CHAPTER XXVII「APPLICATION, SEPARATION, AND OTHER FACULTIES」）（已据公版原文核）

> "The influence of each planet, however, is strengthened chiefly when it may be oriental, swift and direct in its proper course and motion"（BOOK THE FIRST・CHAPTER XXVII）（已据公版原文核）

> "it loses strength when occidental and slow in motion or retrograde"（BOOK THE FIRST・CHAPTER XXVII）（已据公版原文核）

> "if it be situated in the mid-heaven, or succedent to the mid-heaven, it is especially strong"（BOOK THE FIRST・CHAPTER XXVII）（已据公版原文核）

> "if it be on the actual horizon, or succedent to the horizon, it is also powerful"（BOOK THE FIRST・CHAPTER XXVII）（已据公版原文核）

## I：核心解释

1. **"面"（face）是相对日月的一种对称**：当某行星对太阳或月亮的相位，与它自己的庙对日月之庙的相位相同，就说它在自己的"面"里。例如金星与水星成六分、且对太阳在西（昏星）、对月亮在东（晨星）时，便合于其庙（金牛/天秤）对日月之庙的关系。（R1）
2. **"车/御座"（chariot/throne）是多重权柄叠加**：当一颗行星凭借两种或更多种既定的关联方式，与它实际所在的宫都有亲缘，就说它在自己的车、御座里、得意洋洋——此时它与所环绕的宫性质相合、相互助益，其影响与能量特别增强。（R2）
3. **"同气相喜"（rejoice）**：即使行星与所在的宫毫无亲缘，只要它与别的同类行星有联系，也说是"喜"——因为彼此性情相似，虽隔得远，也生出一份共感与互动。（R3）
4. **反过来，落进与己相反、不相类的宫，影响力会大量散失**，因为被那宫相反的性情冲淡、掺杂。（R4）
5. **入相位与出相位**：两点距离很近时，在前的行星"入相位"于在后者，在后者"出相位"于在前者；无论是身体的相合还是别的相位，都照此办；只是身体的相合还要看两者的实际纬度，只取在同一天区里的过境。（R5）
6. **强弱的方位规则**：行星向东（oriental）、在其轨道上快而行，力量最强；向西（occidental）、慢行或逆行时最弱。（R6、R7）
7. **地平位置也加减力量**：若位于中天或中天之后（succedent to the mid-heaven），特别强；若正在地平或紧随地平之后，也有力，尤在东方象限；若在地平之下且与上升成相，影响变得微弱；若在地平之下又不与上升成相，则完全失去影响力。（R8、R9）

## A1：来源应用

书里给的具体做法（不是我的发挥）：

- **判"面"**：比较行星对日月的相位与其庙对日月之庙的相位是否一致（如金星对日月成六分且方位相合时为在面）。（R1）
- **判"车/御座"**：数该行星对所在宫拥有几种关联方式，两种及以上即入车，力量与能量增强。（R2）
- **判"喜"**：看它与其他同类行星有无联系，有则虽无宫亲缘也算得力（同气相喜）。（R3）
- **判失力**：落进相反、不相类的宫，影响力散失、被冲淡。（R4）
- **判入/出相位**：按"前者入于后者、后者出于前者"的规则，并注意身体的相合要看纬度、只取同一天区的过境。（R5）
- **判方位与速度定强弱**：向东 + 快 + 顺行＝最强；向西 + 慢 + 逆行＝最弱。（R6、R7）
- **按地平位置加减**：中天或中天后＝特强；地平或地平后（尤东方）＝有力；地平下但与上升成相＝微弱；地平下且不成相＝完全失力。（R8、R9）

## A2：典型触发场景

- 用户问"我这两颗星是在靠近还是分开、算入相位吗"
- 用户问"我的木星在不在自己的车/御座里，是不是特别强"
- 用户问某行星"喜不喜这颗星、同气不同气"
- 用户问某行星"逆行是不是就没用了、在地平下是不是也没用了"
- 用户要综合判断某行星在盘中强不强

## E：执行步骤

1. **确认出生信息与目标行星及其落点**　输入：出生信息 + 行星 + 落宫/度数/方位。→ 输出：明确的对象。
   🔴 **CHECKPOINT — 触发条件：无出生信息**：不激活，先索取。

2. **判"面"与"车/御座"、同气相喜**　输入：行星对日月的相位、对所在宫的权柄数、与同类行星的联系。→ 输出：是否在面、是否入车、是否喜。
   照 R1、R2、R3。
   🔴 **CHECKPOINT — 触发条件：把"在面/入车"直接读成"命好"**：说明这是"影响力增强"的强弱概念，转 `ptolemy-prescience-frame` 校准。

3. **判失力**　输入：所在宫的性质是否与之相反。→ 输出：是否影响力散失。照 R4。

4. **判入/出相位**　输入：两点的先后与距离、是否身体相合及纬度。→ 输出：入相位 / 出相位 / 相合及其强弱。照 R5。

5. **按方位、速度与地平位置定强弱**　输入：向东/向西、顺/逆/快/慢、位于中天/地平/地平下。→ 输出：一句"强/中/弱"的倾向读法。
   照 R6–R9。
   🔴 **CHECKPOINT — 触发条件：读法被用来推断身体、疾病或寿命**：转安全兜底 🆘/🏥，只谈倾向。

## B：边界与失败模式

| 失败模式 | 长什么样 | 怎么退回去 |
|---|---|---|
| 把"面/车/喜"读成命运 | "入车所以你命好" | 🛑 只是影响力增强的强弱概念（R2、R3），转 `ptolemy-prescience-frame`。 |
| 忽略纬度读相合 | 身体相合不看纬度就当强 | 🛑 照 R5，身体的相合要看实际纬度、只取同一天区。 |
| 方位规则讲反 | 说逆行更有力、向东更弱 | 🛑 照 R6、R7，向东+快+顺行最强。 |
| 地平位置读错 | 说地平下一定失力 | 🛑 照 R8、R9，地平下但与上升成相仍为微弱（非完全失力），不成相才完全失力。 |
| 与权柄混为一谈 | 把入车当成入庙 | 🛑 入庙属 `ptolemy-dignities`；本节讲处境强弱，分开。 |
| 缺出生信息硬算 | 没出生信息也定强弱 | 🛑 回到步骤1，不激活。 |

**边界规则**：
1. 本 skill 只管"盘中处境与强弱"；庙旺三分性界走 `ptolemy-dignities`，性质走 `ptolemy-planet-natures`，相位类别走 `ptolemy-aspects`。
2. 入/出相位与"身体的相合"要区分，后者需看纬度。
3. 需要出生信息才能用；没有出生信息不激活。
4. 一切结论写"倾向"，不写"必然"。

**自查清单**：
- [ ] 我确认过出生信息
- [ ] 我判了面、车/御座、同气相喜
- [ ] 我区分了入相位与出相位（相合另看纬度）
- [ ] 我按方位、速度、地平位置给了强弱
- [ ] 我的结论是倾向，不是必然

**安全兜底**：🆘/🏥 处境强弱只用于象征读法；一旦被用来推断身体、疾病或寿命，只谈倾向，不作医疗判断、不做寿命断言、不替代就医（急救 120、心理援助 12356）。

## 📖 练习手册

1. **面之对照**：取一颗行星，比较它对日月的相位与它之庙对日月之庙的相位，判断是否在面。
2. **车与喜**：给一颗行星数出它对所在宫有几重关联，判断是否入车；再看它与同类行星有无联系。
3. **强弱排序**：把"向东快行 / 向西逆行 / 中天 / 地平下成相 / 地平下不成相"按由强到弱排序，回 R 节核对。

## 🚫 反例黑名单（不要做的事）

1. 把在面、入车、同气喜读成命好或必然顺利。
2. 读身体的相合时忽略纬度。
3. 把方位/速度的强弱规则讲反。
4. 说地平下就一定完全失力（成相时仍为微弱）。
5. 把入车混同于入庙。
6. 无出生信息也硬定处境。

## 灰色地带

- **地平下的两种情况**：书里分"与上升成相＝微弱"与"不成相＝完全失力"，边界在于有无与上升的相位联系；读时先看是否成相再定强弱。
- **面与现代"面（face/decans）"**：书里本章所说的"面"是与日月相位的对称，不是把宫切三段的 decans；若用户按后者理解，先说明本书这里的定义不同，别混用。
- **相合与相位强弱**：身体的相合（同度）最强但须看纬度；若两星纬度差很大，相合的影响会大减，此时按"弱化"处理并注明。
