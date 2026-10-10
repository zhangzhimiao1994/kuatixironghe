---
name: ptolemy-annual-atmosphere
description: 年、季、月与天象的气候推演。当用户问“今年／这季的天气收成怎么推”“按托勒密怎么读云霞晕虹”或要按星座气候本性推演一个时段的大气状况时使用。以年新月为起点，先取季度前最近的新月／满月排盘读主星，再逐月、逐日推演，最后用日月升起落下、晕、虹等征兆微调。只作倾向性描述，不作具体天气预报。
input_schema:
  required: [year_or_period, season_or_month, location]
  optional: [quarter_anchor, ruling_planets, meteors_observed]
output_schema:
  primary: {period_anchor: string, atmosphere_tendency: string, sign_nature: string}
  secondary: [monthly_procedure, meteor_omen, safety_limit]
requires:
  pip: [pymeeus]
  commands: [python3]
---

# 时令气候推演：从年新月到天象征兆

**来源**：《Tetrabiblos》BOOK THE SECOND, CH. XI（THE NEW MOON OF THE YEAR）、CH. XII（THE PARTICULAR NATURES OF THE SIGNS BY WHICH THE DIFFERENT CONSTITUTIONS OF THE ATMOSPHERE ARE PRODUCED）、CH. XIII（MODE OF CONSIDERATION FOR PARTICULAR CONSTITUTIONS OF THE ATMOSPHERE）、CH. XIV（THE SIGNIFICATION OF METEORS）（Ashmand 译本）｜ 证据等级：firsthand

## 触发条件

**应该触发**：
- 用户问“今年／这一季的天气和收成怎么推”
- 用户问“按托勒密，一个时段的冷热干湿从哪儿看起”
- 用户想按十二星座的气候本性判断某段时间的天气
- 用户问“怎么用新月／满月排一个季度的盘”
- 用户问云、霞、晕、虹、流星等天象怎么读

**不应触发**：
- 用户问的是日月食等“全体性事件”的吉凶 → 走 `ptolemy-general-event-eclipse`
- 用户问的是一片地区的常态性格 → 走 `ptolemy-region-familiarity`
- 用户只是想先定大势与个人谁优先 → 走 `ptolemy-general-particular-scope`
- 用户要的是现代意义上的气象预报或灾害预警 → 本 skill 不作具体天气预报；应指向官方气象
- 用户要某个人的本命盘 → 走个人命盘类方法

## R：原文锚点

> "In every annual revolution made by the Sun, the first new Moon of the year is to be considered as the point of the commencement of his circuit"（BOOK THE SECOND, CH. XI）（已据公版原文核）

> "the point of the vernal equinox has been consequently designated by them as the beginning of the year"（BOOK THE SECOND, CH. XI）（已据公版原文核）

> "The sign of Aries has a general tendency, arising from the presence of the Equinox, to promote thunder and hail."（BOOK THE SECOND, CH. XII）（已据公版原文核）

> "Aquarius, in its general character, is cold and watery."（BOOK THE SECOND, CH. XII）（已据公版原文核）

> "in every quarter, to observe, as above directed, the new or full Moon which may happen"（BOOK THE SECOND, CH. XIII）（已据公版原文核）

> "The second part of the consideration relates to each month"（BOOK THE SECOND, CH. XIII）（已据公版原文核）

> "there is a certain variation in the constitution of the atmosphere, which usually commences about three days before, and sometimes, also, about three days after the Moon has equated her course to the Sun."（BOOK THE SECOND, CH. XIII）（已据公版原文核）

> "for the diurnal state of the atmosphere, the Sun's rising should be remarked; for the nocturnal state, his setting"（BOOK THE SECOND, CH. XIV）（已据公版原文核）

> "the Sun, when rising or setting, if he shine clear and open, free from mists, gloom, and clouds, promises serene weather."（BOOK THE SECOND, CH. XIV）（已据公版原文核）

> "if she appear dark, or pale and thick, she threatens storms and showers."（BOOK THE SECOND, CH. XIV）（已据公版原文核）

> "the occasional appearance of the rainbow denotes, in stormy weather, the approach of serenity; in fine weather, storms."（BOOK THE SECOND, CH. XIV）（已据公版原文核）

## I：核心解释

1. **锚点在年新月**：太阳每年运行一圈，其周期的起点是“年新月”（the first new Moon of the year）。整条时令推演从这里挂起。（R1）
2. **起点定在春分**：黄道本无绝对起点，于是取春分点作年之始——从那时起白昼开始超过夜，且该季湿润，而湿是一切初生与生长的主导质。更合自然的做法，是以太阳最接近春分／夏至／秋分／冬至四点时的新月或满月来标四季之始（近白羊首→春，近巨蟹首→夏，近天秤首→秋，近摩羯首→冬）。（R2）
3. **十二星座各有气候本性**：书里逐宫给出总体倾向与分段差异。例：白羊座因春分在场，总体主雷与雹；金牛主暖中带雨、离昴星团近者主地震云风；巨蟹总体晴暖，其近鬼宿星团的前段闷热憋闷；狮子总体主憋闷之热；宝瓶总体又冷又湿。每个星座还分前／中／后段与南／北半，各有冷热干湿。（R3、R4）
4. **三层推演**：季度层——取该季前（或最接近）太阳过至分点的新月／满月，按该纬度排角、定主星，判整季性质；月层——观察太阳进入每个星座后的第一个新月／满月（若季首是新月就一路跟新月，若是满月就一路跟满月），排角、定主星、看行星的近相位与月亮黄纬指示的风；日层——看日月相刑的准确相位，以及月亮与行星的三分、六分等相位。（R5、R6）
5. **变化的窗口**：大气状况的变化，通常起于月亮“对日配速”（equated her course to the Sun）之前约三日，有时也在其后约三日。更亮的恒星在日旁晨见或夕见、或日月过角时，也会把天气拉向自己的本性。（R7）
6. **天象征兆（微调）**：白天看日升、夜里看日落；天象状态的持续时间，看日月之间的相位。太阳升起或落下时清朗无云、无雾无阴，主晴；若日轮摇晃或带火、放射或吸引红光，或伴幻日、伴长射线状的红云，主暴风（来自所示方位）；苍白或昏暗、带云或晕，主来自所示方位的风雨。月亮在合朔／望／中间四分点的前三日或后三日看：薄而清→晴；薄而红、未照面可见且摇动→来自其黄纬与赤纬方位的大风；暗而苍白厚重→风暴与雨。晕：一环明亮渐消→晴；二三环→暴风；红而破碎→暴风与狂风；暗厚→风暴与雪；黑而破碎→风与雪交加；环越多风越猛。恒星异常明亮增大→该方位起风；鬼宿星团等积云状物发暗浑浊→雨，清而持续摇动→狂风。彗星状光带→风与旱；流星一处→该处起风，各处→雷电交加；卷云状云→风暴；虹：暴风雨中→转晴，晴中→转雨。（R8–R11）
7. **主次顺序**：更普遍、先构成的原因优先，特殊的原因随后、其次要；当主导总体效果的行星也与特殊效果相合时，推演最被加强。（补充：对 CH. XIII 结尾一段的归纳）

## A1：来源应用 — 书上给的具体做法

- **用年新月挂起一年**：以太阳每年运行的起点——年新月——作为整年的锚点。（R1）
- **以二分二至定四季之始**：取太阳最近四大至分点时的（新／满）月来标春、夏、秋、冬。（R2）
- **按星座本性读底色**：逐宫查 R3、R4 式的气候倾向，并注意其前／中／后段与南／北半的差异（书里 CH. XII 十二宫逐条列出）。
- **排季度盘**：取该季前的（新／满）月，按当地纬度排角、定主星，判整季。（R5）
- **排月度盘**：跟新月或跟满月，逐宫做同样的动作，并看行星近相位与月亮黄纬指示的风向。（R6）
- **排日层**：看日月相刑的准确相位、月亮与行星的三分／六分；注意配速前后三日的窗口。（R6、R7）
- **读天象征兆**：按 R8–R11 逐条对日升日落、月相、月晕、恒星、积云、光带、流星、卷云、虹作晴雨风的判断。
- ⚠️ **（补充）** 书里这些是“征兆—倾向”的经验规则，不是精确预报。应用时保留“主／多会”的语气，并明确不作具体天气保证。

## A2：典型触发场景

1. 用户问“今年这一季的雨水和收成大概怎么推”
2. 用户问“按托勒密，一个时段的冷热干湿从哪看起”
3. 用户想用新月／满月给某个季度排盘
4. 用户看到了月晕，想知道它主晴还是主雨
5. 用户问“彩虹出来是转晴还是转雨”

## E：执行步骤

### 步骤1：锁定时段与地点

**输入**：年／季／月 + 地点。
**输出**：一个套用时令推演的时间窗与纬度。

🔴 **CHECKPOINT — 触发条件：给不出地点或时段**：先追问；给不出就不推，说明“前提不足（需大致时空信息）”。

### 步骤2：找年新月与四季之始的锚点

**输入**：年份。
**输出**：该年的年新月，以及四季各自的（新／满）月锚点。

🔴 **CHECKPOINT — 触发条件：用户把春分当成唯一绝对起点**：说明书里另给了“以最近至分点的月相标四季”的合自然做法（R2）。

### 步骤3：排季度盘，读星座本性底色

**输入**：该季的（新／满）月 + 地点纬度。
**输出**：整季的大气底色（冷热干湿）。

🔴 **CHECKPOINT — 触发条件：该季跨两个主星座、两套本性冲突**：按书里“更普遍、先构成的原因优先，特殊原因次要”的规则分主次（补充）。

### 步骤4：逐月推演

**输入**：太阳每进入一宫后的第一个（新／满）月。
**输出**：各月的冷热干湿倾向 + 风向（月亮黄纬）。

🔴 **CHECKPOINT — 触发条件：季首是新月还是满月没定，导致跟错序列**：先确认季首锚点是新是满，再统一跟到底。

### 步骤5：日层与天象微调

**输入**：日月相刑相位、月亮与行星相位、观察到的天象。
**输出**：几天尺度上的晴雨风微调。

🔴 **CHECKPOINT — 触发条件：用户要把天象征兆当成精确的降雨预报**：标明这是“征兆—倾向”，不保证具体天气；涉及灾害性天气时按 B 节指向官方气象。

## B：边界与失败模式

### 失败模式分支表

| 情况 | 表现 | 怎么处理 |
|---|---|---|
| 把征兆当预报 | 说“几号会下雨” | 🛑 只作倾向性描述，涉及灾害天气指向官方气象 |
| 缺时空锚点硬推 | 没地点没时段就给结论 | 🛑 回到步骤1 的 CHECKPOINT，先要大致时空信息 |
| 跟错月相序列 | 季首是满月却一路跟新月 | 🛑 回到步骤4，先定季首是新是满再统一跟 |
| 只用日层忽略季度层 | 拿一天的征兆推一整季 | 🛑 回到步骤3，按三层推演，先季度后月再日 |
| 写成命定论 | “今年必然大旱／必然丰收” | 🛑 保留书里的“倾向／多会”语气 |
| 引发恐慌 | 用灾害性天气渲染 | 🛑 走安全兜底：不作预言、不引起恐慌，指向官方气象 |
| 越界判食相吉凶 | 用本 skill 读日月食 | 🛑 转 `ptolemy-general-event-eclipse` |

### 边界规则

1. **本 skill 只管“大气／时令”**：判的是冷热干湿与晴雨风，不判吉凶、不判人事。
2. **必须写明前提**：至少要有地点与大致时段；无则退回追问。
3. **只作倾向**：书里给的是征兆与经验规则，不改写成精确预报。
4. **三层不可乱序**：先季度、再月、后日；普遍原因优先。
5. **与相邻 skill 分工**：层次取舍 → `ptolemy-general-particular-scope`；地区常态 → `ptolemy-region-familiarity`；日月食／彗星 → `ptolemy-general-event-eclipse`；个人命盘 → 个人命盘类方法。
6. **安全兜底**：只作倾向性描述，**不作具体天气预报、不作灾害预言、不引起恐慌**；涉及台风、暴雨、干旱等灾害性天气时，一律以官方气象部门发布为准。涉及就医、心理危机时只做提醒与陪伴，不做诊断。

### 用户自查清单

- [ ] 我能说出这次推演的地点与时段（前提齐备）
- [ ] 我用了年新月／四季锚点挂起时间
- [ ] 我按“季度→月→日”三层推，没有跳层
- [ ] 我保留的是“倾向／较可能”，没有“必然”
- [ ] 涉及灾害性天气时，我把它指向了官方气象，而非自己下结论

**勾选 4+ 项**：推演到位。**≤ 2 项**：多半是跳层或写成了预报，回到对应步骤。

## 📖 练习手册

**三层表**：给一个季度画一张表，分别填“季度主星与底色／各月倾向／关键日的天象微调”。

**星座气候卡**：抄写书里 CH. XII 的十二宫总体倾向，每宫配一句“前段／中段／后段”的差别。

**天象对照**：找一个晴朗夜晚观察月亮，记下它的亮度、颜色、有无晕，再按 R8–R11 写出你的判断与理由。

## 🚫 反例与黑名单

1. **把征兆当预报发出** → 🛑 违背“只作倾向”，且越界到天气预报。
2. **用灾害性天气制造恐慌** → 🛑 违背安全兜底。
3. **跳层推演** → 🛑 必须先季度、再月、后日。
4. **跟错月相序列** → 🛑 先确认季首是新是满。
5. **把大气推演用于判人事吉凶** → 🛑 本 skill 只判天气倾向。

### 灰色地带（需谨慎判断）

1. **年新月的“年”从哪算**：书里以春分为一年之始，但又说更合自然的是以最近至分点的月相标四始。两种口径并存时，写清你用的是哪一种（补充）。
2. **“配速前后三日”的窗口**：书里说变化“通常”起于前三日、有时在后三日，是倾向不是硬线；把它当提醒窗口，不当精确时刻。
3. **现代气象与古法结论冲突**：以官方气象为准，古法只作象征层的倾向叙事，不作替代。
