---
name: ptolemy-marriage
description: 婚姻与伴侣的星盘推演。当用户给出出生信息、问"我的婚姻运""什么时候结婚""会不会离婚""伴侣是什么样的"时使用。男看月、女看日，配以金星（与火 / 土 / 水的连接）判配偶性质与结合的质量；只在象征层做倾向性推演，不替用户做婚姻决定、不断言必结必离。
input_schema:
  required: [birth_data, marriage_question]
  optional: [sex, current_relationship, partner_birth_data]
output_schema:
  primary: {marriage_timing_tendency: string, partner_quality: string, union_stability_tendency: string}
  secondary: [luminary_significator, venus_condition, concord_note, cautions]
requires:
  pip: [pymeeus]
  commands: [python3]
---

# 婚姻与伴侣：从月 / 日与金星看结合倾向

**来源**：《Tetrabiblos（四书 / Quadripartite）》BOOK THE FOURTH 第 V 章（MARRIAGE）｜ 证据等级：firsthand

## 触发条件

**应该触发**：
- 用户给了出生信息，问"我什么时候能结婚 / 婚姻运怎么样"
- 用户问"我会不会离婚 / 婚姻稳不稳"
- 用户好奇"我的伴侣大概是什么样的人"
- 用户想知道"为什么我在感情里总遇到某一类人"

**不应触发**：
- 用户问"我该不该跟他 / 她结婚 / 该不该分手" → 本 skill 只推倾向，**不替用户做婚姻决定**
- 用户问的是"要不要进入一段感情 / 怎么追"这类当下选择 → 不是本 skill
- 用户问子女 → 走 `ptolemy-children`
- 用户没给出出生信息 → 先索取，信息不全不推

## R：原文锚点

> "With regard to men, it is to be observed in what manner the Moon may be disposed"（BOOK THE FOURTH, CHAPTER V: MARRIAGE）（已据公版原文核）

> "should she be in a sign of single form, and in application to only one of the planets, she will cause men to marry only once; but, if she be in a bicorporeal or multiform sign, or in application to several planets, she will cause them to be married several times"（同上，CHAPTER V: MARRIAGE）（已据公版原文核）

> "if Saturn receive the Moon’s application, the wives whom he will provide will be troublesome and morose; but, if Jupiter receive it, they will be decorous and economical; if Mars, bold and refractory; if Venus, cheerful, handsome, and agreeable; and, if Mercury, sensible, prudent, and clever."（同上，CHAPTER V: MARRIAGE）（已据公版原文核）

> "in the case of women, the Sun must be observed, instead of the Moon"（同上，CHAPTER V: MARRIAGE）（已据公版原文核）

> "Whenever both nativities, viz. that of the husband and that of the wife, may exhibit the luminaries configurated together in concord, that is to say, either in trine or in sextile to each other, the cohabitation will most usually be lasting"（同上，CHAPTER V: MARRIAGE）（已据公版原文核）

> "the relative positions of the luminaries be in signs inconjunct, or in opposition, or in quartile, the cohabitation will be speedily dissolved upon slight causes, and the total separation of the parties will ensue."（同上，CHAPTER V: MARRIAGE）（已据公版原文核）

> "if Venus be in concurrence with Mars, she will produce entire love and affection in the cohabiting parties"（同上，CHAPTER V: MARRIAGE）（已据公版原文核）

## I：核心解释

1. **男女分工看不同光体**：谈男人的婚姻看月亮的位置与状态；谈女人的婚姻看太阳，方法对称。（R1、R4）
2. **看"早 / 晚"**：月亮（男）或太阳（女）在东方的象限 → 早婚、或过盛年而娶 / 嫁年少者；在西方的象限 → 晚婚、或与年长者结合。（R1）
3. **看"一次 / 多次"**：在单形星座、且只与一颗星成应用 → 只婚一次；在双体 / 多形星座、或与多颗星成应用 → 多次婚姻。（R2）
4. **看配偶的性质**：与月（男）成应用的是哪颗星——土 → 配偶难缠郁悒；木 → 端正节俭；火 → 强硬;金 → 明快俊美可亲;水 → 明理审慎伶俐。（R3）
5. **金星与火 / 土 / 水的连接**：金与木、土、水相连 → 配偶顾家、忠于伴侣与子女；金与火相连 → 易怒、不定、莽撞。
6. **两人合看结合的质量**：把男女两盘的光体合看——成三合 / 六合且和谐（尤以互容为佳）→ 结合多能长久；若成不合意、冲或刑 → "the cohabitation will be speedily dissolved upon slight causes"，易因小事解体。（R5、R6）
7. **吉凶星作证影响过程**：和谐的结合若得吉星照临 → 在体面、安适与有利中延续；若得凶星照临 → 争吵、争夺与不幸。若本不和谐但吉星作证 → 不至于彻底决裂、还能复合；若凶星作证 → 决裂伴随轻蔑与伤害，水星独与凶星则因"public inculpation"，金星再与它们同位则因通奸、巫蛊一类事由。（R5、R6 附带）
8. **金星与火星的亲和特别点出**：两者一在对方三分的旺宫，适用于年少气盛者；金与土之亲和来自彼此宫位互在对方三分，适用于年长的人。（R7）
9. **年龄差由火星的位置细判**：火与金 / 土 / 水等权成相位 → 姻缘在同年者之间；火更东 → 配年少者；更西 → 配年长者。（附带）

## A1：来源应用 — 书里给的具体做法

- **男看月**：月在东方象限 → 早婚或娶年少者；在西方象限 → 晚婚或配偶年长；月"under the Sun’s beams"且与土星成相位 → 书里说 she then entirely denies marriage（完全没有婚姻）。
- **一次 / 多次**：月落单形星座且只与一星成应用 → 一次；落双体 / 多形或与多星成应用 → 多次。
- **配偶性质**：按与月成应用之星读（土 / 木 / 火 / 金 / 水，见 R3 的五种）。
- **女看日**：太阳在东方象限 → 早婚或嫁年少者；西方象限 → 晚婚或嫁年长者；单形星座或只与一颗东出星成相位 → 一次；双体 / 多形或与多颗东出星成相位 → 多嫁。土与日成相位 → 丈夫坚定、有利、勤勉；木 → 高尚；火 → 严厉而少情；金 → 可亲俊美；水 → 审慎精干。
- **金星与谁相连**：金 + 土 → 丈夫迟钝羞怯；金 + 木 → 善、正、谦；金 + 火 → 急躁、好色、通奸；金 + 水 → 过度贪恋年少者。
- **两人合看**：把男女两盘的日月合看，成三合 / 六合且和谐 → 结合长久（互容更佳；若男盘的月与女盘的日相应则尤为稳固）；成不合意 / 冲 / 刑 → 易散。吉星照临和谐的结合 → 体面安适；凶星照临 → 争吵不幸；本不和谐而吉星作证 → 尚可复合；凶星作证 → 决裂伴随轻蔑。
- **年龄差**：火更东 → 配年少者；更西 → 配年长者；火与诸星等权 → 同年。

## A2：典型触发场景

- 大龄未婚 / 久等不到，想知道盘里"婚缘"的倾向
- 正处在一段反复起落的感情里，想看看"结合的质量"这一层
- 已婚，想理解"我们为什么总在同一个地方吵"
- 好奇"我适合 / 会吸引什么样的伴侣"
- 离异后再看盘，想找线索

## E：执行步骤

### 步骤1：确认出生信息与性别

**输入**：出生日期、时间、地点；用户性别（男看月、女看日）。
**输出**：要观察的光体（男 → 月；女 → 日）＋ 其在哪个象限。
🔴 **CHECKPOINT — 触发条件：用户没说明性别**：先问清，再定观察的光体；若用户不愿说明，则两条线并列给出并注明假设。

### 步骤2：读"时机与次数"的倾向

**输入**：步骤1 的光体所在象限与星座形态。
**输出**：早 / 晚婚的倾向 ＋ 一次 / 多次的倾向。
照 R1、R2：东方象限 → 早；西方象限 → 晚；单形星座且一星 → 一次；双体 / 多形或多星 → 多次。
🔴 **CHECKPOINT — 触发条件：用户把"晚婚 / 多次 / 完全没有婚姻"当成判决**：守边界——书里是倾向；尤其" denies marriage "一条，只作**文化象征层的表述**，不当作对用户人生的判决。

### 步骤3：读配偶性质与金的连接

**输入**：与光体成应用之星 ＋ 金星与火 / 土 / 水的连接。
**输出**：对配偶气质的一组定性词（用书里的对照）。
照 R3 与附带条目。
🔴 **CHECKPOINT — 触发条件：用户据此去要求现实里的伴侣符合描述**：说明这是象征层的倾向词，不是对真实某人的鉴定。

### 步骤4：若有双方出生信息，合看结合质量

**输入**：双方盘的日月位置。
**输出**：结合"多能长久 / 易散"的倾向 ＋ 过程是"体面安适"还是"争执"。
照 R5、R6。
🔴 **CHECKPOINT — 触发条件：用户拿"我们星盘不合"去下要不要结婚 / 要不要分的决定**：退回——**不替用户做婚姻决定**，只作倾向性推演，选择权在人。

### 步骤5：合成倾向小结

**输入**：前几步输出。
**输出**：一段"时机倾向 + 配偶气质 + 结合质量"的象征层小结。
🔴 **CHECKPOINT — 触发条件：用户追问"我到底会不会离婚 / 会不会孤独终老"**：不给断言，退回"倾向"立场，并把话题引回可自主行动的部分。

## B：边界与失败模式

| 情况 | 表现 | 怎么处理 |
|------|------|---------|
| 把"晚婚 / 多次 / 无婚"当判决 | "盘说我没婚姻，那我认命了" | 🛑 那是倾向与文化表述，不是命定；选择与经营在人。 |
| 拿星盘替人做婚姻决定 | "我们盘不合，是不是该分" | 🛑 **不替用户做婚姻决定**，只作倾向性推演。 |
| 用"配偶描述"要求现实的人 | "盘说我该配俊美的，你怎么不……" | 🛑 那是象征层的定性词，不是对真人的鉴定。 |
| 借婚姻问子女 / 健康 | "会不会离婚、会不会影响生育" | 🛑 子女走 `ptolemy-children`；🏥 不做健康 / 寿命断言。 |
| 出生信息不全 | 无出生时间 | 🛑 停在步骤1，索取。 |
| 断章取义制造焦虑 | "金星在火这一条，我是不是婚姻不保" | 🛑 退回全书立场：倾向，不是命定。 |

**边界规则**：
1. 本 skill 只做象征层的**倾向性推演**，不是命定论，也不是对某段具体关系的判决。
2. **只作倾向性推演，选择权在人**：不替用户做婚姻 / 分手 / 生育决定。
3. 配偶性质与结合质量一律用书里的对照与合看规则；不自行添加判法。
4. 与相邻 skill 分工：子女走 `ptolemy-children`；朋友圈 / 敌对关系走 `ptolemy-friends-and-enemies`。
5. 需要出生信息才能触发；缺信息不推。

**自查清单**：
- [ ] 我按性别选对了观察的光体（男月 / 女日）
- [ ] 我确认了完整出生信息
- [ ] "时机 / 次数 / 配偶性质"都用的是倾向性语言
- [ ] 我把"无婚姻 / 多次婚姻"作为文化象征表述处理，没当判决
- [ ] 我说明了不替用户做婚姻决定、选择权在用户

**安全兜底**：
- **不是命定论**。书里原话："it must not be imagined that all things happen to mankind, as though every individual circumstance were ordained by divine decree and some indissoluble supernal cause; nor is it to be thought that all events are shown to proceed from one single inevitable fate, without being influenced by the interposition of any other agency."（BOOK THE FIRST, CHAPTER III: THAT PRESCIENCE IS USEFUL）
- **只作倾向性推演，选择权在人**：不替用户做婚姻 / 分手 / 生育等人生决定，最终选择与责任在用户自己。
- **不做健康 / 寿命断言（🏥）**：涉及身体、疾病、寿数时只做提醒与陪伴，指向专业资源。
- 若对话涉及家庭暴力、危机或自伤 → 走安全兜底：只做陪伴与提醒，指向专业援助（中国大陆可拨 12356；紧急拨 110 / 120）。
- 触发需出生信息；没有出生信息不推。

## 📖 练习手册

**两条线对读**：把你盘里的"光体状态"与"金星连接"各写一句，再和老一辈说的、书里说的对照，练"倾向词"与"判决"的区分。

**合看小实验**：若伴侣愿意给出生信息，照书里的合看规则走一遍，关注"哪种说法让你紧张"，把那句单独标出来，提醒自己它是倾向不是判决。

## 🚫 反例黑名单

1. **把"denies marriage / 多次婚姻"当判决** → 🛑 倾向与文化表述，不是命定。
2. **替用户决定要不要结婚 / 要不要分** → 🛑 越界，选择权在人。
3. **拿配偶描述去评判现实里的某个人** → 🛑 那是对盘的话，不是对人的鉴定。
4. **自创婚姻判法**（书里没写的组合） → 🛑 A1/E 只用书里的对照。
5. **借婚姻话题引向生育 / 健康断言** → 🏥 拒绝并转出。

### 灰色地带

- **用户只给了一方出生信息**：只做单人线的倾向（时机、次数、配偶性质），合看那一层留白，说明需要双方信息。
- **性别未明确 / 用户不认同按性别取用**：可以两条线并列，注明这是书里的取用方式，不是对人身份的判断。
- **用户把星盘当感情里的"裁判"**：把话题从"盘怎么说"拉回"你想怎么选"，选择权在人。
