---
name: ptolemy-planet-natures
description: 行星性质与状态读法。当用户报了出生信息、要看某颗行星"是什么脾性"——热的冷的、湿的干的、吉的凶的、阳的阴的、昼的夜的，以及它因与太阳的相对位置（晨星/昏星、月相盈亏、行星的留）当下偏向湿、热、干、冷哪一端——时使用。需要出生信息；没有出生信息不激活。
input_schema:
  required: [birth_info, planet_or_point, chart_context]
  optional: [solar_relation, phase_or_station, topic]
output_schema:
  primary: {planet_nature: string, phase_modifier: string, temperament_read: string}
  secondary: [benefic_malefic, gender_polarity, diurnal_nocturnal]
requires:
  pip: [pymeeus]
  commands: [python3]
---

# 行星的性质：热冷湿干、吉凶、阴阳、昼夜

**来源**：《Tetrabiblos（四书）》BOOK THE FIRST，CHAPTER IV THE INFLUENCES OF THE PLANETARY ORBS / CHAPTER V BENEFICS AND MALEFICS / CHAPTER VI MASCULINE AND FEMININE / CHAPTER VII DIURNAL AND NOCTURNAL / CHAPTER VIII THE INFLUENCE OF POSITION WITH REGARD TO THE SUN ｜ 证据等级：firsthand

## 触发条件

**应该触发**：
- 用户给了出生信息，问"我这颗水星到底算什么性子""土星是不是就是坏的"
- 用户想知道某颗行星当下偏湿还是偏干、偏热还是偏冷，好配合要看的主题
- 用户问某颗行星是吉星还是凶星、是阳性还是阴性、是昼星还是夜星
- 用户看到自己的月亮处在盈/亏、或某行星是晨星/昏星、或正在逆行、或处在留，问这会怎么改它的性质
- 用户要按《四书》给某行星一个"脾性"的读法，用来和它的星座/相位合参

**不应触发**：
- 用户没给出生信息 → 不激活，先索取
- 用户要的是星座本身的性质 → 走 `ptolemy-sign-natures`
- 用户要的是行星在盘中"强不强"（入庙入旺、向东南西北、快慢） → 走 `ptolemy-dignities`、`ptolemy-planet-condition`
- 用户要的是行星之间成什么相位 → 走 `ptolemy-aspects`
- 用户要的是恒星的作用 → 走 `ptolemy-fixed-stars`
- 用户问的是"我该不该信星象、是不是注定" → 走 `ptolemy-prescience-frame`

## R：原文锚点

> "his approach to the zenith of any part of the earth creates a greater degree of heat in that part and proportionately disposes its inhabitants after his own nature"（BOOK THE FIRST・CHAPTER IV「THE INFLUENCES OF THE PLANETARY ORBS」）（已据公版原文核）

> "The Moon principally generates moisture"（BOOK THE FIRST・CHAPTER IV）（已据公版原文核）

> "Saturn produces cold and dryness, for he is most remote both from the Sun's heat and from the earth's vapours."（BOOK THE FIRST・CHAPTER IV）（已据公版原文核）

> "Mars chiefly causes dryness, and is also strongly heating, by means of his own fiery nature"（BOOK THE FIRST・CHAPTER IV）（已据公版原文核）

> "Jupiter revolves in an intermediate sphere between the extreme cold of Saturn and the burning heat of Mars, and has consequently a temperate influence"（BOOK THE FIRST・CHAPTER IV）（已据公版原文核）

> "To Venus also the same temperate quality belongs, although it exists conversely"（BOOK THE FIRST・CHAPTER IV）（已据公版原文核）

> "Mercury sometimes produces dryness, and at other times moisture, and each with equal vigour."（BOOK THE FIRST・CHAPTER IV）（已据公版原文核）

> "two of the planets, on account of their temperate quality, and because heat and moisture are predominant in them, are considered by the ancients as benefic, or causers of good"（BOOK THE FIRST・CHAPTER V「BENEFICS AND MALEFICS」）（已据公版原文核）

> "But Saturn and Mars are esteemed of a contrary nature, and malefic, or causers of evil"（BOOK THE FIRST・CHAPTER V）（已据公版原文核）

> "The Moon and Venus are therefore said to be feminine, since their qualities are principally moist."（BOOK THE FIRST・CHAPTER VI「MASCULINE AND FEMININE」）（已据公版原文核）

> "the Moon and Venus are esteemed to be nocturnal; the Sun and Jupiter, diurnal; and Mercury, common"（BOOK THE FIRST・CHAPTER VII「DIURNAL AND NOCTURNAL」）（已据公版原文核）

> "The Moon, during her increase, from her first emerging to her first quarter, produces chiefly moisture; on continuing her increase from her first quarter to her full state of illumination, she causes heat; from her full state to her third quarter she causes dryness; and from her third quarter to her occultation she causes cold."（BOOK THE FIRST・CHAPTER VIII「THE INFLUENCE OF POSITION WITH REGARD TO THE SUN」）（已据公版原文核）

> "The planets, when matutine, and from their first emerging until they arrive at their first station, are chiefly productive of moisture"（BOOK THE FIRST・CHAPTER VIII）（已据公版原文核）

## I：核心解释

1. **每颗行星自带一套热冷湿干的脾性**：太阳产热与适度干燥；月亮主湿，也因借太阳之光而带一点热；土星又冷又干（离太阳与地气都最远），产冷多于产干；火星主干且强热；木星处土星之冷与火星之热之间，故温和，兼促温暖与湿润；金星同为温和，但方向相反，湿多于热；水星时而干时而湿，两样都强。（R1–R7）
2. **吉凶来自那套脾性，不是道德评判**：热与湿是滋养、繁殖的，属吉；干与冷是耗损、消散的，属凶。所以木星与金星（加月亮）为吉，土星与火星为凶；太阳与水星性质中性，与谁在一起就助谁。（R8、R9）
3. **阳阴由湿干定，也随位置变**：湿者属阴（月、金星），干者属阳（日、土、木、火），水星两可；行星又按与太阳的位置分——晨星（先于太阳升起）为阳，昏星（随太阳后落）为阴；再按与地平线的关系分四个象限。（R10）
4. **昼夜性有"反配"的巧思**：月、金星为夜，日、木星为昼，水星两可；凶星里，土星配给白天、火星配给夜晚，不是让同类相加，而是让相反的质去中和——土星之冷压白天之热，火星之干压夜晚之湿，从而趋于温和。（R11）
5. **同一颗行星的性质会随与太阳的相对位置而变**：月亮自初现到上弦主湿，上弦到满月致热，满月到下弦致干，下弦到隐没致冷；行星从初现到第一次留主湿，第一次留到夜升致热，夜升到第二次留致干，第二次留到隐没致冷。（R12、R13）
6. **所以读一颗行星，要"本性 × 当下相位"两层叠加**，并记住它们彼此混合还会生出更多变化。（R12、R13）

## A1：来源应用

书里给的具体做法（不是我的发挥）：

- **先定本性**：按 CHAPTER IV 的表给每颗行星定热/冷/湿/干（日热而略干、月湿、土冷干、火干热、木温和偏暖湿、金温和偏湿、水干湿两可）。（R1–R7）
- **再判吉凶**：以"热湿为滋养、干冷为耗损"为标准分吉星（木、金、月）与凶星（土、火），太阳与水星按同伴定吉凶。（R8、R9）
- **定阳阴与昼夜**：按湿干定基础阳阴，再按"晨星/昏星"与地平线象限调整；昼星/夜星照 CHAPTER VII 分派，注意土火是被"反配"到相反时段以中和。（R10、R11）
- **叠加太阳相对位置**：用月相（初现—上弦—满月—下弦—隐没）和行星阶段（初现—第一次留—夜升—第二次留—隐没）把性质再调向湿/热/干/冷。（R12、R13）
- **记混合**：书里提醒行星间相互混合会生出更多性质变化，所以单个本性只是主调，还要看与之同处的其他天体。

## A2：典型触发场景

- 用户问"我的土星是不是就是个坏东西"，想知道凶星是不是等于灾难
- 用户看到盘里月亮在盈/亏，问这会不会改它的含义
- 用户问某行星是晨星还是昏星，为什么有时强有时弱
- 用户想知道木星、金星"吉"在哪、和太阳水星的中性有什么不同
- 用户要按《四书》给某行星一个性子，用来和它的星座/相位合起来读

## E：执行步骤

1. **确认出生信息与要看的那颗行星**　输入：出生信息 + 目标行星（或光体/交点）。→ 输出：明确的对象与要看的主题。
   🔴 **CHECKPOINT — 触发条件：无出生信息**：不激活，先索取。

2. **定这套脾性**　输入：目标天体。→ 输出：一句热/冷/湿/干的定性（照 CHAPTER IV）。
   🔴 **CHECKPOINT — 触发条件：用户把凶星直接等同"必出事"**：说明吉凶只是脾性分类，不是道德或命运的判词，转 `ptolemy-prescience-frame` 做校准。

3. **定吉凶**　输入：脾性与同伴。→ 输出：吉/凶/中性（日、水星视同伴）。照 R8/R9。

4. **定阳阴与昼夜**　输入：湿干 + 与太阳先/后 + 地平线象限。→ 输出：阳/阴、昼/夜。照 R10/R11。
   🔴 **CHECKPOINT — 触发条件：涉及土星/火星的昼夜反配**：提醒这是"异质相配以中和"，不是随便分派。

5. **叠加当下相位**　输入：月相盈亏或行星阶段（初现/留/夜升/隐没）。→ 输出：主调偏湿/热/干/冷哪一端。照 R12/R13。
   🔴 **CHECKPOINT — 触发条件：主调涉及身体（如湿致松弛腐化、冷致耗损）**：转安全兜底 🆘/🏥，不作健康判断。

## B：边界与失败模式

| 失败模式 | 长什么样 | 怎么退回去 |
|---|---|---|
| 把凶星当道德/命运判词 | "你土星重，所以命不好" | 🛑 吉凶只是脾性分类（R8/R9），改讲性质，转 `ptolemy-prescience-frame` 校准。 |
| 只取本性，忘了当下相位 | 忽略月相/留/晨昏就给死结论 | 🛑 回到步骤5 叠加相位（R12/R13）。 |
| 缺出生信息硬算 | 没出生信息也出行星性子 | 🛑 回到步骤1，不激活。 |
| 把湿/冷直接说成病症 | "你湿气重所以要生病" | 🛑 走安全兜底，不作医疗判断。 |
| 忽略混合 | 孤立读一颗星、不看同伴 | 🛑 照 R12/R13 补上与之同处的其他天体。 |
| 昼夜反配被讲反 | 说土星"该配夜晚才顺" | 🛑 照 CHAPTER VII，土星配昼、火星配夜以中和。 |

**边界规则**：
1. 本 skill 只定"行星自身的性质与当下状态"，不判入庙入旺/强弱（走 `ptolemy-dignities`、`ptolemy-planet-condition`）。
2. 吉凶是脾性分类，不是道德或命运判决。
3. 需要出生信息才能用；没有出生信息不激活。
4. 任何涉及身体/疾病的推论，只谈倾向，不作诊断、不替代就医。

**自查清单**：
- [ ] 我确认过出生信息
- [ ] 我给出了这颗行星的热/冷/湿/干定性
- [ ] 我按热湿滋养、干冷耗损定了吉凶
- [ ] 我定了阳阴与昼夜，并留意土火的反配
- [ ] 我叠加了月相/行星阶段，没只取本性

**安全兜底**：🆘/🏥 凡涉及身体、疾病、寿命，只做提醒与陪伴，不作医疗判断、不做寿命断言、不替代就医；健康问题一律以医生为准（急救 120、心理援助 12356）。

## 📖 练习手册

1. **本性速记**：不看原文，默写七颗天体各自的热/冷/湿/干与吉凶，再回 R 节核对。
2. **相位改性质**：挑一颗你自己的行星，写下它在满月/新月、晨星/昏星时性质会怎样变。
3. **反配演练**：解释为什么土星配白天、火星配夜晚反而更"温和"。

## 🚫 反例黑名单（不要做的事）

1. 说"你是凶星所以命坏/是坏人"。
2. 不管月相与行星阶段，只凭本性下结论。
3. 把湿/冷直接翻成病症。
4. 无出生信息也硬读。
5. 把昼夜反配讲成"随便分的"。

## 灰色地带

- **水星的吉凶**：太阳与水星被书里定为"中性、随同伴定吉凶"，遇到水星时不要单独下吉凶，必须看它同处的行星。
- **金星"方向相反"的温和**：金星温和但湿多于热，与木星"暖多于湿"方向不同；读金星时别照搬木星。
- **月亮的双重身份**：月亮既主湿、属阴、为夜星，又在吉星之列；出现冲突说法时以"①本性 → ②吉凶 → ③阴阳昼夜 → ④当下相位"的顺序逐层叠读，别混为一谈。
