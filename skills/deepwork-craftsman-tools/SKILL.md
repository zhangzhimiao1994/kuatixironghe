---
name: deepwork-craftsman-tools
description: 社交/工作工具的取舍（逐工具算账）。当用户说"我该不该卸载某个 App""我刷某个 App 停不下来但又觉得有用""社交媒体到底该不该用""我是不是离不开 XX"时使用。按你最重要的 2–3 项关键活动，给某个工具逐项打 +/0/－，用书里那套固定口径算总分并念出结论；若还犹豫就加一个 30 天退出实验。不劝人当卢德分子，也不做戒网式的道德评判。若被评的是退不掉的娱乐型站点、要的是"有质量的休闲替代"，走 deepwork-quality-leisure。
input_schema:
  required: [tool_name, life_goals, key_activities]
  optional: [domain, current_usage, quit_experiment_allowed]
output_schema:
  primary: {scored_matrix, verdict, spoken_conclusion}
  secondary: [thirty_day_test, next_tool_to_review]
---

# 网络工具取舍：按关键活动逐项打分，念出留还是走

**来源**：《Deep Work》Rule #3: Quit Social Media（工具取舍部分；子策略 *Don't Use the Internet to Entertain Yourself* 已拆出为 deepwork-quality-leisure） | 证据等级：firsthand

## 触发条件

**应该触发**：
- "我该不该卸载某个 App？"
- "我刷某 App 停不下来，可又觉得里面有用。"
- "社交媒体到底该不该用？我总怕错过什么。"
- "我是不是离不开某个工具？"
- "有人说不刷就落伍，可我一刷就半天。"

**不应触发**：
- 用户要选深度工作的排程方式（走 deepwork-depth-philosophy）
- 用户要练专注时长（走 deepwork-embrace-boredom）
- 用户要处理浅层工作太多、下班关不掉（走 deepwork-shallow-shutdown）
- 用户要给退不掉的娱乐型站点（资讯/短视频）找有质量的休闲替代、或管理下班后被娱乐拉走（走 deepwork-quality-leisure）
- 用户要戒断的是成瘾行为、或工具有工作硬性要求（如公司指定通讯工具）→ 前者指向专业帮助，后者不套用本 skill

## R：原文锚点

> "The Any-Benefit Approach to Network Tool Selection: You're justified in using a network tool if you can identify any possible benefit to its use, or anything you might possibly miss out on if you don't use it."（Rule #3, *Quit Social Media*）（已据原文核）

> "The Craftsman Approach to Tool Selection: Identify the core factors that determine success and happiness in your professional and personal life. Adopt a tool only if its positive impacts on these factors substantially outweigh its negative impacts."（Rule #3, *Quit Social Media*）（已据原文核）

> "The Law of the Vital Few*: In many settings, 80 percent of a given effect is due to just 20 percent of the possible causes."（Rule #3, *Apply the Law of the Vital Few to Your Internet Habits*）（已据原文核）

> "For each such tool, go through the key activities you identified and ask whether the use of the tool has a substantially positive impact, a substantially negative impact, or little impact on your regular and successful participation in the activity... Keep using this tool only if you concluded that it has substantial positive impacts and that these outweigh the negative impacts."（Rule #3, *Apply the Law of the Vital Few to Your Internet Habits*）（已据原文核）

## I：核心解释

1. **默认的决策方式是"any-benefit"**：只要能想到一个好处，或"万一错过什么"，就把它留下了。书里说这种口径忽略了工具的**全部负面**——而这些工具是"engineered to be addictive"，会从你的时间与注意力里偷走深度工作。
2. **换成"craftsman"口径**：先定你职业与个人生活里真正决定成败幸福的核心因素，工具只有在这些因素上"substantially outweigh"负面时才采用。书里类比摘樱桃的农民 Pritchard——他不会因为"捆草机有好处"就买，而是先定"土壤肥力是我的基线"，再算机会成本。
3. **用二八律把关键活动压到 2–3 项**：每个目标下只保留最重要的两三项活动，因为所有活动都消耗同一份有限的时间与注意力，是**零和**的。书里说这不是武断，是把 20% 的决定性活动挑出来。
4. **关键活动要"能想象得出、又不绑到一次性结果"**：书里的范例是 "regularly read and understand the cutting-edge results in my field"——"do better research" 太空，"投中某某会议那篇论文" 太具体，都不合格。
5. **结论因人生阶段不同**：同样是 Facebook，对要"维持既有友谊"的人应放弃，对要"建立新关系"的大学新生、或驻外军人则应保留——因为关键活动不一样。本 skill 给的是算法，不是"某 App 一律该删"的结论。
6. **打分不能凭感觉**：要对着关键活动逐项标 +/0/－，再用**固定口径**汇总并念出结论。若打分后仍犹豫，就用书里的 **30 天退出实验**来实测（不注销、不宣布，30 天后问两个问题）。

## A1：来源应用 — 书里那套工具评估法

**三步评估（照书）**：
1. 列出你职业与个人生活里为数不多的高层目标（如"做个好老师/好导师""做好研究""好好经营家庭"）。太具体的目标（"今年挣到一百万""一年发六篇论文"）不合格。
2. 每个目标下列出最重要的 **2–3 项关键活动**——书里的标准是：具体到能清楚想象出自己在做它，同时又不绑到某一次性的结果。
3. 对你正在用的每个网络工具，逐一问它对该活动是 **substantially positive / substantially negative / little impact**；**只有"substantial positive impacts... outweigh the negative impacts"才保留**。

**书里的两个范本**：
- Michael Lewis（职业目标：写改变读者看世界方式的叙事故事）→ 关键活动 "Research patiently and deeply." "Write carefully and with purpose." → Twitter 在这两项上 "at worst could be substantially negative" → 不用。
- Facebook + 社交目标（"维持与我重要之人的亲密友谊"）→ 关键活动是"定期做有意义的连接""为重要的人付出"，两者都离线且费力 → Facebook 的好处够不上 → 该放弃。但大学新生（关键活动是"多参加活动、和很多人社交"）与驻外军人（关键活动是"和远方的亲友保持轻量联系"）→ 结论相反，该用。

**辅助实验（30 天打包派对）**：把所有社交服务停用 30 天——不注销、**不宣布**；30 天后对每个服务问两个问题：
> "Would the last thirty days have been notably better if I had been able to use this service?"
> "Did people care that I wasn't using this service?"
两个都答"no" → 永久退出；两个都明确"yes" → 恢复使用；含糊 → 书里的建议是倾向退出（以后还能再回）。

**娱乐型站点（资讯/短视频）不在本 skill 范围**：书里说这类站点"not something you join"、退不掉，处理它们的"有质量休闲替代"已拆到 deepwork-quality-leisure。

## A2：典型触发场景

- 纠结要不要卸载某个社交/短视频 App，卸载又装回来。
- 总觉得"不刷就错过什么"，但刷完又空虚。
- 想给媒体消费定个边界，不知道从哪入手。
- 想用"某个工具对我的真实目标到底有没有用"来决策，而不是凭内疚感。

## E：执行步骤

### 步骤1：列出目标与关键活动

**输入**：用户的职业与个人生活目标。
**输出**：少量高层目标 + 每个目标下 2–3 项关键活动（能想象得出、不绑一次性结果）。

🔴 **CHECKPOINT — 触发条件：用户列出的"关键活动"太空（"提升自己""多学习"）或太细（"这周把那份报告交了"）**：按书里标准打回重写。给对照：合格的是 "regularly read and understand the cutting-edge results in my field" 这类——具体到能想象、又不绑到一次性结果。

### 步骤2：对某个工具逐项打分

**输入**：具体的一个工具（一次只评一个）+ 步骤1 的关键活动。
**输出**：一张打分表——每项关键活动标 **＋ / 0 / －**（分别对应 substantially positive / little impact / substantially negative）。

按书里的措辞逼问："用它，会让你**显著更好**地持续做这项活动吗？还是显著更糟？还是没有实质影响？" 别停在"有点用"。

🔴 **CHECKPOINT — 触发条件：用户给出的理由是"能娱乐/能认识人/能看看别人在干嘛"这类泛泛的好处**：这正是书里点名的 any-benefit 思维。回应："书里说这些好处'minor and somewhat random'——它们确实存在，但关键问题是它有没有**显著**影响你最重要的那几项活动。"

### 步骤3：用固定口径汇总，并念出结果

**输入**：步骤2 的打分表。
**输出**：一句**念出来**的结论（保留 / 放弃）+ 一句理由。

**固定汇总口径（照书里那句"substantial positive impacts... outweigh the negative impacts"；下面的等权折算为补充）**：
- 计分：**＋ = +2，0 = 0，－ = －2**（补充：书里未给数字，此为等权折算，只为把口径固定下来）。
- 判定（照书里口径）：**只有当该工具至少产生一项 ＋，且所有 ＋ 之和严格大于所有 － 之和时，才保留（即书里说的 positive impacts 要"substantially outweigh"负面）。** 其余情况——全是 0、有 － 而没有足够 ＋、或 ＋ 与 － 打平——一律放弃。
- 全书口径的直觉：书里 Facebook 的例子就是"好处都落在关键活动之外 = 全是 0 = 该放弃"。

**念出结果的模板（必须用一句话说出来）**：
> "在关键活动 A/B/C 上，工具 X 得到 [＋/0/－、＋/0/－、＋/0/－]；因为它的正影响没有实质性盖过负影响，结论是**放弃 X**／当且仅当它有实质性正影响且盖过负面时，才**保留 X**。"

### 步骤4：还犹豫就上 30 天实验

**输入**：步骤3 结论模糊，或用户不信结论。
**输出**：一个 30 天退出实验的安排 + 两个复盘问题。

照书里：停用 30 天，不注销、不宣布；30 天后问 "Would the last thirty days have been notably better if I had been able to use this service?" 和 "Did people care that I wasn't using this service?"。

🔴 **CHECKPOINT — 触发条件：用户想发一条"我要退网 30 天"的动态**：拦住。书里明确要求**不要宣布**——否则"人们想听我说"这种错觉会污染实验结果，你就测不出别人是不是真的在意。

## B：边界与失败模式

### 失败模式分支表

| 情况 | 表现 | 怎么处理 |
|------|------|---------|
| 打分变成道德审判 | 用户一边打分一边自责"我太堕落了" | 拉回口径：这是算账，不是悔过。书里的框架是中性的，只问影不影响关键活动。 |
| 关键活动列成愿望清单 | 列了十几项、每项都"重要" | 回到二八律：每个目标只留 2–3 项；零和，多的会稀释。 |
| 用 any-benefit 反悔 | "可万一错过重要信息呢？" | 这正是 any-benefit 的经典表现；按书里回应——那是"minor and somewhat random"的好处，问题是有没有**显著**影响关键活动。 |
| 被评工具是工作硬性要求 | 公司指定通讯工具，没法退出 | 不套用"退出"结论；只评估它挤占深度时间的部分，转 deepwork-shallow-shutdown 定上限。 |
| 成瘾/自伤关联 | 刷到影响睡眠、情绪、或出现自伤念头 | 🛑 停止评估，指向专业帮助。 |

### 边界规则

1. **不做道德评判**：不评价"该不该用社交软件"，也不给"戒网光荣/不戒就堕落"的腔调。书里的立场是：这不是善恶问题，是成本收益的账。
2. **一次只评一个工具**：连着评一堆会互相污染，也让人疲劳。
3. **口径固定**：汇总必须用上面写死的规则，不许临时改门槛去迁就用户的偏好。
4. **不劝人当卢德分子**：书里明说这些工具"not inherently evil"，有的可能很关键；本 skill 只做筛选。
5. **安全兜底**：若涉及成瘾影响生活、睡眠、情绪，或有自伤念头，指向专业资源（心理援助热线 12356；紧急情况拨 120/110），不做诊断。

### 用户自查清单

- [ ] 我有少量**高层目标**，每个目标下只有 **2–3 项关键活动**
- [ ] 我的关键活动**能想象得出、又不绑一次性结果**
- [ ] 我对这个工具**逐项打了 ＋/0/－**，不是凭整体感觉
- [ ] 我用**固定口径**算过，并**把结论说出口**了
- [ ] 若还有疑虑，我有**30 天退出实验**可上

**勾选 4+ 项**：取舍到位。**≤2 项**：多半是没把关键活动收紧到 2–3 项，回步骤1。

## 📖 练习手册

这周只评**一个**工具：写下一个高层目标 + 两三项关键活动，对它逐项打 ＋/0/－，用固定口径算完，**把结论念出来**。下周再评下一个（练习记录保存在用户批准的位置）。

## 🚫 反例与黑名单

1. **把结论强加给用户**（"所有人都该删掉某 App"）→ 书里明说结论因人而异（学生 vs 驻外军人），只给算法。
2. **用"错过焦虑"当保留理由** → 这就是 any-benefit；回到"有没有**显著**影响关键活动"。
3. **边评估边自责** → 不做道德审判；这是算账。
4. **用本 skill 要求他人**（去劝家人朋友退网）→ 只用于自己；评估是私人账本。
5. **把工作必需的工具当社交工具评** → 不套用"退出"；改用 shallow-shutdown 定上限。

### 灰色地带（需谨慎判断）

6. **用户靠某平台吃饭**（自媒体创作者、销售）→ "发布/获客"可能确实是关键活动；照书里对不太出名的作者的分析——把"营销"当作目标、再问 2–3 项活动里是否包含它，而不是默认保留或默认退出。
7. **用户只是想要一个"少刷点"的通则** → 本 skill 给的是逐工具算账，不是通用时长上限；要上限请走 deepwork-shallow-shutdown。
8. **用户真的想彻底退网**（受 Baratunde Thurston 故事启发）→ 书里说那是"overstuffed straw man"，不可行；引导回"中层道路"：不劝退、只筛选，一次评一个工具。
