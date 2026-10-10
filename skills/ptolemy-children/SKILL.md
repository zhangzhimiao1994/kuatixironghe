---
name: ptolemy-children
description: 子女与后代的星盘推演。当用户给出出生信息、问"我会有孩子吗""会有几个""跟孩子缘分怎么样"时使用。以天顶及其后续宫（吉神宫）所在之星判"给予或拒绝后代"的倾向，以单形 / 双体 / 丰产星座与吉凶星作证判数量与性质；只在象征层做倾向性推演，绝不断言能否生育，绝不做孩子健康 / 夭折的断言。
input_schema:
  required: [birth_data, children_question]
  optional: [current_family_state, partner_birth_data, medical_context]
output_schema:
  primary: {offspring_tendency: string, number_tendency: string, relationship_tendency: string}
  secondary: [givers_and_deniers, prolific_sign_note, cautions]
requires:
  pip: [pymeeus]
  commands: [python3]
---

# 子女与后代：从吉神宫与月 / 木 / 金看后代倾向

**来源**：《Tetrabiblos（四书 / Quadripartite）》BOOK THE FOURTH 第 VI 章（CHILDREN）｜ 证据等级：firsthand

## 触发条件

**应该触发**：
- 用户给了出生信息，问"我会有孩子吗""会有几个"
- 用户问"我跟孩子的缘分 / 关系怎么样"
- 用户在备孕前把星盘当作文化参照来加一层视角（且不替代医学判断）

**不应触发**：
- 用户问的是**医学上的生育能力**、要不要做试管、什么时候能怀上 → 🏥 不是本 skill，指向专业医疗
- 用户问婚姻 → 走 `ptolemy-marriage`
- 用户要一个"你肯定 / 肯定不能生"的结论 → 本 skill 明确不给
- 用户没给出出生信息 → 先索取，信息不全不推

## R：原文锚点

> "the Moon, Jupiter, and Venus are esteemed as givers of offspring; but the Sun, Mars, and Saturn are considered as denying children altogether, or as allowing but few"（BOOK THE FOURTH, CHAPTER VI: CHILDREN）（已据公版原文核）

> "Mercury, being in quality common to both parties, lends co-operation to that with which he may be configurated, and gives offspring, when oriental, but withholds, when occidental."（同上，CHAPTER VI: CHILDREN）（已据公版原文核）

> "if the planets, which grant progeny, be so posited as described, and placed singly, the gift of progeny will be single only"（同上，CHAPTER VI: CHILDREN）（已据公版原文核）

> "so likewise if they should be in prolific or seminal signs, such as Pisces, Cancer, and Scorpio, they will grant twins, or even more."（同上，CHAPTER VI: CHILDREN）（已据公版原文核）

> "a total privation of offspring is thereby indicated"（同上，CHAPTER VI: CHILDREN）（已据公版原文核）

> "the children thus granted will become eminent and illustrious"（同上，CHAPTER VI: CHILDREN）（已据公版原文核）

> "in order to enquire into particular circumstances consequent on the above, it will be necessary to assume, as an ascendant, the position of each planet which gives offspring, and to observe the separate schemes"（同上，CHAPTER VI: CHILDREN）（已据公版原文核）

## I：核心解释

1. **看哪一处**：观察落在天顶（中天）或其后续宫——书里叫"吉神宫"（place of the good dæmon）——的星，以及与这两处成相位的星；若两处都没有星也没有相位，则看与它们成冲的星。（R 前置条件）
2. **谁给、谁拒**：月、木、金是"给予后代"的；日、火、土是"拒绝或只给少数"的；水星居中——东出则助生，西落则抑生。（R1、R2）
3. **数量的倾向**：给予之星的星单一位 → 只一；落双体 / 女性星座 → 双；落丰产 / 种子星座（双鱼、巨蟹、天蝎）→ 双胞胎或更多。（R3、R4）
4. **性别的倾向**：以与太阳的相位、是否在阳性星座来分男 / 女（书里的分法）。
5. **"拒绝"的条件**：日与凶星完全占据上述位置、又落在阳性或荒瘠星座、又无吉星高踞其上 → "a total privation of offspring"；若在女性 / 丰产星座，或有吉星作证 → 仍给子女，但书里说会有病、命短（此条本 skill **坚决不用于用户**，见 B 节）。
6. **数量被"预判"的机制**：两种条件的星同时与丰产星座相关时，看哪一方在数目、影响力、东西位置、角宫、高低、先后上升上更占优，按比例偏向一方。
7. **孩子的性质**：上述星座的显主若是"给予后代"之星、在东或在本位 → 孩子显达；在西或失位 → 孩子平庸。显主与福点、上升和谐 → 孩子可亲、为父母所爱、能承继家产；不和谐 → 孩子与父母疏离、失去继承。（R6）
8. **兄弟姐妹间的关系**：给予之星的相互配置和谐 → 孩子间友爱；不合或相冲 → 相恨、相欺。

## A1：来源应用 — 书里给的具体做法

- **定观察位**：天顶（中天）及其后续宫（吉神宫），看谁在那里、谁与它们成相位，都没有则看对冲它们的星。
- **判给 / 拒**：月、木、金 → 给；日、火、土 → 拒或只给少数；水星东出助生、西落抑生。
- **判数量**：单一位 → 一；双体 / 女性星座 → 双；双鱼 / 巨蟹 / 天蝎 → 双胞胎或更多。
- **判性别**：与太阳成相位、在阳性星座 → 男；否则 → 女。
- **判孩子的性质**：显主在东 / 在本位 → 显达；在西 / 失位 → 平凡；显主与福点、上升和谐 → 可亲、被爱、承继；不和谐 → 疏离、失继承。
- **深入某一子女**：书里说，若要细究，"assume, as an ascendant, the position of each planet which gives offspring"，按立盘的法子单独看。（R7）

## A2：典型触发场景

- 备孕中，把星盘当作文化 / 象征的参照（而非医学判断）
- 已有孩子，想从这一层理解亲子缘分
- 关心"家里会不会人多 / 独生"的象征倾向
- 好奇"书里怎么看后代的显达平简"

## E：执行步骤

### 步骤1：确认出生信息，并确认请求性质

**输入**：出生日期、时间、地点；用户的疑问。
**输出**：确认这是"象征层的倾向性疑问"，而非医学生育咨询。
🔴 **CHECKPOINT — 触发条件：用户问的是生育能力 / 试管婴儿 / 何时能怀上等医学问题（🏥）**：立刻说明本 skill 不做医学判断，指向专业医疗；只把象征层作为文化参照保留。
🔴 **CHECKPOINT — 触发条件：缺出生信息**：停在索取，不给结论。

### 步骤2：读"给 / 拒"与数量的倾向

**输入**：天顶 / 吉神宫的星、与之成相位的星。
**输出**：给予后代之星（月 / 木 / 金 为主）的态势 ＋ 单 / 双 / 多的倾向。
照 R1–R4。
🔴 **CHECKPOINT — 触发条件：出现"拒绝 / 完全无后代"的字面条件**：**绝不**把"total privation"作为对用户的断言；书里给的是倾向，且受条件制约，现实还受医学与选择影响。

### 步骤3：读孩子的性质倾向

**输入**：显主的东西 / 角宫状态、与福点 / 上升的和谐度。
**输出**：孩子"显达 / 平凡""可亲 / 疏离"的定性倾向。
照 R6、R7。
🔴 **CHECKPOINT — 触发条件：用户把这句当对真实孩子的鉴定或对亲子关系的判决**：退回——这是象征层的倾向词，不是对真人的评判，也不是关系的判决。

### 步骤4：合成象征层小结

**输入**：前几步输出。
**输出**：一段"给 / 拒倾向 + 数量倾向 + 孩子性质倾向"的小结，并注明：不能替代医学判断，也不构成对是否生育的建议。
🔴 **CHECKPOINT — 触发条件：用户据此要做"要不要生 / 要不要停"的决定**：退回——**不替用户做生育决定**，选择权与专业判断在人。

## B：边界与失败模式

| 情况 | 表现 | 怎么处理 |
|------|------|---------|
| 把"无后代"当断言 | "盘说我没孩子" | 🛑 书里是倾向与条件式表述，不是判决。 |
| 拿盘替医学做生育判断 | "我该不该做试管 / 是不是怀不上" | 🏥 不做医学判断，指向专业医疗。 |
| 拿盘判真实孩子的健康 / 命运 | "孩子会不会有病 / 活不长" | 🏥 严格禁止：不做健康 / 寿命 / 夭折断言（书里确有此类字句，但**不用于用户**）。 |
| 拿"孩子显达 / 疏离"评判真人 | "盘说这孩子没出息" | 🛑 那是象征层倾向词，不是对真人的鉴定。 |
| 替用户做生育决定 | "那你别生了" | 🛑 **不替用户做生育 / 家庭决定**，选择权在人。 |
| 缺出生信息 | 无出生时间 | 🛑 停在索取。 |

**边界规则**：
1. 本 skill 只做象征层的**倾向性推演**，不是命定论。
2. **只作倾向性推演，选择权在人**：不替用户做生育 / 婚姻 / 家庭决定。
3. 数量与性质一律用书里的对照；**不使用**书里关于孩子健康 / 寿命 / 夭折的字句。
4. 与相邻 skill 分工：婚姻走 `ptolemy-marriage`；朋友与敌对关系走 `ptolemy-friends-and-enemies`。
5. 需要出生信息才能触发；缺信息不推。

**自查清单**：
- [ ] 我确认了用户给的是象征层疑问，不是医学生育咨询
- [ ] 我确认了完整出生信息
- [ ] 我用倾向性语言说"给 / 拒"与数量，没说成断言
- [ ] 我完全没有触碰孩子健康 / 寿命 / 夭折
- [ ] 我说明了不替代医学判断、不替用户做生育决定

**安全兜底**：
- **不是命定论**。书里原话："it must not be imagined that all things happen to mankind, as though every individual circumstance were ordained by divine decree and some indissoluble supernal cause; nor is it to be thought that all events are shown to proceed from one single inevitable fate, without being influenced by the interposition of any other agency."（BOOK THE FIRST, CHAPTER III: THAT PRESCIENCE IS USEFUL）
- **只作倾向性推演，选择权在人**：不替用户做生育 / 婚姻 / 家庭决定。
- **不做健康 / 寿命断言（🏥）**：本文字面确含"有疾、命短"等句，但一律**不用于用户**；涉及身体、疾病、生育时只做提醒与陪伴，指向专业医疗资源。
- 触发需出生信息；没有出生信息不推。

## 📖 练习手册

**分词练习**：把盘里得到的结论改写成"倾向句"，例如把"你会没有孩子"改成"这一层显示在生育上偏向克制，现实还取决于医学与你的选择"。练"象征 / 事实"的边界。

**不落字面**：把书里关于孩子健康与寿数的句子单独抄出来，在旁边写一句"此句不用于个人"，作为自我提醒。

## 🚫 反例黑名单

1. **把"无后代"当断言** → 🛑 倾向不是判决。
2. **替用户做生育决定** → 🛑 越界，选择权在人。
3. **拿书里"有病 / 命短 / 夭折"的句子去说真实孩子** → 🏥 严格禁止。
4. **冒充医学判断** → 🏥 生育能力属医学，指向专业医疗。
5. **自创子女判法** → 🛑 A1/E 只用书里的对照。

### 灰色地带

- **用户把星盘当备孕的唯一依据**：明确这是文化 / 象征参照，医学判断归医学。
- **用户已在医疗过程中，情绪紧张**：只做陪伴与提醒，不给象征层结论，指向专业支持。
- **书里"给予 / 拒绝"两方力量相当**：书里说看哪一方更占优来定比例，如实说明"两方胶着"，不必强行给一个数。
