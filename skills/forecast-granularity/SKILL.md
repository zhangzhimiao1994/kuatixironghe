---
name: forecast-granularity
description: 把"会 / 不会 / 也许"的三档直觉展开成更细的概率刻度——"也许"必须再细分，数字越细越好（只要它捕捉的是真实区别），细刻度才能给判断留出修正空间。当用户说"我就是觉得会或不会，没有中间""这事五五开（其实是说不好说）""我想报个更准的数字""我们只用高/中/低或五档打分"时使用：把三档展开 → 给"也许"定刻度 → 检验刻度是否捕捉真实区别 → 用细刻度留出微调空间。把话改成可判对错的命题走 forecast-calibrate-claim。
input_schema:
  required: [raw_judgment, current_scale, event_definition]
  optional: [distinction_examples, known_anchors, update_history]
output_schema:
  primary: {three_settings_to_scale: string, granular_probability: string, real_distinction_test: string}
  secondary: [coarsen_or_finen_hint, adjustment_note, bafflegab_flags]
---

# 把三档直觉展开成细刻度："也许"还要再细分

**来源**：《Superforecasting》第6章「Superquants?」（THE THIRD SETTING / PROBABILITY FOR THE STONE AGE / PROBABILITY FOR THE INFORMATION AGE / UNCERTAIN SUPERS） | 证据等级：firsthand

## 触发条件

**应该触发**：
- 用户的判断只有两三档："我觉得会 / 不会""八成会吧""就是有没有的事，没有中间"
- 用户拿"五五开""不好说""也许"来代替一个真实概率——这其实是把 50% 当"不确定"的代号
- 用户问"我想报个更准的数字""该报到 5% 还是 1% 的粒度"
- 团队 / 个人想用"高 / 中 / 低"或五档、七档打分，问要不要更细
- 用户写完一个数想再收一收（70% → 65%），或担心自己报的数只是唬人

**不应触发**：
- 命题本身还含糊：没有截止日、没有判定方式 → 先走 `forecast-calibrate-claim`（刻度无处安放）
- 用户要的是"用分数判断谁更准 / 看历史校准" → `forecast-keep-score`（那里读粒度的记分证据）
- 预测已写好，来了新消息要改、或到期要复盘"改多少、为什么改" → `forecast-update-postmortem`
- 还没有任何预测，要从零估一个概率 → `forecast-fermi-baserate`
- 纯算术、纯资料查询 → 直接做

## R：原文锚点

> "In dealing with probabilities, he said, most people only have three settings: 'gonna happen,' 'not gonna happen,' and 'maybe.'"（第6章 THE THIRD SETTING。作者转述 Amos Tversky 语）（已据原文核）

> "A three-setting dial gives quick, clear directions. Is that a lion? YES = run! MAYBE = stay alert! NO = relax. The ability to distinguish between a 60% probability and an 80% probability would add little. In fact, a more fine-grained analysis could slow you down—and get you killed."（第6章 PROBABILITY FOR THE STONE AGE）（已据原文核）

> "So 'maybe' has to be subdivided into degrees of probability."（第6章 PROBABILITY FOR THE INFORMATION AGE）（已据原文核）

> "And those numbers should be as finely subdivided as forecasters can manage. That might mean 10%, 20%, 30%…or 10%, 15%, 20%…or 10%, 11%, 12%. The finer grained the better, as long as the granularity captures real distinctions—meaning that if outcomes you say have an 11% chance of happening really do occur 1% less often than 12% outcomes and 1% more often than 10% outcomes. This complex mental dial is the basis of probabilistic thinking."（第6章 PROBABILITY FOR THE INFORMATION AGE）（已据原文核）

> "Forecasters who use a three-setting mental dial are much likelier to use 50% when they are asked to make probabilistic judgments because they use it as a stand-in for maybe."（第6章 UNCERTAIN SUPERS）（已据原文核）

> "Now I say the probability is 60%—and we can argue over whether it's 59 or 60%."（第6章 PROBABILITY FOR THE INFORMATION AGE。Robert Rubin 的年轻助手语）（已据原文核）

> "How can we be sure that when Brian Labatte makes an initial estimate of 70% but then stops himself and adjusts it to 65% the change is likely to produce a more accurate estimate?"（第6章 UNCERTAIN SUPERS）（已据原文核）

> "This is granularity as bafflegab. It is unfortunately common."（第6章 UNCERTAIN SUPERS）（已据原文核）

## I：核心解释

1. **三档直觉是天性**：人的心里大多只有三个刻度——"会发生 / 不会发生 / 也许"（Tversky）。这不是笨，是进化留下的默认设置。（R1）
2. **三档在远古是优点，在今天不够用**：祖先需要的是又快的指令——是狮子就跑、也许是狮子就警戒、不是就放松；那时把 60% 和 80% 分开反而拖慢你、害死你。但今天的判断要的正是这种细分。（R2）
3. **"也许"必须再细分**：确定性是幻象，只剩"也许"一档毫无用处；唯一出路是把"也许"切成一个个概率刻度。（R3）
4. **越细越好，但以"捕捉真实区别"为准**：可以从 10% 一档细到 5%、1%；前提是你说 11% 会发生的事，真的比 12% 的少发生一点、比 10% 的多发生一点。分得出的细才有意义，分不出的细是唬人。（R4）
5. **细刻度才给判断留出修正空间**：把话说成"60%，还能争是 59 还是 60"，意味着这个估计动得了、能微调；Brian Labatte 把 70% 停一下自己收成 65%，正是细刻度才做得到的自我修正。（R6、R7）
6. **细刻度不是装腔**：抬着下巴报"73% 会涨 24%"、再丢两个术语唬人，只是 granularity as bafflegab；细要与真实区别匹配。粒度是否真的更准，要靠记分去验（见 `forecast-keep-score`）。（R8）
7. **爱用 50% 是"还在三档"的信号**：用三档的人把 50% 当"也许"的代号；真在细刻度上想的人，用 50% 并不比 49%、51% 更多。所以总报 50% 的人往往更不准。（R5）

## A1：来源应用 — 书里怎么把刻度掰细

1. **记分证明细刻度是真的（不是唬人）**：Barbara Mellers 发现"粒度预测准确度"——用整十（20、30、40）的人不如用五（20、25、30），更不如用一（20、21、22）；把预测按五、按十取整后，超级预测者连对 0.05 取整都会掉准，普通预测者对它四倍大的 0.2 取整却几乎无感。书里的结论：Labatte 的细不是 bafflegab，是 precision。
2. **一个具体的自我收窄（Labatte）**：被问平时读什么，他答"大概 70%……"停了停，"不对，65/35 非虚构对虚构"。一句闲聊都细；正式预测里普通预测者常只停在整十。（第6章 UNCERTAIN SUPERS）
3. **Rubin 的助手改口**：年轻助手汇报法案能否过时说"绝对能过"，Rubin 不喜欢；后来他改说"概率是 60%——我们可以争它到底是 59 还是 60%"。（第6章 PROBABILITY FOR THE INFORMATION AGE）
4. **组织刻度可以更细**：国家情报委员会（NIC）让分析员用五档或七档——比三档好得多，但仍够不到最投入的超级预测者；书里主张这类组织只要重视并鼓励，也能做到。（第6章 UNCERTAIN SUPERS）
5. **有时候 1% 的细真的重要**：从"极不可能但可能"走到"绝无可能"，在后果足够大时是本质区别——想想埃博拉爆发，或投中下一个 Google。（第6章 UNCERTAIN SUPERS）

## A2：典型触发场景

- "这事我就觉得会成，或者不会，没有中间。"
- "五五开吧。"——其实是想说"我说不好"。
- "我想把 70% 再收一收，可又不知道该收到哪。"
- "我们开会只让报高 / 中 / 低，会不会太粗？"
- "我这 73% 到底是真区别，还是随口唬人？"

## E：执行步骤

### 步骤1：把三档摊开，先把"也许"拎出来

**输入**：用户的原始判断（`raw_judgment`）与当前用的刻度（`current_scale`）。
**输出**：确认他此刻是停在"会 / 不会 / 也许"三档，还是已经在报百分数。

- 先问一句："你说的'会'，是 100% 还是大概多少？'也许'又是什么程度？"
- 若他报的是"五五开 / 不好说"，提醒：这多半是"也许"（R5），不是真的 50%。

🔴 **CHECKPOINT — 触发条件：用户连"会 / 不会 / 也许"都给不出，只是烦躁地说"不知道"**：先别逼近度 → 退回命题层，确认他到底在给哪件未来事件下判断；没有可判对错的命题，转 `forecast-calibrate-claim`。

### 步骤2：给"也许"定刻度，并往细走一档

**输入**：步骤1 里的"也许"。
**输出**：一个从粗到细的候选刻度 + 用户当前能站住的那一档。

- 从整十开始（0、10、20…100），再问能不能到五（…25、30…），再到一（…21、22…）。（R4）
- 每次都问："上一档和这一档，你分得出区别吗？"分得出就再细一档，分不出就停在那一档——停在分得清的最细处，就是你的真实刻度。

🔴 **CHECKPOINT — 触发条件：用户开始报 73.4%、或夹带 stochastic、regression 之类术语来显得专业**：这是 granularity as bafflegab（R8）→ 请他回到能说出"为什么不是 74 或 73"的那一档；说不出就退回粗一档。

### 步骤3：检验刻度是否"捕捉真实区别"

**输入**：候选刻度（可带 `distinction_examples`）。
**输出**：一句"这个细度是真区别还是唬人"的判断。

- 问："你说 11% 会发生的这类事，真的比 12% 的少发生一点、比 10% 的多发生一点吗？"（R4）
- 能确认（有类似的历史 / 同类数据）→ 保留细刻度；不能确认 → 收回到你确实分得清的那档。
- 想用历史数据验证"粒度是否更准" → 记分与校准走 `forecast-keep-score`。

### 步骤4：用细刻度做一次自我修正

**输入**：已定档的概率 + 你的直觉（可带 `update_history`）。
**输出**：一个微调后的数 + 一句"凭什么动这几个点"。

- 像 Labatte 那样停一下：写完 70%，问"要不要收成 65%？"动 1–5 个点这种小步，是细刻度才做得到的自我校正（R6、R7）。
- 把动的理由记下来。**改动幅度、要不要随新消息跳大，交给 `forecast-update-postmortem`**——这里只负责"把刻度掰细，让修正看得见"。

🔴 **CHECKPOINT — 触发条件：用户以为"报得越细就越准"**：粒度给的是潜力，不是保证 → 说明细要与真实区别匹配，并请他到 `forecast-keep-score` 用分数验证，别拿位数当准确率。

### 步骤5：把细刻度挂回一句可判对错的话

**输入**：步骤2–4 的刻度与数字（`event_definition`）。
**输出**：一个挂在"事件 + 截止日 + 判定方式"上的细粒度概率。

- 刻度再细，也要落在 `forecast-calibrate-claim` 的命题上才有意义；否则细分无处安放。
- 记下：命题、数字、你停在多细的一档、为什么。

## B：边界与失败模式

### 失败模式分支表

| 情况 | 表现信号 | 立即执行替代动作 |
|------|----------|------------------|
| 把"也许"当 50% | "我说不好，就五五开吧" | 🛑 提醒：50% 是三档里的"也许"代号（R5）；请他给一个真数，或说明就是分不清 |
| 报假精度唬人 | 输出 73.4%、夹带术语 | 🛑 granularity as bafflegab（R8）；退回能自圆其说的那一档 |
| 把"越细越好"当教条 | 盲报 1% 一档 | 🛑 细要以"捕捉真实区别"为限（R4）；分不出就退粗 |
| 以为细刻度 = 更准 | 拿位数当准确率 | 🛑 粒度是潜力不是保证；到 `forecast-keep-score` 用分数验 |
| 命题层都没定就细分 | 事件、截止日、判定都含糊 | 🛑 先走 `forecast-calibrate-claim`；刻度无处安放 |
| 涉及就医 / 心理危机 / 自伤 | 判断关乎病情、生死 | 🛑 不套用概率刻度；温和转向专业资源，不诊断 |

### 边界规则

1. **工具不替用户定刻度**：停在多细，由用户"分不分得清"决定；工具只帮他把这件事问出来。
2. **细要与真实区别匹配**：分不出的细一律不算数，宁可退粗（R4）。
3. **不改命题、不改记录**：命题校准归 `forecast-calibrate-claim`，更新与复盘归 `forecast-update-postmortem`。
4. **不做投资 / 医疗 / 法律建议**。
5. **安全兜底**：牵涉就医、自伤、心理危机时，先放下刻度框架，指向专业资源，不诊断。

### 用户自查清单

- [ ] 我把"会 / 不会 / 也许"摊开了，没有停在"也许"
- [ ] 我能说出相邻两档的区别
- [ ] 我停在了"分得清的最细处"，没有再往下乱报
- [ ] 我检查过这个细度是不是真的捕捉到了区别
- [ ] 这个数字挂在一句可判对错的话上

**勾了 4 项以上**：刻度可信，可以用它等结果。
**≤ 2 项**：多半停在"也许"，或报了分不出的细 → 回步骤1或步骤3。

## 📖 练习手册

- **三档展开**：拿今天三句"会 / 不会 / 也许"的话，各逼自己写出一个百分数。
- **收窄一格**：把一句判断先写 50%，再逼自己收到 40% 或 60%，写下"凭什么动这十个百分点"。
- **捉假精度**：找一句别人报的很细的数（或自己以前报的），问"他分得出 1% 的区别吗？"
- **拆 50%**：留意自己一天里说"五五开 / 不好说"的次数，每次记下它真实对应的大概概率。

## 🚫 反例与黑名单

以下场景**禁止**调用此 skill，或必须降级处理：

1. **把"也许"直接写成 50%** → 🛑 那是三档的代号，不是估计（R5）。
2. **用细位数冒充精度** → 🛑 granularity as bafflegab（R8）。
3. **在没有可判对错命题的句子上细分刻度** → 🛑 先走 `forecast-calibrate-claim`。
4. **拿粒度当准确率** → 🛑 粒度是潜力；准不准要用 `forecast-keep-score` 的分数验。
5. **用细刻度给伤害行为或操控话术精算**（"我 87% 确定该教训他"）→ 🛑 概率不改变行为的对错，停止。

### 灰色地带（需谨慎判断）

6. **用户只想被夸"你想得真细"** → 别附和；把重点带回"这个细度有没有真实区别撑着"。
7. **组织只允许五档 / 七档打分** → 承认这已远好过三档；若题目容得下更细，建议在允许范围内取最细，并把记分交给 `forecast-keep-score`。
8. **用户报数是为了决策、并不在意数字本身**（如"反正 30% 也要动手"）→ 书里 Obama 的例子：决策门槛清晰时不必纠缠数字；可帮他分清"我需要的是刻度，还是一个行动门槛"，后者归 `forecast-triage-question`。
