---
name: forecast-keep-score
description: 给预测记分、判断谁（我/某专家/某方法）在真正看得更准——用 Brier 分数（像高尔夫，越低越好）、校准与分辨率、基准与可比性，而不是靠一次对错或名气。当用户说"他上次说错了所以他不准""他这次说中了真神""怎么公平比较两个人的预测""想给团队建预测记分"时使用：先把预测变成可打分的形式 → 算/理解 Brier → 找基准与可比对象 → 用分数反馈改行为。
input_schema:
  required: [forecast_records, outcome_or_pending, comparison_target]
  optional: [base_rate_benchmark, time_frame, granularity]
output_schema:
  primary: {brier_reading: string, calibration_vs_resolution: string, benchmark_comparison: string}
  secondary: [comparability_note, feedback_actions, scoring_caveats]
---

# 给预测记分：用 Brier 分数（越低越好）判断谁在真正看得更准

**来源**：《Superforecasting》第3章「Keeping Score」（JUDGING JUDGMENTS / THE MEANING OF THE MATH）| 证据等级：firsthand

## 触发条件

**应该触发**：
- 用户想判断"谁（我/某专家/某团队/某方法）预测得准"，却只会靠印象或记忆
- 用户说"他上次说错了，所以他不准"或"他这次说对了，真准"——用一次对错定英雄
- 要把两个预测者或两种方法比较，想知道怎么才算公平
- 用户想把模糊话换成可打分的数字概率，并为此担责
- 团队/组织想建一套预测记分，问"该记哪些、怎么记、怎么读"
- 用户想拿"过去的对错"当依据去信或不信某个判断

**不应触发**：
- 从零估一个概率 → `forecast-fermi-baserate`
- 只是给已有预测做一次更新/复盘 → `forecast-update-postmortem`
- 命题还没钉死（事件、时间、口径含糊）→ 先走 `forecast-calibrate-claim`
- 只是判断某道题值不值得花力气 → `forecast-triage-question`
- 纯算术题 → 直接算

## R：原文锚点

> "So Brier scores are like golf scores: lower is better."（第3章 JUDGING JUDGMENTS）（已据原文核）

> "In effect, Brier scores measure the distance between what you forecast and what actually happened."（第3章 JUDGING JUDGMENTS）（已据原文核）

> "A hedged fifty-fifty call, or random guessing in the aggregate, will produce a Brier score of 0.5."（第3章 JUDGING JUDGMENTS）（已据原文核）

> "This is called calibration."（第3章 JUDGING JUDGMENTS）（已据原文核）

> "The technical term for this is “resolution.”"（第3章 JUDGING JUDGMENTS）（已据原文核）

> "To do that, we have to interpret the meaning of the Brier scores, which requires two more things: benchmarks and comparability."（第3章 THE MEANING OF THE MATH）（已据原文核）

> "What a Brier score means depends on what’s being forecast."（第3章 THE MEANING OF THE MATH）（已据原文核）

> "Forecasting the weather in Phoenix is just plain easier than forecasting the weather in Springfield, Missouri, where weather is notoriously variable, so comparing the Brier scores of a Phoenix meteorologist with those of a Springfield meteorologist would be unfair."（第3章 THE MEANING OF THE MATH）（已据原文核）

> "dredging up old forecasts from newspapers will seldom yield apples-to-apples comparisons because, outside of tournaments, real-world forecasters seldom predict exactly the same developments over exactly the same time period."（第3章 THE MEANING OF THE MATH）（已据原文核）

## I：核心解释

1. **为什么必须记分**：目标是判断准确性、搞清什么在起作用。一道概率预测无法被判定（历史不能重跑）；但一批可以——预报说 70% 下雨，就该在 70% 的报次下雨，这叫校准。（R4）
2. **校准不够**：完美校准也可能永远停在 40%–60% 的"暧昧区"（poor resolution，校准好但"胆小"）。分辨率（resolution）是"该高就高、该低就低"的果断度——把高概率给到会发生的事、低概率给到不会发生的。（R5）
3. **合并两者才是我们要的记分**：说 70% 而中了要得分，说 90% 而中了应更高，敢说 100% 且中了满分；但夸口（slam dunk）而没中要重重扣分。扣多重可按赌局想：说 80% 是给你 4:1，说 95% 是 19:1。（第3章 JUDGING JUDGMENTS）
4. **Brier 分数**：1950 年 Glenn W. Brier 发明，衡量预测与实际的距离；像高尔夫，**越低越好**；完美是 0；对冲的 50-50 或随机猜测约 0.5；最糟——每次都说 100% 会发生而没发生——是 2.0。（R1、R2、R3）
5. **数字是估计不是事实**：把"serious possibility"翻译成数字时会逼你想清楚自己到底在想什么（metacognition），但这不改变"数字只是主观估计"这一点。
6. **分数要有意义，得靠两样东西：基准与可比性**。没有它们，一个 Brier 分数本身说明不了太多。（R6）
7. **同一分数在不同题上意义不同**：0.2 在天天晴热的凤凰城很平庸（无脑"永远晴热"就能接近 0）；在天气多变的斯普林菲尔德可能是世界级。（R7、R8）
8. **基准有两种**：一是"无脑规则"（如"永远预测不变"——书里说这能拿 48/50）；二是其他预测者/共识。比较需要"公平赛场"：同样的题、同样的时间窗。（R9）
9. **wrong-side-of-maybe fallacy 是记分的政治阻力**：人们看到 70% 的预测没发生就说错，但预测同时含 30% 不发生的可能。这个谬误逼组织退回模糊话——而模糊话还能反过来被拿来"两头讨好"。
10. **记分是"proper"（适当）的**：它激励预测者报告真实信念、抵抗政治压力；若你不愿按自己给的赔率下注，就该重估（脚注）。记分也是"进行中的工作"：Brier 把假警报与漏报同罚，可按场合调权，但必须**事先**讲明。

## A1：来源应用 — 书里怎么记、怎么读

1. **要把预测变成可打分的**：命题有清晰定义与时间线、用数字概率、并且有大量预测。气象类因天天有、堆得快，校准好用；大选类要重跑几百年不现实，可用州级把样本从 1 提到 50。
2. **实时更新的记法**（原书第3章及第4章开头的操作说明）：预测可随时改动，每次改动都算一次预测；不改则沿用原值；到期后把**同一道题上的所有预测**汇成一个 Brier 分数。
3. **个体数据示例**：Doug Lorch 第 1 年 Brier 0.22（2800 人里第 5），进团队后 0.14（最佳）；Bill Flack 在 Arafat 钋题上 0.36（对这么难的题很不错，而当时内盘预测市场只给 4.27%，Brier 差他五倍）；Tim Minto 叙利亚难民 0.07。
4. **读群体分数**：超级预测者第 1 年集体 0.25，其他 0.37；到四年末 super 比普通高出 60% 以上。
5. **粒度与准确度**：Mellers 发现更细的粒度预测得更准——用 1% 的人比用 5% 的准，用 5% 的比用 10% 的准；把分数朝五/十取整会掉准（super 甚至对 0.05 取整都敏感）。
6. **分数是工作，不是完美**：Brier 把假警报与漏报同罚，但可针对场合调权——"假阳性只按假阴性的十分之一罚"，只要事先讲清规则。
7. **警告别只看数字**：书里提醒——一旦定了官方指标，就有人钻空子（如医院靠拒收重症病人刷"存活率"）。指标要被审查和改进，而不是废掉。

## A2：典型触发场景

- "我到底该不该信这位专家的预测？"——可用他的历史 Brier / 校准，而不是名气
- "我们三个人谁估得准？"——用同题、同时间窗比较
- 组织想引入预测打分、想建排行榜
- 想把自己从"报模糊话"升级到"报数字并担责"
- 一次高置信度预测失败后，纠结"是不是我太自信了"

## E：执行步骤

### 步骤1：把预测变成可打分的形式

**输入**：一组预测（`forecast_records`）。
**输出**：每条都有明确命题、时间线、数字概率的记录。

- 概率用数字；命题要有清晰定义与时间线。

🔴 **CHECKPOINT — 触发条件：命题含糊、带"may/could/可能"**：这没法打分 → 转 `forecast-calibrate-claim` 先把事件、时间、口径钉死。若只有孤零零一次预测，也先攒成一批同样格式的，再谈记分。

### 步骤2：算 / 理解分数

**输入**：一批预测 + 结果（`outcome_or_pending`）。
**输出**：Brier 分数读数 + 一句"校准与分辨率各自如何"的判断。

- 记住：越低越好（高尔夫）；0.5 ≈ 随机，0 完美，2 最糟。（R1、R2、R3）

🔴 **CHECKPOINT — 触发条件：用户把"我说 70% 会成、结果没成"判成错**：纠正 wrong-side-of-maybe fallacy——这条预测同时含 30% 不发生的可能，没有大批重复就没法判定。

### 步骤3：找基准与可比对象

**输入**：分数 + 比较目标（`comparison_target`）。
**输出**：与"无脑规则"和"其他预测者/共识"的对比，且确认题与时间窗可比。

- 先问"这类题，无脑规则能拿多少分"，再问"能不能赢过共识"。（R6、R9）

🔴 **CHECKPOINT — 触发条件：用户拿不同难度、不同题、不同时间窗的分数直接比**：喊停，说明 comparability——像拿凤凰城气象员比斯普林菲尔德气象员那样不公平；换成同题、同窗口再比。（R8）

### 步骤4：用分数反馈改行为

**输入**：分数史（可带 `granularity`）。
**输出**：关于"我偏高/偏低/太粗/太细"的具体结论 + 下一步动作。

- 用分数看清自己是欠自信（校准偏上）还是过度自信（校准偏下），粒度是否够细。
- 记住书里的话：记分给出"我到底偏在哪儿"的反馈，据此调整预测行为。

🔴 **CHECKPOINT — 触发条件：用户想用记分去抓人/贴标签，或反过来钻指标漏洞**：提醒这是"进行中的工作"，指标会被 gaming（如拒收重症刷存活率）；应调权重、加审计、事先讲规则，而不是废掉记分或拿它清算人。

## B：边界与失败模式

### 失败模式分支表

| 情况 | 表现信号 | 立即执行替代动作 |
|------|----------|------------------|
| 用一次对错判英雄 | "他上次说准了，是神" | 🛑 说清单次不可判；要看很多次、看 Brier 与校准 |
| 70% 没中就判错 | "你明明说会下雨" | 🛑 纠正 wrong-side-of-maybe fallacy |
| 跨题跨窗口硬比 | 拿一道题的分数比另一道 | 🛑 提醒 comparability：同题、同时间窗才公平 |
| 追低分而只报暧昧 | 全在 40%–60% 保险 | 🛑 校准得再好，分辨率差也不算好预测 |
| 报假精度 | 输出 37.4% 这类数 | 🛑 书里叫"granularity as bafflegab"；粒度要与真实区别匹配 |
| 指标被 gaming | "定什么就刷什么" | 🛑 事先讲规则、配套防作弊；记分是 work in progress |
| 把分数当客观事实 | 把 0.2 当绝对真理 | 🛑 数字只表达估计；分数也要被解释 |
| 涉及就医 / 自伤 / 危机 | 命题关于病情、生死 | 🛑 放下记分，转专业资源，不诊断 |

### 边界规则

1. **工具只做记分与解读，不替用户拍板**：信不信某人，由用户在数据之上自己决定。
2. **不做投资 / 医疗 / 法律建议**。
3. **Brier 分数必须有基准才有意义**（R6）。
4. **单次概率预测不可判**：需要大量预测，且要有明确命题与时间线。
5. **记分系统不完美**：Brier 把假警报与漏报同罚，可调权但必须事先讲明。
6. **任何指标都可能被 gaming**：配套防作弊与审查。
7. **安全兜底**：涉及就医、自伤、心理危机时放下记分框架，指向专业资源，不诊断。

### 用户自查清单

- [ ] 我的预测有明确命题、时间、数字概率
- [ ] 我用多次预测而非一次对错来评判
- [ ] 我懂"越低越好"，且 0.5 ≈ 随机
- [ ] 我区分了校准与分辨率
- [ ] 我找了基准（无脑规则 / 其他预测者 / 共识）
- [ ] 比较时题与时间窗可比
- [ ] 我清楚分数只是估计的量化，不是事实

**勾了 5 项以上**：记分可用。
**≤ 2 项**：多半只凭一次对错或没找基准 → 回步骤1 或步骤3。

## 📖 练习手册

- **给自己记分**：对你接下来 10 条判断各写一个数字概率（先可"模拟到期结果"），算一个 Brier 分。
- **做一次无脑基准**：用"永远预测不变"或"永远 50%"和你自己的判断来一场对比。
- **校准点检**：翻出过去"我说 80% 会成"的事，看实际成了几成。
- **校准 vs 分辨**：造两个例子——一个校准满分但只在 40%–60% 徘徊，一个既校准又果断，比较两者分数差异。

## 🚫 反例与黑名单

1. **用名气 / 头衔代替分数** → 🛑 书里明说名气与准确度甚至负相关。
2. **用一次输赢给预测者定性** → 🛑 单次不可判；要多次。
3. **把 wrong-side-of-maybe 当逻辑** → 🛑 70% 没发生不等于错。
4. **拿不可比的分数硬排座次** → 🛑 不同题、不同窗口不可比。
5. **为了低分只报 50-50** → 🛑 校准好但分辨率差，不是好预测。
6. **报假精度唬人** → 🛑 granularity as bafflegab。
7. **用记分清算人、或刷分** → 🛑 指标会被 gaming，要防作弊。

### 灰色地带（需谨慎判断）

8. **新预测者没有历史分数** → 先攒同格式的预测，别急着下"准/不准"的结论。
9. **有些题没有现成对照** → 至少用"无脑规则"当基准，并说明它的分量。
10. **组织里报数字有政治风险** → 见 `forecast-leader-culture` 的 kto-kogo 与 wrong-side-of-maybe，先保护记分制度。
11. **指标被 gaming** → 调权重、加审计，而不是废掉记分；书里提醒：改正不是放弃度量。
