---
name: mindset-low-mood-coping
description: 当情绪低落、提不起劲时使用。帮你分清两套自动反应——固定型会反复咀嚼"这说明了我不行"，于是越躺越沉；成长型是哪怕难受也把当天该做的事做完。只做自助梳理，不替代专业评估与治疗，出现自伤念头立即求助。
input_schema:
  required: [low_mood_signal, rumination_thought, current_action]
  optional: [duration, support_person, safety_status]
output_schema:
  primary: {rumination_reframe, today_action, when_where_how}
  secondary: [support_person, safety_check, cautions]
---

# 低潮中的心态读法：把「反复咀嚼」和「哪怕难受也行动」分开

**来源**：《Mindset》第2章 Inside the Mindsets（Mindset and Depression） ｜ 证据等级：firsthand

> ⚠️ **安全前置（最高优先）**：情绪低落本身是一种真实的状态，可能属于需要专业评估与治疗的问题。本 skill 只做"心态读法"层面的自助梳理，**不替代专业评估与治疗，不做诊断**。若出现自伤、自杀念头，或低落长期持续并明显影响生活，**立即**转向专业人员与身边信任的人求助（见 B 节）。

## 触发条件

**应该触发**：
- 用户说"我最近很低落，什么都不想做，只想躺着"
- 用户反复咀嚼同一句话（"我太差了""我又搞砸了"），越嚼越沉
- 用户明明难受，却想知道"我还能不能让今天正常过下去"
- 用户想区分"我今天难受"和"我这个人不行"
- 用户问"为什么有人越难受越能撑住，我却全垮了"

**不应触发**：
- 用户出现自伤/自杀念头，或已有计划 → 立即走 B 节安全兜底，不做心态梳理
- 用户要改的是"某个具体触发情境下自动响起的那句独白" → 走 mindset-trigger-reframe
- 用户要处理的是被霸凌/被排挤后的报复或自责独白 → 走 mindset-bullying-revenge
- 用户问的是"我整体上是哪套读法"的判读 → 走 mindset-reaction-diagnosis
- 用户已在接受精神科治疗，来问用药/诊断 → 交给主治专业人员，本 skill 不介入

## R：原文锚点

> "different students handle depression in dramatically different ways. Some let everything slide. Others, though feeling wretched, hang on."（第2章 Mindset and Depression）（已据原文核）

> "they ruminated over their problems and setbacks, essentially tormenting themselves with the idea that the setbacks meant they were incompetent or unworthy"（第2章 Mindset and Depression）（已据原文核）

> "'It just kept circulating in my head: You're a dope.'"（第2章 Mindset and Depression）（已据原文核）

> "'I just couldn't let go of the thought that this made me less of a man.'"（第2章 Mindset and Depression）（已据原文核）

> "they didn't study what they needed to, they didn't hand in their assignments on time, and they didn't keep up with their chores."（第2章 Mindset and Depression）（已据原文核）

> "The more depressed people with the growth mindset felt, the more they took action to confront their problems, the more they made sure to keep up with their schoolwork, and the more they kept up with their lives. The worse they felt, the more determined they became!"（第2章 Mindset and Depression）（已据原文核）

> "When we taught people the growth mindset, it completely changed the way they reacted to their depressed mood. The worse they felt, the more motivated they became and the more they confronted the problems that faced them."（第2章 Mindset and Depression）（已据原文核）

> "failures may still hurt, but failures don't define them. And if abilities can be expanded—if change and growth are possible"（第2章 Mindset and Depression）（已据原文核）

> "every day I forced myself to get up, shower, shave, and do whatever it was I needed to do."（第2章 Mindset and Depression，学生的自述）（已据原文核）

> "One day I really hit a low point and I decided to ask for help"（第2章 Mindset and Depression，学生的自述）（已据原文核）

> "this mindset seems to rob them of their coping resources."（第2章 Mindset and Depression）（已据原文核）

> "Temperament certainly plays a role, but mindset is the most important part of the story."（第2章 Mindset and Depression）（已据原文核）

## I：核心解释

1. **同一场低潮，人分成两种走法**：书里说，不同学生应对低落的方式差别极大——有的让一切滑掉，"Others, though feeling wretched, hang on."（R1）：他们逼自己去上课、跟上功课、照顾自己，好在状态回来时生活还完整（第2章）。
2. **固定型的机制是"反刍"**：书里发现固定型的人低落水平更高，原因之一是"they ruminated over their problems and setbacks"（R2）——把挫折反复嚼成"我不行/我不配"，独白像录音带一样循环："It just kept circulating in my head: You're a dope."（R3）、"I just couldn't let go of the thought that this made me less of a man."（R4）。
3. **越低落越不动手，是反刍的后果**：书里说，固定型的人越低落越放任——没去学该学的、没交该交的、没做该做的杂事（R5）。于是"我完蛋了"的独白，慢慢变成了事实的一部分。
4. **成长型的机制是"越难受越行动"**：书里的发现是——成长型的人越低落，越会去面对问题、越会守住功课和生活："The worse they felt, the more determined they became!"（R6）。
5. **这个取向是可学的（不是天生就有的）**：书里说，当他们教人成长型读法之后，"it completely changed the way they reacted to their depressed mood."（R7）——说明这不是"性格好的人才能"的事。
6. **关键动作是"把痛和判决分开"**：书里的立场很硬也很温柔——失败仍然会痛，但失败不定义你；只要能力和成长是可能的，路就还在（R8）。所以本 skill 不是"别难过"，是"难过归难过，别把它读成'我这个人不行'"。
7. **书里那个大一学生的样本**：他低落得早上几乎起不来，却"every day I forced myself to get up, shower, shave, and do whatever it was I needed to do."（R9），而且"One day I really hit a low point and I decided to ask for help"（R10）——**撑着做该做的事**和**求助**，在书里是同时存在的两件事，不矛盾。
8. **反刍会偷走你的应对资源**：书里说，固定型读法让人总处在"被失败衡量"的危险里，"this mindset seems to rob them of their coping resources."（R11）。
9. **不是"你性格弱"**：书里承认"Temperament certainly plays a role, but mindset is the most important part of the story."（R12）——天性有份，但读法是可以动手改的那部分。

## A1：来源应用 — 书里给的做法

**区分两种低落反应（第2章 Mindset and Depression，作者的研究设定）：** 让记录者连续三周每天回答"心情、活动、怎么应对问题"（书里在二三月做的日记研究）。你在自助里可以简化成每天一行——"今天心情几分 / 今天守住了哪一件该做的事 / 今天卡在哪句独白"。这不是治疗，只是把书里的观察方式借来用。

**固定型的样本对照（第2章）：** 反刍句是"我太笨了""这让我不像个男人"（R3/R4），后果是放任（R5）。**成长型的样本对照（第2章）：** 撑住生活、必要时求助（R9/R10）。

**作者的研究结论（第2章）：**
- "The more depressed people with the growth mindset felt, the more they took action to confront their problems..."（R6）
- "When we taught people the growth mindset, it completely changed the way they reacted to their depressed mood."（R7）
- "failures may still hurt, but failures don't define them."（R8）

**把"挫折"和"人格"分开的落点（第2章）：** 书里那句总纲——用固定读法看，人总处在被失败衡量的危险中，读法"robs them of their coping resources"（R11）；换成成长读法，失败仍然会痛，但它不再给你下判决（R8）。

## A2：典型触发场景

- 连续几天提不起劲，早上起不来，计划全停
- 一件小挫折（被批评、考试没考好、消息已读不回）后，脑内循环"我太差了"
- 越低落越刷手机、越不睡、越不动，然后更自责
- 明明在难受，却还要强撑上班上课，不知道这样对不对
- 朋友说"你要振作"，你只觉得更累——因为你要的不是"振作"，是"今天怎么过下去"

## E：执行步骤

### 步骤1：先做安全与状态筛查

**输入**：用户的描述。
**输出**：一个明确判断——是否属于"现在就要求助"的范围。

先问三件事：有没有自伤/自杀念头？低落持续多久了？有没有明显影响吃饭、睡觉、工作学习？只要有自伤念头，或长期持续且功能明显受损，**这一步就跳过后面所有步骤，直接走 B 节**。

🔴 **CHECKPOINT — 触发条件：出现自伤/自杀念头，或已订具体计划**：立即停止本流程。明确这不是自助能处理的范围，**立即**向身边信任的人与专业人员求助，给出 B 节资源。不做诊断、不评估风险等级、不追问细节。

### 步骤2：把当下那句"反刍句"逐字抓出来

**输入**：用户脑内的循环句。
**输出**：一句逐字记录的反刍句（"我太差了""都是我的错""我完蛋了"）。

照 R3/R4 的样本做：先正常化——这种循环句很常见，不是你想不开。它是固定读法的自动产物，记录它，不等于它就是事实。

### 步骤3：把"难受"和"判决"拆开

**输入**：步骤2 的反刍句。
**输出**：两句——"我现在确实很难受"（保留痛）+ "但这句独白是在下判决，不是事实"（拆开判决）。

照 R2、R8 讲机制：反刍的本质是把挫折读成"我不行/我不配"（R2）；成长读法是"失败仍然会痛，但失败不定义你"（R8）。**不许把这一步做成"别难过了"**——痛被保留了，被拆掉的只是那个判决。

🔴 **CHECKPOINT — 触发条件：用户的独白内容涉及"我不该存在""结束算了"**：这是危机信号，转 B 节安全兜底，停止认知层工作。

### 步骤4：选一件"哪怕难受也能做"的当天小行动

**输入**：步骤3 的两句。
**输出**：一个具体、极小、当天能完成的行动（起床、洗漱、按点吃一餐、交上那份作业、走十分钟）。

照 R6、R9 做：行动取向不是"状态好了再动"，而是"动着把生活守住"。标准是——不需要状态好、几分钟就能开始、完成后生活里少一件悬着的事。

🔴 **CHECKPOINT — 触发条件：用户给的行动是"从明天起每天学 4 小时/彻底改变"**：打回，缩到"今天就能做完的一件"。同时**不要**把行动量当作衡量"你行不行"的新标尺。

### 步骤5：装 when/where/how，并指定一个求助对象

**输入**：步骤4 的行动。
**输出**：一句能看见画面的计划（时间 + 地点 + 第一步）+ 一个"我可以联系的人"。

照 R9/R10：撑着做该做的事**和**求助同时进行。计划要具体到能执行；求助对象要写成一个真实的名字或渠道。

🔴 **CHECKPOINT — 触发条件：用户说"我今天没做到"**：不指责，照书里成长型的立场——一次没做到不是判决，是"下次改做什么"的信息（第2章）。把行动再缩小一档，并把求助对象提前到"今天就联系"。

## B：边界与失败模式

### 失败模式分支表

| 情况 | 表现 | 怎么处理 |
|------|------|---------|
| 出现自伤/自杀念头 | "我不该存在""想消失" | 🛑 立即停止本流程，优先安全与求助，给下面资源。 |
| 把本流程当治疗 | "照这个做就能治好抑郁" | 🛑 明确：它不是治疗方案，不替代专业评估与治疗。 |
| 强行正能量 | "我不该有这些情绪" | 🛑 引 R8：书里承认失败仍然会痛。痛被保留，只拆掉"判决"。 |
| 用行动量当新标尺 | "今天还是没做完，我果然不行" | 🛑 引 R6/R9：行动是"守住生活"，不是新的考核。缩小行动，别加码。 |
| 长期低落还硬扛 | 数周提不起劲、功能明显受损仍只自助 | 🛑 引第2章"ask for help"（R10）：转专业评估，本流程让位。 |
| 反刍被当成"想通就好" | 反复咀嚼但没有任何行动或求助 | 🛑 引 R2/R5：反刍本身是会加重放任的机制。回步骤4/5，落到行动与求助。 |

### 边界规则

1. **不替代专业评估与治疗**：本流程给的是"心态读法"层的自助方法，抑郁、焦虑等是需要专业评估与治疗的状况；是否就医由专业人员判断，本 skill 不做诊断。
2. **痛是真的，先承认再谈行动**：不取消情绪，只拆掉"挫折=人格判决"这一层。
3. **"越难受越行动"不是自责手段**：书里描述的是成长型的取向，不是要求你达标；做不到不是失败。
4. **求助和撑着做，是并行不是二选一**：书里的样本同时做了这两件事（R9/R10）。
5. **安全兜底（最高优先，务必执行）**：本流程**不替代专业评估与治疗**。若出现自伤、自杀念头，或低落长期持续并明显影响吃饭、睡觉、学习工作，**立即**向身边信任的人与专业人员求助——精神/心理科门诊、心理咨询师、学校心理老师；告诉一位家人或朋友，不要独自扛。中国大陆可拨 12356 或 010-82951332；紧急拨 120/110。不做诊断、不保证疗效。

### 用户自查清单

- [ ] 我先做了安全筛查，知道自己今天在"自助"还是"要求助"的范围里
- [ ] 我能**逐字**说出今天循环的那句反刍句
- [ ] 我把"我现在很难受"和"这句是在下判决"分开写了
- [ ] 我有一件"哪怕难受也能做"的当天小行动，具体到 when/where/how
- [ ] 我写了一个真实的求助对象（名字或渠道），并准备今天就联系

**勾选 4+ 项**：可自助推进。**≤2 项，或触及自伤念头**：立即走 B 节安全兜底。

## 📖 练习手册

**每日三行**：连续七天，每天只写三行——"今天心情几分 / 今天守住了哪一件该做的事 / 今天循环的是哪句独白"。照第2章日记研究的做法，不评判，只记录。周末回看：哪句独白出现的次数最多，给它配一句"这是在下判决，不是事实"。

**小事清单**：先写好 5 件"状态再差也能做"的事（洗漱、煮个鸡蛋、走到楼下、把一封邮件发出去、给一个人发条消息）。低落时不用思考，直接从清单里挑一件。

## 🚫 反例与黑名单

1. **在危机信号里继续做心态梳理** → 先安全兜底，这是硬边界。
2. **把"成长型"讲成"你必须振作/别矫情"** → 与 R8 冲突。
3. **用行动量给用户打新分** → 违背"失败不定义你"的立场。
4. **暗示"心态好就能治好抑郁"** → 本 skill 不替代专业评估与治疗。
5. **劝用户别去看医生、只靠自助** → 严重越界。

### 灰色地带（需谨慎判断）

6. **低落有明确现实原因**（失业、丧亲、分手）→ 这类悲伤是正常的，不必急着"修好"。本流程只帮你守住生活的基本盘，同时允许悲伤存在；若长期不见变化再寻求专业支持。
7. **自助一段时间毫无松动，或反而更沉** → 这不是"你没用好"，是信号。允许暂停，建议寻求专业支持。
8. **用户在服药/治疗中** → 本 skill 只作为心态层的补充，一切以主治专业人员的判断为准，不介入用药与诊断。
9. **用户想用"行动取向"去要求别人**（"我妈抑郁就是不够努力"）→ 明确叫停：这是把书里的观察误用成了指责，且本 skill 不诊断他人。
