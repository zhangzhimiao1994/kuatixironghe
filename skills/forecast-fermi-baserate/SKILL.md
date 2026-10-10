---
name: forecast-fermi-baserate
description: 从零估一个概率，把"能不能按时完成""会不会发生"拆成可算的部件。当用户要一个没有现成数据的估计——"这项目几月能交付""他会不会答应""这事几成会成"——却要么凭感觉报数、要么觉得无从下手时使用：先拆开看 → 找同类情况一般多少（基准率 / 外部视角）→ 按本案加减（内部视角）→ 换一种算法核对。
input_schema:
  required: [question, case_details, target_date_or_threshold]
  optional: [comparable_cases, base_rate_source, alternative_decomposition]
output_schema:
  primary: {decomposition: string, base_rate: string, adjusted_estimate: string}
  secondary: [alternative_estimate, check_questions, uncertainty_range]
---

# 拆开再估：从"说不准"到一个有根据的概率

**来源**：《Superforecasting》第5章「Supersmart?」（FERMI-IZE / OUTSIDE FIRST / THE INSIDE VIEW / THESIS, ANTITHESIS, SYNTHESIS）、第12章「What's Next?」（Ten Commandments 第2、3 条） | 证据等级：firsthand

## 触发条件

**应该触发**：
- 用户要把一个"能不能 / 会不会"变成概率或时间估计："这活儿几天能干完""他会不会来""这事几成能成"
- 用户面对没有现成数据的问题，要么凭感觉报数，要么觉得无从下手
- 用户已经有一个直觉数字，想检验它靠不靠谱
- 工期 / 交付类问题："在 X 日之前完成的把握有多大"
- 用户想给一个判断找"同类情况一般怎样"的参照

**不应触发**：
- 说法本身还含糊、没有事件、没有截止日 → 先走 `forecast-calibrate-claim`
- 只需更新一个已经估好的预测 → `forecast-update-postmortem`
- 有现成权威统计可直接查（如"明天日出几点"）→ 直接查，别做费米估计
- 纯算术题（输入齐全，只差计算）→ 直接算
- 用户在把"精确概率"当事实证明，或要工具替他拍板 → 先纠正（见 B 节）

## R：原文锚点

> "Fermi knew people could do much better and the key was to break down the question with more questions like 'What would have to be true for this to happen?'"（第5章 FERMI-IZE）（已据原文核）

> "What Fermi understood is that by breaking down the question, we can better separate the knowable and the unknowable. So guessing—pulling a number out of the black box—isn't eliminated. But we have brought our guessing process out into the light of day where we can inspect it. And the net result tends to be a more accurate estimate than whatever number happened to pop out of the black box when we first read the question."（第5章 FERMI-IZE）（已据原文核）

> "Statisticians call that the base rate—how common something is within a broader class. Daniel Kahneman has a much more evocative visual term for it. He calls it the 'outside view'—in contrast to the 'inside view,' which is the specifics of the particular case."（第5章 OUTSIDE FIRST）（已据原文核）

> "When we make estimates, we tend to start with some number and adjust. The number we start with is called the anchor. It's important because we typically underadjust, which means a bad anchor can easily produce a bad estimate."（第5章 OUTSIDE FIRST）（已据原文核）

> "He knows about the planning fallacy: when bosses ask employees how long it will take to finish a project, employees tend to underestimate the time they need, often by factors of two or three."（第12章 Ten Commandments 第3条）（已据原文核）

> "Superforecasters know that there is nothing new under the sun. Nothing is 100% 'unique.' Language purists be damned: uniqueness is a matter of degree."（第12章 Ten Commandments 第3条）（已据原文核）

## I：核心解释

1. **把猜测摆到台面上**：费米估计并不消灭"猜"，它只是把原来闷在黑箱里的一口价，拆成几个能逐个检查的猜测。结果是估计反而更准。（R1、R2）
2. **拆问法**：反复问"要答案为真，必须先有什么？"——把一个答不出的问题，换成几个答得出、至少猜得出的小问题。（R1）
3. **外部视角先行**：先问"同类事情一般多久、多常发生"，这就是基准率。别一上来就钻本案的细节。（R3）
4. **为什么必须先外部**：锚定效应——人会从某个起始数往上调，而且**总是调不够**；起始数是坏的，估计就坏。先落一个有意义的外部视角，等于给了一个好锚。（R4）
5. **别信"我这事儿独一无二"**：人的本能是觉得本案特殊。先接受"它属于某一类"，再讨论它在类里偏哪边。（R6）
6. **工期问题的通病是规划谬误**：员工估工期常常低估到"两三倍"的地步，这是有统计规律的偏向，不是个别失误。（R5）
7. **两个视角要合成，不是二选一**：外部视角给起点，内部视角做加减；两边弄完，再换一种算法或换一个类比类别核对一遍。（第5章 THESIS, ANTITHESIS, SYNTHESIS）
8. **估出来的仍是估计**：再细的数字也只是主观判断，不是客观事实（呼应第3章：数字"只表达估计、意见，仅此而已"）。所以结论是给用户参照，不替他拍板。

## A1：来源应用 — 书里的三个拆解示范

1. **钢琴调音师（费米原题）**：不直接猜"芝加哥有多少个调音师"，而拆成——① 芝加哥有多少钢琴（人口 × 有钢琴的比例 + 机构钢琴）；② 一年调几次；③ 一次调多久；④ 一个调音师一年工作多少小时。每个都是一口可检查的粗猜，算出来是 63 个（黄页找得到的是 83 条，含重复）。

2. **阿拉法特的钋（Bill Flack）**：问题问的是"法/瑞的检验会不会测出钋"，而不是"以色列有没有下毒"——后者是 System 1 偷偷把难问题换成易问题。Fermi 化之后，先问"要答案为真需要什么"：钋衰变得快，得先确认死亡多年后还能测出来；再列出多条"能测出钋"的路径（以色列、巴勒斯坦对手、死后污染），每条路径都抬高一点概率。找不到基准率时他用范围法：这类案子至少有 20%，又不可能到 80%，取中点 50% 当起点。

3. **欧洲恐袭（David Rogg）**：先上外部视角——数过去五年同类国家里发生过的袭击次数（6 次），算出基准率 1.2 次/年；再用内部视角看 ISIS 崛起与安保升级两个反向因素，把基准率调到 1.8 次/年；最后按 69 天占比折算，得到 34%。

书里给 Fermi 化列出的四步骨架：**分解问题 → 把未知摆出来、检查假设 → 敢猜（最好的粗估）→ 明确区分可知与不可知**。作者的原话是"Better to discover errors quickly than to hide them behind vague verbiage."

## A2：典型触发场景

- "这个开发任务三天能做完吗？"（工期 → 转成"X 日前完成的概率"）
- "我投的简历会有人回吗？"
- "他会答应我的请求吗？"
- "今年这行业会不会裁员？"
- "我想在某个日期前攒够一笔钱，有多大把握？"

## E：执行步骤

### 步骤1：拆开问题，写下"要答案为真，必须先有什么"

**输入**：待估的问题（`question`）+ 目标日期/阈值（`target_date_or_threshold`）。
**输出**：一张分解清单——3-6 个可分别估的小量，或若干条"要答案为真必须成立的条件"。

- 用费米问法：要它是"是"，先得发生什么？要它是"否"，又得发生什么？
- 对工期类问题，拆成：范围有多大、我实际能投入多少、中间要等的东西有哪些。
- 划清"已知 / 未知"：哪些能查到、哪些只能猜。

🔴 **CHECKPOINT — 触发条件：问题里的事件或时间点仍然含糊（"顺利的话""看情况"）**：命题没成型 → **转 `forecast-calibrate-claim`**，先把事件和截止日钉死，再回来估。

### 步骤2：找基准率（外部视角）

**输入**：步骤1 的分解清单。
**输出**：一个"同类情况一般多少 / 多久"的基准数字，并注明它的来源。

- 先问："这类事情，一般情况下发生率 / 用时是多少？"能查就查（历史频率、行业常态、以往类似项目）。
- 找不到直接数据时，用最接近的类比类别，并说明假设——像 Bill Flack 那样先框定"至少 20%、至多 80%"。

🔴 **CHECKPOINT — 触发条件：用户说"我这情况太特殊，没有同类可比"**：别让他跳过外部视角（R6）。帮他把"特殊"降一档，找一个更宽的类（"找不到一模一样的项目，那同类中型项目呢？"）。若真的一档都找不到 → 回到"最宽的那一类"，用范围法给上下界，取中点，并标注这只是个粗锚。

### 步骤3：内部视角做加减

**输入**：步骤2 的基准率 + 本案细节（`case_details`）。
**输出**：在基准率基础上上调或下调后的估计，并写明每个加减的理由。

- 逐条比对：本案有哪些因素让它比同类更容易 / 更难发生？各动多少？
- 提醒锚定：起始数是基准率，往上/往下调时，人容易调不够，逼自己问一句"是不是调得太保守了？"
- 工期类问题默认对方（包括自己）会低估，先按 R5 的偏向调高再缩范围。

🔴 **CHECKPOINT — 触发条件：调整幅度几乎全靠一个生动的故事或一种情绪（"我觉得这次不一样，因为……"）**：这可能是被"内部视角的故事"带跑 → 让他先听完外部视角，再决定这个故事值几分；故事不能独自决定幅度。

### 步骤4：合成两视角 + 换一种算法核对

**输入**：步骤2、步骤3 的结果。
**输出**：一个合成后的估计（区间或点估计）+ 一次换了算法的复核结果。

- 像 David Rogg 那样把外部基准和内部调整乘到一起，得到一个数。
- 再换一条路算一遍（换类比类别、换单位、从上往下拆 vs 从下往上乘）。两个结果差得远，说明有假设没交代清楚——回到分解找分歧，而不是把两个数一平均了事。
- 最后明确：这个数是给用户的参照，最终概率仍由用户自己认定。

## B：边界与失败模式

### 失败模式分支表

| 情况 | 表现信号 | 立即执行替代动作 |
|------|----------|------------------|
| 要一个"准数" | "你就告诉我几成，别给区间" | 🛑 说明这是估计不是事实；最多给一个好的点估计 + 区间，并说清假设。 |
| 跳过外部视角 | 用户直奔本案细节、讲一长串故事 | 🛑 拉回来："先看同类情况一般怎样，再谈你这个特殊的。"（R3、R4） |
| 找不到基准率就放弃 | "没有数据，估不了" | 🛑 用最宽的类比类别 + 范围法（上下界取中点），标注是粗锚。 |
| 把小数当精确 | 输出 37.4% 这类假精度 | 🛑 收敛到合理粒度；说明细数字只是让思考更清楚，不代表更准。 |
| 涉及就医 / 自伤 / 危机 | 命题关于病情、生死、"还撑不撑得住" | 🛑 不套用概率估计。转向人的支持与专业资源，不诊断。 |

### 边界规则

1. **工具只做拆解与参照，不替用户拍板**：结论的概率由用户认定（补充：把书里"数字只是估计"的立场落成操作）。
2. **不做投资 / 医疗 / 法律建议**：只帮把估计做得更有根据。
3. **每个猜测都要能检查**：任何一个蹦出来的数字，问它从哪来；答不出就标成"黑箱猜测"，别伪装成有依据。
4. **粒度匹配真实区别**：分得越细不见得越好，只在真有区别的地方细分。
5. **安全兜底**：牵涉就医、自伤、心理危机时，放下估计框架，指向专业资源，不诊断。

### 用户自查清单

- [ ] 我把大问题拆成了几个能分别估的小问题
- [ ] 我有一个外部视角（同类情况一般多少 / 多久）
- [ ] 我写下了在基准率上加减的每一条理由
- [ ] 我换了一种算法或类比类别核对过
- [ ] 我清楚这个数字是估计，不是事实

**勾了 4 项以上**：估计有根据，可用。
**≤ 2 项**：多半漏了外部视角或没做复核 → 回步骤2或步骤4。

## 📖 练习手册（放在用户批准的位置）

- **费米热身**：估算"本市有多少家咖啡馆"或"你公司一年用掉多少张 A4 纸"，拆成 3-4 个小量逐一粗估。
- **工期校准**：回想你最近三个"以为几天能做完"的任务，写下实际用了多久，看看你的个人低估倍数。
- **找基准率**：挑一个你关心的"会不会"问题，专门去找它的基准率，先只写外部视角那句结论。
- **换算法核对**：同一个概率，用两种完全不同的分解各算一次，比较差多少、差在哪。

## 🚫 反例与黑名单

以下场景**禁止**调用此 skill，或必须降级处理：

1. **把估计当成"准确概率"来报** → 🛑 任何数字都只是主观估计。工具不得宣称某数字正确，也不得替用户认定最终概率。
2. **没有截止日 / 没有事件就开始估** → 🛑 先走 `forecast-calibrate-claim`。
3. **用本 skill 给医疗、法律、投资做保证** → 🛑 越界。
4. **拿假精度唬人**（"73.2% 的概率"）→ 🛑 书里称之为"granularity as bafflegab"，退回合理粒度。
5. **在危机 / 就医语境里做概率游戏** → 🛑 停，转专业资源。

### 灰色地带（需谨慎判断）

6. **用户想直接抄一个网上的基准率** → 可以，但要问它是不是"同类情况"，不是就直接搬一个不匹配的类（书里 Peggy Noonan 就是把"总统离任后支持率回升"这个常态看成了惊人信号）。
7. **用户的目标是给决定壮胆或劝退自己** → 分清"他想估概率"还是"他想找理由"。若是后者，先说明估计不是用来站队的。
8. **占卜 / 星盘给的"倾向"需要被估** → 可以把它当待验证命题来分解，但不因来源而调整估计，也不背书其有效性。
