---
name: mindset-bullying-revenge
description: 当被霸凌、被排挤、被当众羞辱之后，脑内反复放"我要让他付出代价"或"是不是我活该"这类独白时使用。把"欺负是评判的产物"讲清楚，帮人把评判的所有权还回去，并把报复独白改写成一个既不伤人也不伤己的下一步。只做自助梳理，不替代危机干预与专业帮助。
input_schema:
  required: [bully_situation, revenge_self_talk, felt_judgment]
  optional: [support_person, past_response, safety_status]
output_schema:
  primary: {judgment_ownership, reframed_self_talk, next_step}
  secondary: [support_person, safety_check, cautions]
---

# 被评判与被排挤之后：把评判还回去，把报复独白改写掉

**来源**：《Mindset》第6章 Relationships: Mindsets in Love (or Not)（Bullies and Victims: Revenge Revisited；含 Who Are the Bullies?、Victims and Revenge、What Can Be Done?、Grow Your Mindset） ｜ 证据等级：firsthand

> ⚠️ **安全前置**：被霸凌、被排挤属高风险场景。本 skill 只做"心态读法"层面的自助梳理，**不做心理诊断、不替代心理/精神科评估与危机干预**。若出现自伤、自杀念头，或已有报复的具体计划，先走 B 节安全兜底，优先联系专业人员与身边信任的人，本流程让位。

## 触发条件

**应该触发**：
- 用户说"被同学/同事孤立、起外号、当众嘲弄之后，我满脑子都是怎么报复"
- 用户反复想"是不是我哪里不好，才被这样对待"
- 用户被排挤后想"让他们也尝尝这个滋味"，自己也害怕这个念头
- 用户想把"被拒绝/被排挤"这件事翻过去，但困在怒气和自责里
- 用户替一个被欺负的孩子/朋友来问"这种独白怎么改写"

**不应触发**：
- 用户或身边人正处于当下的危险中、正在被伤害 → 先保障安全与求助，见 B 节
- 用户要判断的是"我用的是固定型还是成长型读法" → 走 mindset-reaction-diagnosis
- 用户要练的是"下一次遇到同样情境怎么做"的整体改写与计划 → 走 mindset-trigger-reframe
- 用户是成年人问职场排挤的应对策略，重点是取证/制度申诉 → 优先走机构内求助与法律/工会渠道，本 skill 只处理独白那一层

## R：原文锚点

> "Bullying is about judging. It's about establishing who is more worthy or important."（第6章 Who Are the Bullies?）（已据原文核）

> "they get a boost in self-esteem. It's not that bullies are low in self-esteem, but judging and demeaning others can give them a self-esteem rush."（第6章 Who Are the Bullies?）（已据原文核）

> "When people feel deeply judged by a rejection, their impulse is to feel bad about themselves and to lash out in bitterness. They have been cruelly reduced and they wish to reduce in return."（第6章 Victims and Revenge）（已据原文核）

> "'I wanted him dead' or 'I could easily have strangled her.'"（第6章 Victims and Revenge）（已据原文核）

> "it's startling how quickly average, everyday kids with a fixed mindset think about violent revenge."（第6章 Victims and Revenge）（已据原文核）

> "the students with the growth mindset were not as prone to see the bullying as a reflection of who they were. Instead, they saw it as a psychological problem of the bullies"（第6章 Victims and Revenge）（已据原文核）

> "'I would want to forgive them eventually' and 'My number one goal would be to help them become better people.'"（第6章 Victims and Revenge）（已据原文核）

> "Victims say that when they're taunted and demeaned and no one comes to their defense, they start to believe they deserve it."（第6章 Victims and Revenge）（已据原文核）

> "do you feel judged, bitter, and vengeful? Or do you feel hurt, but hopeful of forgiving, learning, and moving on?"（第6章 Grow Your Mindset）（已据原文核）

> "It's to use your mind and make things better."（第6章 Victims and Revenge）（已据原文核）

## I：核心解释

1. **欺负不是"你太差"，是对方在"打分"**：书里把欺凌的机制说得很直白——欺负是评判，是在确立"谁更值得、谁更重要"（R1）。评判是对方在做的事，不是关于你是什么人的事实。
2. **对方为什么要打分？** 书里说，欺负能给他们自尊的"快感"，也能换来地位——"judging and demeaning others can give them a self-esteem rush."（R2）。也就是说，那个打分动作服务的是对方的处境和需要，不指向你的价值。
3. **被拒绝后的固定脚本是"接过来"**：书里说，被人狠狠地评判和拒绝时，人的第一反应是"觉得自己不好"并且"带着怨气反弹"——"They have been cruelly reduced and they wish to reduce in return."（R3）。于是打分被从对方那里接到了自己身上。
4. **报复独白很普遍，不代表你邪恶**：书里研究里，受过良好教育、功能良好的成年人谈起被背叛时也说过"I wanted him dead"（R4）；而且"it's startling how quickly average, everyday kids with a fixed mindset think about violent revenge."（R5）。独白本身不稀奇，稀奇的是它接下来把你带向哪里。
5. **成长型把"评判"翻译成"对方的问题"**：书里的对照实验显示，成长型的学生"not as prone to see the bullying as a reflection of who they were"，而是把它看成欺负者自身的心理问题、一种刷地位或刷自尊的方式（R6）。
6. **成长型的落点是"行动指向"而不是"以牙还牙"**：他们的第一反应常是"去问、去谈、去让对方看见这不好笑"，并同意"我愿意最终原谅他们""我的头号目标是帮他们变成更好的人"（R7）。书里也承认"能不能真的改造顽固的欺负者，存疑"，但它明确说这起码比"开着车撞过去"是好得多的第一步（第6章）。
7. **长期被欺负会把评判内化成"我活该"**：书里警告，就算原本不是固定型，长期霸凌也会把人逼进固定型——"Victims say that when they're taunted and demeaned and no one comes to their defense, they start to believe they deserve it."（R8）。所以"我活该"这个念头是环境灌进来的，不是事实。
8. **书里给受害者的自问**：不是"我很惨吗"，而是——被拒绝之后，"do you feel judged, bitter, and vengeful? Or do you feel hurt, but hopeful of forgiving, learning, and moving on?"（R9）。允许自己痛，同时把方向留在"原谅、学习、往前走"。
9. **方向是"用心把事弄好"，不是"把对方弄坏"**：书里讲 Brooks Brown 的选择——被欺负多年却不寻仇，他给出的答案是"It's to use your mind and make things better."（R10）。
10. **求助与改变环境是正当路径**：书里说"个体孩子通常挡不住霸凌，但学校能——靠改变学校的心态"（第6章 What Can Be Done?），并举 Stan Davis 的项目——帮欺负者改变、支持受害者、让旁观者出手。所以"告诉可信的成人/机构"不是软弱，是书里认可的正解。

## A1：来源应用 — 书里给的做法

**书里学生的成长型独白样本（第6章 Victims and Revenge，可当模板）：**
- "I'd think that the reason he is bothering me is probably that he has problems at home or at school with his grades."（把原因放回对方）
- "They need to get a life—not just feel good if they make me feel bad."（认出对方的"刷自尊"）
- "I would really actually talk to them. I would ask them questions (why are they saying all of these things and why are they doing all of this to me)."（把报复换成"去问、去谈"）
- "Confront the person and discuss the issue; I would feel like trying to help them see they are not funny."

**修复的样本（第6章，Brooks Brown）：** 他被欺负多年却没有寻仇，而是主动接下了成长型读法，原话是"People do have the potential to change."；毕业前他向曾欺负自己的人递出和解——大意是"我这些年变了很多，希望你也变了；如果你没变，我可以再退回来；如果你成长了，为什么不给他一次证明的机会"（第6章，按原文转述）。

**环境层面的正解（第6章 What Can Be Done?）：** Stan Davis 的项目建立在 Dan Olweus 的工作上——帮欺负者改变、支持受害者、让旁观者敢于出手；书里说他"doesn't judge the bully as a person. No criticism is directed at traits."，而是指出行为、表扬每一个往对的方向走的一步（"I notice that you have been staying out of fights..."）。这一点同时告诉我们：**对欺负者也是"对事不对人"**。

**给受害者的自问（第6章 Grow Your Mindset）：**
> "do you feel judged, bitter, and vengeful? Or do you feel hurt, but hopeful of forgiving, learning, and moving on?"

并追问：从里面学到了什么？它教会了你想要和不想要什么？能不能原谅并祝对方好、放下怨气？（第6章）

## A2：典型触发场景

- 班里/办公室一群人起外号、孤立你，你回家反复排演"怎么让他们难堪"
- 被当众嘲笑的画面在脑内循环，伴随"是不是我本来就招人厌"
- 拉黑/被踢出群之后，反复想写一段让对方后悔的信息
- 孩子被同学排挤后说"我想打回去"，家长不知道怎么接
- 被排挤后自己也认同了那套评判——开始讨厌自己的长相/口音/背景

## E：执行步骤

### 步骤1：先确认"现在安不安全"

**输入**：用户的描述。
**输出**：一句对当下处境的确认（最近一次发生的时间、是否仍在持续、今天是否安全、身边有没有一个可信任的人）。

这一步优先于任何独白改写。**先谈安全与求助，再谈心态。**

🔴 **CHECKPOINT — 触发条件：用户提到自伤、自杀念头、或已有报复的具体计划（时间/对象/方式）**：立即停止独白改写，转 B 节安全分支。明确这需要专业人员与身边信任的人介入，本流程不做危机处理。

### 步骤2：把"评判"的所有权还给对方

**输入**：用户感到被评判的具体内容（"他们说我是废物"）。
**输出**：一句把打分动作归位的话——"这是他们在打分，打分服务的是他们的需要，不是关于我的事实。"

照 R1、R2 讲机制：欺凌是"确立谁更重要"的评判动作，能给对方自尊快感与地位。让用户自己复述一遍。**不做诊断**，不去评判对方的心理健康程度，只描述"打分动作"本身。

### 步骤3：把报复独白逐字写下来

**输入**：用户脑内循环的那句话。
**输出**：一句逐字记录的独白（如"我想让他也当众出丑"）。

照 R4、R5 先正常化：这种独白很普遍，受过良好教育的成年人也会有。**记录不等于认同**，是为了改写它。

🔴 **CHECKPOINT — 触发条件：独白里出现具体的伤害对象、方式、时间**：这不是"表达愤怒"而是"计划"，转 B 节安全分支，并明确建议尽快告诉可信任的成人/专业人员。

### 步骤4：给独白配对一句成长型改写

**输入**：步骤3 的独白。
**输出**：一句成对的改写（"我现在想 ___；换成 ___"），两句都在，不删旧句。

照 A1 的四个样本做：把原因放回对方、认出那是"刷自尊"、把动作换成"去问/去谈"。改写要诚实——不是"我没事"，而是"这是他的问题，我下一步要为自己做什么"。

### 步骤5：落一个"不伤人也不伤己"的下一步 + 找一个求助对象

**输入**：步骤4 的改写。
**输出**：一个具体、安全、指向"把事弄好"的动作（如告诉可信任的成人/老师/主管、保留记录、和一位朋友约见、加入支持性的同伴群体），以及一个"我现在就可以联系的人"。

照 R10 与第6章"学校能改变"的立场：方向是"用它把事弄好"，不是"把对方弄坏"。求助是被书里认可的正路，不是软弱。

🔴 **CHECKPOINT — 触发条件：用户说"没人会信我/说了也没用"**：不辩论，先降门槛——确认有没有任何一个人（朋友、家人、咨询师、热线）可以成为"第一个听众"。若连一个都没有，直接给 B 节的求助资源，把"找人听我说"当成第一步。

## B：边界与失败模式

### 失败模式分支表

| 情况 | 表现 | 怎么处理 |
|------|------|---------|
| 独白升级成计划 | 说出对象、时间、方式 | 🛑 立即转 B 节安全兜底，停止改写，明确联系专业人员与信任的人。 |
| 出现自伤/自杀念头 | "活着没意思""想消失" | 🛑 停止本流程，优先安全与求助，给下面资源。 |
| 把改写当"必须原谅" | "我是不是该原谅他"被逼着原谅 | 🛑 引 R9：书里的立足点是"痛了但往前"，不是强迫自己立刻原谅。允许愤怒与悲伤先存在。 |
| 把"是他的问题"用成否认 | "他心理有病，所以我不用处理" | 🛑 不做诊断。对方是否有问题不由我们判定；你能做的是求助、留证、保护自己。 |
| 为报复独白感到羞耻 | "我怎么这么恶毒" | 🛑 引 R4/R5 正常化：独白普遍，关键看它把你带向哪里。避免用羞耻再压一层。 |
| 独自硬扛 | "说了也没用，算了" | 🛑 引第6章：个体挡不住霸凌，改变环境才是正解。降门槛找"第一个听众"。 |

### 边界规则

1. **不做心理诊断**：本流程不判定用户、欺负者或任何人的心理状态；"对方是不是有病"不属于这里能回答的问题。
2. **安全高于改写**：任何时候，只要涉及自伤、自杀或报复的具体计划，本流程让位，先求助。
3. **改写只对"自己的独白"生效**：不替别人做心理工作，也不要求受害者去"修复"欺负者——书里也承认能否改造顽固的欺负者存疑。
4. **不把"成长型"当必须宽容的规训**：允许愤怒、悲伤与不原谅。书里的落点是"痛了，但往前"，不是"你不该有情绪"。
5. **安全兜底（务必执行）**：被霸凌/被排挤属高风险场景。若出现自伤念头、自杀念头，或已有报复的具体计划——**立即**向身边信任的成人/家人/朋友求助，并联系专业人员（学校心理老师、心理咨询师、精神科门诊）。未成年人请务必告诉一位可信任的成人（父母、老师、亲戚）。中国大陆可拨 12356 或 010-82951332；紧急拨 120/110。本流程不替代专业评估与治疗，不做诊断、不保证疗效。

### 用户自查清单

- [ ] 我确认了"现在安不安全"，并知道今天可以联系谁
- [ ] 我能说清"被评判"的具体内容，并把它归位为对方的打分动作
- [ ] 我把报复独白**逐字**写了下来（没美化、没删除）
- [ ] 我为它配了一句诚实的成长型改写（两句都在）
- [ ] 我有一个"不伤人也不伤己"的具体下一步 + 一个求助对象

**勾选 4+ 项**：可继续自助推进。**≤2 项，或触及自伤/报复计划**：立即走 B 节安全兜底。

## 📖 练习手册

**独白-归位两栏表**：左栏逐字写下脑内那句报复/自责独白，右栏写一句"这是他的打分动作，不是关于我的事实"。每天一条，连做七天。

**找听众清单**：写下三个"如果我告诉他/她，应该会被听见"的人或渠道（朋友、家人、老师、学校心理老师、咨询师、热线），并按"最先想打给谁"排序。允许它只是"我现在能开始"的一步。

## 🚫 反例与黑名单

1. **替用户诊断任何人**（"他就是自恋型人格"）→ 越界，本 skill 不做诊断。
2. **用成长型语言逼人原谅**（"你不原谅就是没成长"）→ 与 R9 冲突。
3. **在危机或具体报复计划中继续做独白改写** → 先安全兜底。
4. **把"是他的问题"当作不必求助的理由** → 求助与改变环境是书里明说的正路。
5. **要求受害者去改造欺负者** → 书里都承认存疑，不把责任压给受害者。

### 灰色地带（需谨慎判断）

6. **确实是"我做了什么"引来被针对**（如先有过节）→ 不取消对方的责任，也不假装自己全无参与。照第2章的做法：诚实看自己在其中的那部分，但不让它定义你的价值，然后问"下一步怎么把事弄好"。
7. **改写后毫无松动、只剩麻木** → 可能情绪过载或触及更深的东西。允许暂停，必要时建议寻求专业支持。
8. **用户是家长，来替孩子问** → 只把"怎么听孩子说、怎么陪他求助"这一层交给家长；孩子的情绪评估交给学校心理老师或专业人员。
