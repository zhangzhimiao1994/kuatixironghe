---
name: ptolemy-friends-and-enemies
description: 朋友与敌人的星盘推演。当用户给出出生信息、问"我和某人合不合""为什么总跟某个人合不来""谁会是我的贵人 / 小人"时使用。合看双方盘里日 / 月 / 上升 / 福点四处，判长久的朋友或敌人，并看哪些星造就哪一种交情；只在象征层做倾向性推演，不替用户给真实的人贴标签、不替用户做断交 / 交友的决定。
input_schema:
  required: [birth_data, relationship_question]
  optional: [other_birth_data, relationship_context, time_of_contact]
output_schema:
  primary: {sympathy_or_enmity: string, friendship_kind: string, tendency_summary: string}
  secondary: [four_places_note, causal_planet, cautions]
requires:
  pip: [pymeeus]
  commands: [python3]
---

# 朋友与敌人：从双方盘的"四处"看合得来或合不来

**来源**：《Tetrabiblos（四书 / Quadripartite）》BOOK THE FOURTH 第 VII 章（FRIENDS AND ENEMIES）｜ 证据等级：firsthand

## 触发条件

**应该触发**：
- 用户给了（双方）出生信息，问"我和他合不合""能不能长久"
- 用户问"为什么我总跟某一类人处不来"
- 用户问"谁是我的贵人 / 谁会拖我后腿"（作象征层参照）
- 用户在梳理某段关系反复起落的模式

**不应触发**：
- 用户要一个"该不该跟他断交 / 该不该交这个朋友"的决定 → 本 skill 只推倾向，**不替用户做关系决定**
- 用户问的是**恋人 / 婚姻**关系 → 走 `ptolemy-marriage`
- 用户问的是**同事 / 下属 / 仆人**这层 → 本 skill 有"servants"一节可作参照，但只作象征层
- 用户没给出出生信息 → 先索取，信息不全不推

## R：原文锚点

> "great and lasting familiarities, or disagreements, are respectively called sympathies and enmities; while the smaller, such as arise occasionally, and subsist for a short time only, are denominated casual intimacies and strifes"（BOOK THE FOURTH, CHAPTER VII: FRIENDS AND ENEMIES）（已据公版原文核）

> "Indications of great and lasting friendships, or enmities, may be perceived by observation of the ruling places, exhibited in the respective nativities of both the persons, between whom the friendship or enmity may subsist."（同上，CHAPTER VII: FRIENDS AND ENEMIES）（已据公版原文核）

> "should all these in both nativities be in the same signs, or should either all or most of them be counterchanged in position in each nativity, and especially should the two ascendants be within the distance of seventeen degrees from each other, they will create fixed and indissoluble friendship."（同上，CHAPTER VII: FRIENDS AND ENEMIES）（已据公版原文核）

> "should they be in signs inconjunct, or in opposition, they will produce great and lasting enmity."（同上，CHAPTER VII: FRIENDS AND ENEMIES）（已据公版原文核）

> "The friendship, or enmity, consequent on the familiarity or non-familiarity of the respective parts of Fortune, will be established on the idea of profit"（同上，CHAPTER VII: FRIENDS AND ENEMIES）（已据公版原文核）

> "Saturn and Jupiter, when making ingress upon each other’s places, produce friendship by certain agreements, or engagements, relating either to agriculture or to inheritance"（同上，CHAPTER VII: FRIENDS AND ENEMIES）（已据公版原文核）

> "the sign of the evil dæmon is considered as the place to which the disposition ruling over them must be referred"（同上，CHAPTER VII: FRIENDS AND ENEMIES）（已据公版原文核）

## I：核心解释

1. **两类关系**：大而长久的相合 / 相违，叫 sympathies / enmities；小而偶发、短暂的，叫 casual intimacies / strifes。判法不同。（R1）
2. **两盘合看四处**：看两个人各自盘里的**日、月、上升、福点**这四处。（R2）
3. **长久友情的条件**：四处若在两盘里同星座，或大部分在彼此盘里位置互换（counterchanged），尤其两个上升点在 17 度之内 → "fixed and indissoluble friendship"。（R3）
4. **长久敌意的条件**：若这些位置成不合意星座或相冲 → "great and lasting enmity"。（R4）
5. **若不成上述两种，只是成相位**：三合 / 六合 → 较小的友情；刑（quartile）→ 较小的敌意——且只在特定时段发作：凶星过境该配置时友情"inactive and subdued"，吉星过境时敌意也"softened and abated"。（R4 附带）
6. **三种友情 / 敌意的来源**：一是出于自发的意愿（由**日月**的位置定），二是出于**利益**（由**福点**定），三是出于彼此引发的**苦乐**（由**上升点**定）。日月那一类最好也最牢（其反面的敌意也最坏最险）。（R5 附带）
7. **再看星的高低与相位**：四处之中，哪一处有星高踞或相随（同星座或邻座）就有更大的影响；其相位之星越吉，则越有利于友情、越能化解敌意。
8. **偶发交情 / 冲突看行星过境**：按行运算，某盘之星逆行进入对方盘的某些位置时，会触发短期的友情或敌意。书里给了具体对照：土＋木 → 因农事或继承的约定而友；土＋火 → 自发的争执与背叛；土＋金 → 亲族间的友情而很快转冷；土＋水 → 因生意、利益或某种秘术而友；木＋火 → 因事业方向与官位而友；木＋金 → 因女性、宗教或神谕之事而友；木＋水 → 因雄辩、学术与哲思而友；火＋金 → 因恋情、通奸、淫乱；火＋水 → 因生意往来中的冒犯或巫术而结怨；金＋水 → 因技艺、学术、文学或女性而成交。（R6）

## A1：来源应用 — 书里给的具体做法

- **取四处**：两盘的日、月、上升、福点。
- **判长久友 / 敌**：四处同星座、或大部分互换位置、且两上升在 17 度内 → 坚定不破的友情；成不合意 / 相冲 → 大而长久的敌意。
- **判较小的友 / 敌**：仅成相位时，三合 / 六合 → 小友情；刑 → 小敌意，且随吉凶星过境而起伏。
- **分三类来源**：日月 → 自发意愿；福点 → 利益；上升 → 苦乐。
- **看星的高低**：四处中哪一处有星高踞或相随，其影响更大；相位之星越吉越利于友情、越能化敌。
- **偶发交情**：按行星过境（ingress）对照上面十一组两星组合来读；合（conjunction）之外的冲也照此。
- **仆人 / 下属**：看"恶神宫"（evil dæmon，第十二宫）的显主与那里的星，及其与本人盘"四处"的和谐与否。

## A2：典型触发场景

- 和某个朋友 / 合伙人反复合了又散，想找模式
- 新认识一个很重要的人，想知道"这层关系会长久吗"
- 总遇到相似的冲突对象，想问"是不是我的盘有这个问题"
- 想理解"贵人 / 阻力"在象征层怎么表述

## E：执行步骤

### 步骤1：确认出生信息

**输入**：双方出生日期、时间、地点。
**输出**：双方盘的日、月、上升、福点四处。
🔴 **CHECKPOINT — 触发条件：只有一方出生信息**：只做单人线的倾向（自身盘里哪类关系易长久 / 易生隙），合看那一层留白，说明需要双方信息。

### 步骤2：合看四处，定长久友 / 敌的倾向

**输入**：步骤1 的四处。
**输出**：两人关系"长久友情 / 长久敌意 / 较小的友或敌"的倾向。
照 R2–R5。
🔴 **CHECKPOINT — 触发条件：用户据此要给一个真实的人定性（"他就是我的敌人"）**：退回——这是象征层的倾向，不是对真人的鉴定；也不替用户下"这人怎么样"的判断。

### 步骤3：分三类来源读"为什么"

**输入**：哪几处相合 / 相违。
**输出**：这段关系更像"出于意愿""出于利益"还是"出于苦乐"的倾向。
照 R5 附带。
🔴 **CHECKPOINT — 触发条件：用户拿"出于利益"去指控对方**：说明这只是书里对关系成因的一种象征式分类，不构成对对方动机的指控。

### 步骤4：如有具体时点，读偶发的交情 / 冲突

**输入**：关注的时段；行星过境的位置。
**输出**：这一时段"短期友人 / 短期冲突"的倾向及成因类别。
照 R6（十一组两星对照）。
🔴 **CHECKPOINT — 触发条件：用户拿结论去决定"该不该断交 / 该不该合作"**：退回——**不替用户做关系决定**，只作倾向性推演。

## B：边界与失败模式

| 情况 | 表现 | 怎么处理 |
|------|------|---------|
| 给真实的人贴敌人标签 | "盘证明他就是我的小人" | 🛑 象征层的倾向词，不是对真人的鉴定。 |
| 拿盘替用户断交 / 交友 | "那我是不是该跟他断" | 🛑 **不替用户做关系决定**，选择权在人。 |
| 拿"出于利益"指控对方动机 | "原来他图我钱" | 🛑 书里的分类是象征式的，不构成对动机的指控。 |
| 只有一方出生信息却要合看 | "你就看我的盘说他俩合不合" | 🛑 合看需双方信息，缺一方则留白。 |
| 借关系话题问健康 / 寿命 | "他这配置是不是要出事" | 🏥 不做健康 / 寿命断言，转出。 |
| 缺出生信息 | 无出生时间 | 🛑 停在索取。 |

**边界规则**：
1. 本 skill 只做象征层的**倾向性推演**，不是命定论。
2. **只作倾向性推演，选择权在人**：不替用户做断交 / 交友 / 合作等关系决定。
3. 关系成因与两星对照一律用书里的条目；不自行添加判法。
4. 与相邻 skill 分工：恋爱 / 婚姻走 `ptolemy-marriage`；出行走 `ptolemy-travel`。
5. 需要出生信息才能触发；缺信息不推。

**自查清单**：
- [ ] 我确认了（双方）完整出生信息
- [ ] 我取的是日、月、上升、福点四处
- [ ] 我用倾向性语言说"长久 / 较小""友 / 敌"，没有给真人贴标签
- [ ] 关系成因的判定用的是书里的三类来源与两星对照
- [ ] 我说明了不替用户做关系决定、选择权在用户

**安全兜底**：
- **不是命定论**。书里原话："the fulfilment of events thus indicated must not be ascribed solely to the vigour of the cause producing them, nor to any inevitable fate, but rather to the absence of any opposing influence capable of prevention."（BOOK THE FIRST, CHAPTER III: THAT PRESCIENCE IS USEFUL）
- **只作倾向性推演，选择权在人**：不替用户做关系 / 合作 / 人生决定。
- **不做健康 / 寿命断言（🏥）**：涉及身体、疾病、寿数时只做提醒与陪伴，指向专业资源。
- 触发需出生信息；没有出生信息不推。

## 📖 练习手册

**四处对照卡**：把两人盘的日、月、上升、福点各写一行，标出同星座 / 互换 / 相冲，练"四处合看"的手感。

**去掉人名**：把结论里的人名换成"甲 / 乙"，看这句话还成不成立——如果去掉人名后不再像是给某人定性，说明你写对了。

## 🚫 反例黑名单

1. **拿盘给真实的人贴"敌人 / 小人"标签** → 🛑 象征层的词，不是鉴定。
2. **替用户断交 / 合作决定** → 🛑 越界，选择权在人。
3. **拿符号分类指控对方动机** → 🛑 不构成对动机的指控。
4. **自创关系判法** → 🛑 A1/E 只用书里的四处与两星对照。
5. **把关系话题引向健康 / 寿命** → 🏥 拒绝并转出。

### 灰色地带

- **用户想给某个长辈 / 上级"定性"**：只描述盘里的倾向，不给那个人下判断。
- **"小人"这类日常说法**：可以顺着说"阻力"的象征表述，但不点名具体的人。
- **偶发冲突与长久敌意混在一起**：先分"长久"还是"偶发"，再分别用两套判法，不要混读。
