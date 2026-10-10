---
name: mindset-relationship-growth
description: 当用户把"关系本身"当成一件天生注定、可被一次性判定的事时使用——识别「要努力就说明不是对的人」这一固定型信念、拆开 mind reading 与"必须处处一致"，把冲突重读成可修的沟通问题，而不是"性格缺陷/我们不适合"的判决。
input_schema:
  required: [relationship_story, stuck_belief, what_they_want]
  optional: [partner_reaction, conflict_topic, prior_attempts]
output_schema:
  primary:
    fixed_belief_named: string
    reframe: string
    next_move: string
  secondary: [conflict_reading, partner_potential_check, cautions]
---

# 关系心态：把关系当成一件会长大的东西

**来源**：《Mindset: The New Psychology of Success》第6章 RELATIONSHIPS: MINDSETS IN LOVE (OR NOT)（整章） ｜ 证据等级：firsthand（原书机制、专家引述与案例为 firsthand）；把整章归纳成步骤为 reliable-secondary

## 触发条件

**应该触发**：
- 用户说"如果是对的人，应该什么都不用努力就顺"，或"我们要费这么大劲，是不是根本不合适"
- 用户坚信"他应该懂我""不用我说他就该知道"，因为伴侣没猜到而受伤
- 用户因为一点分歧就觉得"我们三观不合、完了"
- 用户分手/被拒后整段复述只有报复或"我是不可爱的"的判决
- 用户困惑"为什么每段关系都从天堂变成战场"

**不应触发**：
- 用户描述的是家暴、骚扰、控制等安全议题 → 立刻走 B 节安全兜底，不做"关系要努力"的劝说
- 用户要的是具体沟通话术脚本（可走 mindset-trigger-reframe，本工具只做读法与最小动作）
- 用户要诊断的是"我此刻在证明还是发展自己"的通用读法（走 mindset-reaction-diagnosis）
- 用户在做婚前/伴侣咨询等专业流程 → 优先尊重专业结论，本工具仅作补充

## R：原文锚点

1. "You can believe that your qualities are fixed, your partner’s qualities are fixed, and the relationship’s qualities are fixed—that it’s inherently good or bad, meant-to-be or not meant-to-be."（第6章 MINDSETS FALLING IN LOVE）（已据原文核）
2. "This is the same belief applied to relationships: If you’re compatible, everything should just come naturally."（第6章 If You Have to Work at It, It Wasn’t Meant to Be）（已据原文核）
3. "If we need to work at it, there’s something seriously wrong with our relationship."（第6章 If You Have to Work at It, It Wasn’t Meant to Be，Aaron Beck 语）（已据原文核）
4. "A no-effort relationship is a doomed relationship, not a great relationship."（第6章 AGREEING ON EVERYTHING）（已据原文核）
5. "there are no great relationships without conflicts and problems along the way."（第6章 Problems Indicate Character Flaws）（已据原文核）
6. "People with the growth mindset, on the other hand, can see their partners’ imperfections and still think they have a fine relationship."（第6章 Problems Indicate Character Flaws）（已据原文核）
7. "The belief that partners have the potential for change should not be confused with the belief that the partner will change."（第6章 CAN THIS MARRIAGE BE SAVED?）（已据原文核）
8. "For people with the growth mindset, the number one goal was forgiveness."（第6章 开篇，rejection 研究）（已据原文核）
9. "choosing a partner is choosing a set of problems. There are no problem-free candidates."（第6章 EACH ONE A LOSER）（已据原文核）

## I：核心解释

1. **关系里有三样东西都可能被当成固定之物**：你、对方、以及"关系本身"（R1）。固定型把关系读成一件"天生 good / bad、注定 / 不注定"的东西，于是每一点摩擦都成了对关系的终审判决。
2. **固定型把"努力"当红灯**：它把"关系需要经营"翻译成"我们不是对的人"（R2、R3）——这正是"有天赋就不该费劲"这条信念被搬运到了关系里。
3. **不努力的关系是注定失败的关系，不是好关系**（R4）：书里说，两个人都觉得"若是命定，就不必这么费力"，于是渐行渐远。真正的差别不是"要不要努力"，而是把努力读成"发展"还是"证明不合适"。
4. **冲突不是性格缺陷的证据**：固定型把矛盾归因到一个**性格特质**（"他就是自私"），于是从 anger 到 contempt，问题被读成不可解（第6章 Problems Indicate Character Flaws）。而"没有一段伟大的关系是不经过冲突和问题"的（R5）。
5. **成长型能同时看见缺憾与好的关系**（R6）：它把冲突重读成沟通问题（"细节太多我听不懂你了"而不是"你这个人很无聊"）。
6. **一个关键的边界提醒**：相信伴侣**有可能**改变，不等于相信伴侣**会**改变（R7）——对方得自己想改、愿意改、并做出实际动作。这不冲突于成长型，恰恰是它的诚实版。
7. **被拒后的两条路**：固定型把拒绝读成永久的烙印（"UNLOVABLE!"），目标是报复；成长型的目标是理解、宽恕、向前走（R8）。选择伴侣其实是"选择一组问题"，没有无问题的候选人（R9）。

## A1：来源应用 — 书里给的具体做法

（书上给的，非我的发挥）

- **把"命定信念"直接说破**：书里点名 Beck 与 Gottman 的原话，把"要努力就是有问题"当成"对关系最有破坏性的信念"之一，让当事人看见它是信念、不是事实（第6章 If You Have to Work at It…）。
- **拆掉 mind reading**：书里有 Tom 与 Lucy 的案例——Lucy 以为"不平衡"是说他不爱她，鼓起勇气去问才发现是"想微调、升级关系"；作者自己也被"I need more space"吓到，问了才知道是"你挪一下，让点地方"。做法是：**先问清对方真正的意思，而不是自己翻译**（第6章 MIND READING）。
- **拆掉"必须处处一致"**：书里让情侣谈各自对关系的看法，固定型一遇到微小分歧就感到受威胁；建议是承认"一对伴侣不可能共有彼此所有的假设与期待"（第6章 AGREEING ON EVERYTHING）。
- **把脾气改成"有帮助的动作"**：Ted 想骂 Karen 时先问自己"成熟的做法是什么"，然后动手收拾屋子——用支持代替评判（第6章 THE FLAWS FLY）。
- **宽恕的两条实证**：被拒研究里，成长型第一目标是宽恕；Cathy、Nicole 的案例讲的是"放下苦毒、走出去"。书里的落脚点是：成长型让人越过指责，理解问题、一起修（第6章 THE PARTNER AS ENEMY）。

## A2：典型触发场景

1. 刚吵完架，脑子里全是"我们是不是不合适"。
2. 因为伴侣没主动猜到自己的需要而委屈。
3. 一次观念分歧（要不要孩子、钱怎么花）后就想分手。
4. 被分手/被拒后，反复计划怎么让对方不好过。
5. 每段关系都从"命中注定"走到"看错了人"。

## E：执行步骤

### 步骤1：把"命定信念"抓住并复述出来

**输入**：用户对关系/伴侣的原话。
**输出**：一句被复述出来的固定型信念，例如"如果是对的人，我就不该觉得累"。

🔴 **CHECKPOINT — 触发条件：用户给不出具体事件，只反复说"就是不合适"**：追问最近一次具体的摩擦——谁说了什么、你当时怎么想。若仍拿不出 → 转 B 节「只有结论没有事件」分支。

### 步骤2：定位三样东西里，被当成固定的是哪一样

**输入**：步骤1 的信念。
**输出**：指认——是把"我"、把"对方"，还是把"关系本身"当成了不可改的（对照 R1）。

🔴 **CHECKPOINT — 触发条件：用户说"他这个人就这样，改不了"**：别急着反驳，先分清 R7——他**可能**改 vs 他**会**改；把"他愿不愿意自己想改"作为下一步的问题。

### 步骤3：拆 mind reading / "必须一致"

**输入**：用户对伴侣心意或分歧的猜测。
**输出**：一句"你其实没问过"的提醒，或一个待确认的问题（照 A1 的 Tom/Lucy 法）。

🔴 **CHECKPOINT — 触发条件：用户的复述里出现重度自我否定（"我根本不值得被爱""我不配活着"）**：这可能超出本工具范围 → 立即转 B 节「抑郁/自伤信号」，只做陪伴与转介，不继续认知层拆解。

### 步骤4：把冲突从"性格判决"改写成"沟通问题"

**输入**：用户认定的对方"性格缺陷"。
**输出**：一个可修的表述（"当你说我没在听时，我其实是怕说错——我们该怎么谈"）。

🔴 **CHECKPOINT — 触发条件：用户只想要"他必须承认他有问题"**：把焦点拉回 R6——成长型允许同时看见缺憾与好的关系，不等于对方无罪，而是"问题可解"。

### 步骤5：给一个最小动作（含退出选项）

**输入**：步骤4 的改写。
**输出**：一次具体行动（先问清 / 说清自己的一半 / 提一次沟通而非审判），并明确——这也可以是"确认后决定离开"。

🔴 **CHECKPOINT — 触发条件：用户把"努力"理解成"必须留下来"**：纠正——书里 Nicole、Cathy 的成长型也包含"move on and embrace that future"；努力不等于绑死。

## B：边界与失败模式

### 失败模式分支表

| 情况 | 表现 | 怎么处理 |
|------|------|---------|
| 只有结论没有事件 | 用户只会说"不合适"，给不出任何具体经过 | 🛑 不套框架，先要一件具体摩擦的经过与原话。 |
| 拿"关系要努力"绑住受害者 | 用户身处虐待/控制关系 | 🛑 停。先走 B 节安全兜底：本工具绝不用于劝人留在危险关系里。 |
| 用"成长型"道德绑架伴侣 | 用户想拿框架逼对方改变 | 🛑 回到 R7：改变得对方自己想、且做出来，不能强求。 |
| 把框架当新的判决书 | 用户问"我是不是固定型，所以注定谈不好" | 🛑 纠偏：这是此刻的读法，不是你的身份标签。 |
| 轻度冲突被夸大成危机 | 用户把一次小分歧当成"关系崩了" | 🛑 正常化：R5——没有一段好关系不经过冲突。 |

### 边界规则

1. **不做诊断，不做人格判决**：只分类"此刻把这个理念用在哪一样东西上"，不判定"你是不是好人/他是不是烂人"，不替代心理或婚姻评估。
2. **努力 ≠ 必须留下**：成长型既包含"一起修"，也包含"确认后 move on"；不要把本工具变成"无论如何都不能分手"的束缚。
3. **安全优先**：涉及暴力、威胁、跟踪、胁迫、经济/性控制时，**停止关系心态工作**，优先人身安全与现实资源。涉及临床抑郁、自伤、自杀意念或进食障碍的严重信号时，停止本框架，明确告诉用户这需要专业人员，并指向当地心理援助资源（中国大陆可拨 12356 或 010-82951332，紧急时拨 110/120），不做诊断、不保证效果。
4. **尊重专业流程**：若用户已在伴侣咨询/治疗中，遵循专业结论，本框架仅作补充理解。

### 用户自查清单

- [ ] 我能说清我信的是哪一句固定型信念（如"要努力就不是对的人"）
- [ ] 我能说出被当成固定不变的是"我""对方"还是"关系本身"
- [ ] 我能分清"他可能改"和"他会改"，并承认改变得由他自愿
- [ ] 我能把至少一个"性格判决"改写成可修的沟通表述
- [ ] 我知道一个下一步能做的最小动作，也知道"确认后离开"同样是有效选项

**勾选 4+ 项**：读法到位。**≤2 项**：回到对应步骤重做，或考虑转 B 节。

## 📖 练习手册

**三栏"固定/可长"表**：写下"我""他""我们的关系"三行，每行左边写"我把它当成固定的证据"，右边写"如果它可长，会是什么样"，再标出你愿意先动哪一格。

**"我以为／其实是"追踪**：连续一周，每次因"他没猜到"而受伤时，记下"我以为他是什么意思"和"我实际问过没有"，周末回看。

## 🚫 反例与黑名单（不要做的事）

1. 用"关系需要经营"去劝人留在虐待、控制关系里 → 🛑 绝对禁止，先谈安全与资源。
2. 把"你是固定型"拿来指责伴侣 → 🛑 停，本工具是自助读法，不是给别人的判决书。
3. 把"宽恕/move on"当命令 → 🛑 允许用户现在只想伤心的权利；框架只提供选项。
4. 把"我们注定"讲成"我们没救"或反之的宿命论 → 🛑 两种都是固定型读法。

### 灰色地带（需谨慎判断）

- **用户真心享受"命中注定"的浪漫**（"知道他是我的人让我踏实"）→ 不把成长型强加；只帮他把"宿命感"和"遇到问题时的反应"分开看。
- **伴侣确实不愿改变且反复伤害** → 成长型不等于无限忍耐；把"可能改 vs 会改"（R7）说清，让用户对现实做判断。
- **谈的是别人的关系**（"我女儿找的这个人就是不行"）→ 引导回到用户自己能做的那一步，否则变成越界评判。
