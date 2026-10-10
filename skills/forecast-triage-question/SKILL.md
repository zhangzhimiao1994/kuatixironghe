---
name: forecast-triage-question
description: 分诊题目、判断哪些值得预测（只在 Goldilocks 区下功夫，别碰太易的 clocklike 题、也别碰不可解的 cloud-like 题），并为超出预测范围的未来做"为意外计划"。当用户说"这事到底能不能预测""要不要花力气估十年后的格局""油价/汇率/大选值不值得估""预测不了那怎么准备""我们是不是在猜一个根本猜不出的东西"时使用：分诊 → 在 Goldilocks 区收窄、在 cloud-like 区止损 → 为范围之外做适应性与韧性计划 → 把"要不要防某类意外"变成明说的概率取舍。
input_schema:
  required: [candidate_questions, time_horizon, planning_goal]
  optional: [known_unpredictables, resource_constraints, attempt_budget]
output_schema:
  primary: {triage_classification: string, goldilocks_focus: string, surprise_plan: string}
  secondary: [stop_loss_list, probability_assumptions, hindsight_check]
---

# 分诊题目：只在 Goldilocks 区下功夫，并为不可预测做计划

**来源**：《Superforecasting》附录「Ten Commandments for Aspiring Superforecasters」第1条 Triage + 第11章「Are They Really So Super?」（ENTER THE BLACK SWAN / ALL THAT SAID…）+ 第4章「Superforecasters」（Goldilocks zone 段）| 证据等级：firsthand

## 触发条件

**应该触发**：
- 用户面对一堆问题，不知先估哪个、或问"这事到底能不能预测"
- 用户想预测明显不可预测的东西（长期油价、汇率、十年后的格局/选举）
- 用户要为一个"超出预测范围"的未来做计划（防灾、应急预案、长期战略）
- 用户问"我们是不是在浪费时间，估一个根本估不出的东西"
- 用户在"该不该努力预测"上纠结，或过度自信能预测转折点

**不应触发**：
- 已确认题目值得做、要开始估 → `forecast-fermi-baserate`
- 要给一个命题具体概率 → `forecast-fermi-baserate`
- 要给预测记分、比较谁更准 → `forecast-keep-score`
- 只是召集一队人一起判断 → `forecast-superteam`
- 领导层如何为不确定性做组织安排 → `forecast-leader-culture`
- 纯事实查询或算术 → 直接做

## R：原文锚点

> "Focus on questions where your hard work is likely to pay off. Don’t waste time either on easy “clocklike” questions (where simple rules of thumb can get you close to the right answer) or on impenetrable “cloud-like” questions (where even fancy statistical models can’t beat the dart-throwing chimp). Concentrate on questions in the Goldilocks zone of difficulty, where effort pays off the most."（附录 Ten Commandments 第1条 Triage）（已据原文核）

> "IARPA was looking for questions in the Goldilocks zone of difficulty, neither so easy that any attentive reader of the New York Times could get them right nor so hard that no one on the planet could."（第4章 Superforecasters）（已据原文核）

> "Certain classes of outcomes have well-deserved reputations for being radically unpredictable (e.g., oil prices, currency markets)."（附录第1条 Triage）（已据原文核）

> "we usually don’t discover how unpredictable outcomes are until we have spun our wheels for a while trying to gain analytical traction."（附录第1条 Triage）（已据原文核）

> "We could fail to try to predict the potentially predictable or we could waste our time trying to predict the unpredictable."（附录第1条 Triage）（已据原文核）

> "If you have to plan for a future beyond the forecasting horizon, plan for surprise. That means, as Danzig advises, planning for adaptability and resilience."（第11章 ALL THAT SAID…）（已据原文核）

> "“Plans are useless,” Eisenhower said about preparing for battle, “but planning is indispensable.”"（第11章 ALL THAT SAID…）（已据原文核）

> "History does sometimes jump. But it also crawls, and slow, incremental change can be profoundly important."（第11章 ENTER THE BLACK SWAN）（已据原文核）

> "IARPA has commissioned a fool’s errand. What matters can’t be forecast and what can be forecast doesn’t matter."（第11章 ENTER THE BLACK SWAN）（已据原文核）

## I：核心解释

1. **分诊（triage）是第一步**：把精力放在"努力大概率有回报"的题上。两端都不碰——太易的"clocklike"题（简单经验法则就够准）与太难的"cloud-like"题（再花哨的模型也打不过扔飞镖的黑猩猩）。集中在难度刚好的 Goldilocks 区。（R1）
2. **举例**：现在估 2028 年谁当总统是不可能的，别试；但越近越能收窄——2016 年至少能列出少数可能人选。（附录第1条）
3. **有些类别"名声在外"地不可预测**（油价、汇率）；但我们也常常要"空转一阵、试着获得分析抓手"之后才发现它不可预测——所以分诊本身要一点试错，别一上来就断言。（R3、R4）
4. **两种错误要先掂量**：漏掉本可预测的，或把时间浪费在不可预测的上。先问"在你这个情形里，哪种错更糟"——这是判断，不是公式。（R5）
5. **Taleb 的黑天鹅挑战（书里作为最强反驳之一）**：如果只有黑天鹅重要、且它们不可预测，那预测就是白费——"要紧的预测不了，能预测的不要紧"。书里承认：第一代赛事对超级预测者能否预见黑/灰天鹅**没有证据**，别假装知道。
6. **但并非没有出路**：严格的"事前完全无法想象"的黑天鹅其实很少（9/11 事前在安全圈被讨论过）；而且"事件"的边界会随时间扩张（袭击的后果也算事件），后果可以逐段预测。历史有时跳，但也爬——缓慢增量同样了不起。（R8）
7. **范围之外就为"意外"计划**：为适应性（adaptability）与韧性（resilience）做准备。想象现实给你一记耳光、再补一记踢在胫骨上，想你会怎么应对。（R6）
8. **计划的价值在过程，不在文本**："计划无用，但计划不可或缺"——计划是让你想清楚，而不是给你一份应验的未来。（R7）
9. **为意外作准备有成本**：东京的抗震标准值得，因为那里是"地震中心"；地震少的穷地区就未必。要不要为某类意外掏钱、掏多少，又回到概率判断——而这些判断应当被明说出来。
10. **承认极限**：书里 EPJ 研究显示专家预测的精度随跨度下降、五年外趋近随机；系统性"知道自己不知道"胜过"以为自己知道"。

## A1：来源应用 — 书里怎么分诊、怎么为意外计划

1. **附录第1条**：明确划出 clocklike / Goldilocks / cloud-like 三类；用"1940 年能否预见 1952 年是艾森豪威尔"来检验自己有没有事后聪明——若你以为当年就该知道，那是极严重的事后偏见。
2. **第4章**：IARPA 专门筛 Goldilocks 区的问题（太易：概率 <10% 或 >90%；太难：没人能合理知晓），用来找人才、试方法；并明说"推人去做几乎不可能的事是浪费钱"——人的认知系统无法预测个人或国家多年后的转折点。
3. **第11章**：EPJ 里专家预测五年外趋近随机；二十年式国防预测是仪式性的（Lin Wells 的"非正规反抗"备忘录：2010 会与我们预期大不相同，所以要据此计划）。
4. **Danzig 的建议**：为适应性、韧性做计划——想象"现实给你一记耳光"，再想象"现实又踢你一脚"，各想怎么应对。
5. **代价视角**（东京抗震规范 vs 两国/三国/外星入侵式军备）：为哪种意外掏钱取决于概率判断；判断不可回避，把概率明说出来，猜的就承认是猜的。
6. **样本极限**：稀有事件（1%、0.1% 概率）几乎不发生，要几十年上百年才攒够数据——所以别指望这类检验能快速给出结论。

## A2：典型触发场景

- "我在纠结要不要花力气预测十年后的行业格局。"
- "油价/汇率/明年大选要不要预测？"
- 防灾、应急预案、长期战略："既然预测不了，那怎么准备？"
- 手上一堆待估问题，不知先估哪个
- "我们是不是在猜一个根本猜不出的东西？"
- 有人宣称能预测某个明显的转折点，用户想知道该不该信

## E：执行步骤

### 步骤1：给题目分诊

**输入**：一张候选问题清单（`candidate_questions`）。
**输出**：把它们分到 clocklike / Goldilocks / cloud-like 三类，并标出值得花力气的。

- 判断依据：太易（简单规则就够准）？太难（连花哨模型也打不过扔飞镖的黑猩猩）？还是难度刚好？（R1、R2）

🔴 **CHECKPOINT — 触发条件：分不清属于哪一类**：允许"空转一小段"去试分析（R4），但要设一个**停损预算**；同时问"哪种错误（漏掉可预测的 vs 浪费在不可预测上）在你情形里更糟"（R5）。

### 步骤2：在 Goldilocks 区收窄，在 cloud-like 区止损

**输入**：分类结果 + 时间跨度（`time_horizon`）。
**输出**：对 Goldilocks 题排优先级、准备估计；对 cloud-like 题写下"为什么不可预测、别再加码"。

- 越近越能收窄：像 2016 年能列出少数人选，而 2028 年不能。

🔴 **CHECKPOINT — 触发条件：用户坚称一个明显不可预测的题"这次能猜中"**：提醒随机命中不等于能力（扔飞镖的猩猩偶尔正中），并给出"越远越趋近随机"的证据；把精力挪回 Goldilocks 区或转为"为意外计划"（步骤3）。

### 步骤3：为范围之外做"意外计划"

**输入**：超出可预测范围的目标/威胁（`planning_goal`）。
**输出**：一份"适应性与韧性"计划——想到意外→如何响应→再想下一脚。

- 用 Danzig 的两步想象（一记耳光、再补一脚），每次各写两步应对。（R6）
- 记住：这是**为意外准备**，不是预测一个具体未来。（R7）

🔴 **CHECKPOINT — 触发条件：计划变成"把某个具体未来钉死"**：拉回——"计划无用但不可或缺"；它训练的是应变，不是给你一份应验的剧本。

### 步骤4：把"要不要防某类意外"变成明说的概率取舍

**输入**：资源约束（`resource_constraints`）。
**输出**：明说你的概率假设与取舍——哪些意外值得花钱、哪些不值得、为什么。

- 像东京 vs 地震少的地区那样，按"发生可能性 × 后果"决定投入。

🔴 **CHECKPOINT — 触发条件：通篇没有概率、只有口号**：要求把假设写出来；若确实只能猜，就标出"这是猜的"——书里说"知道自己不知道"胜过"以为自己知道"。

## B：边界与失败模式

### 失败模式分支表

| 情况 | 表现信号 | 立即执行替代动作 |
|------|----------|------------------|
| 在 clocklike 题上过度用力 | 用复杂模型估"明天日出" | 🛑 简单经验法则就够，别浪费 |
| 在 cloud-like 题上死磕 | 硬估十年后汇率 | 🛑 止损；改为"为意外做计划" |
| 用一次命中证明能力 | "他预测对了" | 🛑 随机也会命中；看多次、看分数（见 `forecast-keep-score`） |
| 事后聪明 | "这在当年就该看得出" | 🛑 用 1940→1952 的测试；警惕 hindsight bias |
| 把"计划"当"预测未来" | 一份固化的未来图景 | 🛑 改为适应性/韧性；"计划无用但不可或缺" |
| 为所有意外都掏钱 | 不计成本全面设防 | 🛑 明确概率与成本，做取舍 |
| 假装知道黑天鹅 | "我们能预见一切" | 🛑 书里承认无证据；别装 |
| 涉及就医 / 自伤 / 危机 | 议题关于生死、病情 | 🛑 放下框架，转专业资源，不诊断 |

### 边界规则

1. **分诊是判断，不是公式**：两端都可能错，先问哪种错更糟（R5）。
2. **不承诺能预测云状问题**；不把随机命中说成能力。
3. **"为意外计划"是准备，不是预测**。
4. **为意外设防有成本**，取舍要基于**明说的**概率。
5. **承认样本极限**：稀有事件检验不了，别假装有证据。
6. **本 skill 不做投资 / 医疗 / 法律建议**。
7. **安全兜底**：涉及就医、自伤、心理危机时转专业资源，不诊断。

### 用户自查清单

- [ ] 我给题目分了诊（太易 / 恰好 / 太难）
- [ ] 我没有在明显不可预测的题上继续投入
- [ ] 我用"这次命中可能是运气"的尺度看预测
- [ ] 我检查了有没有事后聪明
- [ ] 我为范围之外做了适应性 / 韧性计划
- [ ] 我把"要不要防某类意外"变成明说的概率取舍
- [ ] 我承认了"我知道自己不知道"

**勾了 5 项以上**：精力用在了刀刃上。
**≤ 2 项**：多半还在 cloud-like 题上硬撞、或没有为意外做准备 → 回步骤1 或步骤3。

## 📖 练习手册

- **分类练习**：把最近关心的 10 个问题分到 clocklike / Goldilocks / cloud-like 三类，各标一句理由。
- **事后聪明测试**：拿一件过去的事，认真问"当年真能预知吗"，用 1940→1952 做对照。
- **意外计划**：写下"现实给你一记耳光"和"再补一脚"两次，各想两步应对。
- **成本取舍**：挑一类意外，写下你愿意花多少资源、为什么。

## 🚫 反例与黑名单

1. **在 cloud-like 题上反复加码** → 🛑 先设停损预算；转"为意外计划"。
2. **用一次命中封神、一次失手否定** → 🛑 随机也会命中；要看多次与分数。
3. **用现在知识审判过去的判断** → 🛑 事后聪明是最常见的错。
4. **把"为意外计划"做成固化的未来剧本** → 🛑 它训练的是应变。
5. **不计成本地为一切设防** → 🛑 要按概率与成本取舍。
6. **宣称能预测黑天鹅** → 🛑 书里明确说没有证据，别装。

### 灰色地带（需谨慎判断）

7. **分不清 clocklike 与 cloud-like** → 允许试错一段，但先设停损预算（`attempt_budget`）；试完还无抓手，就归入 cloud-like。
8. **"要不要预测油价"** → 这类整体"名声在外"地不可预测；但它的具体子问题（如"某事件是否触发"）也许落在 Goldilocks 区，可拆开看。
9. **某类意外该不该设防** → 取决于你所在地区与资源（东京的抗震标准 vs 穷地区未必划算），没有统一答案。
10. **预测与投资的资源该往哪放** → 书里区分"黑天鹅式投资"（大多数失败、博少数暴利）与"更准地预测以稳定取胜"——两者不同、不分高下，取决于你的处境；领导层怎么在"看得清时预测、看不清时为韧性投资"间调度，见 `forecast-leader-culture`。
