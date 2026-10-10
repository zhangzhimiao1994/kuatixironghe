# 蒸馏计划 · 堪舆择日（kanyu）

维度：**堪舆择日**（象征层，注册表顺序 16）｜前缀 `kanyu-*`｜入口 skill `kanyu-hub`
来源（包内相对路径，只准从这里抄引文）：
- `sources/zangshu.txt` — 葬書（舊題郭璞；内篇/外篇/雜篇＋《錦囊》注疏）
- `sources/hanlongjing.txt` — 撼龍經／疑龍經／葬法倒杖（唐楊筠松，四庫本，含倒杖十二法、二十四砂葬法）
- `sources/yilongjing.txt` — 疑龍經（維基文庫本，有标点，作**互校**用；冲突以四庫本为准）
- `sources/xieji.txt` — 欽定協紀辨方書（三十六卷，四庫本）

规矩：`distill/kanyu/STYLE.md`；骨架：`templates/skill-template/SKILL.md`；范例：`skills/hexagram-situation-diagnosis/SKILL.md`。

## 一、相地（葬書）9 个

| # | slug | 标题 | 出处（行号＝`sources/zangshu.txt`） |
|---|---|---|---|
| 1 | `kanyu-zangshu-cheng-shengqi` | 葬者乘生气：相地的第一原理 | 内篇一 L24–39 |
| 2 | `kanyu-zangshu-cang-feng-de-shui` | 藏风得水：什么叫「风水」 | 内篇二 L40–62 |
| 3 | `kanyu-zangshu-zhi-long-bian` | 支垄之辨：平洋与山垄两套体认 | 内篇二～四 L40–102 |
| 4 | `kanyu-zangshu-shi-lai-xing-zhi` | 势来形止：千尺为势、百尺为形 | 内篇三 L63–89 |
| 5 | `kanyu-zangshu-xing-shi-pin-lei` | 形势品类：势与形的吉凶读法 | 雜篇 L259–340 |
| 6 | `kanyu-zangshu-shen-fei-ze-xiang` | 审其所废、择其所相、避其所害 | 審其所廢 L103–155 |
| 7 | `kanyu-zangshu-zhi-e-long-lu` | 支葬其额、垄葬其麓 | 外篇 L160–254 |
| 8 | `kanyu-zangshu-ze-te` | 择其特：众山之中取哪一个 | 外篇 L160–254 |
| 9 | `kanyu-zangshu-si-fa` | 乘金相水、穴土印木 | 外篇 L160–254 |

## 二、相地（楊筠松）10 个

| # | slug | 标题 | 出处（`sources/hanlongjing.txt` 行号；疑龍經另参 `sources/yilongjing.txt`） |
|---|---|---|---|
| 10 | `kanyu-hanlong-gan-zhi-long` | 干龙枝龙：天下大势怎么分 | 撼龍經 L9–55 |
| 11 | `kanyu-hanlong-jiu-xing` | 九星辨形与星峰吉凶 | 撼龍經 L9–55 |
| 12 | `kanyu-yilong-shang` | 疑龙经·上篇：干上寻龙 | 疑龍經上篇 L58–59；互校 `yilongjing.txt` L7 起 |
| 13 | `kanyu-yilong-zhong` | 疑龙经·中篇：枝中干、州县都会 | 疑龍經中篇 L60–61；互校 `yilongjing.txt` |
| 14 | `kanyu-yilong-xia` | 疑龙经·下篇：真龙落穴与虚穴 | 疑龍經下篇 L62–63；互校 `yilongjing.txt` |
| 15 | `kanyu-yilong-shi-wen` | 疑龙十问 | L64–84 |
| 16 | `kanyu-wei-long-pian` | 卫龙篇 | L85–86 |
| 17 | `kanyu-bian-xing-pian` | 变星篇 | L87–89 |
| 18 | `kanyu-dao-zhang-shi-er-fa` | 倒杖十二法 | 葬法倒杖 L92–139（認太極 L92–116 + 十二法 L117–139） |
| 19 | `kanyu-er-shi-si-sha-zang-fa` | 二十四砂葬法 | L140–189 |

## 三、择日（協紀辨方書）15 个

卷次 ↔ 行号（`sources/xieji.txt`，正文那一份；文件末尾另有一份重复，取**前一份**）：

| 卷 | 篇 | 行范围 |
|---|---|---|
| 卷一 | 本原一（河圖、洛書、先天八卦次序/方位） | 294–419 |
| 卷二 | 本原二（二十四方位、正五行、中針雙山五行、縫針三合五行、洪範五行） | 420–516 |
| 卷三 | 義例一（總論、歲德、歲德合、歲幹合…） | 517–629 |
| 卷四 | 義例二（建除十二神、建除同位異名） | 630–795 |
| 卷五 | 義例三（天道、天德、月德、天德合、月德合、月空…） | 796–904 |
| 卷六 | 義例四（三合、臨日、驛馬、刼煞、災煞…） | 905–1024 |
| 卷七 | 義例五（黄道黑道、天乙貴人、天官貴人、福星貴人、喜神…） | 1025–1105 |
| 卷八 | 義例六（歲禄、飛天禄、飛天馬、飛宫貴人、通天竅…） | 1106–1216 |
| 卷九 | 立成（各類起例彙列成表） | 1217–1366 |
| 卷十 | 宜忌（神煞輕重相勝、趨避取捨） | 1367–1863 |
| 卷十一 | 用事（御用六十七事／民用三十七事／選擇六十事） | 1864–2152 |
| 卷十二 | 公規一（祀典、春牛經、歲時紀事、氣候） | 2153–2461 |
| 卷十三 | 公規二（更漏中星、星圖步天歌） | 2462–2640 |
| 卷十四–十九 | 年表 | 2641–4607 |
| 卷二十–三十一 | 月表 | 4608–5550 |
| 卷三十二 | 日表 | 5551–6122 |
| 卷三十三 | 利用一（選擇要論、楊筠松造命歌、論造葬） | 6123–6282 |
| 卷三十四 | 利用二（年神總論、月吉神總論、月凶神總論、諸家年月日吉凶神附論、制煞要法） | 6283–6459 |
| 卷三十五 | 附錄（推測時刻、男女九宫、逐日人神所在、太白逐日遊方、長短星、洗頭日、嫁娶周堂、五姓修宅…） | 6460–6875 |
| 卷三十六 | 辨訛 | 6876–7188 |

| # | slug | 标题 | 出处 |
|---|---|---|---|
| 20 | `kanyu-xieji-ben-yuan` | 本原：河洛八卦、二十四方位与诸家五行 | 卷一～卷二 |
| 21 | `kanyu-xieji-yi-li-nian-shen` | 义例·年神 | 卷三 |
| 22 | `kanyu-xieji-jian-chu` | 义例·建除十二神 | 卷四 |
| 23 | `kanyu-xieji-yue-shen` | 义例·月神 | 卷五 |
| 24 | `kanyu-xieji-ri-shen` | 义例·日神 | 卷六 |
| 25 | `kanyu-xieji-huang-dao-gui-ren` | 义例·黄道黑道与诸贵人 | 卷七 |
| 26 | `kanyu-xieji-lu-ma` | 义例·岁禄、飞天禄马、飞宫贵人 | 卷八 |
| 27 | `kanyu-xieji-li-cheng` | 立成：起例与查表 | 卷九 |
| 28 | `kanyu-xieji-yi-ji` | 宜忌：轻重相胜与趋避取舍 | 卷十 |
| 29 | `kanyu-xieji-yong-shi` | 用事：御用六十七事、民用三十七事 | 卷十一 |
| 30 | `kanyu-xieji-gong-gui` | 公规：祀典、春牛经、气候、更漏中星 | 卷十二～十三 |
| 31 | `kanyu-xieji-li-yong-zao-ming` | 利用·选择要论与杨筠松造命歌 | 卷三十三 |
| 32 | `kanyu-xieji-zhi-sha` | 利用·制煞要法 | 卷三十四 |
| 33 | `kanyu-xieji-fu-lu` | 附录：世俗相沿的择日条目 | 卷三十五 |
| 34 | `kanyu-xieji-bian-e` | 辨讹：辨世俗术家之讹 | 卷三十六 |

## 四、入口 1 个

| # | slug | 标题 | 说明 |
|---|---|---|---|
| 35 | `kanyu-hub` | 堪舆择日总览：一处形势、一个日子怎么读 | 由 `tools/new_dimension.py` 建好骨架，需按本族风格填全；路由到上面 34 个 skill |

合计 **35 个 skill**。数量由原书结构定（葬書三篇＋撼龍經/疑龍經/葬法倒杖；協紀辨方書三十六卷），不预设、不为凑数硬拆。

## 五、收尾顺序（不可颠倒）

1. 35 个 skill 的 SKILL.md + test-prompts.json 写完
2. 注册表 `| 16 | 堪舆择日 …| 35 |`、hub 概览表计数、hub H 节分组计数与名单 → 全部改成 35
3. `python tools/install_deps.py --install`
4. `python tools/dim_check.py`（0 错）
5. 整包升级 + 版本号 +1 + 打包
