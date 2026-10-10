---
name: mindset-process-praise
description: 当你正要给孩子/学生/下属/伴侣一句表扬或安慰，却怕"夸了反而害了他"时使用——把"给特质打分"的话（你真聪明/你太有天赋了/你天生就是这块料）改成关注过程、策略和下一步的话，并按对方此刻的具体状态预判这句话会被他听成什么。若对方已被贴上"笨/没天赋/脾气差"这类负面标签，走 mindset-negative-labels。
input_schema:
  required: [recipient, situation, original_line]
  optional: [recipient_state, past_pattern, desired_message]
output_schema:
  primary: {what_it_will_be_heard_as, rewritten_line, why_this_works}
  secondary: [anticipate_next_snag, alternative_lines, cautions]
---

# 过程表扬改写：别给特质打分，给他看路

**来源**：《Mindset》第3章 The Danger of Praise and Positive Labels、第7章 Parents, Teachers, and Coaches | 证据等级：firsthand

## 触发条件

**应该触发**：
- 用户问"我夸孩子聪明是不是不好？该换成什么说法？"
- 用户遇到孩子/学生考砸、比赛没拿到名次，想安慰又怕说错
- 用户发现自己张口就是"你真棒""你太聪明了"，想改

**不应触发**：
- 用户要给的是负向的话/反馈，指向人格（"你就是笨""你天生就马虎""你就是不靠谱"）→ 走 mindset-negative-labels
- 用户要判断的是"我此刻自己的读法"（走 mindset-reaction-diagnosis）
- 用户要审查自己作为家长/管理者的整体 mindset 真伪（走 mindset-false-growth-check）
- 用户要处理的是"被批评后自己内心怎么转化"（走 mindset-trigger-reframe）
- 情境涉及必须上报的伤害/虐待/安全事件 → 走机构/专业流程，本 skill 不适用

## R：原文锚点

> "Praising children's intelligence harms their motivation and it harms their performance."（第7章 Parents, Teachers, and Coaches）（已据原文核）

> "The minute they hit a snag, their confidence goes out the window and their motivation hits rock bottom. If success means they're smart, then failure means they're dumb."（第7章）（已据原文核）

> "We can praise them as much as we want for the growth-oriented process—what they accomplished through practice, study, persistence, and good strategies."（第7章）（已据原文核）

> "Praise should deal, not with the child's personality attributes, but with his efforts and achievements."（Haim Ginott，引于第7章）（已据原文核）

## I：核心解释

1. **夸特质=把能力和自我绑在一起**：一旦"成功=我聪明"，那么"没成功=我笨"就是同一枚硬币。所以书里七次实验后下了狠结论——夸智力同时伤动机和表现（R 第一条、第二条）。
2. **孩子听得懂"你其实在评价我"**：Dweck 问孩子"爸妈为什么关心你成绩？"固定型读法的孩子答"他们想确认我是个聪明的孩子"；成长型读法的孩子答"他们高兴是因为我真的用功了"。（第7章 Children Learn the Messages）同一句话，两种耳朵。
3. **改的不是"夸不夸"，是"夸哪一层"**：书上明说不用克制欣赏，只要避开**评判智力/天赋**的那一类，转而夸"practice, study, persistence, and good strategies"（R 第三条）——注意里面**包含策略**，不只是"努力"。
4. **过程 ≠ 空夸努力**：真正过程性的话要点出具体做了什么、用了什么办法、下次往哪走；只喊"你好努力"会滑成第3条之外的空话（另见 mindset-false-growth-check）。
5. **安慰也一样**：书里"保护孩子免于失败"的五种常见反应里，最危险的是"你有能力，下次一定赢"——因为它假设能力会自动带你去想去的地方（第7章 Messages About Failure）。真正有用的是"诚实地讲清楚还差什么、怎么说才能做到"。
6. **预判听感是本 skill 的关键**：同一句改写，落在低自信者、完美主义者、刚受过挫的人耳朵里，收到的意思不同。改写前先判断对方此刻会把这句话听成什么。

## A1：来源应用 — 书里给的过程话术与"失败时刻"应答

**表扬（书上给的原句范例，第7章）：**
> "That homework was so long and involved. I really admire the way you concentrated and finished it."
> "That picture has so many beautiful colors. Tell me about them."
> "The passion you put into that piano piece gives me a real feeling of joy. How do you feel when you play it?"

即：**描述你看到的具体过程 + 好奇地问他**，而不是给一个分数式的形容词。

**给考试/表演前紧张的孩子的安慰（第7章，Kristina 的故事）：** 父母原来想说"你知道你多聪明，我们知道的，这把你稳了"——书里指出这是把赌注抬得更高。真正的替代：
> "It must be a terrible thing to feel that everyone is evaluating you and you can't show what you know. We want you to know that we are not evaluating you. We care about your learning, and we know that you've learned your stuff. We're proud that you've stuck to it and kept learning."

**失败时刻的正解（第7章，Elizabeth 的体操比赛）：** 父亲没有说"你是最棒的"，而是：
> "Elizabeth, I know how you feel. It's so disappointing to have your hopes up and to perform your best but not to win. But you know, you haven't really earned it yet. There were many girls there who've been in gymnastics longer than you and who've worked a lot harder than you. If this is something you really want, then it's something you'll really have to work for."

**把特质式自责换成过程式叙述（第7章，Ginott 的 Philip）：**
> PHILIP: "Gee, I'm so clumsy."
> FATHER: "That's not what we say when nails spill."
> PHILIP: "What do you say?"
> FATHER: "You say, the nails spilled—I'll pick them up!"

## A2：典型触发场景

- 孩子拿回 102 分，家长脱口而出"你真聪明！"
- 孩子比赛没进前三，家长想说"裁判不公平/这不重要/你本来能赢"
- 下属交了一份方案，经理说"你这个人就是细心"
- 伴侣做成一件事，你夸张地说"你简直是个天才"
- 老师想给一句鼓励，张口却是"你这次真棒！"（空泛形容词）

## E：执行步骤

### 步骤1：按下原文，标出它属于哪一类

**输入**：用户原本要说/说过的那句话。
**输出**：分类——是①评判智力/天赋 ②评判人格/特质 ③评判努力但空洞 ④包含过程/策略/下一步，还是⑤"保护式"安慰（怪外部/贬低事情/保证"你有能力"）。

🔴 **CHECKPOINT — 触发条件：用户那句"表扬"其实是负向的话，且指向人格（"你就是笨""你天生就马虎"）**：本 skill 不做标签拆解。指出这已属于负向标签问题——被贴标签的人会怕"这正是我的问题、活该"——并转 mindset-negative-labels 处理，不在这里做话术美容。

### 步骤2：预判这句话会被听成什么

**输入**：类别 + 对对方状态的了解。
**输出**：一句话说清"对方大概率会把这句话听成什么"（是对他能力的裁决，还是对做法的反馈）。

按两条线判断：
- **它是把信息指向"他是谁"，还是"他做了什么/下一步做什么"？**（R 第二条：成功=聪明，则失败=笨）
- **对方此刻是在受挫、在得意、还是在紧张？** 受挫的人怕被判死刑；得意的人容易把特质夸当承认为"我就是这样"；紧张的人怕被评价。

### 步骤3：改写成过程句

**输入**：步骤2 的听感预判。
**输出**：一句新的说法，要求同时具备：**看见具体做法 + 认可策略/毅力 + 指向下一步或发出好奇**。

照 A1 的范例改，而不是造新模板。注意别只留"你好努力"，要带上**策略/方法**（R 第三条原文含 good strategies）。

### 步骤4：按情境选正确的一句话（表扬 / 前紧张 / 失败）

**输入**：步骤1 的情境类型。
**输出**：一句落地的话。

- **表扬成功时** → 用 A1 表扬范例（描述过程+发问）。
- **事前紧张时** → 用 A1 的 Kristina 版（先说中他的感受，再明确"我们不是在评价你，我们在意的是你的学习"）。
- **失败/没赢时** → 用 A1 的 Elizabeth 版（共情失望 + 诚实说出差在哪 + 给出"真要就得更投入"的路径），**不要**说"你有能力下次一定赢"（这是书里点名的"最危险"信息）。

🔴 **CHECKPOINT — 触发条件：用户问"直接说孩子还不行，会不会伤他？"**：书上明说，不能为了当场好受就放弃真话——"her father not only told her the truth, but also taught her how to learn from her failures"（第7章）。守则：**先共情，再讲真话，后给路径**，三者缺一不可。

### 步骤5：为"下一个坎"预先埋好话

**输入**：步骤4 的落地句。
**输出**：一句当对方下次又遇到同类坎时，你准备说的话。

因为过程性话术的目标是改变读法，不是修好这一次。参照 A1 的 Philip 版：把"我又搞砸了"这种特质自责，当场改成"事情发生了，我来收拾"的过程叙述。

## B：边界与失败模式

### 失败模式分支表

| 情况 | 表现 | 怎么处理 |
|------|------|---------|
| 把过程表扬做成新表演 | 家长刻意背话术，孩子感到假 | 回到"描述你真实看到的过程"，演不出来别硬演；书里作者自己也被丈夫一句"你是天才"绊住，坦承会绊住。 |
| 只夸努力、不带策略 | "你努力了就好"对着一份没有改进的作业 | 补上策略层（R 第三条含 good strategies），否则滑向 false-growth 陷阱 → 转 mindset-false-growth-check。 |
| 用过程话术规避真话 | 明明还差得远，却说"你已经很棒了" | 🛑 引用 Elizabeth 案例：要诚实说差在哪 + 给路径。保护式安慰是书里点名的坑。 |
| 对成年人过度工具化 | 把同事/伴侣当孩子"话术管理" | 成人反馈重点是"对事、对下一步"，不是教育姿态；尊重对方的自主。 |
| 涉及虐待/伤害事件 | 用户描述体罚、羞辱式管教 | 🛑 这不是话术问题。停止改写，指向儿童保护/专业咨询资源，安全优先。 |

### 边界规则

1. **不诊断、不评价用户是好家长/坏家长**：本 skill 只改一句话，不做人格判断。
2. **过程表扬不是万能**：书里同时承认能力、资源、机会存在差异——"effort isn't quite everything and that all effort is not created equal"（第2章 Questions and Answers）。别把一切结果都归因于努力。
3. **文化要落在地上**：话术要让用户用自己的语言说出，照搬英文范例会生硬。
4. **安全兜底**：若对话中出现儿童被伤害、被虐待、或有自伤风险的信息，立即停止话术工作，指向专业资源（学校心理辅导/当地儿童保护机构；紧急情况拨 120/110；心理援助热线 12356）。不做诊断。

### 用户自查清单

- [ ] 我能标出我原本那句话属于哪一类
- [ ] 我能说出**对方会把这句话听成什么**
- [ ] 我的新说法里**有对方具体做了什么**（不是形容词）
- [ ] 我的新说法里**有策略或方法**（不只是"努力"）
- [ ] 我能为**下一个坎**备好一句话

**勾选 4+ 项**：改写到位。**≤2 项**：回到对应步骤重做。

## 📖 练习手册

**换耳练习**：把书里给孩子的三个问题问自己一遍——"你今天学到了什么？""你今天犯的什么错教会了你东西？""你今天在哪件事上使劲了？"（源自第8章 Changing Your Child's Mindset 的家庭餐桌做法）。先对自己用熟，再去对别人用。

**一句话日记**：连续七天，每天记下一句你本来想给的"特质表扬"，在旁写出过程版。

## 🚫 反例与黑名单

1. **把过程表扬当操控手段**（为了让孩子更拼而表演欣赏）→ 🛑 书里的过程话术以真实观察为前提，表演会反噬。
2. **夸完之后仍传递"只有成功才值得爱"**（"我们不在意你分数"然后冷脸）→ 书里的核心是让孩子确信"我们不是在评价你"（第7章"WE LOVE YOU—ON OUR TERMS"）。
3. **用于职场绩效/免责场景**（想用话术回避真实反馈）→ 不适用；直接给具体、可执行的工作反馈（负向反馈、对事不对人见 mindset-negative-labels）。

### 灰色地带（需谨慎判断）

4. **对方主动求一个"你真好"的确认** → 书里承认有些时刻人确实需要安慰："Tell me I'm not a bad person..."（第6章 Friendship）。此时一句真诚的确认不是罪，随后再补过程视角即可，别机械拒绝安慰。
5. **天赋型孩子明显超前** → 更要给过程反馈。书里 Adam Guettel 的悲剧正是"in my family, to be good is to fail"（第3章）。别让"天才"标签把人钉死。
6. **用户语言里本来就没有"过程"词汇** → 帮他从对方的实际行动里找素材，别硬塞术语。
