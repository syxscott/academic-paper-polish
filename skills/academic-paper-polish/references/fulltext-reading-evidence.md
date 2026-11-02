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

## 九、横切统计（156 篇精读笔记，机器计数）

对 156 篇精读笔记做关键词计数（**仅作覆盖率参考，不作论证动作判断**）：

| 现象 | 篇数 | 占比 |
|---|---|---|
| 提到图版 / Plate / 図版 | 156 | 100% |
| 提到引言 / Introduction / はじめに | 154 | 99% |
| **没有独立 Discussion 段** | **101** | **65%** |
| 有摘要 | 116 | 74% |
| 提到表格 / Table / Таблица | 78 | 50% |
| 提到比例尺 | 66 | 42% |
| 提到放大倍数 | 47 | 30% |
| 提到标本号 / Holotype / PIN | 15 | 10% |

→ 🔴 **最重要的一条：65%（101/156）的论文没有独立 Discussion 段。**
   这与"短篇没有 Discussion"的旧印象不同——**在 10 页以上的论文里同样普遍**。
   因此 skill 不应假设"一定有 Discussion 段可写"，而应先判断本文属于哪一种骨架。

## 十、引文回源校验（机器口径）

主会话用校验器把笔记中的每条引文拿回源文件核对，结果：

| 类别 | 条数 | 说明 |
|---|---|---|
| 完全精确命中 | 6,125 | 引文逐字出现在源文件 |
| 部分命中（跨排版断行） | 607 | 引文被 PDF 断行/分栏拆开 |
| 图内文字（无文本层） | 274 | 引文来自图片 artwork，只能靠看图获得 |
| 无法核对 | 877 | 多为 OCR 噪声或笔记转述 |
| **合计** | **7,883** | **有据率 88.9%** |

→ 🔴 **88.9% 的引文能在源文件中找到证据**；无法核对的 11.1% 主要是 OCR 噪声，
   笔记中已逐条标注 ⚠️。

## 十一、本文件的局限（必须如实说明）

1. **每刊通常只有 1–2 篇样本**，"按刊"结论只能视为该刊该篇的观察。
2. 12 篇为无文本层扫描件，**无法逐字读**，只能渲染页面看图。
3. 中文 PDF 文本层有损（部分数字与拉丁字符整体丢失），需靠渲染页核对。
4. 章节自动切分对俄文/老刊失效（sec_order 常为 _full），结构靠通读判断。
5. 引文回源校验的机器口径：**含 ≥12 个拉丁/西里尔字符的引文**才纳入核对；
   纯中文分析性描述不计入（避免把分析文字误当原文引文）。
