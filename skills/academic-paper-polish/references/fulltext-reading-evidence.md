# 全文逐字精读实证（v2.15.0 新增）

> **本文件的每一条结论都来自「逐字读完整个正文文件」，不是关键词命中率，也不是段落骨架扫描。**
> 语料：D:\数据集\PDF_Radiolaria 全库 8162 篇 PDF 中按 28 个主子目录**分层随机**抽取 181 篇
> （种子 20261103，**不按文件大小排序**）；其中正文可逐字读取者 164 篇（≥3000 字符、文本层乱码率 ≤30%）。
> 每篇由独立子 Agent 用 read 工具**读到文件末尾**，并在分片末尾的覆盖率表中逐篇声明
> 「文件字符数 / 实际读到的字符数 / 覆盖章节」；主会话另用机器校验器把笔记中的每条引文回源核对。

## 一、阅读口径与可兑现范围（先说清楚）

| 口径 | 数值 | 说明 |
|---|---|---|
| 分层随机抽取 | 181 篇 | 28 个主子目录按篇数比例分配，目录内均匀随机，**不按文件大小排序** |
| 正文可逐字读取 | 164 篇 | ≥3000 字符且文本层乱码率 ≤30% |
| 其中期刊论文（≤60 页） | 约 120 篇 | 逐字读完 Abstract→Conclusion→Acknowledgements |
| 其中专著/图幅（>60 页） | 约 12 篇 | 逐字读完，按章节结构层记录 |
| 无文本层（扫描件） | 12 篇 | 只能渲染页面看图，无法逐字读 |
| 正文合计 | 约 570 万字符（切掉参考文献后） | 参考文献列表不计入正文 |

**🔴 重要更正**：本 skill 早期版本（v2.12.0–v2.14.0）声称"130 篇逐篇读段落骨架"，
该口径作废。原因有二：(1) 旧抽取器用 dict 存章节，遇同名标题会**覆盖前一段正文**；
(2) 旧"130 篇"取自按文件大小升序排列的清单，实为全语料**最小的** 130 篇（中位 0.89 MB），
而其余 216 篇中位 6.88 MB、最大 435 MB——**样本严重偏小**。v2.15.0 已重抽并重跑。

## 二、章节链实测：没有统一模板

164 篇中**没有一篇的章节链与另一篇完全相同**。实测到的骨架可归为五类：

### 2.1 完整 IMRaD + 声明块（高标准地学刊）

刊头(含 Article history 四日期) → 摘要 → 1. INTRODUCTION → 2. Oceanographical settings → 3. METHODS (3.1…) → 4. RESULTS (4.1…) → 5. DISCUSSION (5.1 MIS 6.2 / 5.2 MIS 5e …) → 6. CONCLUSION → Author statement → Data availability → Declaration of competing interest → ACKNOWLEDGEMENTS

（证据：Gorbarenko et al 2020, Quaternary Science Reviews 247:106569）

### 2.2 分类学体系论文（无 Discussion、无 Methods）

刊名头 + УДК → 标题 → 无标题摘要 → Описание видов → Отряд → …

（证据：Mamedov 1973, Известия АН Азербайджанской ССР 1973(2):59–64）

### 2.3 短篇发现报告（3–10 页，无独立 Discussion）

（无标题引言）→ 正文连续散文 → 图注 → 图注

（证据：Deflandre 1946, C.R. Acad. Sci. Paris 223:515–517）

刊头 → 摘要 → 一、火山岩野外观察 → 二、放射虫 → 参考文献 → 图版I

（证据：Yang Wanrong & Jiang Nayan 1980, 地层学杂志 4(1):67–69）

### 2.4 区域生物地层学（无独立 Methods，方法只有一句）

刊名头 + УДК + 标题 → 摘要（无标题）→ Ключевые слова. → 无标题正文 → 逐剖面描述 → 无标题结论段（4 段）→ СПИСОК ЛИТЕРАТУРЫ

（证据：Гольтман и др. 2002, Стратиграфия. Геологическая корреляция 10(5):92–107）

### 2.5 系统描述类（讨论不在 Discussion 段）

SYSTEMATIC → 逐类群块 → 结论

（证据：Baker 1983, J. Paleontology；Afanasieva 2019, Pal J 53(5):435–446）

## 三、中间部分（Methods / Results）的真实写法

### 3.1 Methods 的三种详略档次

| 档次 | 特征 | 证据 |
|---|---|---|
| **完整式** | 公式 + 逐符号定义 + 仪器 + 测量间隔 + 自陈简化 | Gorbarenko 2020: "ARM (individuals cm⁻² kyr⁻¹) = CM × DBD / LSR; where CM is the content of microfossils (individuals per gram of dry sediment), DBD is the dry bulk density (g cm⁻³) and LSR is the linear sedimentation rate (cm kyr⁻¹)" |
| **一句式** | 只说材料类型 | Гольтман 2002: "Материалом для радиоляриевого анализа послужили, главным образом, шлифы." |
| **写进摘要式** | 俄文分类学把绘图方法写进摘要 | Mamedov 1973: "Зарисовки радиолярий выполнялись под микроскопом МБИ-3 при 280-кратном увеличении художником А. А. Захаряном." |

→ **没有"必须写满 Methods"的规则**；但**只要用了指标，就必须给公式与符号定义**。

### 3.2 Results 的两条硬要求

1. **先给总量与采样密度**：
   "The 23 species and 7 genera BF were identified in the 245 samples of the core PC-7R. The BF abundance varies down core from 0 to 916 ind./g"（Gorbarenko 2020）
2. **直接说某组不具信息量**：
   "Therefore, this group is not informative (Fig. 4)."（同上）

### 3.3 结果段里嵌"反常发现"，为讨论埋伏笔

"However, during the HEE 9 of MIS 5c, the ARs of R-surface, A. setosa and R-dichothermal showed sharp increases, which were contrary to the drop in the AR of BF and productivity."（Gorbarenko 2020）

## 四、Discussion 的四拍结构（最值得抄的一条）

**按时间段分节，每节固定四拍**（证据：Gorbarenko 2020 的 5.1 MIS 6.2 / 5.2 MIS 5e）：

1. **数据陈述**："The high values of IRD during MIS 6.2 indicate that…"
2. **机制解释**："…forced active sea ice formation and caused its expansion into the central OS"
3. **与前人比对（一致 or 矛盾，二选一，明确写出）**：
   "Such a pattern of duration and intensity during interstadial B1 is consistent with the pattern of B1 in the southern Bering Sea according to Gorbarenko et al. (2019) but contradicts its timing and intensity according to Ovsepyan et al. (2017)."
4. **本研究结论 + 不确定性**："Such hypothesized glaciers should have strongly cooled the OS area by geostrophic winds related to the enhancement of the Siberian High."

→ **"consistent with … but contradicts …" 是本领域讨论的标准句式**，把分歧显性化，而不是和稀泥。

## 五、结论（Conclusion）的两种形态

### 5.1 连续散文式（高标准刊）

开头一句**复述研究做了什么**（含时段、方法、指标）：

"The responses of the production of BF and radiolarian ecological groups in the central OS to orbital and millennial-time scale climate and environmental changes over the last 136 kyr were studied on the basis of available productivity, geochemical and lithological records in the sediment core PC-7R. A previously constructed age model of this core was modified to millennial scale resolution."

然后按「代理 → 现象 → 机制」逐条展开，机制归因用 **"rather than" 做排除**：

"Therefore, we suggest that the enlarged production of R-mesopelagic during late MIS 5e was mostly supported by the large lateral transportation of detritus and OM from the subarctic western Pacific into the intermediate water of the central OS, rather than from the northwestern OS shelf and slope."

不确定性用 **"likely due to"** 而非断言：

"the radiolarian production, especially for R-mesopelagic, was significantly suppressed in the central OS, likely due to low primary productivity and weak lateral transport of detritus from the WSAP while ventilation of the OSIW was high."

末尾留**明确的开放问题**：

"The sources of these peaks of mesopelagic radiolarian production may lay in the western North Pacific, including the Okhotsk and Bering Seas and their hinterlands, and they present an important subject for further high-resolution investigation."

### 5.2 编号清单式（短篇/区域地层）

"以下地区情况可资鉴别：1. … 2. … 3. … 4. … 5. …"（Zheng Haixiang et al 1986, Bull. Chengdu Inst. Geol. M.R. 7:85–93）

## 六、短篇（3–10 页）的三种讨论形态

**实测：本领域 3–10 页短篇绝大多数没有独立 Discussion 段**，讨论以三种形态出现：

| 形态 | 证据 |
|---|---|
| **点名质疑前人** | Zheng 1986 点名 Miyashiro(1973)、Pearce et al(1981)、Robinson(1984) 三个既有范式，再逐条给五条反证："以下地区情况可资鉴别：1. … 2. …" |
| **承认局限再修正** | Deflandre 1946: "la première étude des nodules phosphatés donne une idée incomplète et fausse de leur microfaune de Radiolaires. Il en est exactement de même si l'on n'étudie que les spécimens dégagés. Mais, grâce à cette seconde méthode…" |
| **"不能断言但可能"** | Yamasaki & Yamasaki 1999: "Amphipyndax aff. enesseffi および A. aff. tylotus の形態特に diagonal ridge の発達についての時間的変化は検討されていないので…明確なことは言えないが，DK群集帯の中での上位層準であることを示す可能性があると思われる。" |

## 七、引言（Introduction）的起手模式（逐字实证）

| 模式 | 逐字证据 | 出处 |
|---|---|---|
| **区域重要性 + 研究史 + 缺口 + 范围句**（五段式） | "this is why the OS, as the lowest-latitude region with seasonal sea ice cover in the world, plays a leading role in high-latitude paleoceanography" … "Here, we focus on the high-resolution study of radiolarian and BF species…" | Gorbarenko 2020 |
| **孤例价值 + 原因** | "Радиолярии отряда Phaeodaria исключительно редки в ископаемом состоянии. Это обстоятельство объясняется особенностями их скелета…" | Runeva 1974 |
| **承认现状困难 → 引出动作** | "Si l'on ne s'aperçoit qu'un type de sclérite peut se rencontrer dans plusieurs genres… néanmoins les micropaléontologistes… ne peuvent éviter la création de dénominations particulières pour chaque type." | Deflandre 1946 |
| **区域综述 + 缺口 + 本文动作** | "…からの報告であり，…については…が報告しているだけである" | Yamasaki 1999 |
| **时间地点 + 发现 + 自陈局限** | "1983年野外地质调查期间，我们在西藏阿里地区发现了四条蛇绿岩剖面（图1）虽然尚未取得岩石学、岩石地球化学的室内测试资料…但是，在野外这四条剖面上均可追索和鉴别出相对完整的 steimann 三元体系。" | Zheng 1986 |
| **背景 + 目的（无引言段）** | "我国南部长兴阶的层型剖面在浙江长兴煤山藻青采石场。层型剖面经我所二迭—三迭纪地层队研究（1978）…" | Yang 1980 |

## 八、系统描述类（类群块）的标签模板（跨语种汇总）

| 模板 | 标签序列 | 出处 |
|---|---|---|
| **Pal J 英文制式** | Genus X gen. nov. → Etymology. → Type species. → Diagnosis. → Species composition. → Comparison. | Afanasieva 2019 |
| **Pal J 种级** | X sp. nov. → Etymology. → Holotype. → Description. → Measurements in μm and ratios (Fig. 6): → Comparison. → Material. → Remarks. | Afanasieva 2019 |
| **俄文五拍** | 学名 + sp. n. → 图版引用 → Голтип 存放地行 → Оригинал 存放地行 → Описание. → Размеры, мк: → Изменчивость. → Сравнение. → Местонахождение и возраст. | Mamedov 1973 |
| **俄文阶元诊断集** | ОТРЯД → Диагноз. → Состав. → Распространение. | Afanasieva 2002 |
| **附录匿名新种** | species D → Dimensions-(based on 60 specimens…) → Remarks- | Baker 1983 |

→ **俄文必写两句**："Близкие по морфологии виды не установлены."（无近似种时）
和 "…позволяет выделить новый род, так как подобный род в семействе … не выделен."（新属理由）。

## 八之二、摘要（Abstract）写法实证

### 8.2.1 一个必须先说的口径问题

164 篇里**只有 44 篇**（27%）有机器可识别的独立 ABSTRACT 段；
其余 **120 篇（73%）的摘要没有标题标记**，直接嵌在标题页/正文流里
（俄文刊、中文刊、日文刊、老刊尤其如此）。
→ **写摘要时不必纠结"要不要 Abstract 标题"**：老刊常省略标题，新刊（Elsevier/Springer）必有。

### 8.2.2 摘要长度与句数（44 篇有独立摘要段的样本）

| 指标 | 数值 |
|---|---|
| 字符数 min / p25 / **中位** / p75 / max | 314 / 1089 / **1992** / 2553 / 6340 |
| 句数 min / **中位** / max | 3 / **13** / 150 |

→ 中位 **约 2000 字符 ≈ 300 词**，**约 13 句**。
  比多数期刊的 150–250 词上限**偏长**——说明本领域摘要偏向"小型引言"，不限定字数时容易写长。

### 8.2.3 摘要的五个功能件（38 篇英文摘要，逐字标记）

| 功能件 | 出现率 | 写法 |
|---|---|---|
| **结果** | **87%** | 必写，且常带数据 |
| **方法** | **74%** | 材料 + 产地 + 手段 |
| **背景/现状** | **68%** | 1–2 句，常用 however / remains / poorly known |
| **结论/意义** | **50%** | suggest / indicate / provide / first record |
| **目的** | **29%** | 反而不常见——本领域摘要常**开门见山报结果**，不写"本文旨在" |

→ 🔴 **与通用模板最大的不同：本领域摘要以"结果"打头（87%），"目的句"只占 29%。**
  通用模板要求的"背景→目的→方法→结果→结论"五段式，在本领域**只有约 30% 的摘要**真的写了目的句。

### 8.2.4 时态与语态（38 篇英文摘要）

| 特征 | 出现率 |
|---|---|
| 现在时标记（is/are/shows/indicates/suggests） | **95%** |
| 过去时/完成体标记（was/were/has been） | 68% |
| 被动结构（be + 过去分词） | **87%** |
| 第一人称 "we" | **仅 18%** |
| 含数字/数据 | 84% |
| 含新分类单元声明（gen. nov./sp. nov.） | 3% |

→ 🔴 **摘要用现在时陈述结论（95%），用被动语态（87%），几乎不用 "we"（18%）。**
  这与通用模板"避免被动"的建议**相反**——本领域的规范是**被动 + 现在时**。

### 8.2.5 逐字例句

**开门见山报结果型**（本领域主流）：
> "There appear to be about six shallow-water polycystine radiolarian provinces in the modern ocean. These provinces owe their integrity to the major circulation systems that create packages of water and environments which vary in degrees of oceanographic and temporal stability."
> —— Casey 1989, Palaeogeogr. Palaeoclimatol. Palaeoecol. 74:15–22

**新分类单元摘要型**（注意：标题即新类群名，摘要直接列新属新种）：
> "Based on the structure of microsphere and systems of girdles the author describes a new family — Miropylidae, two new pyloniid subfamilies — Palaeotetrapylinae and Dipylissinae, and three new genera and species — Miropyle mirabilis, Palaeotetrapyle muelleri and Dipylissa bensoni."
> —— Dumitrica 1988, Pylonioidea

**多语摘要型**（德/法刊同一篇附多种语言摘要）：
> "Résumé — ... / Zusammenfassung — ..."
> —— Baumgartner 1985（121 页专著，附三语摘要）

### 8.2.6 可抄的摘要骨架（按体裁选）

| 体裁 | 骨架 |
|---|---|
| **分类学新类群** | 新类群名 + 产地层位 → 鉴别特征 → 与近缘类群差异 → 意义 |
| **生物地层** | 剖面/层位 → 群集特征 → 与已知带的对比 → 时代结论 |
| **古环境重建** | 材料与方法 → 代理指标结果 → 与环境事件的对应 → 结论 |
| **综述** | 领域范围 → 已有共识 → 分歧/空白 → 本文如何处理 |

## 八之三、现代期刊的强制声明块（1% 覆盖率，但属硬性要求）

164 篇里只有极个别论文（主要是 Elsevier/Springer 系）带这些块，但**目标期刊若要求，缺失即退稿**。

### 8.3.1 四日期投稿流程（Elsevier）

> "Received 11 June 2020 / Received in revised form 26 August 2020 / Accepted 27 August 2020 / Available online 13 September 2020"

### 8.3.2 作者贡献（CRediT）

> "Author statement — Sergey A. Gorbarenko: Conceptualization, Methodology, Validation, Investigation, Writing - Original Draft, Writing - Review & Editing. Elena A. Yanchenko: Methodology, Validation, Formal analysis, Investigation."

→ **逐作者列角色**，用 CRediT 词表（Conceptualization / Methodology / Validation / Investigation / Formal analysis / Writing - Original Draft / Writing - Review & Editing）。

### 8.3.3 数据可用性

> "Data availability — All relevant data in this paper have been uploaded to MendeleyData https://data.mendeley.com/datasets/gbr7tprkyd/1."

### 8.3.4 利益冲突

> "Declaration of competing interest — The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper."

### 8.3.5 致谢

> "We are grateful to Captain Akamine and the crew of the R/V Mirai for their help with sediment collection in the OS during the MR06-04 cruise."

→ 致谢顺序：**先谢船上/野外协助 → 再谢合作机构 → 最后谢基金号**。

---

## 八之四、决策树：先判断体裁，再选骨架

**写之前先回答三个问题**（依据：164 篇章节链实测）：

**Q1 本文的主要贡献是什么？**
- 新分类单元 / 新类群 → 骨架 A（系统描述类）
- 地层的时代确定 / 对比 → 骨架 B（生物地层类）
- 环境 / 气候重建 → 骨架 C（多指标古环境类）
- 方法 / 理论 / 综述 → 骨架 D（方法或综述类）

**Q2 目标刊是"老刊"还是"新刊"？**
- 老刊（Pal J / 俄文刊 / 中文老刊 / 日文刊）→ 可省独立摘要标题、可省 Discussion、可用图版制、可用 × magn.
- 新刊（Elsevier / Springer / Wiley）→ 必须有独立 Abstract、必须带声明块、必须给比例尺条、彩色图需免责句

**Q3 篇幅多长？**
- ≤10 页 → 短篇骨架（无独立 Discussion，讨论嵌入末段）
- >10 页 → 完整骨架（但仍可能无 Discussion——65% 的论文没有）

### 五种骨架速查

| 骨架 | 章节链 | 典型刊 |
|---|---|---|
| **A 系统描述** | INTRODUCTION → [Repository] → SYSTEMATIC DESCRIPTION（逐类群块）→ [Discussion 常缺省] | Pal J, Pal Zh, 分类学专刊 |
| **B 生物地层** | INTRODUCTION → GEOLOGICAL SETTING → MATERIAL & METHODS → RESULTS（逐剖面/逐层）→ DISCUSSION → CONCLUSION | Palaeo 3P, 地层学杂志 |
| **C 多指标古环境** | INTRODUCTION → OCEANOGRAPHICAL SETTING → METHODS → RESULTS → DISCUSSION（按时间段分节）→ CONCLUSION + 声明块 | QSR, Palaeo 3P, Deep-Sea Res. |
| **D 区域综合/综述** | 无统一链，按主题分节 | 综述刊 |
| **E 短篇报告** | （无标题引言）→ 正文连续散文 → 图注；或 一、二、三 编号小节 | 各类刊的短通讯 |

## 九、横切统计（164 篇精读笔记，机器计数）

对 164 篇精读笔记做关键词计数（**仅作覆盖率参考，不作论证动作判断**）：

| 现象 | 篇数 | 占比 |
|---|---|---|
| 提到图版 / Plate / 図版 | 164 | 100% |
| 提到引言 / Introduction / はじめに | 162 | 99% |
| **没有独立 Discussion 段** | **106** | **65%** |
| 有摘要 | 122 | 74% |
| 提到表格 / Table / Таблица | 83 | 51% |
| 提到比例尺 | 71 | 43% |
| 提到放大倍数 | 50 | 30% |
| 提到标本号 / Holotype / PIN | 15 | 10% |

→ 🔴 **最重要的一条：65%（106/164）的论文没有独立 Discussion 段。**
   这与"短篇没有 Discussion"的旧印象不同——**在 10 页以上的论文里同样普遍**。
   因此 skill 不应假设"一定有 Discussion 段可写"，而应先判断本文属于哪一种骨架。

## 十、引文回源校验（机器口径）

主会话用校验器把笔记中的每条引文拿回源文件核对，结果：

| 类别 | 条数 | 说明 |
|---|---|---|
| 完全精确命中 | 6,448 | 引文逐字出现在源文件 |
| 部分命中（跨排版断行） | 618 | 引文被 PDF 断行/分栏拆开 |
| 图内文字（无文本层） | 282 | 引文来自图片 artwork，只能靠看图获得 |
| 无法核对 | 932 | 多为 OCR 噪声或笔记转述 |
| **合计** | **8,280** | **有据率 88.7%** |

→ 🔴 **88.7% 的引文能在源文件中找到证据**；无法核对的 11.3% 主要是 OCR 噪声，
   笔记中已逐条标注 ⚠️。

## 十一、本文件的局限（必须如实说明）

1. **每刊通常只有 1–2 篇样本**，"按刊"结论只能视为该刊该篇的观察。
2. 12 篇为无文本层扫描件，**无法逐字读**，只能渲染页面看图。
3. 中文 PDF 文本层有损（部分数字与拉丁字符整体丢失），需靠渲染页核对。
4. 章节自动切分对俄文/老刊失效（sec_order 常为 _full），结构靠通读判断。
5. 引文回源校验的机器口径：**含 ≥12 个拉丁/西里尔字符的引文**才纳入核对；
   纯中文分析性描述不计入（避免把分析文字误当原文引文）。
