---
name: habit-least-effort
description: 最省力法则。当用户"好习惯太难开始、环境处处添堵、想戒的坏习惯伸手就能做"，因为阻力太大而失败时使用。用 addition by subtraction 减少好习惯的摩擦、给坏习惯制造即刻不便，并把环境预备好，让对的事变成阻力最小的那条路。
input_schema:
  required: [target_good_habit, friction_points, current_environment]
  optional: [bad_habit_to_block, daily_route, past_failures]
output_schema:
  primary: {friction_audit, reduce_steps_plan, prime_environment_plan}
  secondary: [bad_habit_friction_plan, environment_reset_ritual, cautions]
---

# 最省力法则：把对的事变成阻力最小的那条路

**来源**：《Atomic Habits》第12章 The Law of Least Effort ｜ 证据等级：firsthand

## 触发条件

**应该触发**：
- 用户说"我知道该做，但每次要开始都太麻烦、太费劲了"
- 好习惯路径上障碍很多：器材不在手边、要专门绕路、要准备很久
- 用户说"我想戒的坏习惯，手一伸就能做"（刷手机、零食、电视）
- 用户抱怨环境太乱、静不下心、家里坐不住
- 用户问"怎么让好习惯毫不费力地发生、怎么让坏习惯变麻烦"

**不应触发**：
- 用户连一个带提示的启动句都还没有，要的是"何时何地开始" → 走 habit-starter-design
- 用户要的是"哪一环断了"的机制诊断 → 走 habit-four-laws-audit
- 用户想做一次性锁死未来行为、自动化、让坏习惯不可能 → 走 habit-commitment-device
- 用户要的是公开代价、找人监督、签契约 → 走 habit-accountability-contract
- 用户在纠结"该选哪个习惯、哪个赛道" → 走 habit-talent-fit
- 用户处在成瘾急性期或抑郁，只想靠藏东西硬扛 → 先转 B 节安全分支

## R：原文锚点

> "Energy is precious, and the brain is wired to conserve it whenever possible. It is human nature to follow the Law of Least Effort, which states that when deciding between two similar options, people will naturally gravitate toward the option that requires the least amount of work."（第12章）（已据原文核）

> "Out of all the possible actions we could take, the one that is realized is the one that delivers the most value for the least effort. We are motivated to do what is easy."（第12章）（已据原文核）

> "Trying to pump up your motivation to stick with a hard habit is like trying to force water through a bent hose. You can do it, but it requires a lot of effort and increases the tension in your life. Meanwhile, making your habits simple and easy is like removing the bend in the hose. Rather than trying to overcome the friction in your life, you reduce it."（第12章 · HOW TO ACHIEVE MORE WITH LESS EFFORT）（已据原文核）

> "I like to refer to this strategy as addition by subtraction."（第12章 · HOW TO ACHIEVE MORE WITH LESS EFFORT）（已据原文核）

> "The central idea is to create an environment where doing the right thing is as easy as possible. Much of the battle of building better habits comes down to finding ways to reduce the friction associated with our good habits and increase the friction associated with our bad ones."（第12章）（已据原文核）

> "It is remarkable how little friction is required to prevent unwanted behavior."（第12章 · PRIME THE ENVIRONMENT FOR FUTURE USE）（已据原文核）

> "Redesign your life so the actions that matter most are also the actions that are easiest to do."（第12章）（已据原文核）

## I：核心解释

1. **人性默认走阻力最小的路**：书里把"面对两个相近选项时自然挑更省力的那个"叫 Law of Least Effort。这不是懒——书里说这是 "a smart strategy, not a dumb one"，能量宝贵，大脑被设计成能省就省。（R1）
2. **努力越大的行为越不会发生**：每个动作都要耗能，耗能越多越难发生。书里的对比是"每天一百个俯卧撑"和"每天一个俯卧撑"——"the less energy a habit requires, the more likely it is to occur"。（R2）
3. **习惯本身是障碍，你真正要的是它带来的结果**：节食是健身的障碍，冥想是平静的障碍。摩擦越大，你和想要的结果之间隔得越远，所以要"make your habits so easy that you'll do them even when you don't feel like it"。（R2、R3）
4. **别去硬顶摩擦，要减掉摩擦**：书里用弯折的水管打比方——你可以拧大阀门硬泵（靠意志力扛），也可以把弯折解开让水自然流（减摩擦）。"Rather than trying to overcome the friction in your life, you reduce it."（R3）
5. **addition by subtraction**：借日本"lean production"——逐个找出流程里的摩擦点并消掉，减掉浪费反而加出效率和收益。放到生活里就是：去掉消耗你时间和精力的摩擦点，就能"achieve more with less effort"。（R4）
6. **核心是一句话：把对的事变容易，把错的事变难**：书里把整场仗归结为"reduce the friction associated with our good habits and increase the friction associated with our bad ones"。两头都要动，不是只减不减。（R5）
7. **很少的摩擦就够挡住一个行为**：把啤酒藏到冰箱深处看不见、把社交 App 删掉，行为就会变。"a little bit of friction can be the difference between sticking with a good habit or sliding into a bad one"。（R6）
8. **收尾是那句设计问题**：无论个人、家长、教练还是领导，都该问"How can we design a world where it's easy to do what's right?"——把最重要的动作同时变成最容易做的动作。（R7）

## A1：来源应用 — 书上给的具体做法

- **减少好习惯的摩擦**（第12章 · HOW TO ACHIEVE MORE WITH LESS EFFORT）：
  - 习惯地点选在**你日常动线上**：书里说把健身房选在上班路上，顺路就不算"out of your way"；偏离几个街区，就变成专门绕路。
  - 先承认很多人**故意在高压摩擦环境里起新习惯**（在饭局上节食、在吵闹的家里写书、边玩手机边专注），书里说"It doesn't have to be this way"。
  - 英国政府把报税从"给一个可下载表格的网页"改成**直接链到表格**，少一步就把回复率从 19.2% 提到 23.4%。
- **预备环境**（第12章 · PRIME THE ENVIRONMENT FOR FUTURE USE）：
  - Oswald Nuckols 的 **"resetting the room"**：看完电视把遥控器放回、靠垫摆好、毯子叠好；下车就丢垃圾；洗澡前趁水热擦马桶。目的不只是收拾，是**为下一个动作做铺垫**。
  - 妻子把**贺卡按场合预分类**放一盒，要寄时顺手抽一张；作者对照自己"想寄卡却总忘"，差别就在摩擦。
  - 书里列的一串预备：前一晚把锅、喷油、餐具摆好；把画笔纸本摊在桌上随手可及；把运动服、鞋、包、水壶提前拿出来；周末切好一堆果蔬装盒，工作日随手拿。这些都是"make the good habit the path of least resistance"。
- **给坏习惯加摩擦**（第12章 · PRIME THE ENVIRONMENT FOR FUTURE USE）：
  - 书里给了个**逐级加码的梯子**（以看电视为例）：先完全拔掉电源 → 若要再看必须说出节目名；不够就**连遥控器电池也取下来**，多花十秒才能开；再狠就把电视**搬出客厅收进壁橱**，只有真想看才搬出来。"The greater the friction, the less likely the habit."
  - 作者自己：上午把**手机留在另一个房间**直到午餐，摩擦高到"没有理由就不会去拿"，于是上午能有三四个小时不被打断；不够还可以**请朋友或家人把手机藏起来几个小时**。
  - 书里还说：把啤酒藏到冰箱深处就少喝；把社交 App 从手机删掉，常常要好几周才会再下回来。
- **Chapter Summary 的五条清单**（第12章）：① 人天然 follow the Law of Least Effort；② 造一个"对的事尽可能容易"的环境；③ 减少好行为的摩擦，摩擦低习惯就易；④ 增加坏行为的摩擦，摩擦高习惯就难；⑤ 预备环境让未来动作更易。

## A2：典型触发场景

- 想晨跑，但跑鞋在柜子最深处、要穿十分钟装备
- 想做饭，但冰箱里没有处理好的食材，只好点外卖
- 想读书，但书在另一个房间，手机就在手边
- 想少刷短视频，却每次解锁先点开 App
- 书桌堆满东西，坐下来就烦，专注不了
- 想早睡，但平板就放在床头充电

## E：执行步骤

### 步骤1：摩擦审计——找出好习惯路径上的每个摩擦点

**输入**：用户的目标好习惯，以及它现在的发生方式。
**输出**：一张"从想做→到真正做完"的分步清单，标出每一步的摩擦。

把行为拆成一步一步：起念 → 找东西 → 准备 → 开始 → 做完。逐条问"这一步会不会让我想放弃、多花力气？"书里的秤是"The more energy required, the less likely it is to occur"。（R2）

🔴 **CHECKPOINT — 触发条件：摩擦点超过三四个，或根本找不到"起点动作"**：说明这个习惯的粒度太大 → 要么先把它压到一个最小动作，要么转 habit-starter-design 先定一个带提示的启动句，再回来减摩擦。

### 步骤2：addition by subtraction——减掉好习惯路径上的步骤

**输入**：步骤1 的摩擦清单。
**输出**：reduce_steps_plan（少几步、哪几步、怎么少）。

逐条把摩擦点消掉或合并：把习惯放在**日常动线上**（顺路的健身房、上班前顺手做），把要用的东西**放到必经之路上**。一次只求少一步，不是重排人生。

🔴 **CHECKPOINT — 触发条件：用户想全靠意志力把摩擦顶过去（"我就逼自己一下"）**：拉回 R3 的水管比喻——硬泵是增摩擦，越顶越紧；改成减掉那个弯折。摩擦是设计问题，不是毅力问题。

### 步骤3：预备环境——为下一个动作做铺垫

**输入**：reduce_steps_plan。
**输出**：prime_environment_plan（前一晚、或前一动作做完时，顺手要做的一件预备动作）。

用 resetting the room 的思路：每次动作结束后不是只收尾，而是**为下一步摆好台**（前一晚摆好锅具；出门前把运动包放门口；周末切好果蔬）。让未来那个"开始"变得不费劲。

🔴 **CHECKPOINT — 触发条件：用户觉得"预备太麻烦、我做不到"**：把预备动作**挂到已经会做的动作后面**并缩到一步（洗完澡顺手把明天的衣服拿出来）。若连一步都排不动，先回 habit-starter-design 建"现身"的习惯，或转 B 节看是不是状态问题。

### 步骤4：给要戒的坏习惯加摩擦

**输入**：用户想减少的坏习惯，以及它现在有多顺手。
**输出**：bad_habit_friction_plan（用加码梯子给一档或几档摩擦）。

用书里的逐级梯子：先加**一点点**摩擦（拔插头、挪远、退出登录），不够再加（取电池、藏起来、搬走）。本 skill 只做**环境摩擦**；若要对行为本身加不可逆的限制，转 habit-commitment-device。

🔴 **CHECKPOINT — 触发条件：要戒的是成瘾性行为（酒精、赌博、强效药物）或出现戒断风险**：停，不靠藏东西硬扛 → 转 B 节安全分支，指向专业支持。书里也明说这些小招"unlikely to curb a true addiction"。（R6）

### 步骤5：用"阻力最小路径"验证

**输入**：以上四步的产出。
**输出**：过审的方案，或标注还要减哪一处。

实地走一遍：假设你现在最累、最没动力，这条路径还能不能走通？书里的标准是"make your habits so easy that you'll do them even when you don't feel like it"。（R3）

🔴 **CHECKPOINT — 触发条件：用户为了"减摩擦"把要做的事也缩没了（"每天跑一公里"变成"看一眼跑鞋"）**：区分**减摩擦**与**降目标**——减摩擦是把同一件事的入口变轻，不是把事取消。若用户其实需要的是缩小目标，转 habit-starter-design。

## B：边界与失败模式

### 失败模式分支表

| 情况 | 表现 | 怎么处理 |
|------|------|---------|
| 只减好习惯的摩擦，不管坏习惯 | 环境全为好事优化，坏事照样伸手就做 | 🛑 回到 R5/R6：两头都要动。补上步骤4，给坏习惯加摩擦。 |
| 拿"减摩擦"当借口降低标准 | 目标越缩越小，最后什么也没做 | 🛑 区分减摩擦与降目标：入口可以变轻，事还是要做；要缩目标走 habit-starter-design。 |
| 想用环境改造一次性解决一切 | 大动干戈重排全屋或全流程，执行不动 | 🛑 回到 addition by subtraction：一次减一步，累积比大改可行。 |
| 靠摩擦硬扛成瘾 | 想用藏酒、删 App 戒掉真成瘾 | 🛑 书里明说这些小招不能治真瘾 → 转 B 节安全分支，指向专业资源。 |
| 把摩擦当道德审判 | "连这都嫌麻烦，就是懒" | 🛑 书里说走省力路是聪明的策略，不是懒。去掉评判，只谈设计。 |
| 环境动了，提示却没变 | 东西摆好了，用户还是想不起来做 | 🛑 这可能是缺提示而非缺摩擦 → 转 habit-starter-design 定执行意图或习惯堆叠。 |
| 反复优化环境却从不行动 | 一直在"布置"，就是不开始 | 🛑 书里点名的 motion vs. action 陷阱（第11章）：优化是手段，行动才是目的。 |

### 边界规则

1. **两头都要动**：减少好习惯摩擦 + 增加坏习惯摩擦，缺一不可（第12章）。
2. **一次减一步**：addition by subtraction 是逐点消摩擦，不是一次重排人生。
3. **减摩擦不等于降目标**：入口变轻，事照做；要缩小目标走 habit-starter-design。
4. **摩擦只治"顺手"，不治成瘾**：真成瘾与戒断风险交专业资源。
5. **不做好坏评判**：省力是人性策略，不做道德指责。
6. **不越界到自动化与契约**：要一次性锁死未来或让别人监督，分别转 habit-commitment-device / habit-accountability-contract。

### 用户自查清单

- [ ] 我能列出好习惯路径上的**具体摩擦点**，且不超过三四个
- [ ] 我至少**减掉了其中一步**，或把习惯挪到了日常动线上
- [ ] 我有一个**前一晚或前一动作就做好的预备动作**
- [ ] 我给了要戒的坏习惯**至少一档加摩擦**（拔插头、挪远、退出登录）
- [ ] 假设我此刻最累，这条路径**还能走通**
- [ ] 我没有把"减摩擦"用成"降目标"

**勾选 5+ 项**：环境已站在你这边。**≤2 项**：多半停在"只想不做"或"只减好事不治坏事"——回对应步骤。

**安全兜底**：涉及就医、用药、成瘾戒断或心理危机时，只做提醒与陪伴，不做诊断。书里明说环境小招"unlikely to curb a true addiction"；遇到真成瘾或戒断风险，指向专业医疗与心理服务。

## 📖 练习手册

1. **数步骤**：把你想做的那个习惯，从"起念"到"做完"数出来几步；每步后面标一个"+"（增加摩擦）或"−"（减少摩擦）。目标是把净摩擦往"−"推。
2. **resetting the room**：选一个房间，每次做完一件事就顺手为下一件事摆好台（看完电视收遥控、铺毯；洗完澡擦马桶；下车丢垃圾）。坚持一周，体会"proactively lazy"给回的时间。
3. **加摩擦梯子**：给一个想减少的行为列三档越来越麻烦的做法（拔、取、搬），先从第一档开始。

## 🚫 反例与黑名单

1. **只减好习惯摩擦、给坏习惯一路开绿灯** → 🛑 两头都要动（R5）。
2. **把"减摩擦"做成"降目标"甚至取消** → 🛑 入口变轻，事照做。
3. **靠藏东西、删 App 硬戒真成瘾** → 🛑 这些招不治真瘾，转专业资源。
4. **把省力说成懒、加道德评判** → 🛑 书里说这是聪明策略。
5. **用"先优化环境"代替真正开始** → 🛑 motion vs. action，优化是手段不是目的。
6. **一次重排全屋、全流程** → 🛑 一次减一步，累积才可行。

### 灰色地带（需谨慎判断）

7. **摩擦来自现实生活压力而非环境**（照护、夜班、经济压力）→ 先承认约束，只在能动的范围里减摩擦，不把结构性问题说成个人不努力。
8. **用户想把环境摩擦用于"疑似成瘾"** → 区分"顺手多做了"和"临床成瘾"；后者不靠自己藏东西，交专业评估。
9. **"减摩擦"与"缩小目标"的界线** → 若某步既是入口又是实质工作（如写书的"打开文档"和"写正文"），减摩擦只动前者，别把后者也削掉。
