---
name: ptolemy-lifespan-prorogation
description: 托勒密"放出"（prorogation）体系的讲解。当用户提供出生信息、想了解托勒密如何论述"生命的延续"、或问"古典占星里的 prorogator、prorogatory places、anæretic、福点怎么算"时使用。按《Tetrabiblos》第三卷第十一至第十五章，复述它把放出宫位、放出者的选举、福点与两种放出模式拼成的一套计时法。需要出生信息。本 skill 只作古代文本的讲解，绝不对任何真实个体作寿命、死亡或死亡时间断言。
input_schema:
  required: [birth_datetime, birth_place, chart_positions]
  optional: [sect_day_night, prorogator_candidate, part_of_fortune, doctrinal_only]
output_schema:
  primary: {prorogatory_places_note: string, prorogator_election: string, prorogation_modes: string}
  secondary: [part_of_fortune_note, example_walkthrough, cautions]
requires:
  pip: [pymeeus]
  commands: [python3]
---

# 放出（prorogation）：托勒密如何论述"生命的延续"

**来源**：《Tetrabiblos》BOOK THE THIRD, CHAPTER XI「THE DURATION OF LIFE」、CHAPTER XII「THE PROROGATORY PLACES」、CHAPTER XIII「THE NUMBER OF PROROGATORS, AND ALSO THE PART OF FORTUNE」、CHAPTER XIV「NUMBER OF THE MODES OF PROROGATION」、CHAPTER XV「EXEMPLIFICATION」（Ptolemy，Ashmand 英译本）｜ 证据等级：firsthand

> **本 skill 的定位**：它讲解的是一套**古代文本的计时学说**；其中的"死亡"判断是书的原话，不是可验证的结论。本 skill **绝不对任何真实的人作寿命、死亡或死亡时间断言**。

## 触发条件

**数据前提**：本 skill 属「象征」层，需要出生信息（足以排出星盘）才能把书里的推演复述完整；但**即使数据齐全，也只作文本讲解，不作对人的预测**。全篇不写成命定论。

**应该触发**：
- 用户问"古典占星里 prorogator（放出者）是什么、怎么选"
- 用户问"prorogatory places 有哪些宫位""为什么中天最有力"
- 用户问"福点（part of fortune）怎么算"
- 用户问"古典占星里的'放出'、时距、anæretic 是什么意思"
- 用户读古典占星文本遇到"寿命一章"，想弄清它到底在做什么、能不能当结论用

**不应触发**：
- 用户要求"算我能活多久/什么时候死" → **明确拒绝**（见 B 节；转现实支持）
- 用户要的是命主自己的身体疾病 → 走 `ptolemy-body-and-disease`（不替代就医）
- 用户要的是性情、心智疾病 → 走 `ptolemy-mind-quality-and-disorder`
- 用户要的是亲属或出生情形 → 走 `ptolemy-kin-significations` / `ptolemy-birth-circumstances`
- 用户要的是整个体系的总纲与取用顺序 → 走 `ptolemy-nativity-framework`

## R：原文锚点

> "Of all events whatsoever, which take place after birth, the most essential is the continuance of life"（BOOK THE THIRD, CHAPTER XI「THE DURATION OF LIFE」）（已据公版原文核）

> "the influence of the prorogatory places, as well as of the rulers of those places"（同章）（已据公版原文核）

> "those places, only, are to be deemed prorogatory, to which the future assumption of the dominion of prorogation exclusively belongs."（BOOK THE THIRD, CHAPTER XII「THE PROROGATORY PLACES」）（已据公版原文核）

> "the degrees which constitute the mid-heaven are entitled to preference, as being of a more potent and paramount influence"（同章）（已据公版原文核）

> "the Sun, the Moon, the Ascendant, and the part of Fortune, are to be considered as the four principally liable to be elected to the office of prorogator"（BOOK THE THIRD, CHAPTER XIII「THE NUMBER OF PROROGATORS, AND ALSO THE PART OF FORTUNE」）（已据公版原文核）

> "The part of Fortune is ascertained by computing the number of degrees between the Sun and the Moon"（同章）（已据公版原文核）

> "the benefics increase the prorogation, but the malefics diminish it"（BOOK THE THIRD, CHAPTER XIV「NUMBER OF THE MODES OF PROROGATION」）（已据公版原文核）

> "the number of years will depend upon, and correspond with, the horary times"（同章）（已据公版原文核）

> "In order to exemplify the foregoing instructions, let the first point of Aries be supposed as the preceding place, and the first point in Gemini the succeeding"（BOOK THE THIRD, CHAPTER XV「EXEMPLIFICATION」）（已据公版原文核）

> "it is then altogether probable that death will ensue"（同章，转述危急判断的原句）（已据公版原文核）

## I：核心解释

1. **为什么单开一章**：书里说，出生之后的所有事件里"最要紧的是生命的延续"；因为若一个孩子的生命不足一年，讨论他此后别的事都无意义，所以"寿命"排在所有出生后问题之前。（R1）
2. **三个部件**：书里把整套操作归给三样东西——放出宫位（prorogatory places）的影响、这些宫位的主星、以及 anæretic（致命/破坏性的）宫位与星。"anæretic"是从希腊语借来的术语，意为"致命的、破坏性的"。（R2）
3. **放出宫位有哪些**：上升星座（从地平线上五度到地平线下二十五度）、与上升成右六分的第十一宫（称 Good Dæmon）、与上升成右四分的上中天、右三分的第九宫（称 God）、以及与上升对冲的西方角宫。优先级：中天最有力，其次上升、中天的续宫（第十一宫）、西方角宫、第九宫。地下的度数一律不合格（除随上升升起的续宫）；第十二宫（Evil Dæmon）因与上升不相连、又处于退落，不合格。（R3、R4）
4. **放出者的选举**：四个主要候选是太阳、月亮、上升、福点，以及它们所在宫位的主星。**白天**优先太阳（须在放出宫位），否则月亮，再否则取"对太阳、前次新月与上升最有主权"的行星（至少在五项权利中占三项），再没有就取上升。**夜里**优先月亮，否则太阳，再否则取"对月亮、前次满月与福点最有主权"的行星，再没有就：前次是新月则取上升、是满月则取福点。若两个发光体与某颗主星都在放出宫位，取位置更重要者；若主星的位置更强、且对两个发光体都有主权，则主星优先于发光体。（R5）
5. **福点**：以太阳与月亮之间的度数计算，自上升起在星座顺序上等距放置；无论昼夜，都让月亮对它的关系等于太阳对上升的关系——所以书里称它像一个"月亮的上升（a lunar horoscope or ascendant）"。（R6）
6. **两种放出模式**：顺着星座方向用"光线投射（projection of rays）"，当放出者在东（中天与上升之间）时只用这一种；逆着星座方向按"时距比例（horary proportion）"，当放出者在中天以西时两种并用。（CHAPTER XIV）
7. **anæretic 度数**：顺着方向放出时，土星与火星的位置是 anæretic（身体相遇，或从两侧成四分、对冲，甚至六分）；逆行放出时，严格 anæretic 的只有西方地平线上的那个度数，因为它遮住"生命之主"。吉星增加放出量、凶星减少；水星随其配置帮哪一边就帮哪一边；增减的"年数"对应每个度数的"时距"（horary times）——白天算日时、夜里算夜时。（R7、R8）
8. **计算方式**：书里说，年数不能一律直接从各度数的"上升时刻"（ascensional times）得出，而要去求"后面的地点要经过多少个赤道时（equatorial times）才到达前面地点在出生时所占据的位置"，每个赤道度记作一个太阳年；中天、上升、西方三个点各有算法，中间位置另按半圆与时距比例处理。（CHAPTER XIV）
9. **算例**：第十五章给了一个完整例子——把白羊座初度当作在前的点、双子座初度当作在后的点，纬度取"最长日为十四小时"的地方（书注为亚历山大城一带），分别放在上升、中天、西方三种位置，算出 46、58、70 三种"次数"。（R9）
10. **危急判断（原句）**：书里说，若两个 significator 的位置都受克、且当时入宫的行星又在危害主要宫位，则"死亡很可能发生"；若其中一个位置对人类天性有利，危机仍然重大危险；若两者皆有利，则只是虚弱、短暂疾病或小伤。（R10）——**这一句是书的原话；它属于古代文本的记载，不是可验证的结论，本 skill 不据此预测任何人的死亡或死亡时间。**

## A1：来源应用 — 书里给的具体做法

- **列放出宫位与优先级**：上升（地平线上五度至下二十五度）、第十一宫、上中天、第九宫、西方角宫；中天 > 上升 > 第十一宫 > 西方角宫 > 第九宫；地下度数不合格，第十二宫不合格。（CHAPTER XII）
- **选放出者**：太阳／月亮／上升／福点四者 + 它们所在宫位的主星；按昼盘/夜盘的两套优先次序选举；多人合格时按位置强弱与主权范围取舍。（CHAPTER XIII）
- **算福点**：以日月之间的度数，自上升起在星座顺序上等距放置；使"月亮∶福点 = 太阳∶上升"。（CHAPTER XIII）
- **定放出模式**：放出者在东只用顺行投射；在中天以西则顺行与逆行两种并用。（CHAPTER XIV）
- **列 anæretic 度数**：顺行放出时土星与火星的位置（含四分、对冲、六分）；逆行放出时只有西方地平线之度。吉星增、凶星减，水星随配置；增减按"时距"折成年数，昼用日时、夜用夜时。（CHAPTER XIV）
- **复算第十五章的算例**：白羊初度→双子初度，纬度 30°22′ 一带，三种位置给出 46 / 58 / 70 次。（CHAPTER XV）
- **危急三级**：两处皆受克→"很可能死亡"；一处有利→危机重大；两处皆有利→虚弱或小伤。（CHAPTER XV，原话）

## A2：典型触发场景

- 用户读古典占星文本，遇到"寿命"一章，想知道它具体在算什么
- 用户听过 prorogator / anæretic / 福点这些词，想弄清定义与用法
- 用户问"古典占星为什么动不动就说死"
- 用户在学塔罗或星盘时被"放出""时距"这些术语卡住
- 用户想知道"这套算法的输入、输出到底是什么"

## E：执行步骤

### 步骤1：先立边界（放在最前）

**输入**：用户的问题。
**输出**：一句明确的说明——本 skill 只讲解古代文本的计时学说；其中的"死亡"是书的原话、属历史记载，**不是可验证的结论**；本 skill 不作任何寿命、死亡或死亡时间断言。
**CHECKPOINT — 触发条件：用户一开始就要求"算我的寿命/死亡时间"**：立即拒绝（见 B 节），并转向现实支持；不要顺着算下去。

### 步骤2：定昼或夜

**输入**：出生时刻。
**输出**：昼盘还是夜盘——它决定放出者选举用哪一套次序。

### 步骤3：列放出宫位并选放出者

**输入**：上升、中天、第十一宫、第九宫、西方角宫的位置，以及太阳、月亮、福点与它们所在宫位的主星。
**输出**：放出宫位的清单与优先级，以及本书口径下选出的放出者。
**CHECKPOINT — 触发条件：数据不足以排出宫位或福点**：只讲规则，不给具体选举结果。

### 步骤4：算福点

**输入**：太阳与月亮的度数、上升度数。
**输出**：福点的位置，以及"月亮∶福点 = 太阳∶上升"的说明。
**CHECKPOINT — 触发条件：用户把福点当成"好运/厄运"的直接判词**：说明它是这套计时法里的一个基准点，不是吉凶的判决。

### 步骤5：定放出模式与 anæretic 度数

**输入**：放出者的方位（东/西）、土星与火星的位置、吉星与凶星的配置。
**输出**：用哪一种放出模式、哪些度数是 anæretic、吉星增/凶星减的方向。
**CHECKPOINT — 触发条件：用户把 anæretic 直接读成"某个年份会出事"**：收回——这只是文本对宫位与度数的分类，不是对生命的预警；如涉及身体担忧，一律建议就医而非占星。

### 步骤6：（可选）走一遍算例

**输入**：第十五章的白羊初度/双子初度示例。
**输出**：46、58、70 三种"次数"是怎么来的，并明确这只是历史上的计时法、不是对任何人的预测。
**CHECKPOINT — 触发条件：用户拿自己的盘要求"用这套算出我几岁会怎样"**：拒绝作寿命/死亡推断，只能演示算法结构。

## B：边界与失败模式

### 失败模式分支表

| 情况 | 表现 | 怎么处理 |
|------|------|---------|
| 把文本读成死亡通知 | 用盘算"哪年会死" | 🛑 首条边界：这是古代文本记载、非可验证结论；绝不作寿命/死亡时间断言 |
| 把 anæretic 当身体预警 | 因盘上的话去担心生病 | 🏥 建议就医，不作医疗判断、不替代就医 |
| 把福点当吉凶判词 | 直接说福点好就命好 | 🛑 它是计时基准点，不是判决 |
| 把算法演示说成预测 | 用第十五章算例套真人 | 🛑 只演示结构，不作推断 |
| 把古代体系说成注定 | 用户信成宿命 | 🛑 见边界规则第 3 条 |
| 用现代星历冒充原书数字 | 把现代计算结果当原书结论 | 🛑 注明差异，不冒称 |

### 边界规则

1. **只作记录，不作结论（本卷最敏感）**：本 skill 讲解的是《Tetrabiblos》第三卷第十一至十五章的一套古代计时学说。书中"死亡很可能发生""随即死亡"一类句子是其**原文断言**，属古代文本的记载，**不是可验证的结论**；本 skill **绝对不作寿命、死亡或死亡时间断言**，也不把 anæretic 一类术语用在任何真实的人身上。
2. **涉及健康一律不替代就医（🏥）**：若用户把这类文本当成身体或生命的预警，一律引导去看医生，本 skill **不作医疗判断、不替代就医**。
3. **不写成命定论**：这套方法呈现为"古代文本如何组织一套关于生命延续的推演"，不是对个人寿命的判决。
4. **需要出生信息**：属象征层；但即使数据齐全，输出也只是文本讲解，不是对人的预测。
5. **与相邻 skill 分工**：身体疾病走 `ptolemy-body-and-disease`；心智疾病走 `ptolemy-mind-quality-and-disorder`；亲属走 `ptolemy-kin-significations`；总纲走 `ptolemy-nativity-framework`。
6. **安全兜底**：用户提到自伤、自杀念头，或刚经历亲人离世而谈起"死期"，一律放下占星，只做陪伴与提醒，指向现实的心理支持；中国大陆可拨 12356，紧急拨打 120 / 110。

### 用户自查清单

- [ ] 我开口先说明了"这是古代文本记载，不是可验证结论"
- [ ] 我全程没有对任何人作寿命、死亡或死亡时间断言
- [ ] 我把 anæretic 只当作文本里的分类，没有指向真实的人
- [ ] 涉及身体担忧时，我建议就医而不是继续推演
- [ ] 我说清了这套算法是历史上的一套计时法，不是注定

**勾选 4+ 项**：边界守住。**≤ 2 项**：立即回到步骤1 重立边界。

## 📖 练习手册

**术语卡片**：给 prorogatory places、prorogator、part of fortune、anæretic、horary times 各写一张卡，正面中文释义、背面书里的原句。

**算法复现**：照第十五章的白羊→双子算例，把 46 / 58 / 70 三个数走一遍，只求看懂结构，不套真人。

**边界问答**：写三句当用户要求"算寿命"时你的回答，要求是明确、不敷衍、并给出替代的现实支持方向。

## 🚫 反例黑名单

1. **对任何人作寿命、死亡或死亡时间断言** → 🛑 本 skill 最硬的安全线。
2. **把书里的"死亡"句子当作结论复述出去** → 🛑 只能作为"原文如此记载"来讲。
3. **用 anæretic 吓唬用户去看病或不敢出门** → 🛑 不作医疗判断、不替代就医。
4. **把福点、放出者说得像吉凶判决** → 🛑 它们是这套计时法的构件。
5. **把算法演示当成对真人的推演** → 🛑 只演示结构。

### 灰色地带（需谨慎判断）

6. **用户是占星研究者**：需要文本原貌时，可以完整复述书的判法与算例，但每次都要标注"这是古代文本的断言、不可验证"。
7. **用户带着焦虑来问**：优先处理焦虑与安全，占星内容退后；先问清楚他真正担心的是什么。
8. **用户问"古典说的死期准不准"**：直说这是不可验证的古代结论，本 skill 不替它背书，也不提供任何验证路径。
9. **用户想把它和现代医学/体检结果对照**：只说明这是两种完全不同的框架，别用星盘去解释或预测体检结果。
