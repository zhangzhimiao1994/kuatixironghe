---
name: freud-hub
description: 弗洛伊德全集技能中心。当用户的问题涉及弗洛伊德相关领域但不确定用哪个具体技能时，由此 Hub 进行路由。当用户说「弗洛伊德怎么说」「精神分析怎么看」等笼统触发词时激活。
input_schema:
  required: [user_message]
  optional: [conversation_context, prior_skill_used, topic_signal_words]
output_schema:
  primary: {route_target: string, matched_keywords: string, route_reason: string}
  secondary: [needs_classic_hub, cross_domain_count, fallback_used]
---

# Freud Hub —— 弗洛伊德全集技能路由中心

## 触发条件

### 应该触发
- 用户提到「弗洛伊德」「精神分析」「心理动力学」等关键词
- 用户表现出与精神分析理论匹配的症状/困惑
- 用户说「帮我用弗洛伊德视角分析」
- 用户问题跨越多个子skill边界

### 不应触发
- 纯书单 / 纯理论科普请求（只想了解理论，不要个人分析）→ 可指向 `freud-development-overview` 做概览，不做个人深度分析
- 用户描述含自杀意念 → 不路由、不分析，直接给热线（见下方「安全兜底」）
- 与弗洛伊德领域无关的问题 → 交回上层路由（如 `cross-system-hub`）

## R：原文锚点（路由判定所依据的原典原句）

> 说明：以下中文为**中译，译自英文全集**（Ivan Smith 编 *Freud – Complete Works*），非逐字原文；英文原句已逐字回书核，见各条括号内。

> 「本我在哪里，自我就应该在那里。」（《精神分析新论》1933a，第三十一讲「心理人格的解剖」；原句 *Where id was, there ego shall be.*）——路由到结构模型类问题的依据。（已据英文全集核）

> 「它（被压抑物）在黑暗中增殖，呈现出极端的表达形式。」（《压抑》1915d *Repression*；原句 *It proliferates in the dark, as it were, and takes on extreme forms of expression.*）——路由到压抑/潜意识（元心理学）类问题的依据。（已据英文全集核）

> 「癔症患者主要受回忆的折磨。」（《癔症研究》1895d，布洛伊尔「论癔症现象的心理机制」；原句 *Hysterics suffer mainly from reminiscences.*）——路由到创伤/躯体化类问题的依据。（已据英文全集核）

> 「群体从不渴求真理。它们要求幻觉，不能没有幻觉。」（《群体心理学与自我的分析》1921c，第二章「勒庞对群体心灵的描述」；原句 *They demand illusions, and cannot do without them.*）——路由到自恋/群体心理类问题的依据。（已据英文全集核）

## I：核心解释（路由原理）

本 Hub 不亲自分析，只做**主题路由**：把用户的笼统表述翻译成弗洛伊德理论坐标，再交给覆盖该坐标的子 skill。路由的核心原理是：**先看问题属于哪一套心理装置（结构冲突 / 丧失 / 压抑 / 创伤 / 自恋 / 重复 / 焦虑 / 发展），再定位唯一目标 skill**——一次只激活一个。

### 一级判别：是否是经典三模型？

先判断是否属于经典三模型范畴（内心冲突/丧失/焦虑防御）。若是 → 转发 `freud-classic-hub`，不在此 Hub 内处理。

```
if 用户问题含以下任一模式:
  「我应该…但我不想」「控制不住自己」→ classic → structural-model
  「我不配」「我活该」「失去后走不出来」→ classic → mourning-melancholia
  「我怕」「我躲」「不知道怕什么」→ classic → anxiety-defense
  → 转发 freud-classic-hub
```

### 二级路由：主题匹配

```
用户问题
  │
  ├─ 属于经典三模型范畴 → freud-classic-hub（二级路由）
  │
  ├─ 「查不出原因的身体症状」「哭不出来」「嗓子堵」→ freud-trauma-hysteria
  ├─ 「做了个梦」「反复做同一个梦」「怎么老是忘记/口误」→ freud-dreams-parapraxes
  ├─ 「我为什么总是这样」「性格从哪来」「洁癖/抠门/控制欲」→ freud-sexuality-development
  ├─ 「越压抑越反弹」「说不出来」「想不通为什么」→ freud-metapsychology
  ├─ 「我不够好」「别人怎么看我」「被孤立」「大家都这样」→ freud-narcissism-identification
  ├─ 「我纠结」「走不出来」「我不配好起来」→ freud-mourning-structure
  ├─ 「我又在重复」「每次都这样」「为什么又重蹈覆辙」→ freud-death-drive-repetition
  ├─ 「控制不住地担心」「为什么这么痛苦」「这社会是不是有问题」→ freud-anxiety-civilization
  ├─ 「整体怎么看弗洛伊德」「越不能越想」「禁忌」→ freud-development-overview
  └─ 跨3个以上领域 → freud-complete（全量一次性分析）
```

### 跨领域处理

```
if 命中 2 个主题:
  选主导主题（用户花最多篇幅描述的那个）
  先说明：「这个问题主要涉及 {主题A}，同时关联 {主题B}，先从 A 切入」

if 命中 3+ 个主题:
  → 🔴 CHECKPOINT：「这个问题跨 {N} 个领域，用 freud-complete 做全量分析还是逐个子 skill 查？」
```

### 理论精华速查

**结构模型**：本我（我要）← 自我（调解）→ 超我（你不配）+ 外部现实（不行）
**动力学**：力比多 = 可量化的性能量 → 可转移（升华）或堵住（症状）
**发展**：口欲→肛欲→阴茎（俄狄浦斯）→潜伏→生殖
**二元本能**：Eros（联结/爱）↔ Thanatos（解体/死）
**治疗目标**：本我在哪里，自我就应该在那里

### 关键修正历程
- 1895：创伤→躯体化（癔症研究）
- 1900：梦 = 愿望满足（梦的解析）
- 1915：压抑消耗持续能量、潜意识用物表象思考
- 1920：**转向**——强迫重复 + 死本能，创伤梦不是愿望满足
- 1923：结构模型（本我-自我-超我）
- 1926：**第二次修正**——焦虑先于压抑（不是压抑产生焦虑）
- 1930：文明的代价 = 本能压抑，幸福不在宇宙的设计中

## A1：来源应用 —— 哪类问题路由到哪个子 skill

把上面的路由树落成一张**「问题信号 → 目标 skill」**对照表（原「二级路由」的实例化）：

| 用户问题信号 | 路由目标 | 依据的原典域 |
|-------------|---------|------------|
| 「我应该…但我不想」「控制不住自己」 | `freud-classic-hub` → `freud-structural-model` | 结构模型（自我与本我） |
| 「我不配」「我活该」「失去后走不出来」 | `freud-classic-hub` → `freud-mourning-melancholia` | 哀悼与忧郁 |
| 「我怕」「我躲」「不知道怕什么」 | `freud-classic-hub` → `freud-anxiety-defense` | 焦虑信号 / 防御 |
| 「查不出原因的身体症状」「哭不出来」 | `freud-trauma-hysteria` | 癔症研究 |
| 「做了个梦」「老是忘记/口误」 | `freud-dreams-parapraxes` | 梦的解析 + 日常心理病理学 |
| 「我为什么总是这样」「性格从哪来」 | `freud-sexuality-development` | 性学三论 |
| 「越压抑越反弹」「想不通为什么」 | `freud-metapsychology` | 压抑 + 潜意识 |
| 「我不够好」「被孤立」「大家都这样」 | `freud-narcissism-identification` | 自恋导论 + 群体心理学 |
| 「我纠结」「我不配好起来」 | `freud-mourning-structure` | 哀悼与忧郁 + 自我与本我 + 纲要 |
| 「我又在重复」「每次都这样」 | `freud-death-drive-repetition` | 超越快乐原则 |
| 「控制不住地担心」「这社会是不是有问题」 | `freud-anxiety-civilization` | 抑制症状与焦虑 + 文明及其不满 |
| 跨 3+ 领域 | `freud-complete` | 全量一次性分析 |

### 子 Skill 清单（原样保留）

| Skill | 覆盖著作 | 核心功能 |
|-------|---------|---------|
| `freud-trauma-hysteria` | 癔症研究 | 创伤→躯体化、宣泄疗法 |
| `freud-dreams-parapraxes` | 梦的解析 + 日常心理病理学 | 梦解析、失误行为 |
| `freud-sexuality-development` | 性学三论 | 力比多发展、性心理阶段 |
| `freud-metapsychology` | 压抑 + 潜意识 | 压抑机制、物/词表象 |
| `freud-narcissism-identification` | 自恋导论 + 群体心理学 | 自恋类型、认同、群体力比多 |
| `freud-mourning-structure` | 哀悼与忧郁 + 自我与本我 + 纲要 | 结构模型、哀悼vs忧郁 |
| `freud-death-drive-repetition` | 超越快乐原则 | 强迫重复、死本能 |
| `freud-anxiety-civilization` | 抑制症状与焦虑 + 文明及其不满 | 焦虑信号、文明代价 |
| `freud-development-overview` | 图腾与禁忌 + 引论 | 俄狄浦斯全景、导航索引 |

## A2：典型触发场景

- 「用弗洛伊德的视角帮我分析下，我最近老是做同一个梦」→ 命中「反复做同一个梦」→ `freud-dreams-parapraxes`
- 「精神分析怎么看——我为什么总是这样，性格好像一直就很黏人、过度依赖」→ 命中「我为什么总是这样」「性格从哪来」→ `freud-sexuality-development`
- 「我越是想压下去，它反弹得越厉害」→ 命中「越压抑越反弹」→ `freud-metapsychology`
- 「医生查不出问题，可我就是不舒服」→ 命中「查不出原因的身体症状」→ `freud-trauma-hysteria`
- 「同事随口一句话，我却觉得自己一无是处」→ 命中「我不够好」→ `freud-narcissism-identification`
- 「我应该留下但我不想，整个人在和自已打架」→ 命中经典三模型「应该…但不想」→ 转发 `freud-classic-hub`
- 用户一段话里同时出现「控制不住发火」「觉得自己不配」「反复做梦」→ 跨 3 领域 → 🔴 CHECKPOINT 问是否用 `freud-complete`

## E：执行步骤

| 步骤 | 输入 | 操作 | 输出 |
|------|------|------|------|
| 1 | 用户原始消息 | 扫描是否命中经典三模型关键词 | 是 → 转发 `freud-classic-hub`；否 → 继续步骤2 |
| 2 | 过滤后的消息 | 按路由树匹配主题（关键词计数，最高命中即目标） | 目标 skill |
| 3 | 目标 skill | **🔴 CHECKPOINT**：输出路由决策 `→ freud-{target}（命中关键词：{具体词}）` | 等待用户确认 |
| 4 | 确认 | `read` 对应 skill 的 SKILL.md | 子 skill 内容 |
| 5 | 子 skill 结果 | 检查用户反馈 | 满意 → 结束；不满意 → fallback 表 |

- **步骤 1**：输入＝用户原始消息；输出＝是否转发 classic-hub。
- **步骤 2**：输入＝过滤后的消息；输出＝目标 skill。
- **步骤 3**：输入＝目标 skill；输出＝路由决策文本，等确认。
- **步骤 4**：输入＝用户确认；输出＝子 skill 内容。
- **步骤 5**：输入＝子 skill 结果；输出＝满意则结束，不满意则查 fallback。

### 🔴 CHECKPOINT：路由前确认

```
🔴 路由决策：→ freud-{target}（命中关键词：{具体词}）
如果路由错误，回复「不对」我将重新匹配。
```

### 子 Skill 路径速查

| Skill | 路径 |
|-------|------|
| `freud-trauma-hysteria` | `skills/freud-trauma-hysteria/SKILL.md` |
| `freud-dreams-parapraxes` | `skills/freud-dreams-parapraxes/SKILL.md` |
| `freud-sexuality-development` | `skills/freud-sexuality-development/SKILL.md` |
| `freud-metapsychology` | `skills/freud-metapsychology/SKILL.md` |
| `freud-narcissism-identification` | `skills/freud-narcissism-identification/SKILL.md` |
| `freud-mourning-structure` | `skills/freud-mourning-structure/SKILL.md` |
| `freud-death-drive-repetition` | `skills/freud-death-drive-repetition/SKILL.md` |
| `freud-anxiety-civilization` | `skills/freud-anxiety-civilization/SKILL.md` |
| `freud-development-overview` | `skills/freud-development-overview/SKILL.md` |
| `freud-classic-hub` | `skills/freud-classic-hub/SKILL.md` |
| `freud-complete` | `skills/freud-complete/SKILL.md` |

## B：边界与失败模式

### 失败模式分支表

| 触发条件 | 一线修复 | 仍失败兜底 |
|---------|---------|-----------|
| 用户说「不对，不是这个主题」 | 取次高分主题重新路由 | → 输出完整路由树让用户手动选 |
| 用户话太短无法判定主题 | 追问：「你最困扰的是哪个方面——(A)身体/症状 (B)梦/行为 (C)关系/性格 (D)焦虑/情绪 (E)反复的模式？」 | → 转发 `freud-complete` 做全量分析 |
| 用户描述含自杀意念 | 不路由，直接 12356 | → 提醒后可接 `freud-mourning-structure`（含自杀评估） |
| 子 skill 文件不存在 | 从速查表直接输出该模型的简要框架 | → 转发 `freud-complete` |

### 边界规则
- 本 Hub 只做路由，不做分析；一次只激活一个子 skill。
- 路由决策必须展示给用户确认，不替用户静默决定。
- 一级判别永远先跑——即使问题看起来不属于经典三模型，也先扫一遍。
- 跨 3+ 领域不硬塞进单一 skill，直接建议 `freud-complete`。

### 用户自查清单

- [ ] 是否已先跑一级判别（经典三模型）？
- [ ] 是否命中并只命中一个目标 skill？（或被判定为跨领域）
- [ ] 是否输出了 🔴 CHECKPOINT 路由决策并等用户确认？
- [ ] 是否扫描了自杀意念？（有 → 已转热线，未继续分析）
- [ ] 是否只 read 了目标子 skill，没有一次输出全部子 skill？

### 安全兜底（原文逐字保留）

如果用户表达自杀意念：
- **不分析、不解释**——这不是精神分析能处理的
- 提供：全国心理援助热线 12356
- 建议前往最近的精神卫生中心或急诊

## 练习手册

- **一次一题**：拿到任何笼统提问，先只写一句话判断「这属于哪套装置」，再看路由树核对——练「先判别、后路由」的手感。
- **关键词标注**：拿一段真实描述，逐词圈出触发词（如「反复做同一个梦」），数出命中主题，验证是否唯一命中。
- **跨领域演练**：故意写一段同时踩 3 个领域的描述，练习按规则输出 CHECKPOINT 而不是硬选一个。
- **反向练习**：给定一个目标子 skill，倒推「什么样的话会路由到这里」，用来检查路由树是否有盲区。

## 反例黑名单 —— 不要做的事

1. **不要跳过一级判别** —— 即使问题看起来不属于经典三模型，也先扫一遍
2. **不要把所有子 skill 都输出一遍** —— 一次只激活一个
3. **不要在用户话太短时猜一个主题** —— 追问 A/B/C/D/E
4. **不要在跨领域时假装单一主题能覆盖** —— 3+ 领域直接建议 freud-complete
5. **不要跳过 CHECKPOINT** —— 路由决策必须展示给用户确认
6. **不要在自杀意念出现时继续分析** —— 先给热线

## 灰色地带

1. **一句话同时踩两个相邻主题**：如「越压抑越反弹 + 每次都重蹈覆辙」——压抑反弹（metapsychology）与强迫重复（death-drive-repetition）本就相邻，按用户篇幅取主导，并明说关联项，不假装只有一个。
2. **经典三模型 vs 扩展主题的边界模糊**：如「我不配」（像忧郁）又「控制不住自己」（像结构冲突）——先按一级判别转发 `freud-classic-hub`，由其四维打分决定，不在本 Hub 提前裁定。
3. **用户拒绝确认路由**：不强行推进；给完整路由树让其手动选，或转 `freud-complete`。
4. **理论好奇 vs 个人深挖**：用户只想了解概念时不触发个人分析；若用户中途转入自身困扰，再按新信号重新路由。
5. **自杀意念夹杂理论提问**：无论问题多「学术」，只要出现意念，安全优先于路由——先给热线，不分析。
