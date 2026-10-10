---
name: mindset-leadership-culture
description: 当管理者/团队负责人要诊断"这是不是一个把成长当回事的组织"时使用——识别「人才心态（talent mind-set）」如何逼出固定型行为与 groupthink，判断组织在培养能力还是逼人自证，并给出把团队从「我」改回「我们」的干预动作。
input_schema:
  required: [org_context, observed_practice, role]
  optional: [team_size, recent_failure_handling, leader_self_report]
output_schema:
  primary:
    mindset_audit: string
    risk_mechanism: string
    intervention: string
  secondary: [groupthink_check, leader_development_view, cautions]
---

# 组织心态审计：你的公司是在培养人，还是在逼人自证？

**来源**：《Mindset: The New Psychology of Success》第5章 BUSINESS: MINDSET AND LEADERSHIP（整章） ｜ 证据等级：firsthand（书中的研究与引述均为原书原话）；把整章归纳成审计步骤为 reliable-secondary

## 触发条件

**应该触发**：
- 管理者说"我们高薪挖了一批聪明人，结果没人愿意承认错误、没人敢说真话"
- 用户描述团队"开会都不表态，散会才私下抱怨"，想知道是不是文化出了机制问题
- 用户是负责人，问"到底该奖励明星个人，还是奖励团队"
- 用户在招人/晋升时纠结"要不要只招有天赋、名校背景的人"
- 用户观察到自己或上级用贬低下属来确认权力，想弄清这背后的机制

**不应触发**：
- 用户要的是某一句批评/表扬的话术改写（走 mindset-process-praise）
- 用户要诊断的是"我个人此刻在证明还是在发展"（走 mindset-reaction-diagnosis）
- 用户问的是具体业务、财务或合规决策，与心态文化无关
- 出现职场霸凌、骚扰、歧视等需要 HR / 法律 / 专业介入的实况 → 先走 B 节兜底，不做心态说服

## R：原文锚点

1. "This ‘talent mind-set’ is the new orthodoxy of American management."（第5章 ENRON AND THE TALENT MINDSET）（已据原文核）
2. "It created a culture that worshiped talent, thereby forcing its employees to look and act extraordinarily talented."（第5章 ENRON AND THE TALENT MINDSET）（已据原文核）
3. "These were not the larger-than-life, charismatic types who oozed ego and self-proclaimed talent."（第5章 ORGANIZATIONS THAT GROW）（已据原文核）
4. "they use it as an engine of growth—for themselves, the employees, and the company as a whole."（第5章 GROWTH-MINDSET LEADERS IN ACTION）（已据原文核）
5. "The members of the growth-mindset groups were much more likely to state their honest opinions and openly express their disagreements as they communicated about their management decisions."（第5章 A STUDY OF GROUP PROCESSES）（已据原文核）
6. "It’s hard for courage and innovation to survive a companywide fixed mindset."（第5章 Brutal Bosses）（已据原文核）
7. "leaders are made, not born, and made more by themselves than by any external means."（第5章 ARE LEADERS BORN OR MADE?）（已据原文核）
8. "Create an organization that prizes the development of ability—and watch the leaders emerge."（第5章 ARE LEADERS BORN OR MADE?）（已据原文核）

## I：核心解释

1. **"人才心态"是组织级的固定型**：把"公司成功靠天赋"当信条（R1），等于告诉员工"你的价值是一道要被测量的题"。Enron 按这条信条建文化，逼员工"看起来、表现得很天才"（R2），于是没人能承认并修正缺陷——公司也失去了自我纠错的能力。
2. **成长型组织的第一个标志：领导不靠证明自己**：good-to-great 的领导者不是自带光环的强人（R3），他们把公司当成长引擎，而不是个人纪念碑（R4）。
3. **心态决定团队怎么开会**：把管理能力看成固定的一组，怕被评判，于是不表态、滑向 groupthink；把它看成可长的一组，敢亮出分歧，越做越好（R5）。
4. **霸凌会传染成公司级固定型**：老板用羞辱和威慑"让人绷着"，全公司就从"学习"切换到"怕被评判"，勇气与创新很难活下来（R6）。
5. **领导者是造就的，不是天生的**：Bennis 访谈的领导者一致认为领导力是造出来的（R7）。组织若只信天生，就会筛掉一大批可造之才，还可能把被贴"天赋"的人惯成傲慢不学的人。
6. **可操作的那句话**：想让领导者冒出来，先把组织改成奖励"能力可以发展"的地方（R8）。

## A1：来源应用 — 书里给的三个可操作做法

（以下都是书上给的做法，不是我的发挥）

- **对照两组 CEO**：Collins 的 good-to-great 领导者 self-effacing、常问问题、直面最残酷的答案；comparison 公司的领导者则是 "gargantuan personal ego"，靠 "genius with a thousand helpers" 运作（第5章 LEADERSHIP AND THE FIXED MINDSET）。
- **Wood & Bandura 的"心态说明书"实验**：把管理学生分两组，一组被告知"这个任务测量你的底层能力"，另一组被告知"管理技能靠练习养成"。固定型组不利用错误，成长型组直面错误、改用反馈、最后产出更高（第5章 A STUDY OF MINDSET AND MANAGEMENT DECISIONS）。审计时可直接照这两句去问：团队实际收到的是哪一种说明书。
- **三位成长型领导者的动作清单**（第5章 GROWTH-MINDSET LEADERS IN ACTION）：
  - 打开对话与反馈通道（Gerstner 上任六天就给每位员工写 memo）；
  - 关掉精英主义（Welch 当着精英俱乐部的面说"我在你们做的事里找不到价值"；Gerstner 解散管理委员会）；
  - 干掉"残酷老板"（Welch 让业绩达标但不践行价值观的四位高管离开）；
  - 把奖励从"个人天才"转向"团队"（Gerstner 让高管奖金更多挂公司整体表现；Welch 让团队分享创意的功劳）；
  - Mulcahy 式"既硬又暖"：讲清冷酷事实，同时不放弃员工士气与发展。

## A2：典型触发场景

1. 高绩效团队开会沉默，真问题都留到会后茶水间。
2. 公司只表彰"明星个人"，协作没人愿做。
3. 老板靠公开贬低、挑动下属互相比较来"激励"。
4. 招聘只看名校与光环，进来的人反而怕犯错、不学习。
5. 一次失败之后，全员忙着找替罪羊，而不是复盘。

## E：执行步骤

### 步骤1：收集"心态说明书"

**输入**：组织近期的招募话术、绩效口径、一次真实失败的处理方式。
**输出**：一句话说明——这个组织实际告诉员工的是"能力是固定的"，还是"能力可发展"。

🔴 **CHECKPOINT — 触发条件：用户只能给"感觉"，给不出任何具体证据**：先追问一件具体的事——最近一次失败里，谁被表扬、谁被罚、原话是什么。若仍拿不出 → 转 B 节「只有情绪没有事件」分支。

### 步骤2：给文化照 X 光

**输入**：步骤1 的证据。
**输出**：对照 A1 的成长型动作清单逐项打勾——对话通道 / 精英主义 / 残酷老板 / 奖励对象（个人 or 团队）/ 失败的学习。

🔴 **CHECKPOINT — 触发条件：用户开始用"我们就是固定型公司"给自己贴死标签**：纠偏——书里讲的是文化可以反向把固定型 root out（Welch 先在自己身上根除，再动组织），这不是判决书。

### 步骤3：定位 groupthink

**输入**：团队最近一次重大决策的过程。
**输出**：判断是 "we think" 还是 "groupthink"，并指认它是从哪种机制长出来的（把领导当神 / 自封特殊天赋 / 压制异议 / 为取悦领导而附和——第5章 GROUPTHINK VERSUS WE THINK 列出这四种）。

🔴 **CHECKPOINT — 触发条件：用户说"我们一致同意，从没分歧"**：这正是可疑信号，追问"上一次有人公开反对是谁、后来怎样"。

### 步骤4：给一个最小干预

**输入**：步骤3 的定位。
**输出**：一个本周就能开始的动作（指定 devil's advocate / 就同一议题组织对立辩论 / 匿名建议箱并强制参与决策 / 把一次奖励从个人改成团队）。

🔴 **CHECKPOINT — 触发条件：用户想一步改造全公司**：降到一个点。书里的转变都是从"从自己开始"、从一个动作开始。

### 步骤5：把"人"重新放回视野

**输入**：现有的绩效与晋升标准。
**输出**：一句话——"我们是在找天生的人，还是在培养能发展的人"。

🔴 **CHECKPOINT — 触发条件：用户抱怨"招不到好苗子"**：回到 R8——先建一个奖励能力发展的组织，再看谁会冒出来。

## B：边界与失败模式

### 失败模式分支表

| 情况 | 表现 | 怎么处理 |
|------|------|---------|
| 只有情绪没有事件 | 用户只会说"公司很 toxic"，给不出任何具体经过 | 🛑 不套框架，先要一件具体失败的处理经过与当事原话。 |
| 把审计变成批斗 | 用户想拿"你是固定型领导"去攻击上级或同事 | 🛑 停。本工具是自助诊断，不是给别人的判决书；审计只落到"你自己能改的那一半"。 |
| 把成长型当新 KPI | 团队开始"证明我们是成长型" | 🛑 这本身就是固定型读法，转 mindset-false-growth-check。 |
| 用文化解释一切 | 用户拿"心态"掩盖真实的经营、合规问题 | 🛑 分开：心态只解释"为什么人不学、不说真话"，不替代业务与法务判断。 |
| 职场霸凌/骚扰/违法 | 出现人身攻击、报复、歧视实况 | 🛑 不做心态说服，指向 HR / 法律 / 专业渠道与心理支持资源。 |

### 边界规则

1. **不做人格判决**：只审计"文化此刻在奖励什么行为"，不判定某人是"固定型人格"。书里的 CEO 是行为模式，不是诊断标签。
2. **一次只动一个点**：Welch 也是先在自己身上 root out，再动组织；不要许诺一次性文化改造。
3. **不夸大数据**：本工具不预测业绩，不保证融资、涨薪或股价。
4. **安全兜底**：若用户正遭受职场霸凌、骚扰、歧视，或身处被报复的高压中，先谈人身安全与现实资源（HR、法律援助、心理咨询），不做"你换个心态就好"的说服。涉及严重心理困扰时，只做提醒与陪伴，不做诊断，并指向当地心理援助资源（中国大陆可拨 12356 或 010-82951332，紧急时拨 110/120）。

### 用户自查清单

- [ ] 我能用一件具体的事说明"这个组织实际奖励的是自证还是成长"
- [ ] 我能说出团队上一次失败后，大家做的是复盘还是找替罪羊
- [ ] 我能指认 groupthink 是被哪一种机制引出来的
- [ ] 我挑出的干预是本周能开始的一个动作，而不是一句口号
- [ ] 我的审计只指向"我自己能改的那一半"，没有变成给人贴标签

## 📖 练习手册

**四格文化卡**：把一张纸分成"对话通道 / 精英主义 / 残酷老板 / 奖励对象"四格，每格写下你所在组织的一个真实证据，再写下"成长型组织在这里会怎么做"。

**从自己开始**：模仿 Welch，先写下你自己最近一次"捍卫面子"的时刻，再写下——如果把能力当成可发展的，那一步你会怎么走。

## 🚫 反例与黑名单（不要做的事）

1. 把"你是固定型领导"当武器去攻击上级或同事 → 🛑 停止，本工具只用于自助。
2. 把 Enron、Iacocca 的故事讲成八卦式的道德审判 → 🛑 提取机制（自证需要 → 不认错 → 失去纠错），不是嘲笑个人。
3. 让团队开始"表演成长型" → 🛑 这恰是固定型读法。
4. 用"心态"给真实的经营失败、财务造假、违法洗白 → 🛑 分开处理。

### 灰色地带（需谨慎判断）

- **用户真心欣赏强人文化**（"我们就是要明星，看着爽"）→ 不强行推销成长型，只帮他把代价看清，把选择权留给他。
- **短期业绩很好但靠恐惧驱动** → 不急于推翻：先说清"恐惧驱动的代价会以创新与留人的形式延迟出现"（书里明说公司级固定型下勇气与创新难活），再谈要不要动。
- **用户改变不了组织，只能改自己那一半** → 把审计落到他可控的动作上，不要让他背全公司的账。
