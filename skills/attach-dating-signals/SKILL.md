---
name: attach-dating-signals
description: 约会择偶的红灯判读。当用户单身或刚在一起，想知道"他到底值不值得我继续投入""这些算不算红灯""他是不是回避型"时使用。用书中「不在乎你感受」的 Smoking Guns 清单，把一条真实需要直接说出口做试探（有效沟通 litmus test），按对方的实时回应判断要不要继续投入。只判读对方信号与投入决策，不做焦虑型本人的情绪调节（那走 attach-anxious-style）。
input_schema:
  required: [dating_stage, the_signals, user_feelings]
  optional: [partner_history, past_patterns, specific_incidents]
output_schema:
  primary: {signal_reading: string, litmus_test: string, decision_criteria: string}
  secondary: [smoking_gun_flags, safety_notes, follow_up_questions]
---

# 约会红灯判读：他值不值得投入的观察框架

**来源**：《Attached》第 5 章「Smoking Guns That Indicate You're Dating Someone Avoidant」+ 第 4 章 Golden Rule 3/4 + 第 11 章「Effective Communication: Getting the Message Across」 | 证据等级：firsthand

## 触发条件

**应该触发**：
- "约会几次了，怎么判断他值不值得我继续投入？"
- "他嘴上说要找对的人，却总暗示那个人不是我，这算红灯吗？"
- "他从来不在乎我的感受，被我说了还照旧，这正常吗？"
- "我怕自己又选错人，怎么早点看出来？"

**不应触发**：
- 用户的核心是自己"一恋爱就焦虑、反复琢磨、忍不住查岗/发一堆消息"→ 那是焦虑型本人的自助，转 attach-anxious-style
- 想系统判读自己或对方的依恋风格（安全/焦虑/回避/混合）→ 转 attach-style-reading
- 回避倾向本人的自助（一靠近就想跑、挑刺、总惦记前任）→ 转 attach-avoidant-style
- 已长期在一起、核心是生活争吵 → 转 attach-anxious-avoidant-trap
- 要的是一句能直接说出口的话术 → 转 attach-secure-communication
- 需要处理分手创伤 → 转专业支持
- 纯"我该怎么打扮/去哪里约会" → 不相关

## R：原文锚点

> "**Disregards your emotional well-being** —and when confronted, continues to disregard it."（第 5 章，「Smoking Guns That Indicate You're Dating Someone Avoidant」）（已据原文核）

> "**Sends mixed messages** —about his/her feelings toward you or about his/her commitment to you."（第 5 章，同上清单）（已据原文核）

> "Note that it is not specific behaviors that threaten to become smoking guns but rather an emotional stance—an ambiguity about the relationship that goes hand in hand with a strong message that your emotional needs are not so important to him or her."（第 5 章，同上）（已据原文核）

> "expressing your needs and true feelings can be a useful litmus test of the other person’s capacity to meet your needs. The response, in real time, is usually much more telling than anything he or she could ever reveal of their own accord"（第 4 章，Golden Rule 4）（已据原文核）

## I：核心解释

1. **红灯是一种"情绪立场"，不是某句话**：书里说，真正危险的不是某个具体行为，而是一种"对关系含糊、同时强烈暗示你的情绪不重要"的立场。他可能偶尔说对的话，但行动讲的是另一个故事。（追 R 第 3 条）
2. **"不在乎你感受、被指出后仍不改"是最硬的红灯**：不是一次疏忽，而是持续地无视你的情绪健康。（追 R 第 1 条）
3. **混合信号要当信号看**：对感情或承诺发混合信号，本身就高度指向回避——你不必把它解释成"他只是需要时间"。（追 R 第 2 条）
4. **试探不是操控，是取样**：把自己的需要直接、不带指控地说出来，看他在实时里怎么回应；回应比任何"他平时说什么"都真实。（追 R 第 4 条）

## A1：来源应用 — 书上的做法

1. **Smoking Guns 清单**（第 5 章）：把下列任何一条当作"高信号"对待——
   - 对你的感情/承诺发混合信号（sends mixed messages）
   - 嘴上要理想关系，但暗示那个人不是你（longs for an ideal relationship—but…）
   - 拼命要找"the one"，却总能在对方或情境里挑出无法投入的毛病
   - **无视你的情绪状态**，被指出后继续无视
   - 说你是"太黏/太敏感/反应过度"，让你怀疑自己
   - 忽略你说的话（不回或换话题）
   - 用"法庭式"回应：只回事实，不接你的感受（in a court of law）
   - 你的需要怎么都说不到他心里
2. **有效沟通当试金石**（第 4 章 Golden Rule 4 + 第 11 章）：把自己的需要直接、不带指控地说出来，看回应。回避型会露出：说"你太敏感/太黏/要求太多"、不想谈、"别分析那么多"、"你到底要我怎样，我又没做错"、道歉后照旧。
3. **别用单一症状定罪**（第 4 章 Golden Rule 3）：一次"症状"不算数，要看整体模式。

## A2：典型触发场景

- 约会几次后想早点看出他值不值得投入
- 他说喜欢你，但从不明确你们是什么关系
- 你表达需要后，他说"你想太多"
- 分开就冷、约会完就消失，你拿不准是不是红灯
- 他偶尔很甜，但总体让你觉得不确定

## E：执行步骤

### 步骤1：拿到具体互动，不接泛化

**输入**：用户的描述。 **输出**：2-3 个具体情境（谁、何时、发生了什么、对方怎么反应）。

🔴 **CHECKPOINT — 触发条件：用户只说"他忽冷忽热"这类泛化词**：信息不足以判断 → 追问最近一次的具体情境。若始终是泛化 → 转 attach-style-reading，不硬判。

### 步骤2：逐条对照 Smoking Guns

**输入**：具体互动。 **输出**：命中的红灯清单（0 条也算结果）。

🔴 **CHECKPOINT — 触发条件：出现"无视你的情绪状态且被指出后仍不改"或"贬低/羞辱你"** → 这是硬红灯；若伴随恐吓、跟踪、限制自由、人身威胁 → 立即转 B 节安全出口，不再往下"设计试探"。

### 步骤3：设计一次可观察的试探

**输入**：一条真实的需要（不是指控）。 **输出**：一句可以直接说出口的话 + 判读标准。

用有效沟通五原则（小样）：wear your heart on your sleeve / focus on your needs（用 need、feel、want）/ be specific / don't blame / be assertive。示例句来自书：
> "I need to feel confident in the relationship. When you chat up the waitress, I feel like I’m on thin ice."（第 11 章）

判读：他是否想弄清你的顾虑？接不接你的感受？还是回避/贬低/只讲事实？（第 11 章 Judging the Response）

### 步骤4：按回应做决定，而不是"再等等"

**输入**：试探的回应。 **输出**：继续观察 / 给一次机会再试 / 停止投入。

有真切的在意 + 愿意找中间地带 → 可以继续。回避、防御、让你觉得自己可笑 → 严重警示。

## B：边界与失败模式

### 失败模式分支表

| 情况 | 表现 | 怎么处理 |
|---|---|---|
| 把对方当标签 | "他一次没回消息就是回避型" | 🛑 一次"症状"不算数（第 4 章 Golden Rule 3）；看整体模式。 |
| 把试探做成操控/通牒 | "我要故意冷他才行" | 🛑 试探 = 直接说出需要并观察，不是钓鱼、冷战、下最后通牒。 |
| 替对方下诊断 | "他就是不会爱人" | 🛑 只描述他与你的互动方式，不诊断这个人。 |
| 无视硬红灯继续投入 | 被贬低/被羞辱仍想"再试一次" | 🛑 明确指出红灯，鼓励止损；反复被贬低是止盈点。 |
| 暴力/控制/恐吓 | 威胁、跟踪、限制人身自由 | 🛑 立即安全出口，停止"试探"。 |

### 边界规则

1. 试探的目的是拿到信息做决定，不是逼对方改变。
2. 一次不回应可以是偶然，同一模式重复两三次才是信号。
3. 判读的产出是"要不要继续投入"，不是给对方下一个终身定论。
4. 不替任何人做"他适不适合长期"的判决，只提供观察框架与判读标准。
5. 安全优先：任何人身风险先于关系分析。

### 用户自查清单

- [ ] 我手上是具体互动，不是泛化印象
- [ ] 我逐条对照过 Smoking Guns，知道命中了几条
- [ ] 我的试探是一句真话，不是操控
- [ ] 我知道不同回应分别意味着什么
- [ ] 遇到硬红灯（被贬低/被无视情绪）时我会止损

**安全出口**：若出现威胁、恐吓、跟踪、限制自由、肢体暴力 → 先处理安全：告诉可信任的人，联系当地求助/紧急服务（中国大陆 110；美国全国反家暴热线 1-800-799-7233）。（补充：热线为常识性安全资源）

## 📖 练习手册

两个动作（书中来源）：Smoking Guns 清单逐条打勾（第 5 章）；按 Golden Rule 4 写一句符合五原则的真话，并记录对方的实时回应（第 4/11 章）。

## 🚫 反例与黑名单

1. **操控式"试探"**（装忙、故意不回、制造嫉妒）→ 书中明确反对游戏话术，禁止。
2. **用红灯清单去审判一个只约会两次的人** → 样本太小，不足以定论。
3. **把"没火花"等同于不合适** → 焦虑者常误把安心当没感觉；这类自我调节请转 attach-anxious-style（第 5 章）。
4. **在暴力关系里"设计试探"** → 停止，转安全出口。

### 灰色地带（需谨慎判断）

5. **对方是害羞而非回避** → 书中 Tina/Serge 例：害羞也可能被直接的需要打动，试一次再说。
6. **用户的"需要"本身模糊** → 先帮其澄清需要（可借 attach-secure-communication）。
7. **用户想用此 skill 证明"所有异性都不行"** → 先查是不是在泛化，别顺着走。
