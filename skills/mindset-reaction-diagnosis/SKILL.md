---
name: mindset-reaction-diagnosis
description: 当用户在「失败/出错、需要付出努力、被批评、看到别人成功」这四类时刻卡住时使用——判断他此刻用的是「证明自己」（固定型）还是「发展自己」（成长型）的读法，把这个读法"看见了什么、接下来会把他带到哪里"点破，让他有机会换一种读法。
input_schema:
  required: [moment_type, user_reaction, inner_monologue]
  optional: [context, past_pattern, audience]
output_schema:
  primary: {mindset_reading, what_the_moment_means, where_it_leads}
  secondary: [growth_reading, first_step, cautions]
---

# 四时刻读法诊断：你此刻在「证明自己」还是「发展自己」

**来源**：《Mindset: The New Psychology of Success》第1章 The Mindsets、第2章 Inside the Mindsets | 证据等级：firsthand（机制与分类为 firsthand；四时刻的归纳为 reliable-secondary）

## 触发条件

**应该触发**：
- 用户考砸/项目失败/被拒后说"我就是不行""我是个失败者""我完了"
- 用户面对一件难事说"如果我真聪明/有天赋，就不用这么费劲"、"我可能没这个天分"
- 用户被批评后第一反应是"他在否定我这个人"，或整段复述都在自证清白
- 用户看到同事/朋友/同龄人成功，说"我怎么这么差""这本来该是我"
- 用户描述"每次遇到这类事我就……"并想搞清楚这反应会把他带向哪里

**不应触发**：
- 用户要的是表扬/批评的**话术改写**（走 mindset-process-praise）
- 用户要审查自己"我是不是真成长型"的口头化问题（走 mindset-false-growth-check）
- 用户已有明确的触发情境但想做的是转化+行动计划（走 mindset-trigger-reframe）
- 用户处于急性抑郁/自伤/危机状态 → 先走 B 节转介，不做读法诊断

## R：原文锚点

> "When you enter a mindset, you enter a new world. In one world—the world of fixed traits—success is about proving you're smart or talented. Validating yourself. In the other—the world of changing qualities—it's about stretching yourself to learn something new. Developing yourself."（第2章 Inside the Mindsets，开篇）（已据原文核）

> "In one world, failure is about having a setback. Getting a bad grade. Losing a tournament. Getting fired. Getting rejected. It means you're not smart or talented. In the other world, failure is about not growing. Not reaching for the things you value. It means you're not fulfilling your potential."（第2章 Inside the Mindsets）（已据原文核）

> "People with the fixed mindset tell us, 'If you have to work at something, you must not be good at it.' They add, 'Things come easily to people who are true geniuses.'"（第2章，Mindsets Change the Meaning of Effort）（已据原文核）

> "The fixed mindset creates an internal monologue that is focused on judging: 'This means I'm a loser.' 'This means I'm a better person than they are.' 'This means I'm a bad husband.' 'This means my partner is selfish.'"（第8章，Mindsets Go Further）（已据原文核）

## I：核心解释

1. **同一个事件，两套读法**：不是"会不会应对失败"两种人，而是同一件难事被读成两件不同的事。固定型把事件读成对**特质**的测量（我聪明不聪明），成长型把事件读成对**过程**的反馈（我下次该改什么）。上面 R 第一、二条就是这两套世界。
2. **四时刻是读法的四个探针**：失败、需要努力、被批评、看见别人成功——这四个时刻最容易触发评判式读法，也最容易暴露用户此刻在哪套世界里。
3. **努力＝探针上的红灯**：在固定型里，"需要努力"本身被读成"你不行"的证据（R 第三条）；在成长型里，努力是把能力点燃成成绩的东西。
4. **失败不等于没有痛苦**：书上明说，即便成长型，失败也很痛——区别只在于"它不定义你，它是个要被处理、被学习的问题"。（第2章 Defining Moments）
5. **看到别人成功＝照镜子还是看路**：固定型把别人的成功读成对我的排名，于是"心一沉/发窘/贬低对方"；成长型更可能把它读成"他怎么做到的"。书里那个钓鱼的故事最直白：作者钓到鱼，丈夫跑来祝贺，另两个男人却问丈夫"你是怎么撑过来的"——他们默认妻子的成功会让他觉得自己变小。（第2章）
6. **读法会自我实现**：固定型的读法把人推向"少努力、别暴露、甩锅、保面子"（第2章 Shirk, Cheat, Blame），成长型的读法把人推向"加把劲、换策略、问人、继续"。点破"接下来会去哪"，就是给用户选择的余地。

## A1：来源应用 — 书里诊断两套读法用的对照法

Dweck 让固定型和成长型被试看**同一个**普通挫折情境，然后对比他们的内心独白和打算：情境刻意做得温和——"a C+, not an F... a parking ticket, not a car wreck"（第1章，A View from the Two Mindsets）。

- 固定型反应：> "'I'd feel like a reject.' 'I'm a total failure.'"（第1章）
- 成长型反应：> "'The C+ would tell me that I'd have to work a lot harder in the class, but I have the rest of the semester to pull up my grade.'"（第1章）

诊断动作照抄这个对照法：**把用户此刻的独白和书里两组原话并排**，让用户自己对上号——不替他贴标签，让他认出"这是我"。

书里还给了另外两个探针，用来定位"看见别人成功"和"努力"两个时刻：
- 问"你什么时候觉得自己聪明？"固定型答"我不犯错的时候""别人做不出来而我轻松做出来的时候"；成长型答"真的很努力、做成我以前做不到的事的时候"。（第2章 When Do You Feel Smart）
- 固定型觉得"真正有天赋的人做事很轻松"。（第2章）

## A2：典型触发场景

- 收到差评/退稿/被拒面试后，反复在脑内替自己辩护
- 一节课/一个项目刚开始变难，就想找理由退出
- 上级一条模糊的反馈，被听成对整人价值的判决
- 刷到同龄人升职/买房/发论文，情绪骤降
- 明知该举手/该开口，却因为"答错会被发现我不行"而沉默

## E：执行步骤

### 步骤1：锁定是哪一个时刻

**输入**：用户的原话与情境。
**输出**：明确归类到四时刻之一（失败 / 需要努力 / 被批评 / 看见别人成功）。

🔴 **CHECKPOINT — 触发条件：用户只说"我最近很丧""我觉得自己很差"，给不出具体时刻**：泛化情绪不适合四时刻诊断 → 追问最近一次具体发生了什么："形容一下那一刻——当时谁在场、屏幕上/老师说了什么、你第一句话是什么？"若仍拿不出具体事件 → 转 B 节「泛化情绪」分支。

### 步骤2：抓出评判式独白

**输入**：用户对那一刻的描述。
**输出**：一句被复述出来的内心独白（"这意味着我是……"）。

对照 R 第四条的句式去引导：把"这代表我是___"补完。让用户自己说，而不是你替他填。

🔴 **CHECKPOINT — 触发条件：用户独白里出现重度自我否定（"我这样活着没意义""我什么都做不好，没救了"）**：这可能超出读法诊断的范围 → 立即转 B 节「抑郁/自伤信号」，不继续在认知层拆解，改做陪伴与转介。

### 步骤3：并排放书里的两组原话

**输入**：步骤2 的独白。
**输出**：用户对固定型/成长型两套读法的自我指认（"这是固定型，因为我……"）。

用 A1 的对照法：先给固定型原话让他认，再给成长型原话让他试。

### 步骤4：点出"这个读法接下来会带你去哪"

**输入**：步骤3 的指认 + 步骤1 的时刻。
**输出**：一句关于后果的预判（会走向学习，还是走向少努力/藏起自己/甩锅/保面子）。

这是本 skill 的落点：不做道德评判，只把因果说清。例如固定型读法在"需要努力"这个时刻会导向"减少投入以保护自我评价"（第2章 Low-Effort Syndrome，第3章）。

### 步骤5：给一个"换读法"的最小动作（可选出口）

**输入**：步骤4 的后果预判。
**输出**：一个用户下一步能做的小动作，或一句成长型读法的替换句。

若用户还想继续到"改独白+定计划"，转 mindset-trigger-reframe skill。

## B：边界与失败模式

### 失败模式分支表

| 情况 | 表现 | 怎么处理 |
|------|------|---------|
| 泛化情绪 | 用户给不出任何具体时刻，只说"我一直很丧" | 🛑 不硬套四时刻。先降级为倾听，问"最近一次让你有这种感觉的具体场景"。 |
| 把诊断当判决 | 用户说"所以我就是固定型人格，没救了" | 🛑 纠偏："读法是此刻的选择，不是你的身份标签。你不是固定型的人，你是此刻用了固定型的读法。"（第2章：Mindsets are just beliefs... you can change your mind） |
| 用成长型话术压真实痛苦 | 用户说"我该积极点，不该难过" | 🛑 正常化：书上明说成长型的人失败也会痛，区别是不被定义。（第2章 Defining Moments） |
| 抑郁/自伤信号 | 出现"没意义""活不下去""不想存在" | 🛑 停止读法诊断，转 B 节安全分支，给专业资源。 |
| 被用来合理化不作为 | 用户用"我在成长"掩盖继续什么都不做 | 🛑 指出成长型也要求"做"，转 mindset-false-growth-check。 |

### 边界规则

1. **不做诊断，不做人格判决**：本 skill 只分类"此刻的读法"，不判定用户是哪种人，不替代心理评估。
2. **读法不是非黑即白**：书里明确一个人的intelligence mindset和personality mindset可以不一致，多数人"lean toward one or the other"（第1章）。别把用户一刀切。
3. **四时刻只是探针，不是全部人生**：别把每个生活片段都套进四时刻。
4. **安全兜底**：若出现临床抑郁、自伤、自杀意念、饮食/身体相关的严重信号，**停止 mindset 工作**，明确告诉用户这需要专业人员，并指向当地心理援助资源（如各地心理援助热线；中国大陆可拨 12356 或 010-82951332，紧急时拨 120/110）。不做诊断、不保证效果。

### 用户自查清单

- [ ] 我能说清刚才卡在四时刻里的**哪一个**
- [ ] 我能**逐字说出**那一刻脑内的独白（而不是笼统的"我很烦"）
- [ ] 我能认出这句独白属于哪套读法，并说出**为什么**
- [ ] 我能说出这个读法**接下来会把我带向哪里**
- [ ] 我知道一个**换读法的最小动作**或替换句

**勾选 4+ 项**：诊断到位。**≤2 项**：回到对应的步骤重做，或考虑转 B 节。

## 📖 练习手册

**四时刻对照卡**（把书里的对照法用在你自己身上）：拿一张纸，分四栏——失败 / 需要努力 / 被批评 / 看见别人成功。每栏左边写"固定型读法会说什么"，右边写"成长型读法会说什么"，然后标出你最近一次真实经历落在哪。

**"这意味着"追踪**：连续三天，每次情绪骤降时记下一句以"这意味着我是……"开头的独白，周末回看，归类。

## 🚫 反例与黑名单

1. **急性精神病性症状 / 重度抑郁 / 自伤** → 先转专业评估，本框架不适用急性期。
2. **纯外部困境**（失业、灾害、战乱）→ 读法诊断不能替代现实援助；先谈资源和处境。
3. **用"你是固定型心态"攻击他人** → 🛑 停止。读法诊断是自助工具，不是给别人的判决书。
4. **把"成长型"当新的表现标准** → 用户在"证明自己是成长型的"，这本身就是固定型读法，转 mindset-false-growth-check。

### 灰色地带（需谨慎判断）

5. **用户真诚地说喜欢自己的固定型读法**（"知道我擅长什么让我踏实"）→ 不要把成长型强加。书里明说："If you like it, by all means keep it."（第2章 Questions and Answers）只帮他看清代价，留选择权给他。
6. **用户在专业治疗中** → 优先遵循治疗师结论，本框架仅作补充理解。
7. **谈的是别人的读法**（"我老公就是固定型"）→ 引导回到"你自己在这一刻的读法"，否则变成指责工具。
