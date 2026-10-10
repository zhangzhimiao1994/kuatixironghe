---
name: ptolemy-sign-natures
description: 星座本身的性质读法。当用户报了出生信息，要问某个星座"本性是热是冷、是湿是干、是阳是阴、是始动还是固定还是双体"，或问四季与年龄的对应、上升/中天/下降/下天四个关键点各带什么性质时使用。需要出生信息；没有出生信息不激活。
input_schema:
  required: [birth_info, sign_or_angle, topic]
  optional: [season_context, age_stage, chart_context]
output_schema:
  primary: {sign_nature: string, seasonal_quality: string, polarity_read: string}
  secondary: [angular_quality, age_analogue, caveats]
requires:
  pip: [pymeeus]
  commands: [python3]
---

# 星座的性质：四季、四轴、以及分类与阴阳

**来源**：《Tetrabiblos（四书）》BOOK THE FIRST，CHAPTER XII THE ANNUAL SEASONS / CHAPTER XIII THE INFLUENCE OF THE FOUR ANGLES / CHAPTER XIV TROPICAL, EQUINOCTIAL, FIXED, AND BICORPOREAL SIGNS / CHAPTER XV MASCULINE AND FEMININE SIGNS ｜ 证据等级：firsthand

## 触发条件

**应该触发**：
- 用户给了出生信息，问"我这个星座本性是热是冷、是湿是干"
- 用户问四季怎么对应到星座、人在不同年龄段的性质
- 用户问上升、中天、下降、下天这四个点（四轴）各带什么性质
- 用户问某星座是"始动（回至）/固定/双体（多体）"哪一类、或问某星座是阳（昼）还是阴（夜）
- 用户要按《四书》给一个星座或一个四轴点定基础性质，用来和行星/相位合参

**不应触发**：
- 用户没给出生信息 → 不激活，先索取
- 用户要的是行星本身的性质 → 走 `ptolemy-planet-natures`
- 用户要的是星座之间成什么相位 → 走 `ptolemy-aspects`
- 用户要的是行星在某星座入庙入旺 → 走 `ptolemy-dignities`
- 用户问"是不是命中注定" → 走 `ptolemy-prescience-frame`

## R：原文锚点

> "The year comprises four seasons; spring, summer, autumn, and winter; of these, the spring partakes chiefly of moisture"（BOOK THE FIRST・CHAPTER XII「THE ANNUAL SEASONS」）（已据公版原文核）

> "the summer is principally hot, owing to the Sun's nearest approach to the zenith: the autumn is principally dry, because the recent heat has absorbed the moisture: and the winter is chiefly cold"（BOOK THE FIRST・CHAPTER XII）（已据公版原文核）

> "is therefore assumed to be the sign of Aries, which commences at the vernal equinox"（BOOK THE FIRST・CHAPTER XII）（已据公版原文核）

> "the final period of old age, hastening to dissolution, is principally cold, like the winter."（BOOK THE FIRST・CHAPTER XII）（已据公版原文核）

> "the eastern point, or angle of the ascendant, is chiefly dry in its nature"（BOOK THE FIRST・CHAPTER XIII「THE INFLUENCE OF THE FOUR ANGLES」）（已据公版原文核）

> "The southern point, or angle of the mid-heaven, is the most hot"（BOOK THE FIRST・CHAPTER XIII）（已据公版原文核）

> "The western point, or occidental angle, is moist"（BOOK THE FIRST・CHAPTER XIII）（已据公版原文核）

> "The northern point, or angle of the lower heaven, is the most cold"（BOOK THE FIRST・CHAPTER XIII）（已据公版原文核）

> "The tropical signs are two: viz. the first thirty degrees after the summer solstice, which compose the sign of Cancer; and the first thirty degrees after the winter solstice, composing the sign of Capricorn."（BOOK THE FIRST・CHAPTER XIV「TROPICAL, EQUINOCTIAL, FIXED, AND BICORPOREAL SIGNS」）（已据公版原文核）

> "There are also two equinoctial signs: Aries, the first after the vernal equinox; and Libra, the first after the autumnal equinox"（BOOK THE FIRST・CHAPTER XIV）（已据公版原文核）

> "among the twelve signs, six are called masculine and diurnal, and six feminine and nocturnal."（BOOK THE FIRST・CHAPTER XV「MASCULINE AND FEMININE SIGNS」）（已据公版原文核）

> "the signs of Aries and Libra are consequently considered to be masculine and diurnal."（BOOK THE FIRST・CHAPTER XV）（已据公版原文核）

## I：核心解释

1. **星座的基础性质取自四季**：春主湿、夏主热、秋主干、冬主冷。因为整条黄道作为圆本无起点，所以把白羊（春分点）当作开端，其余季节依次排开。（R1、R2、R3）
2. **四季又是人生的四个阶段**：春似生命的初年（湿、柔嫩），夏似壮年（热、有力），秋似盛年已过、衰败将临（干），冬似奔向消散的老境（冷）。所以星座性质既可读季节，也可读年龄。（R4）
3. **上升、中天、下降、下天四个点各带风向性质**：上升（东）主于干，中天（南）最热，下降（西）主湿，下天（北）最冷；对应的风也相应为干燥、炎热、轻湿、寒冷。（R5–R8）
4. **十二宫分四类**：两个"回至宫"（tropical）＝夏至后的前 30 度（巨蟹）与冬至后的前 30 度（摩羯），因太阳行至其首点"转向"；两个"二分宫"（equinoctial）＝春分白羊与秋分天秤，此处昼夜等长；其余八个分为四个"固定宫"（紧随回至/二分宫之后，其季节性质量因而更稳固）与四个"双体宫"（紧随固定宫，性质兼具固定与回至）。（R9、R10）
5. **星座的阴阳按昼夜交替排列**：十二宫中六为阳（昼）、六为阴（夜），自白羊起一阳一阴交替；白羊与天秤为阳（昼），紧随其后者为阴（夜），余者依交替类推。（R11、R12）
6. **所以读一个星座（或四轴点），先取四季之质，再叠四轴方位、分类与阴阳，合起来才是它的完整"本性"。**

## A1：来源应用

书里给的具体做法（不是我的发挥）：

- **先定季节之质**：春湿、夏热、秋干、冬冷，按该星座属哪季取基础性质（R1、R2）。
- **代入年龄**：把同一季节对应到人生的春（初年）、夏（壮年）、秋（衰）、冬（老），需要看阶段时使用（R4）。
- **按四轴取方位性质**：上升干、中天热、下降湿、下天冷；同时联想到相应的风（R5–R8）。
- **按分类取用**：判某星座是回至、二分、固定还是双体；固定宫的性质更稳固，双体宫兼具两性（R9、R10）。
- **按阴阳交替取用**：自白羊起一阳一阴，白羊与天秤为阳（昼）；如采用"以命宫（上升）为第一阳宫"的另一种排法，书里也列出并承认这一分歧（R11、R12）。

## A2：典型触发场景

- 用户问"白羊座本性是湿的吗？为什么"
- 用户想知道上升点、中天各带什么性质，为什么人们总强调上升
- 用户问"固定星座是不是比双体星座更稳"
- 用户问"我星座属阳还是属阴，和我是男是女有关吗"
- 用户想把季节/年龄的含义并进某主题的读法

## E：执行步骤

1. **确认出生信息与目标（星座 / 四轴点 / 年龄段）**　输入：出生信息 + 问题。→ 输出：明确的对象。
   🔴 **CHECKPOINT — 触发条件：无出生信息**：不激活，先索取。

2. **取季节之质**　输入：目标星座所属季节。→ 输出：热/冷/湿/干的基础定性（R1、R2）。
   🔴 **CHECKPOINT — 触发条件：涉及"冬＝老境/消散"被读成寿命**：转安全兜底 🆘/🏥，只作象征阶段，不做寿命断言。

3. **（可选）代入四轴性质**　输入：是否在看上升/中天/下降/下天。→ 输出：对应的干/热/湿/冷（R5–R8）。
   🔴 **CHECKPOINT — 触发条件：把四轴方位与星座性质混为一谈**：分开标注——一个是方位之质，一个是季节之质，别相加成错误结论。

4. **判分类**　输入：该星座在黄道中的位置。→ 输出：回至 / 二分 / 固定 / 双体（R9、R10）。
   🔴 **CHECKPOINT — 触发条件：用户问"固定宫是不是等于一定稳定"**：说明"更稳固"指季节质量更确立，不是命运上的必然，转 `ptolemy-prescience-frame`。

5. **判阴阳（昼/夜）**　输入：星座序号与起算方式。→ 输出：阳（昼）/阴（夜）。
   照 R11、R12：默认自白羊起交替；若用户采用"上升为第一阳宫"的说法，照书里列出并注明分歧。

## B：边界与失败模式

| 失败模式 | 长什么样 | 怎么退回去 |
|---|---|---|
| 把季节质量当命运 | "你冬生所以晚年凄凉" | 🛑 只是象征阶段，转 `ptolemy-prescience-frame` 改写。 |
| 四轴之质与星座之质混算 | 把上升的"干"加成白羊的"湿" | 🛑 分开标注两类性质，别直接相加。 |
| 缺出生信息硬算 | 没出生信息也定星座 | 🛑 回到步骤1，不激活。 |
| 把固定/双体读成必然 | "固定宫就一定稳定" | 🛑 说明是季节质量更确立（R10），非命运必然。 |
| 阴阳与性别等同 | "阴宫＝女性化＝弱" | 🛑 书里阴阳是昼夜交替的配对，不是价值高低。 |
| 用冬季/老境断寿 | "属冬主老，寿不长" | 🛑 走安全兜底，不做寿命断言。 |

**边界规则**：
1. 本 skill 只管星座与四轴自身的性质，不判行星入庙入旺（走 `ptolemy-dignities`），不判相位（走 `ptolemy-aspects`）。
2. 季节→年龄只是象征对应，不预言寿命。
3. 需要出生信息才能用；没有出生信息不激活。
4. 一切结论写"倾向"，不写"必然"。

**自查清单**：
- [ ] 我确认过出生信息
- [ ] 我给出了季节之质（热/冷/湿/干）
- [ ] 需要时能区分四轴方位之质与星座季节之质
- [ ] 我判了回至/二分/固定/双体的分类
- [ ] 我判了阴阳（昼夜），并说明起算方式

**安全兜底**：🆘/🏥 "冬＝老境、趋向消散"只是象征年龄阶段，绝不当寿命或病况断言；涉及身体、寿命时只提醒与陪伴，不替代就医（急救 120、心理援助 12356）。

## 📖 练习手册

1. **四季表**：把十二宫按季节分成四组，标上各自的热/冷/湿/干。
2. **四轴记忆**：不看原文，默写上升干、中天热、下降湿、下天冷，再回 R 节核对。
3. **分类辨认**：对着黄道圆，标出哪两个是回至、哪两个是二分、哪四个固定、哪四个双体。

## 🚫 反例黑名单（不要做的事）

1. 用季节对应去断寿命或病况。
2. 把四轴方位性质与星座性质直接相加。
3. 无出生信息也硬定星座。
4. 把固定宫说成命定的稳定。
5. 把阴宫等同于弱势或女性化价值判断。

## 灰色地带

- **起算方式的两种说法**：书里主流是"自白羊起一阳一阴交替"，但也记录了一种"以命宫/上升为第一阳宫、并据此排"的做法。用户若采用后者，照书里做法列出并注明分歧，不强改。
- **双体宫的性质**：它介于固定宫与回至宫之间、兼具两者，读时不要非此即彼，按"从首度到末度渐变"处理。
- **固定宫"更稳固"的分寸**：这是季节质量在时间中更确立的意思，不是命运上的确定性，别越界成"必然"。
