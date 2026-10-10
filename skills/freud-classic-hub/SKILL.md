---
name: freud-classic-hub
description: 弗洛伊德经典三模型 Hub。当用户的问题属于「内心冲突/纠结」「丧失后走不出来」「焦虑回避」三大经典领域时，由此 Hub 路由到对应的原始蒸馏 skill。当用户说「弗洛伊德经典模型」「用最基础的那个」等触发词时激活。
input_schema:
  required: [presenting_problem]
  optional: [emotion_tone, time_feature, body_signal, loss_clue]
output_schema:
  primary: {route_target: string, score: string, reason: string}
  secondary: [routing_checkpoint, sub_skill_read, follow_up_prompts]
---

# Freud Classic Hub —— 弗洛伊德经典三模型路由中心

## 触发条件

**应该触发**
- 用户提到「结构模型」「本我自我超我」「三我冲突」
- 用户说「我是不是在哀悼还是忧郁」「丧失后走不出来」
- 用户说「我很焦虑但不知道为什么」「我在回避什么」
- 用户的问题属于经典弗洛伊德核心三模型范畴

**不应触发（路由到其他架构）**
- 涉及梦/口误 → `freud-hub` → `freud-dreams-parapraxes`
- 涉及身体症状 → `freud-hub` → `freud-trauma-hysteria`
- 涉及性格/性心理 → `freud-hub` → `freud-sexuality-development`
- 涉及压抑/潜意识 → `freud-hub` → `freud-metapsychology`
- 涉及自恋/群体 → `freud-hub` → `freud-narcissism-identification`
- 涉及强迫重复 → `freud-hub` → `freud-death-drive-repetition`
- 涉及文明批判 → `freud-hub` → `freud-anxiety-civilization`
- 纯外部现实问题、非精神分析框架

## R：原文锚点

> **The Ego and the Id (1923b)**：原文 — "we see this same ego as a poor creature owing service to three masters and consequently menaced by three dangers: from the external world, from the libido of the id, and from the severity of the super-ego."（已据英文全集核）
> 中译（译自英文全集，下同）：「我们看到这个自我是一个可怜的、侍奉三位主人的造物，因而受到三重危险的威胁：来自外部世界、来自本我的力比多、以及来自超我的严厉。」

> **Mourning and Melancholia (1917e)**：原文 — "we perceive that the self-reproaches are reproaches against a loved object which have been shifted away from it on to the patient's own ego."（已据英文全集核）
> 中译：「我们看到，这些自我谴责其实是对某个被爱对象的谴责，它们已从该对象身上转移到了病人自己的自我之上。」

> **Inhibitions, Symptoms and Anxiety (1926d)**：原文 — "It was anxiety which produced repression and not, as I formerly believed, repression which produced anxiety."（已据英文全集核）
> 中译：「是焦虑产生了压抑，而不是像我以前所相信的那样，压抑产生了焦虑。」

## I：核心解释

### 判别标准

首先判断问题类型——按以下维度打分，最高分即目标 skill：

| 判定维度 | 指向 structural-model | 指向 mourning-melancholia | 指向 anxiety-defense |
|---------|----------------------|--------------------------|---------------------|
| 核心冲突 | 「我应该…但我不想」「我控制不住」 | 「我配不上」「我活该」「我不好」 | 「我怕」「我躲」「我不知道怕什么」 |
| 情绪基调 | 纠结、拉扯、矛盾 | 空虚、自责、无价值 | 紧张、回避、恐慌 |
| 时间特征 | 当下正在发生 | 追溯某个丧失后开始 | 持续或阵发，无明确起点 |
| 身体信号 | 无明显躯体化 | 疲劳、食欲↓、兴趣↓ | 心跳加速、出汗、胃紧 |

**路由决策** `=` 按上述四维度逐项打分（每条命中 +1），最高累计分即目标。

```
用户问题
  │
  ├─ 「应该…但不想」「控制不住」> 其他 → freud-structural-model
  │   （本我-自我-超我三角冲突）
  │
  ├─ 「配不上/活该/不好」> 其他，且有丧失线索 → freud-mourning-melancholia
  │   （哀悼 vs 忧郁鉴别）
  │
  └─ 「怕/躲/不知道怕什么」> 其他 → freud-anxiety-defense
      （焦虑信号 + 防御机制）
```

### 跨模型处理

```
if 两维度分数持平:
  按优先级：structure > mourning > anxiety
  （内心冲突是最紧迫的——先拆解三角，再往下走）

if 三个维度均分:
  → 🔴 CHECKPOINT 提示用户："这个问题涉及内心冲突、丧失和焦虑三个维度，建议从 freud-structural-model 开始，后续按需接入另两个。确认？"
```

### 三个经典模型速查

| Skill | 核心问题 | 关键概念 |
|-------|---------|---------|
| `freud-structural-model` | 谁在脑子里吵架？ | 本我（我要）、自我（调解）、超我（你不配） |
| `freud-mourning-melancholia` | 你在骂谁？ | 丧失对象内化进自我，自我谴责 = 骂内化对象 |
| `freud-anxiety-defense` | 你在怕什么？ | 焦虑先于压抑，防御是自我的自我保护 |

## A1：来源应用 — 三个经典模型的谱系

- **结构模型（1923，《自我与本我》）**：自我被本我、超我与外部现实三方拉扯；自我的大部分也是潜意识的。对应「内心冲突」。
- **哀悼与忧郁（1917）**：丧失对象通过认同被内化进自我，批判性代理转而攻击被对象染色的自我——自我谴责其实是被转移的对对象的指控。对应「丧失后走不出来」。
- **焦虑信号理论（1926，《抑制、症状与焦虑》）**：弗洛伊德第二次大修正——焦虑信号先于压抑，防御是自我的自我保护。对应「焦虑回避」。

**日常案例**：用户说「我明知道该睡觉了，可就是控制不住想再刷会儿手机，另一个我又骂自己没自制力」——四维打分中「应该…但不想」「控制不住」命中结构模型最高分，于是 Hub 输出 `→ freud-structural-model（原因：核心冲突，得分 X/4）`，等确认后再读取子 skill。

## A2：典型触发场景

- 内心在打架（「应该…但不想」「控制不住」）→ structural-model
- 丧失后自我谴责（「我不配」「我活该」「什么都怪我」）→ mourning-melancholia
- 说不出理由的焦虑与回避（「我怕」「我躲」「不知道怕什么」）→ anxiety-defense
- 两三个维度都沾一点、用户自己也说不清 → 先打分再 CHECKPOINT 确认
- 用户点名要「用最基础的那个弗洛伊德模型」→ 从本 Hub 进入
- 梦境、身体症状、性格、压抑、自恋、强迫重复、文明批判 → 不在此 Hub，转 `freud-hub`

## E：执行步骤

| 步骤 | 输入 | 操作 | 输出 |
|------|------|------|------|
| 1 | 用户原始消息 | 按「判别标准」四维度打分 | 三个分数（各0-4） |
| 2 | 三个分数 | **🔴 CHECKPOINT**：输出路由决策 `→ freud-{target}（{原因}，得分 {X}/4）` | 等待用户确认 |
| 3 | 确认后的 target | `read` 对应子 skill 的 SKILL.md | 子 skill 内容 |
|  |  | `freud-structural-model` → `skills/freud-structural-model/SKILL.md` |  |
|  |  | `freud-mourning-melancholia` → `skills/freud-mourning-melancholia/SKILL.md` |  |
|  |  | `freud-anxiety-defense` → `skills/freud-anxiety-defense/SKILL.md` |  |
| 4 | 子 skill 执行结果 | 检查用户反馈 | 满意 → 结束；不满意 → fallback 表 |

### 🔴 CHECKPOINT：路由前确认

在进入具体子 skill 之前，输出一行确认：

```
🔴 路由决策：→ freud-{target}（原因：{最高分维度}，得分 {X}/4）
如果路由错误，回复「不对，应该是…」我将重新判别。
```

## B：边界与失败模式

### 失败模式分支表

| 触发条件 | 一线修复 | 仍失败兜底 |
|---------|---------|-----------|
| 用户说「不对，不是这个」 | 改用次高分 skill 重新判别 | → 转发到 `freud-hub`（让更广的主题路由接管） |
| 四条判定维度均不明确 | 追问一句：「你现在更接近哪种感觉——(A)内心在打架 (B)觉得自己不配 (C)在怕什么但说不清？」 | 用户拒绝选择 → 转发 `freud-hub` |
| 用户描述含自杀意念 | 停止路由，直接提供 12356，不分析 | 强制转发 `freud-mourning-melancholia`（含自杀评估） |
| 子 skill 文件不存在 | 从 Hub 速查表直接输出该模型的简要框架 | 转发 `freud-complete` 做全量分析 |

### 边界规则
- 一次只激活一个子 skill——不做三模型并联输出
- 路由必须展示判别理由，不替用户「黑箱」决定
- 涉及自杀意念、危机时，路由让位于安全干预
- 经典三模型不覆盖梦、身体症状、性心理、自恋、强迫重复、文明批判——这些归 `freud-hub`

### 用户自查清单

（Hub 出队前逐项确认）

```
[ ] 四维打分完成？（核心冲突/情绪基调/时间特征/身体信号各给分 = ✅）
[ ] 最高分维度 = 路由目标？（一致 = ✅ / 持平 → 按优先级 structure>mourning>anxiety）
[ ] 🔴 CHECKPOINT 路由决策是否已展示给用户并等待确认？（是 = ✅）
[ ] 子 skill 路径是否正确？（`skills/freud-{target}/SKILL.md` = ✅）
[ ] 是否只激活了一个子 skill？（是 = ✅）
[ ] 自杀意念筛查通过？（无 = ✅ / 有 → 停止路由，直接 12356）
```

**通过标准**：全部 ✅，无❌。路由错误或维度持平按 fallback 处理。

### 🆘 安全兜底
- 出现自杀意念、自伤或伤人意念 → **停止路由**，直接提供：全国心理援助热线 **12356**，或 **010-82951332**。
- 处于紧急人身危险 → 拨打 **110**；需要急救 → **120**。
- 忧郁线索 + 自杀意念 → 强制转发 `freud-mourning-melancholia`（含自杀评估）。

## 练习手册

配套 7 天实操（每天只做一条）：
1. 用四维度给自己的一个困扰打分（核心冲突/情绪基调/时间特征/身体信号）。
2. 找出最高分维度，写出它对应的经典模型。
3. 用一句话说明「为什么是这个模型」。
4. 对照速查表核对：这个模型的核心问题是不是「你在骂谁 / 谁在吵架 / 你在怕什么」。
5. 练习跨模型判断：找出一个同时沾两个维度的问题。
6. 练习优先级：两维持平时，按 structure > mourning > anxiety 排序。
7. 练习 CHECKPOINT 话术：写出你打算展示给用户的那一行路由决策。

## 反例黑名单 —— 不要做的事

1. **不要跳过判别直接分析** —— 即使问题看起来很明显，也先打分后路由
2. **不要把三个模型都输出一遍** —— 一次只激活一个子 skill
3. **不要替用户决定「你应该用哪个」而不解释** —— 给出判别理由
4. **不要在用户表达自杀意念时继续分析** —— 停止路由，给热线
5. **不要在四维度均不明确时猜一个** —— 追问 A/B/C 三选一

## 灰色地带

1. **四维打分持平** —— 两维持平时按优先级（structure > mourning > anxiety）；三维均分时先 CHECKPOINT，建议从结构模型进入。
2. **用户拒绝对号入座** —— 不硬塞模型；可转发 `freud-hub` 用更广的主题路由，或先做支持性对话。
3. **问题看似经典三模型、实则另有主线** —— 例如「我不配」里其实夹着强迫重复或自恋议题；若打分上限都不高，转 `freud-hub`。
4. **自杀意念与经典模型并存** —— 安全永远优先于路由；停止分析，给热线，再考虑忧郁评估。
5. **同一用户跨会话换了主诉** —— 每次重新打分，不沿用上次路由结论。

## 与其他架构的关系

- `freud-classic-hub`：3个经典模型，最基础、最原始蒸馏
- `freud-hub`：9个按主题的扩展模型，覆盖更广
- `freud-complete`：全量16本著作一次性分析
