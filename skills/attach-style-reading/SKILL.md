---
name: attach-style-reading
description: 依恋风格判读。当用户想知道"我/他到底是安全型、焦虑型还是回避型""为什么我一恋爱就变个人""他为什么忽冷忽热"时使用。用「亲密回避 × 关系焦虑」两条轴 + 五条观察法则，帮用户看清自己或伴侣在亲密关系里的依恋倾向（安全/焦虑/回避/混合），不给人贴死标签。
input_schema:
  required: [target_person, relationship_context, observed_behaviors]
  optional: [self_report_feelings, conflict_reactions, past_patterns]
output_schema:
  primary: {intimacy_avoidance: string, relationship_anxiety: string, likely_style: string}
  secondary: [evidence_notes, uncertainty_flags, follow_up_questions]
---

# 依恋风格判读：两条轴，看清你或他在关系里靠多近

**来源**：《Attached》(Levine & Heller) 第 3 章「Step One: What Is My Attachment Style?」+ 第 4 章「Step Two: Cracking the Code—What Is My Partner's Style?」 | 证据等级：firsthand

## 触发条件

**应该触发**：
- "我好像一谈恋爱就变得特别粘人，这不是平时的我"
- "他到底是不是喜欢我？为什么他忽冷忽热"
- "我是安全型还是焦虑型？怎么判断我和他合不合适"
- "为什么每段关系我都陷得特别深/总想逃"

**不应触发**：
- 需要精神科诊断的急性症状（抑郁发作、惊恐、自伤意念）→ 先转专业评估
- 用户只想吐槽情绪、没有想理解模式 → 先倾听
- 纯外部问题（异地、家人反对、工作）→ 不属依恋风格问题
- 用户要的是"怎么让他主动回消息"这类操控技巧 → 转 attach-secure-communication

## R：原文锚点

> "secure people feel comfortable with intimacy and are usually warm and loving; anxious people crave intimacy, are often preoccupied with their relationships, and tend to worry about their partner's ability to love them back; avoidant people equate intimacy with a loss of independence and constantly try to minimize closeness."（第 1 章，「The Secure, the Anxious, and the Avoidant」）（已据原文核）

> "Your comfort with intimacy and closeness (or the degree to which you try to avoid intimacy)." / "Your anxiety about your partner's love and attentiveness and your preoccupation with the relationship."（第 3 章，「WHAT IF I'M STILL NOT SURE?」两条维度）（已据原文核）

> "Determine whether s/he seeks intimacy and closeness." + "This is the number-one question to ask yourself about your partner. All other attachment traits and behaviors stem from this one overriding issue."（第 4 章，Golden Rule 1）（已据原文核）

> "Don't rely on one “symptom,” look for various signs."（第 4 章，Golden Rule 3）（已据原文核）

## I：核心解释

1. **依恋风格不是一个标签，是两条轴上的位置**：横轴是「亲密回避」（多不舒服于靠太近，还是多渴望靠近），纵轴是「关系焦虑」（多担心对方不够爱我、多琢磨这段关系）。两轴交叉得到四种倾向：低回避+低焦虑=安全；低回避+高焦虑=焦虑；高回避+低焦虑=回避；高回避+高焦虑=混合（书中说这是少数人群）。（追第 3 章两轴定义）
2. **回避型不是"不需要爱"**：书里的说法是 equate intimacy with a loss of independence、constantly try to minimize closeness——他要的是自主，不是孤独。实验显示回避者的依恋"机器"仍在运作，只是被压着。（追第 1 章定义 + 第 6 章）
3. **焦虑型的核心是"过度灵敏"**：他们对关系威胁的觉察特别快，但太快下结论时会误读；书里明确提醒"等久一点再反应"。（第 5 章）
4. **判断对方先问一句话**：他是否寻求亲密与靠近。想→安全或焦虑；不想→大概率回避。这是 Golden Rule 1。（第 4 章）
5. **别追单一症状**：一个行为可能是甲也可能是乙（比如不介绍你见孩子，可能是为孩子好，也可能是在拉开距离），要看整体模式。（第 4 章 Golden Rule 3）
6. **安全型的关键差别在"不报警"**：书里说安全型更少接触 danger/loss/separation 主题，情绪系统不当机也不关机。（第 7 章）

## A1：来源应用 — 书上的两套工具

1. **两维自评**（第 3 章，基于 ECR 问卷）：问自己两句话——(a) 和伴侣亲密、靠得近，我舒服吗？还是不自觉地想拉开？(b) 我是不是常担心他爱我/在意我的程度，常琢磨这段关系？书里给了四个象限的对照读法：
   - 舒服靠近 + 不焦虑 = 安全
   - 渴望靠近 + 高焦虑 = 焦虑
   - 不舒服太近 + 不焦虑 = 回避
   - 既不舒服太近 + 又很担心 = 焦虑-回避混合
2. **五条 Golden Rules**（第 4 章，用于判读对方）：
   - 1 他是否寻求亲密与靠近（最关键）。
   - 2 他对关系有多上心、对拒绝多敏感（敏感=焦虑线索）。
   - 3 别只看单一症状，看整体模式。
   - 4 看他对"有效沟通"的反应（见 attach-secure-communication）。
   - 5 注意他没说、没做的部分（书里 Rob 的女友、Jim 对 Pat 的例子）。

## A2：典型触发场景

- 约会几次后反复琢磨"他到底什么态度"
- 同一个人：当面很甜，一分开就冷
- 自己一恋爱就焦虑，单身时挺好
- 伴侣总说"你想太多""你太黏"，你开始怀疑自己
- 想弄清"我们是不是焦虑-回避组合"（→ 转 attach-anxious-avoidant-trap）

## E：执行步骤

### 步骤1：先拿到具体行为，不接泛化

**输入**：用户的描述。 **输出**：2-3 个具体情境（谁、何时、发生了什么、对方怎么反应）。

🔴 **CHECKPOINT — 触发条件：用户只说"他忽冷忽热""我很粘人"这类泛化词**：信息不足以判断 → 追问最近一次的具体情境。若仍是泛化 → 转 B 节「泛化不适合判读」，不硬判。

### 步骤2：沿两条轴打分

**输入**：步骤 1 的情境。 **输出**：两张初步清单——「亲密回避线索」与「关系焦虑线索」。

问：亲密/靠近时他是舒服还是本能地想拉开？分开或冷淡时他是否反复担心、琢磨？（第 3 章两轴）

### 步骤3：用五条 Golden Rules 交叉验证

**输入**：步骤 2 的清单。 **输出**：倾向命名（安全/焦虑/回避/混合）+ 保留的不确定。

🔴 **CHECKPOINT — 触发条件：两种风格线索都强、分不清**：不强行归类。说"有些行为焦虑和回避表面上像，要看它背后是想靠近还是想拉开"。必要时跳过命名，只描述两轴位置。（第 4 章：分不清就回到两条轴）

### 步骤4：给观察任务，而非结论

**输入**：步骤 3 的倾向。 **输出**：一段"下次可以观察什么"的清单 + 自查问题。

用 Golden Rule 4/5：注意他对你说出需要时的反应、他没说没做的部分。强调"依恋风格稳定但可塑"（第 3 章），位置会移动。

## B：边界与失败模式

### 失败模式分支表

| 情况 | 表现 | 怎么处理 |
|---|---|---|
| 把依恋类型当人格标签 | "我就是回避型，所以不适合恋爱" | 🛑 去标签。类型是两条轴上的位置，会随关系变化（第 3 章 "stable but plastic"）。 |
| 替对方下诊断式结论 | "他肯定是回避型，所以他不会改" | 🛑 只描述可观察行为与两轴位置，不说"他就是这样的人"。 |
| 用类型合理化伤害 | 用户拿"我是焦虑型"当查岗/失控的借口 | 🛑 类型解释倾向，不豁免行为责任。 |
| 性别刻板印象 | "男人都回避、女人都焦虑" | 🛑 书中明说 majority of the population—both male and female—are secure，回避≠男性（第 5 章）。 |
| 泛化到无法观察 | 只有抽象描述 | 🛑 追问具体情境，否则不判。 |
| 暴力/被控制 | 提到被打、被威胁、被限制自由 | 🛑 立即转安全出口，先谈安全与求助，不做风格分析。 |

### 边界规则

1. **不做诊断**：依恋风格不是临床诊断，书中明确 "None of the attachment styles is in itself seen as “pathological.”"（第 1 章）。
2. **两条轴 > 一个标签**：优先给两轴位置，标签是副产品。
3. **稳定但可塑**：一次判读只是快照。
4. **判读是为了选，不是为了改对方**：重点是"这个人能不能满足我的需要"，不是"怎么把他改成安全型"。
5. **暴力优先于一切**：出现人身安全风险，先走安全出口（见下）。

### 用户自查清单

- [ ] 我手上有 2-3 个具体情境，不是抽象印象
- [ ] 我能分别说出对方的「亲密回避」和「关系焦虑」线索
- [ ] 我没有只凭一个行为就下结论
- [ ] 我给的是"两条轴的位置"，不是"他就是 XX 型"
- [ ] 我知道这些会随关系变化，不是终身判决

**安全出口**：若涉及暴力、威胁、被控制、限制人身自由等 → 先停下风格分析，确认人身安全，鼓励联系可信任的人 / 当地求助渠道与紧急服务（中国大陆可拨 110；美国全国反家暴热线 1-800-799-7233）。（补充：热线信息为常识性安全资源，非书中内容）

## 📖 练习手册

本 skill 配套 3 个自测动作（书中来源）：两维自评两句提问（第 3 章）；五条 Golden Rules 清单逐条对照（第 4 章）；"他没说没做"观察日志（第 4 章 Golden Rule 5）。可逐条手写。

## 🚫 反例与黑名单

以下场景**禁止**调用此 skill，或必须降级处理：

1. **精神科急性症状**（抑郁发作、惊恐、自伤意念）→ 先转专业评估，不用风格框架。
2. **纯外部问题**（异地、家人反对、经济）→ 与依恋风格无关。
3. **要操控技巧**（"怎么让他主动""怎么让他离不开我"）→ 转 attach-secure-communication（有效沟通），拒绝游戏话术。
4. **用类型给人贴死标签**（"回避型没救"）→ 书中明说可塑，禁止宿命论。

### 灰色地带（需谨慎判断）

5. **用户在专业治疗中**，用本框架与治疗师结论冲突 → 优先治疗师。
6. **判断对象是伴侣，但用户想要的是"证明他错"** → 先区分"想理解"还是"想定罪"，后者先停。
7. **混合型自评** → 不简化成三选一，同时给焦虑与回避两条线的说明。
