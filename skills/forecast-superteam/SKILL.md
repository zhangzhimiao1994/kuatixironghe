---
name: forecast-superteam
description: 组织一队人一起做判断/预测——先各自独立估、再防 groupthink、用精确提问与 premortem 拆解、靠视角多样把群体智慧放大。当用户说"我们几个人要一起估一个事""一开会大家都很客气没人反对""一讨论就吵起来""问了一圈人还不如我一个人想的""怎么避免一个人的声音盖过全场"时使用：独立加总 → 精确提问 → premortem → 查多样性 → 养分享文化。
input_schema:
  required: [question, members, decision_stakes]
  optional: [shared_info_state, meeting_format, leader_present]
output_schema:
  primary: {independent_pool: string, precision_questions: string, premortem: string}
  secondary: [diversity_check, aggregation_note, culture_actions]
---

# 组一支超级预测团队：把独立判断、多样视角与建设性对质合起来

**来源**：《Superforecasting》第9章「Superteams」（TO TEAM OR NOT TO TEAM? / SUPERTEAMS）+ 附录「Ten Commandments for Aspiring Superforecasters」第9条 | 证据等级：firsthand

## 触发条件

**应该触发**：
- 用户要一队人一起做预测/判断/评估："我们几个人得一起估这个事到底成不成"
- 团队"很和谐但没人反对"，或反过来"一讨论就吵成一团"
- 用户问怎么把不同人的长处聚起来、别让嗓门大或头衔高的人定了调
- 要做一次重大决定，想先做 premortem、想防 groupthink
- 用户抱怨"问了一圈人，结论还不如我一个人想的"
- 线上小组彼此陌生，想提问又怕得罪人

**不应触发**：
- 只是一个人做一次估计 → 走 `forecast-fermi-baserate`
- 命题还含糊、没有事件与截止日 → 先走 `forecast-calibrate-claim`
- 只是给已有预测做更新 → `forecast-update-postmortem`
- 领导要在"准确"与"士气/执行"之间做取舍、或要建组织文化 → `forecast-leader-culture`
- 要给预测打分、比较谁更准 → `forecast-keep-score`
- 纯事实查询或算术 → 直接做

## R：原文锚点

> "Teams can cause terrible mistakes. They can also sharpen judgment and accomplish together what cannot be done alone."（第9章 Superteams 章首）（已据原文核）

> "When people gather and discuss in a group, independence of thought and expression can be lost."（第9章 TO TEAM OR NOT TO TEAM?）（已据原文核）

> "Pointed questions are as essential to a team as vitamins are to a human body."（第9章 TO TEAM OR NOT TO TEAM?）（已据原文核）

> "Practice “constructive confrontation,” to use the phrase of Andy Grove, the former CEO of Intel."（第9章 TO TEAM OR NOT TO TEAM?）（已据原文核）

> "There’s also the “premortem,” in which the team is told to assume a course of action has failed and to explain why—which makes team members feel safe to express doubts they may have about the leader’s plan."（第9章 SUPERTEAMS）（已据原文核）

> "It is the diversity of the perspectives that makes the magic work."（第9章 SUPERTEAMS）（已据原文核）

> "At the end of the year, the results were unequivocal: on average, teams were 23% more accurate than individuals."（第9章 SUPERTEAMS）（已据原文核）

> "Master the fine arts of team management, especially perspective taking (understanding the arguments of the other side so well that you can reproduce them to the other’s satisfaction), precision questioning (helping others to clarify their arguments so they are not misunderstood), and constructive confrontation (learning to disagree without being disagreeable)."（附录 Ten Commandments 第9条）（已据原文核）

## I：核心解释

1. **团队是双刃的**：能铸成大错（Bay of Pigs），也能把一个人做不到的判断做出来（古巴导弹危机）。看团队不能只看好或只看坏，两种可能同时存在。（R1）
2. **加总要奏效，前提是"独立"**：群体之所以准，是因为每人独立判断、误差方向随机、互相抵消（像猜牛重的人群）。一旦聚在一起讨论，独立判断与独立表达就可能丢失。（R2）
3. **独立性是怎么丢的**：一个人嗓门大、是霸凌者、口才好、或头衔吓人，就能让其他人放弃独立判断、买进错误——这时错误不是抵消，而是累积。这就是集体糊涂的根源（郁金香热、2005 年美国房市）。
4. **groupthink 的检验**：小团体会为了"团结合拍"而无意识地共享幻觉、压低批判性思考；于是"大家都同意"被默默当成"我们没错"。检验办法就是问：如果这个方案被登在《纽约时报》头版，我们还会照走吗？
5. **反 groupthink 不等于纵容火药味**：另一个极端是 rancor 与 dysfunction。要"disagree without being disagreeable"，即 constructive confrontation。精确提问是实现它的一种方式。（R3、R4）
6. **精确提问怎么问**：不要说"你真蠢"（加火不添光）、"我不这么认为"（只说不同意不说为什么）、"你什么意思"（太笼统）。要落到"你说的某个词指什么？""有什么证据、在什么时间跨度上？"——答案不一定定胜负，但把结论背后的思路摊开，可以被检验。（R3）
7. **premortem 的作用**：让团队先假定某个方案已经失败、解释为什么。因为"大家都觉得已经定了"，成员往往不敢质疑领导者的方案；premortem 给了他们一个安全出口。（R5）
8. **多样性胜过能力（diversity trumps ability）**：把不同视角加总才有魔法；相同视角只复制同样的东西，小变化只带来小改进。但它不是"能力 vs 多样性"的假二分——是调配两者的比例。（R6）
9. **团队不是个体的加总**：团队的开明程度（actively open-minded）是涌现属性，取决于成员间的沟通模式，而不只是每个人脑子里怎么想。互不关心的一群开明者，还不如一群爱抬杠但认真求真的偏执者。
10. **书里的实验数字**：平均而言团队比个人准 23%（R7）；逐年看，普通团队胜"群体智慧"约 10%，预测市场胜普通团队约 20%，而超级团队胜预测市场 15%–30%。这些是有边界（线上、不面对面、特定人群）的实验结果，不承诺复制。
11. **书给的三种"团队管理手艺"**：perspective taking（把对立面的论证理解到能向其本人复述并让他满意）、precision questioning、constructive confrontation。（R8）

## A1：来源应用 — 书里怎么组队与防 groupthink

1. **随机分组的对照实验**（第9章 TO TEAM OR NOT TO TEAM?）：几百人单干、几百人组队；团队不得面对面，用线上论坛、邮件、Skype。个人照常记分，团队分由成员分数汇总。目标只有准确，怎么做到随你。
2. **给团队的团队手册**：一边警告 groupthink——"合作但别顺从""共识不总是好、异议不总是坏""如果你确实同意，也别把'同意'本身当成你对了的证明""永远别停止怀疑""精确的问题对团队就像维生素对身体"；一边警告相反的极端——rancor 与 dysfunction，要"disagree without being disagreeable"。
3. **精确提问的对白示范**：书里想象用精确提问重演 Bay of Pigs 的撤退计划——"如果被攻击、计划崩了怎么办？""撤进 Escambray 山区与其他反卡斯特罗力量会合。""从落点到山区多远？""八十英里。""地形呢？""多半是沼泽与丛林。""所以游击队被打了、计划崩了、没有直升机也没有坦克，却要先徒步穿过八十英里沼泽丛林才能找掩体，对吗？"——作者说，这种对话不会以"sounds good"收尾。
4. **超级团队（第 2、3 年）**：每队约 12 人，仍不面对面。真实痛点不是不想问，而是怕冒犯：Elaine Rich 说有些问题"几乎成了禁忌"，Marty Rosenthal 说大家在"dancing around"（绕着说、措辞小心、盼着不用自己把话说出来）。转变靠经验：大家开始明确表态"看到我看不到的问题尽管 push back"，并对建设性批评致谢，"dancing around"才减少。
5. **没有正式领导时**：Marty 用"leading from behind"——以身作则，先把自己的预测写得非常详细并邀请评论，还组织电话会分工；反馈很好，团队承诺感上升。
6. **线上 vs 线下**：线上更容易忽略从没见过的人，也更容易升级冲突；但也更容易保持批判距离。书里第二次、第三次年会让团队线下见面（Wharton、Berkeley），以增加"人的维度"，帮助彼此更敢互相 push back。
7. **大方给予者（givers）**：书中引 Adam Grant 的 giver/matcher/taker。超级团队里 Doug Lorch 分享编程工具、Tim Minto 分享随时间自动微调预测的分析，带动其他人也分享；他们的个人分也是最好的。
8. **书里也明说别过度通用化**：单拎出人打上"超级"标签可能制造分裂；把人转进跨职能团队会造成扰动；结果不保证。还有例外——有的队并不互相支持却表现不错，有一位最好的预测者干脆拒绝给队友留评论，怕诱发 groupthink。

## A2：典型触发场景

- 团队做季度目标/项目评估，总是第一个发言的人定了调，其余人附和
- 领导要做重大决定，想组织一次"唱反调会"/premortem
- 线上小组做判断，彼此陌生，怕开口得罪人
- 一群人给同一个问题各报一个数，想合成一个更好的答案
- 招人/配组时纠结：该按能力挑，还是按视角多样挑

## E：执行步骤

### 步骤1：先各自独立判断，再开始讨论

**输入**：待判问题（`question`）+ 成员（`members`）。
**输出**：一份"成员 → 独立判断 + 理由"的清单，写好在讨论之前。

- 让每个人在不看别人答案的情况下给出自己的判断与一条理由。
- 讨论的目的是暴露彼此不知道的碎片信息，而不是互相说服。

🔴 **CHECKPOINT — 触发条件：有人已经听过别人的结论（或被头衔/嗓门镇住）**：让他补写"如果没听别人，我会怎么估"，并标注这条可能被锚定。加总只在判断独立时才奏效（R2），这一步是后面一切的前提。

### 步骤2：用精确提问拆解最含糊或最关键的一条主张

**输入**：步骤1 里最含糊、或对结论影响最大的那条主张。
**输出**：至少两个指向具体的追问（指什么？证据？时间跨度？）。

- 只针对主张本身提问，不做人身评价（"你真蠢""我不这么认为"都不算精确提问）。
- 被问的人若觉得被冒犯，先说明这是"求真的对质"而不是攻击，并在提问后就答案致谢。

🔴 **CHECKPOINT — 触发条件：提问变味成人身攻击，或团队开始"dancing around"**：把它改写成精确问题，或明确表态"看到我看不到的问题尽管 push back"——超级团队就是靠这句话把绕圈子降下来的。

### 步骤3：做一次 premortem

**输入**：当前倾向的方案/判断。
**输出**：每人独立写下的"如果它已经失败，原因是……"清单。

- 假定方案已失败，让每个人解释为什么——这让成员敢说出对领导者方案的疑虑（R5）。

🔴 **CHECKPOINT — 触发条件：领导在场导致大家不敢说**：让领导先离场或最后发言（书里 Kennedy 有时离开房间，让小组自由讨论；他也把自己的底线判断留着不说，以免主导讨论）。

### 步骤4：查多样性并合成

**输入**：各人独立判断、碎片信息、premortem 结果。
**输出**：一个合成结论 + 一句"我们的视角是否太同质"的判断。

- 加总不同的碎片信息：若把这些碎片摊开给每个人，他们各自的估计会往哪动？（书里 Abbottabad 的例子：把碎片补齐，群体估算可能从约 70% 升到 80%–85%。）
- 别把"能力 vs 多样性"当二选一，而是问"这个情境下两者怎么配"。

🔴 **CHECKPOINT — 触发条件：团队已经高度共享信息、或把多样性当标签排挤能人**：若信息已高度共享（像超级团队那样），"极端化加总"帮不上什么忙；若还在挑同质的人，补进不同视角。守回机制，不贴标签。

### 步骤5：养出归属感与分享文化

**输入**：团队当前的互动状态。
**输出**：一条"看到我漏掉的就 push back"的公开表态 + 一两个分享/拉近关系的动作。

- 定一条大家都同意的表态，并对建设性批评致谢。
- 适度的线下/更私人接触能增加"人的维度"，帮助彼此更敢 push back。
- 注意 freeload：书里说最好的团队工作量是分摊的，但承诺越强、投入越多；只读不写不分享是一份 temptation。

🔴 **CHECKPOINT — 触发条件：有人持续搭便车，或有人靠压服他人推进**：搭便车的用"分工 + 承诺"处理；靠压服的回到步骤2，把讨论拉回"针对主张"。

## B：边界与失败模式

### 失败模式分支表

| 情况 | 表现信号 | 立即执行替代动作 |
|------|----------|------------------|
| 团队太客气、不敢反对（groupthink） | "大家都同意，没人有异议" | 🛑 用精确提问与 premortem；让领导最后发言；明确"共识本身不是证明" |
| 团队变成火药桶（rancor） | 讨论人身化、互相攻击 | 🛑 转 constructive confrontation：只针对主张、精确提问、答完致谢 |
| 有人压场、被头衔镇住 | 一个人先发言，其余附和 | 🛑 先各自独立写下判断再讨论；把"独立"写回流程 |
| 只挑同质的人（视角复制） | 全组同一专业、同一信息源 | 🛑 引入不同视角；多样性不是弃能取多，而是调配比例 |
| 把群体智慧当自动售货机 | "人多自然准" | 🛑 加总只在判断独立、误差随机时奏效；讨论会破坏独立性 |
| premortem 变成批斗 / 多样性变成排挤 | 变成清算或政治站队 | 🛑 守回机制：先做失败复盘、再谈改进；多样性是调配不是标签 |
| 涉及就医 / 自伤 / 危机 | 议题关于生死、病情 | 🛑 放下团队方法，转专业资源，不诊断 |

### 边界规则

1. **工具只做组织与纠偏，不替用户拍板**：结论由团队与用户认定。
2. **独立性是前提**：任何"先统一思想再开始估"的做法都要先拆开。
3. **团队不是个体加总**：别把成员分数简单相加就当成团队判断，沟通模式才是关键。
4. **书里的效果数字有边界**：线上、不面对面、特定人群的实验结果，不承诺复制到任何团队。
5. **不做投资 / 医疗 / 法律建议**：只帮把群体判断做得更有根据。
6. **安全兜底**：牵涉就医、自伤、心理危机时放下团队方法，指向专业资源，不诊断。

### 用户自查清单

- [ ] 每个人在讨论前都独立给过判断
- [ ] 我们至少做了一次精确提问，而不是人身评价
- [ ] 我们做过 premortem（假定失败、解释为什么）
- [ ] 我们的成员视角不全是同一个模子
- [ ] 我们知道"共识本身不是证明"
- [ ] 有人敢说"看到我看不到的问题尽管 push back"，并且被致谢

**勾了 4 项以上**：团队判断有根据，可用。
**≤ 2 项**：多半只是"客气地附和"或"吵成一团" → 回步骤1或步骤2。

## 📖 练习手册

- **独立加总小实验**：让 5 个人先各自估同一个量、写下理由，看加总值离真实值多远；再让他们讨论后重估一次，比较两次的差。
- **premortem 演练**：选一个正在定的方案，先假定它已经失败，每人独立写三条原因，再一起看。
- **精确提问改写**：把"我不这么认为""你不对"各改写成两个指向具体的追问。
- **leading from behind 练习**：下次在小组里，先把你的推理写得非常详细并邀请评论，看会发生什么。

## 🚫 反例与黑名单

1. **把"求共识"当目标** → 🛑 这正是 groupthink：共识本身不是证明。
2. **用"人多"替代"独立"** → 🛑 讨论会破坏独立性，加总随之失效。
3. **让人身攻击、资历压场主导讨论** → 🛑 这会让人放弃独立判断、错误累积。
4. **把 premortem 做成批斗** → 🛑 它是让疑虑安全地流出来，不是清算。
5. **把"diversity trumps ability"读成"能力不重要"** → 🛑 书里已标明这是假二分，要调配比例。
6. **把 23%、15%–30% 当普遍保证** → 🛑 这是特定实验、特定条件下的结果。

### 灰色地带（需谨慎判断）

7. **领导在场成员就不敢说真话** → 让领导先离场或最后发言（书里 Kennedy 的做法之一），也可以先分头匿名写、再合议。
8. **有一位"最好的预测者"拒绝分享、怕 groupthink** → 书里真实存在这种例外。尊重个体风格，但提醒他这会让团队少一块信息；不强迫、不贴标签。
9. **远程 vs 面对面** → 线上更容易忽略陌生人、也更容易升级冲突，但更容易保持批判距离；可混合使用，用线下会把"人的维度"补上。
10. **团队已高度共享信息 vs 信息仍分散** → 已高度共享时极端化加总帮不上忙，信息分散时更值得加总；先判断属于哪种。
