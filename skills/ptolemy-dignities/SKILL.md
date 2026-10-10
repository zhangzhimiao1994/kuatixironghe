---
name: ptolemy-dignities
description: 行星在星座中的"权柄"读法。当用户报了出生信息，要问某颗行星落在某星座"是有力还是无力"——是否入庙、入旺、是否在其三分性里、是否落在自己的界（terms）、以及界的起点怎么算时使用。需要出生信息；没有出生信息不激活。
input_schema:
  required: [birth_info, planet, sign_and_degree]
  optional: [sect_day_night, dignity_system, topic]
output_schema:
  primary: {dignity_type: string, strength_reading: string, bound_lord: string}
  secondary: [triplicity_lord, exaltation_note, origin_rule]
requires:
  pip: [pymeeus]
  commands: [python3]
---

# 行星的权柄：庙、旺、三分性、界

**来源**：《Tetrabiblos（四书）》BOOK THE FIRST，CHAPTER XX HOUSES OF THE PLANETS / CHAPTER XXI THE TRIPLICITIES / CHAPTER XXII EXALTATIONS / CHAPTER XXIII THE DISPOSITION OF THE TERMS / CHAPTER XXIV THE TERMS ACCORDING TO PTOLEMY / CHAPTER XXV THE PLACES AND DEGREES OF EVERY PLANET ｜ 证据等级：firsthand

## 触发条件

**应该触发**：
- 用户给了出生信息，问某颗行星"落在这个星座算不算入庙/入旺"
- 用户问"它在不在自己的三分性（triplicity）里、由谁主"
- 用户问某行星在某星座的"界（terms/bounds）"归谁、界怎么切
- 用户问"埃及界还是迦勒底界""托勒密界跟它们有什么不同"
- 用户问"入庙和入旺哪个更有力""强不强怎么算"
- 用户要把权柄并入某主题的强弱判断

**不应触发**：
- 用户没给出生信息 → 不激活，先索取
- 用户要的是行星本身的热冷湿干/吉凶 → 走 `ptolemy-planet-natures`
- 用户要的是星座自身性质 → 走 `ptolemy-sign-natures`
- 用户要的是两颗星之间的关系/相位 → 走 `ptolemy-aspects`
- 用户要的是行星在盘中"强不强"的另一套（入相位/速度/方位/面与车） → 走 `ptolemy-planet-condition`
- 用户问"是不是命中注定" → 走 `ptolemy-prescience-frame`

## R：原文锚点

> "Those stars which are denominated planetary orbs have particular familiarity with certain places in the zodiac, by means of parts designated as their houses, and also by their triplicities, exaltations, terms, and so forth."（BOOK THE FIRST・CHAPTER XX「HOUSES OF THE PLANETS」）（已据公版原文核）

> "Leo for the Sun, as being masculine; and Cancer for the Moon, as being feminine."（BOOK THE FIRST・CHAPTER XX）（已据公版原文核）

> "Saturn, therefore, since he is cold and inimical to heat, moving also in a superior orbit most remote from the luminaries, occupies the signs opposite to Cancer and Leo: these are Aquarius and Capricorn"（BOOK THE FIRST・CHAPTER XX）（已据公版原文核）

> "The triplicity preserves accordance with an equilateral triangle, and the whole zodiacal orbit is defined by three circles, viz. that of the equinox, and those of the two tropics; the twelve signs are, therefore, distributed among four equilateral triangles."（BOOK THE FIRST・CHAPTER XXI「THE TRIPLICITIES」）（已据公版原文核）

> "The first triangle, or triplicity, is formed by three masculine signs, Aries, Leo, and Sagittarius"（BOOK THE FIRST・CHAPTER XXI）（已据公版原文核）

> "his exaltation, therefore, is determined to be in Aries, as, when present in that sign, he begins to lengthen the days, and the influence of his heating nature increases at the same time."（BOOK THE FIRST・CHAPTER XXII「EXALTATIONS」）（已据公版原文核）

> "Mars possesses a fiery nature, which receives its greatest intensity in Capricorn"（BOOK THE FIRST・CHAPTER XXII）（已据公版原文核）

> "There are two methods of disposing the terms of the planets, in reference to the dominion of the triplicities; one is Ægyptian, the other Chaldaic."（BOOK THE FIRST・CHAPTER XXIII「THE DISPOSITION OF THE TERMS」）（已据公版原文核）

> "Of these two distributions of the terms, that of the Ægyptians seems more to be relied on than the other"（BOOK THE FIRST・CHAPTER XXIII）（已据公版原文核）

> "In arranging the order in which the planets take their terms in each sign, their exaltations, triplicities, and houses, are taken into consideration"（BOOK THE FIRST・CHAPTER XXIV「THE TERMS ACCORDING TO PTOLEMY」）（已据公版原文核）

> "The lord of the exaltation is placed first; then the lord of the triplicity; and then the lord of the house"（BOOK THE FIRST・CHAPTER XXIV）（已据公版原文核）

> "The beginnings of the signs, and likewise those of the terms, are to be taken from the equinoctial and tropical points."（BOOK THE FIRST・CHAPTER XXV「THE PLACES AND DEGREES OF EVERY PLANET」）（已据公版原文核）

> "all these imaginary attributes cannot be herein detailed, for they receive no confirmation from nature, are not capable of being rationally demonstrated, and are, in fact, merely the offspring of scientific vanity."（BOOK THE FIRST・CHAPTER XXV）（已据公版原文核）

## I：核心解释

1. **"权柄"（familiarity）是一套行星与黄道特定位置的亲缘关系**：包括庙（houses）、三分性（triplicities）、旺（exaltations）、界（terms）等。行星落进自己的地盘就更有力。（R1）
2. **庙**：以巨蟹、狮子为最北、最暖，故分给两大光体——狮子给太阳（阳），巨蟹给月亮（阴）。由此从狮子到摩羯为太阳半圆、从水瓶到巨蟹为月亮半圆；每颗行星各占一个宫于两半圆，从而一庙与太阳成相、一庙与月亮成相。土星性冷恶热、又在最远的高轨，故占与巨蟹狮子相对的水瓶与摩羯；木星温和、在土星之下，占人马与双鱼；火星性干、在木星之下，占白羊与天蝎；金星温和、在火星之下，占金牛与天秤；水星离太阳不出一个宫、又在众星之下，占双子与处女。（R2、R3）
3. **三分性**：以等边三角形为准，黄道被两至一圈 + 二分圈三条圈界定，十二宫分成四个等边三角形（三分性）。第一个三分性由三个阳宫白羊、狮子、人马构成……（R4、R5）
4. **旺（exaltation）**：太阳入白羊进入更高的北半圆、开始加长白昼，故旺在白羊、落在天秤；土星则反置，旺在天秤、落在白羊；月亮在金牛初现增光，故旺在金牛、落在天蝎；木星在巨蟹最北、旺在巨蟹、落在摩羯；火星性热、在摩羯最南、旺在摩羯、落在巨蟹；金星性湿、在双鱼最湿、旺在双鱼、落在处女；水星性干、反于金星，旺在处女、落在双鱼。（R6、R7）
5. **界（terms）**：有两套排法，埃及式与迦勒底式；书中认为埃及式更可信，因为它见于埃及作者们的著作、且经核定的实例普遍与之一致。（R8、R9）
6. **托勒密界的排法**：依据旺、三分性、庙来排——同一宫中有两项权柄的行星排在最先；没有两项权柄的凶星排在最后；旺主第一、其次三分性主、再次庙主，按宫序排列。巨蟹与狮子（月亮与太阳的庙，光体不占界）里由凶星占首度（火星在巨蟹、土星在狮子）。度数上，吉星各 7 度、凶星各 5 度、水星 6 度；享双权者再加 1 度，从单权者（多取土星、木星）扣。（R10、R11）
7. **界的起点从二分二至点算**：界的首度、乃至各宫的首度，都要从二分（昼夜等）与二至（至点）处起算；因为诸宫的性质、影响与亲缘都源于这些点。（R12）
8. **第九章式的"更细分"（把宫再切成更小份、各归某行星）是虚妄的**：书里明确说这些"不能尽述，既无自然依据、也无法理性证明，只是学问虚荣的产物"，故不采用。（R13）

## A1：来源应用

书里给的具体做法（不是我的发挥）：

- **判庙**：照 CHAPTER XX 的分配（日-狮子、月-巨蟹、土-水瓶/摩羯、木-人马/双鱼、火-白羊/天蝎、金-金牛/天秤、水-双子/处女）定某行星是否入庙。（R2、R3）
- **判三分性**：按四个等边三角形给该宫分派主星，并区分昼主/夜主。（R4、R5）
- **判旺**：照 CHAPTER XXII 的对照（日-白羊、月-金牛、土-天秤、木-巨蟹、火-摩羯、金-双鱼、水-处女为各自的旺，反之为落）。（R6、R7）
- **判界**：采用埃及式的分配（书里更推荐），按界表查某度归于哪颗行星；若采用托勒密的排法，按"旺主→三分性主→庙主"的次序与固定度数（吉 7、凶 5、水 6，双权 +1）。（R8、R9、R10、R11）
- **界的起点一律从二分二至点算**，不可从别处起算。（R12）
- **不用更细的"度权"切分**：书里明说其为虚妄，不采用。（R13）
- **强弱的合读**：入庙、入旺、居三分性、居界，都是"有力"的来源；反之落于敌宫、落（fall）等为无力。

## A2：典型触发场景

- 用户问"我的金星在天秤，算不算入庙、有力吗"
- 用户问"入庙和入旺哪个更强？为什么"
- 用户问"我这个星座的界归谁管，怎么切的"
- 用户问"埃及界还是迦勒底界该用哪个"
- 用户看到盘里某度标着某行星，问"这是不是书上说的'度权'、该不该信"

## E：执行步骤

1. **确认出生信息与目标（行星 + 所在星座与度数）**　输入：出生信息 + 行星 + 度数。→ 输出：明确的对象。
   🔴 **CHECKPOINT — 触发条件：无出生信息**：不激活，先索取。

2. **判庙与旺**　输入：行星 + 星座 + 昼夜。→ 输出：是否入庙、是否入旺（或处于落/陷）。
   照 R2、R3、R6、R7。
   🔴 **CHECKPOINT — 触发条件：用户把"入庙/入旺"直接读成"一定顺/命好"**：说明这是"有力与否"的强弱概念，转 `ptolemy-prescience-frame` 校准。

3. **判三分性**　输入：星座 + 昼夜。→ 输出：该行星是否在其三分性、是昼主还是夜主。照 R4、R5。

4. **判界**　输入：星座 + 度数。→ 输出：该度的界主。
   照 R8、R9：默认用埃及式（书里更推荐）；如需托勒密式，按 R10、R11 的次序与度数。
   🔴 **CHECKPOINT — 触发条件：用户问该用哪套界**：说明书里推荐埃及式，并注明托勒密式的排法与原由，让用户知所依据。

5. **定界的起点并合读强弱**　输入：上面几项。→ 输出：一句"有力/无力 + 主由谁"的倾向读法。
   照 R12：起点一律从二分二至点算。
   🔴 **CHECKPOINT — 触发条件：用户要求用"度权"等更细切分**：照 R13 说明书里视其为虚妄、无自然依据，不采用。

## B：边界与失败模式

| 失败模式 | 长什么样 | 怎么退回去 |
|---|---|---|
| 把入庙入旺读成命好 | "入庙所以你命好" | 🛑 只是强弱概念（R1），转 `ptolemy-prescience-frame` 改写。 |
| 用错界的起点 | 从别处起算界 | 🛑 照 R12 一律从二分二至点起算。 |
| 采用"度权"细分 | 拿小度切分当权威 | 🛑 照 R13 说明其为虚妄，不采用。 |
| 混淆两套界 | 把埃及式和迦勒底式混着用 | 🛑 二选一，说明依据（R8、R9）。 |
| 缺出生信息硬算 | 没出生信息也定权柄 | 🛑 回到步骤1，不激活。 |
| 把旺/落当吉凶本身 | "落＝凶、旺＝吉" | 🛑 旺/落是强弱的极端，与吉凶是两套概念，分开讲。 |

**边界规则**：
1. 本 skill 只管庙、旺、三分性、界这套"权柄"；行星固有性质走 `ptolemy-planet-natures`，关系走 `ptolemy-aspects`，盘中处境强弱走 `ptolemy-planet-condition`。
2. 界的起点一律从二分二至点算。
3. 不采用书里判定为虚妄的更细度权。
4. 需要出生信息才能用；没有出生信息不激活。
5. 一切结论写"倾向"，不写"必然"。

**自查清单**：
- [ ] 我确认过出生信息
- [ ] 我判了庙与旺（含落/陷）
- [ ] 我判了三分性，并区分了昼主/夜主
- [ ] 我判了界，并说明了所用体系（埃及式为准）
- [ ] 我用的是二分二至点起的界，没有越界用度权

**安全兜底**：🆘/🏥 权柄强弱只用于象征读法，若被用来推断身体、疾病或寿命，一律只谈倾向，不作医疗判断、不做寿命断言、不替代就医（急救 120、心理援助 12356）。

## 📖 练习手册

1. **庙旺配对**：默写七颗天体各自的庙与旺，再回 R 节核对。
2. **三分性分组**：把十二宫按四个等边三角形分组，标出各组的昼主与夜主。
3. **界定序**：拿一个星座，按"旺主→三分性主→庙主"写出托勒密式的界序，并标注各界度数（吉 7、凶 5、水 6）。

## 🚫 反例黑名单（不要做的事）

1. 把入庙入旺说成命好或必然顺利。
2. 从非二分二至点起算界。
3. 使用书里判为虚妄的度权细分。
4. 把埃及式与迦勒底式混用。
5. 无出生信息也硬定权柄。
6. 把旺/落等同于吉/凶。

## 灰色地带

- **埃及界 vs 迦勒底界**：书里推荐埃及式（有作者传统与实例支持），但也承认它是"不规整"的；遇到必须用迦勒底式的场合，注明其缺点与出处存疑，不默认采用。
- **托勒密界的双权加度**：双权者 +1 度、从单权者扣除，书里说多数从土星、木星扣（因它们慢）；遇到哪颗单权星被扣的取舍，按书里"多扣土星、木星"处理并注明。
- **落的读法**：旺的对宫为落，读时与"庙的敌宫"区分开——一个是旺的极端反面，一个是庙的对立，别合并。
