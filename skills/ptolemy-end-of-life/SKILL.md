---
name: ptolemy-end-of-life
description: 生命的终结（结局）话题的安全护栏。当用户给出出生信息、问"我会怎么死""我能活多久""我的结局是什么"时使用。本 skill 只把书里"死亡的种类"这一章作为文化 / 象征层的知识来理解，绝不预测个人死亡的方式、时间或原因，绝不做健康 / 寿命断言（🏥）；把可能的死亡焦虑转成陪伴与专业支持。
input_schema:
  required: [birth_data, end_of_life_question]
  optional: [emotional_state, support_context]
output_schema:
  primary: {scope_statement: string, comfort_or_reframe: string, referral: string}
  secondary: [symbolic_context, cautions]
requires:
  pip: [pymeeus]
  commands: [python3]
---

# 结局与死亡：只作象征层理解，绝不预测

**来源**：《Tetrabiblos（四书 / Quadripartite）》BOOK THE FOURTH 第 IX 章（THE KIND OF DEATH）｜ 证据等级：firsthand

## 触发条件

**应该触发**（触发后按"安全护栏"处理，**不给个人预测**）：
- 用户给了出生信息，问"我会怎么死""我的结局是什么"
- 用户问"我能活多久""我是不是短命"
- 用户想了解"书里怎么看死亡的种类"（作为文化 / 历史知识）
- 用户流露出对死亡的焦虑、想找人说一说

**不应触发**：
- 用户问的是**具体的健康 / 疾病 / 就医**问题 → 🏥 直接指向专业医疗，不走本 skill
- 用户问的是**眼前的安全危机或自伤念头** → 走紧急安全流程（见 B 节），本 skill 只做陪伴与转介
- 用户问的是财富 / 婚姻 / 子女 → 走对应的 `ptolemy-*` skill
- 用户没给出出生信息 → 先索取；但即便如此，也**不给个人死亡预测**

## R：原文锚点

> "It now remains to treat of the kind and species of death."（BOOK THE FOURTH, CHAPTER IX: THE KIND OF DEATH）（已据公版原文核）

> "death is to be expected conformable in character to the influences, whatever they may be, which preside over the said places"（同上，CHAPTER IX: THE KIND OF DEATH）（已据公版原文核）

> "if the dominion of death be vested in Saturn, he will produce death by means of lingering diseases"（同上，CHAPTER IX: THE KIND OF DEATH）（已据公版原文核）

> "a violent and remarkable death will occur when both the malefics, either in conjunction, or in quartile or opposition to each other, may be lords of the anæretic places"（同上，CHAPTER IX: THE KIND OF DEATH）（已据公版原文核）

> "death will occur in foreign lands, when it may happen that the planets controlling the anæretic places may be posited in cadent houses"（同上，CHAPTER IX: THE KIND OF DEATH）（已据公版原文核）

> "One direction, how malevolent soever, rarely kills; and, in most nativities, there is required a train of malevolent directions to concur to death"（同上，CHAPTER IX: THE KIND OF DEATH，章末注）（已据公版原文核）

## I：核心解释

1. **这一章讲什么**：书里把"死亡的种类"当作一个可以分类的题目来讨论——先由判定寿数的规则定死亡是起于东升之势还是西落之势，再据相关位置的星的性质来"分种类"。（R1、R2）
2. **书里的分类**（作为文化 / 历史知识，**不用于用户**）：土星主 → 迁延的疾病一类；木星主 → 炎症、卒中、痉挛一类；火星主 → 急热、伤创、出血一类；金星主 → 肠胃、肝、消耗一类；水星主 → 狂乱、癫痫、咳嗽一类。
3. **书里对"凶死"的判法**（同样**不用于用户**）：两凶星合 / 刑 / 冲而主"致命之宫" → 凶死；若两凶星都主致命宫，则尸体曝于外、为鸟兽所食（附条件）。
4. **书里的重要提醒**：书里自己说**单一的凶向极少致命**，"there is required a train of malevolent directions to concur to death"——即死亡是多重因素汇聚，不是单条断言；而且它把"致命的时点"与"死亡的性质"分给不同的星。（R6）
5. **本 skill 的立场**：正因为书里把它讲成一门"分类学"，这类内容在**现代只能当文化 / 历史与象征层的知识**来看；把"分类"应用到具体的活人身上，既不符合书里"多重因素汇聚"的自我限定，也可能造成严重伤害——**本 skill 一律不用于个人预测**。（此为对原文在当代语境下的边界处理。）
6. **健康 / 寿命不是本 skill 的题目**：真实的健康、疾病、寿命问题属于医学；本 skill 只做文化层的解说与情绪上的陪伴、转介。（🏥）

## A1：来源应用 — 书里给的具体做法（**仅作历史 / 文化说明，禁止用于用户个人**）

- **书里的流程**：先由判定寿数的规则确定死亡起于东升还是西落；若起于东升 / 会合之日，看会合之处；若起于"指示者的沉落"，看沉落之处；再据主该处的星之性质定"种类"；并有星的配置、致命之处的性质、星座与界主（terms）共同参与。
- **书里的分类对照**：土、木、火、金、水各主一类死因（见 I 节）。
- **书里的"凶死"条件**：两凶星合 / 刑 / 冲而主致命宫；或两凶（或其）攻击光体。
- **书里的自我限定**：单一凶向少致命，常需多重凶向汇聚；致命时点与死亡性质分属不同的星。
- **本 skill 如何使用这些**：只用来回答"书里写了些什么"这类文化问题；**不把上述任何一条套到用户的盘上**。

## A2：典型触发场景

- 用户在学占星史 / 读原典，想了解这一章的内容
- 用户对死亡好奇，随口问一句"你看我会怎么死"
- 用户正经历亲人的离世，想找人说说话
- 用户反复想到死亡，带明显的焦虑

## E：执行步骤

### 步骤1：识别请求，判断是哪一类

**输入**：用户的提问与情绪状态。
**输出**：分三类——(a) 文化 / 历史的知识提问；(b) 对个人的死亡 / 寿命预测请求；(c) 情绪上的死亡焦虑或危机。
🔴 **CHECKPOINT — 触发条件：出现自伤念头、危机或"不想活"的字句**：立即走紧急安全流程——只做陪伴与提醒，指向当地紧急资源（中国大陆可拨 110 / 120；心理援助可拨 12356），不做任何分析。

### 步骤2：对(a) 类，讲书里写了什么

**输入**：用户的求知问题。
**输出**：对第 IX 章内容的**文化 / 历史**说明（可引 R 节原文），并明确这是古代分类，不是现代事实。
🔴 **CHECKPOINT — 触发条件：用户把文化说明当成"教我怎么算自己的死法"**：停住，转步骤3。

### 步骤3：对(b) 类的个人预测请求——明确拒绝

**输入**：用户想要个人预测。
**输出**：一句清晰的**不做**：本 skill 不预测个人的死亡方式 / 时间 / 原因，也不做健康 / 寿命断言（🏥）。
要点：说明书里自己也说"单一凶向极少致命、需多重因素汇聚"，把分类套到活人身上不成立；真实的健康与寿命归医学。
🔴 **CHECKPOINT — 触发条件：用户坚持要一个"答案"或逼迫下结论**：重复边界，不松口；把话题转向可自主行动的部分（体检、就医、想做的事）。

### 步骤4：对(c) 类，做陪伴与转介

**输入**：用户的焦虑或哀伤。
**输出**：陪伴性的回应 ＋ 专业资源指向。
🔴 **CHECKPOINT — 触发条件：焦虑持续、影响生活**：建议寻求专业心理支持（中国大陆心理援助热线 12356；紧急拨 110 / 120），不替代专业帮助。

## B：边界与失败模式

| 情况 | 表现 | 怎么处理 |
|------|------|---------|
| 要求个人死亡预测 | "我会怎么死、几岁死" | 🏥 明确拒绝：不预测死亡方式 / 时间 / 原因，不做寿命断言。 |
| 要求健康 / 疾病判断 | "我是不是有心脏病" | 🏥 指向专业医疗，不做诊断。 |
| 把书里分类当事实套用 | "土星主，我会得慢性病" | 🛑 那是古代分类，不是对活人的事实；拒绝套用。 |
| 拿"要害处 / 凶死"吓人 | "盘说你凶死" | 🛑 严格禁止；退回书里的"多重因素汇聚"自我限定。 |
| 自伤 / 危机字句 | "活着没意思" | 🚨 走紧急安全流程：陪伴 + 紧急资源（中国大陆 110 / 120；心理援助 12356）。 |
| 缺出生信息 | 无出生时间 | 🛑 仍不给个人预测；只在(a) 类做文化说明。 |

**边界规则**：
1. 本 skill **不预测个人死亡、健康、寿命**（🏥），这不是"倾向"强弱的问题，而是**根本不做**。
2. 书里第 IX 章的内容只作**文化 / 历史 / 象征层**的知识，**不套用到用户**。
3. **只作倾向性推演，选择权在人**：即使在别的话题上，也不替用户做人生决定。
4. 与相邻 skill 分工：健康 / 就医走医学与专业渠道；其余主题走对应的 `ptolemy-*` skill。
5. 出现危机字句 → 优先走紧急安全流程。
6. 触发需出生信息，但**即便有**也不给个人死亡预测。

**自查清单**：
- [ ] 我没有给出任何关于用户死亡方式 / 时间 / 原因的预测
- [ ] 我没有做健康 / 寿命断言（🏥）
- [ ] 我把第 IX 章只当文化 / 历史知识来讲
- [ ] 我引用了书里"单一凶向极少致命、需多重凶向汇聚"的自我限定
- [ ] 涉及焦虑 / 危机时，我给了陪伴与专业 / 紧急资源

**安全兜底**：
- **不做健康 / 寿命断言（🏥）**：不预测死亡、疾病、寿数；真实健康问题归医学。
- **不是命定论**。书里原话："it must not be imagined that all things happen to mankind, as though every individual circumstance were ordained by divine decree and some indissoluble supernal cause; nor is it to be thought that all events are shown to proceed from one single inevitable fate, without being influenced by the interposition of any other agency."（BOOK THE FIRST, CHAPTER III: THAT PRESCIENCE IS USEFUL）
- **只作倾向性推演，选择权在人**：不替用户做任何人生决定。
- **危机转介**：出现自伤 / 危机字句时，只做陪伴与提醒，指向当地紧急与心理援助资源（中国大陆：紧急 110 / 120，心理援助 12356）。
- 触发需出生信息；有信息也不给个人死亡预测。

## 📖 练习手册

**文化 vs 事实**：把第 IX 章里的一条分类抄下来，用两种口吻各写一句——一种像"文化解说"，一种像"事实断言"。找出区别，作为自我提醒。

**谈死亡不吓人**：练习把"你会怎么死"转成"你是怎么看待死亡的"，把话题从预测转到人对生命的态度。

## 🚫 反例黑名单

1. **给个人死亡预测**（方式 / 时间 / 原因） → 🏥 根本禁止。
2. **把书里分类套到用户身上** → 🛑 古代分类不是对活人的事实。
3. **拿"凶死 / 要害处"制造恐惧** → 🛑 严格禁止。
4. **做健康 / 疾病诊断** → 🏥 越界，指向医学。
5. **无视自伤 / 危机字句继续分析** → 🚨 必须优先走紧急安全流程。

### 灰色地带

- **用户是研究者，真心问这一章写了什么**：可以讲（a）类文化内容，并保持"这是古代文本"的框架。
- **用户半开玩笑地问"我会怎么死"**：不顺着玩笑预测；轻描淡写地把边界说清，再转向他想谈的东西。
- **用户反复回到死亡话题、明显焦虑**：不再提供任何"分析"，只做陪伴与转介，必要时建议专业心理支持。
