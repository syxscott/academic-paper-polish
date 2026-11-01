# 微体古生物 / 放射虫论文的写作与制图模式

> **本文件解决什么问题**：`figure-design-system.md` 讲**通用**图件设计（版式、原型、语义色）；
> `multi-journal-style-guides.md` 讲**各刊官方格式条款**。
> 本文件讲第三件事：**这个领域（微体古生物 / 放射虫）的论文实际长什么样** ——
> 章节怎么排、图叫 Fig. 还是 Plate.、图是彩色的还是灰度的、图注怎么写。
>
> **取样口径**：本地语料库 `D:/数据集/PDF_Radiolaria`（**8162 篇 PDF / 62 GB / 33 个子目录**）。
> - 全库按子目录**比例分层抽样 319 篇**（每层 3–14 篇，固定随机种子 20261101）
> - 其中 **272 篇有可用文本层**（**47 篇为纯扫描件**，无文本层，已剔除出统计）
> - 共解析出 **1139 条图注**；另抽 **40 篇的 376 张嵌入图**做配色统计
> - ⚠️ **口径限制（先读这段再用下面的数字）**：
>   「提及 Fig / Plate」是**文本层词频近似**，不等于严格的图件计数；
>   「有摘要 / 关键词 / 参考文献」只统计**前 30 页**文本中是否出现该词，是**下限估计**；
>   配色统计只覆盖**嵌入位图**，纯矢量图（老刊常见）未被计入。
>   **下面每条结论都标注了样本量与口径，不要把它当成全库普查。**

---

## 一、🔴 四种主题的论文骨架

按语料实际写法，**微体古生物论文分成四类，骨架互不相同**。把综述稿写成系统描述稿，
或把系统描述稿写成数据稿，是这个领域最常见的结构性错误。

| 主题 | 语料中的识别特征 | 典型章节序列（按出现频率排序） |
|---|---|---|
| **A 分类 / 系统描述** | 出现 Systematic description / Taxonomy / Holotype / n. sp. / gen. nov. | Geological setting → Material and methods → **Systematic descriptions（每个分类单元一个并列小节）** → Conclusions → References |
| **B 生物地层 / 带对比** | Zonation / biozone / range chart | Introduction → Geological setting → Material and methods → **Regional geology** → **Radiolarian biostratigraphy（对比表 + 图）** → Conclusions |
| **C 定量 / 古生态** | abundance / diversity / isotope / geochemistry | Introduction → Geological setting → Samples and methods → Results → Discussion → Conclusions |
| **D 综述 / 专著** | review / overview / monograph | Introduction → 各专题章节 → Conclusions → References |

**英文章节标题在 272 篇中的出现频度**（逐字统计）：

| 标题 | 出现篇数 | 占比 |
|---|---|---|
| Introduction | 32 | 12% |
| Conclusions | 17 | 6% |
| Discussion | 17 | 6% |
| Results | 12 | 4% |
| Materials and methods | 7 | 3% |
| Geological setting | 5 | 2% |
| Profile descriptions / Systematic descriptions | 4 / 2 | 各 1% |

⚠️ **这些百分比偏低是有原因的**：许多老论文用 "Summary" 代替 "Abstract"、
用 "Paleogeography" / "Geology" 等自定义标题，且部分为扫描件未被计入。
**能读出来的章节标题里，"Introduction / Conclusions / Discussion" 稳居前三** ——
这个排序本身是可靠的；单个标题的绝对占比则不可靠。

### 🔴 A 类（系统描述）的关键结构特征

在语料里反复出现**同一层级的并列小节**，而不是把描述塞进一个大段落：

- 每个分类单元一个独立小节；小节内固定四段式：
  **Holotype（正模）→ Paratype（副模）→ Description（描述）→ Discussion（讨论）**
- 小节标题直接用**分类单元名**（属名 + 种名，斜体），不写"描述"二字
- 分类学记号固定为 `gen. nov.` / `sp. nov.` / `n. sp.` / `aff.` / `cf.` / `ex gr.`

🔴 **可直接照抄的英文骨架（语料原句）**：

> "Material and methods — In accordance with the recommendations of the International Codes of Zoological Nomenclature (ICZN) … all illustrated and described fossils should be deposited in an appropriate museum or collection …"

> "Research Articles — Research Articles present original, analytical results in any area of paleobiology. These should be timely, relevant, and of broad interest."

---

## 二、🔴 图件范式：Fig. 制 vs 图版（Plate）制

**这是本领域最需要先定的一件事**，因为它决定后面所有排版。

| 范式 | 语料中的论文占比（272 篇有文本层） | 适用 |
|---|---|---|
| **Fig. / Figure 常规图** | **194 篇 = 71%** | 绝大多数论文（数据图、地图、示意图） |
| **Plate. / 图版** | **51 篇 = 19%** | 系统描述类（化石照片版） |
| **两者兼有** | **49 篇 = 18%** | 系统描述 + 数据图的完整研究 |

🔴 **判据**：**要展示"某个分类单元长什么样" → 用图版（Plate）**；
**要展示"分布 / 关系 / 趋势" → 用 Fig.**。系统描述论文几乎一定两者都有。

### 2.1 图注前缀的实际分布（1139 条图注，逐字统计）

| 前缀 | 条数 | 占比 |
|---|---|---|
| `Fig.` | 765 | **67%** |
| `Figure` | 227 | 20% |
| `FIG.` | 45 | 4% |
| `Plate` | 40 | 4% |
| `Рис.`（俄文） | 29 | 3% |
| `图`（中文） | 11 | 1% |
| `図`（日文） | 5 | <1% |

🔴 **首选 "Fig."（带点、缩写）**：67% vs 20% 的差距说明这不是风格偏好，而是领域惯例。
写 "Figure 1." 不会错，但若要贴合本领域习惯，用 **"Fig. 1."**。

### 2.2 面板字母体系（语料原句逐字）

> "Figure 1A. Main features of a polycystine spumellarian cell. Slightly modified from Kling …"
> "Figure 2A. Characters used for the identification of spumellarian radiolarians. From Haeckel …"
> "Figure 2F. Characters used for the identification of spumellarian radiolarians. Original."
> "Figure 2N-S. Characters used for the identification of spumellarian radiolarians. M, P, Q: …"
> "Plate 3, figures K and L; plate 4, figures C, D, F, G, K, L; plate 5, …"
> "Figure 1C-E. General view of entire radiolarian colonies. C, D: by courtesy of Neil Swanberg …"

🔴 **可直接复用的四条写法**：
1. **面板用大写字母 + 连字符区间**："Figure 2N-S."（不是 2N–S，也不是 N to S）
2. **每个面板单独成图注**："Figure 1A." / "Figure 1B." / "Figure 1C-E." —— 不是把一整版写成一个长图注
3. **图版跨页引用写成清单**："Plate 3, figures K and L; plate 4, figures C, D, F, G, K, L"
4. **正文用面板级引用**："(Fig. 2C and D)"、"(Fig. 3B)" —— 不是笼统的"Fig. 3"

### 2.3 🔴 图注里的来源声明（本领域特有）

语料中系统描述与示意图图注常带**来源句**，这是版权合规的天然落点：

> "… Slightly modified from Kling …"
> "… From Haeckel …"
> "… Original."
> "Fig. 1. Schematic classification of Radiolaria based on ribosomal genes (18S and 28S rDNA) modified from Sandin (2019). Non-supported nodes are reported by a surrounded question mark."

🔴 **借用的图必须在图注里写来源**："From X"（直接引用）/ "Slightly modified from X"（轻微改动）/
"modified from X (year)"（改造）/ "Original."（自绘）。**这与 skill 的版权红线是同一条规则**，
本领域把它落到了图注里执行。

---

## 三、🔴 色彩风格：灰度优先，形状承担分组

**实测：40 篇抽样的 376 张嵌入图中，349 张（93%）近灰度，仅 7% 为彩色；
图内平均饱和度中位数 = 0.000（即绝大多数图完全没有彩色信息）。**

这不是"做得糙"，而是这个领域的**信息载体不是颜色**：

| 编码任务 | 语料中的实际做法 |
|---|---|
| 区分组别 | **形状**：● / ▲ / ■ / ◆；或**灰度深浅**；或**黑白花纹填充** |
| 区分地质体 | **花纹（hatching）**：点、斜线、实心深灰 |
| 突出某一条线 | **线型**：实线 / 虚线 + 线宽 |
| 范围包络 | **凸包轮廓线**（白色细线，不填色） |

🔴 **所以在微体古生物论文里，"同一颜色 = 同一组"这条规则要改写成**
**"同一形状 + 同一灰度 = 同一组"** —— 这正是 §二 中
`color-system.md` 说的"一通道一变量"：轴和位置已经用掉信息，
形状与灰度才是剩下的通道。

### 3.1 彩色出现在哪里

彩色只在两类图里出现，且都是**系统发育 / 现代生态**这类新刊论文：

- **系统发育树**：末端三角按类群分色（见 §三.2 的 Biard 2022 范例）
- **现代生态统计图**：多样性、丰度、nMDS 等

🔴 **因此：写一篇放射虫化石系统描述论文（1990–2020 年代风格），
不要用彩色配色表；写一篇现代海洋放射虫多样性论文，可以。**
**先定体裁，再定色。**

### 3.2 彩色系统树的三个可抄细节（Biard et al. 2022, *Environ Microbiol*）

1. **外群用灰色横条**（"Phaeodaria"），一眼看出哪支是外
2. **类群分组用灰色圆角框**，框右上角写类群名（Taxopodia / Spumellaria / Nassellaria / Orcadiaria / Collodaria）
3. **不支持的节点标 "?"**，并在图注里说明："Non-supported nodes are reported by a surrounded question mark."

🔴 **图注要解释图里的符号约定**，这是现代刊的硬要求：
读者不看方法部分也能读懂"?"、灰条、彩色三角各代表什么。

---

## 四、🔴 地图与地质图：灰度花纹 + 插图 + 比例尺

语料中的标准地质图版式（以 Aitchison et al. 1999, *Micropaleontology* 45(2) 的 TEXT-FIGURE 1 为范例）：

- **图号写成 "TEXT-FIGURE 1."**（Micropaleontology / SEPM 系的刊式，与普通 "Fig." 不同）
- **主图 + 右上角插图定位图**（inset locator map），标注研究区在更大区域中的位置
- **指北针 + 比例尺**（"0 — 50 km"），比例尺放在图内而非图注
- **经纬度刻度**直接标在图框上（30°、31°、32°、151°、152°、153°E）
- **地质体用黑白花纹**：点填充、斜线填充、实心深灰
- **图例按构造单元分块**："TAMWORTH BELT" 和 "HASTINGS BLOCK" 各一块，而非一张大图例
- **样点直接标在图上**（"Significant radiolarian localities are also indicated"）

> **原文（逐字）**："TEXT-FIGURE 1. Simplified tectonostratigraphic map of the southern New England orogen, eastern Australia showing the areal distribution of rocks assigned to the Gamilaroi terrane. Significant radiolarian localities are also indicated."

🔴 **图注的第一句要说明"这张图传达什么"，不是"这张图画了什么"** ——
这是 Micropaleontology 的原文要求，也是 skill 版权/可读性规则在本领域的落地。

---

## 五、🔴 标本图版（Plate）的制图要求

语料中系统描述论文的图版（Plate）遵守：

- **黑底或纯白底**，标本颜色即数据，不加任何色偏（与 `color-system.md` 的化石照片条款一致）
- **每个视图单独编号**（A、A1、A2、A3…），同一标本的多个视图用**同一字母 + 数字下标**
- **比例尺用数字线段**，常与图注里的放大倍数并存
  （语料实测：1139 条图注中"含放大倍数" 1.5%、"含 scale bar" 1.2%、"含 μm/mm 数值" 1.2%，
  但**这 1% 多是数据图**，图版类图注的比例尺信息多以 "Plate N" + 正文说明形式出现）
- **图注必含分类学记号**（语料实测 1139 条图注中 **7.4%** 含 `gen.` / `sp.` / `n. sp.` / `aff.` / `cf.` / `ex gr.`）

> **原文（逐字）**："Letters on figures (A, B, C, etc.) should run consecutively from left to right and from top to bottom. If more than one specimen is illustrated in a figure, label all views of the same specimen with the same letter with numerical subscripts (A1, A2, A3, etc.)."

---

## 六、🔴 前置要素：这个领域的老刊与新刊差别很大

272 篇有文本层中的英文子集（N=179），前 30 页内出现相应字段的篇数：

| 字段 | 出现篇数 | 占比（下限） |
|---|---|---|
| References | 118 | **66%** |
| Abstract | 95 | 53% |
| Acknowledgements | 94 | 53% |
| Keywords | 41 | **23%** |

🔴 **关键判断**：
- **摘要与致谢**在这个领域是**未必有**的（老刊常无 Abstract；俄文/中文刊另有格式），
  **不要按"通用 SCI 模板"硬套**——先查目标刊（见 `multi-journal-style-guides.md`）
- **Keywords 出现率最低（23%）**：放射虫系统描述类论文普遍不列关键词
  （因为检索靠分类单元名与图版），**加关键词不是硬性要求，但加了不违规**
- 🔴 **因此本领域的"摘要/关键词缺失"不能一律判为格式错误** ——
  这与 `journal-constraints.md` 的通用规则存在张力，**以目标刊官方要求为准**

---

## 七、交稿前自查（微体古生物 / 放射虫专用）

- [ ] 图号用的是 **"Fig."** 而不是 "Figure"？（本领域 67% 用前者）
- [ ] 展示分类单元形态 → 用 **图版 Plate**；展示分布/关系 → 用 **Fig.**（两者可兼有）
- [ ] 图是**灰度**的吗？分组用**形状/灰度/花纹**而不是颜色？（语料 93% 灰度）
- [ ] 每个面板单独一条图注，用 **"Figure 1A." / "Figure 2N-S."** 的写法？
- [ ] 正文用**面板级引用**："(Fig. 2C and D)"？
- [ ] 借用/改造的图，在**图注里写了来源**（From X / modified from X (year) / Original.）？
- [ ] 图版里同一标本的多个视图用**同一字母 + 数字下标**？
- [ ] 地质图有**比例尺 + 指北针 + 插图定位图**，地质体用**黑白花纹**？
- [ ] 图注第一句讲**这张图传达什么**（the message），不是只描述内容？
- [ ] 系统描述是 **Holotype → Paratype → Description → Discussion** 四段式？
- [ ] 分类单元名用**斜体**，新分类单元带 `gen. nov.` / `sp. nov.` 记号？
- [ ] 标本已按 **ICZN** 存入公开藏馆，收藏号已写明？
- [ ] 目标刊是否真的要求 Abstract / Keywords？（本领域 23%–53% 的实际情况）

---

## 九、🔴 论文整体结构：Introduction 怎么写、Discussion 怎么讨论

> **本节的依据**：对同一批抽样论文做**逐篇精读** —— **5 篇 Introduction 全文**
> （Little et al. 1999 *Geology*；Fortey & Bruton 1973 *GSA Bull.*；Robinson & Haslett 1995；
> Vashchenkova 2011 *Marine Geology*；教科书式综述章）+ **1 篇 Discussion 全文**
> （Robinson & Haslett 1995）+ **8 篇 Discussion 的首句与末句**。
> 🔴 **本节不给出任何"命中率"** —— 词频只能证明"某个词出现过"，
> 不能证明"作者在这里做了什么论证动作"。结构结论一律来自**通读全文后的判断**，
> 并附逐字原文供复核。

### 9.1 Introduction：**没有统一模板，实测四种写法并存**

#### 模式 A｜"缺口 → 目的"式（系统描述与新发现类最常见）

Little et al. 1999 (*Geology*) 的引言**只有一段**，内部走完四步：

> ① 领域事实 + 文献："Modern hydrothermal vent sites support communities of animals whose primary producers are chemoautotrophic bacteria … (e.g., Van Dover, 1995; Grassle, 1986)."
> ② **数量化的知识空白**："Although more than 50 modern vent fields with flourishing communities are known, the known fossil record of vent fauna is sparse: **only 19 occurrences in the entire Phanerozoic—three from the Silurian, six from the Devonian, one from the Jurassic (described here), seven from the Cretaceous …**"
> ③ 结论句："**Consequently, the evolutionary history of these novel communities is not well understood.**"
> ④ **目的句 + 贡献句**（两句连排）："**Here, we give the first description of** the only known Jurassic hydrothermal vent fossils, recently discovered in a small lens of massive sulfide (named here the Figueroa deposit) and in an associated iron-silica bed in central California. The Figueroa assemblage **fills a 270 m.y. gap** in the vent fossil record, from the Middle Devonian to the Cretaceous, and **offers important insights into** the structure of ancient vent communities."

🔴 **模式 A 的四个可抄动作**：
1. 缺口**用数量写出来**（"50 个现代 vs 化石记录仅 19 处"），不写 "remains unclear"
2. 缺口句后紧跟 "**Consequently, … is not well understood**" 这类**结论化缺口句**
3. 目的句用 **"Here, we give the first description of …"**（含 "first"/"only known" 等**新颖性限定词**）
4. 目的句**之后再加一句"贡献句"**，写清楚这个发现**填补了什么、提供了什么认识**

#### 模式 B｜"为什么重要 → 为什么必须做"式（成因/沉积类）

Vashchenkova 2011 (*Marine Geology*) 的引言是**一整段没有小标题**的"必要性论证"：

> "The study of the sedimentary processes in the continent–ocean transition zone is **one of the most important tasks of modern marine geology**. In this connection, of particular interest are the Tertiary siliceous sediments … since the formation of the ancient siliceous sequences **remains one of the most intriguing problems in geology**, and the origin of the pelitomorphic siliceous rocks … is still debatable."
> 层层加码："Moreover, the mineralization type and its intensity are determined by the composition and texture of the host rocks." → "Owing to their high moisture saturation, porosity, and the occurrence of chemically active amorphous silica, siliceous rocks frequently serve as a substrate for …" → 收束："**All these properties determine the necessity of the investigation of siliceous sediments and their formation conditions.**"

🔴 **模式 B 的特点**：**没有"文献回顾"段**，而是**用重要性 + 未决性 + 现实意义三件事把必要性堆出来**，
最后一句落到"因此必须研究"。作者甚至把 **"Results and Discussion" 合并成一个段**（本文段2 标题即 RESULTS AND DISCUSSION）——
**讨论与结果合并，是本领域老论文的常见形态。**

#### 模式 C｜教科书式铺陈式（综述、教科书章节、术语解释型）

教科书式章节（放射虫学教材章）的引言**没有"缺口→目的"结构**，而是**按知识体系逐段铺陈**：
形态解剖 → 分类 → 生态 → 繁殖：

> "Polycystine radiolarians are exclusively marine, pelagic, solitary or colonial protists provided with actinopods."
> "A distinguishing feature of all radiolarians … is the central capsule, a proteinaceous perforated membrane that divides the cytoplasm into two areas … (Figure 1A)."
> "Polycystine skeletons are typically constructed of a network of structures which can be either connected at both ends with other elements - the bars (Figure 2F), or formations attached to the rest of the shell by one end only - the spines (Figure 2A-B, 2G)."
> "Polycystines consume a wide variety of prey including bacteria, algae, protists, copepods …"

🔴 **模式 C 的注意**：这类章节的图引用写 **"(Figure 1A)"**（不带点），
与期刊论文的 "(Fig. 1A)" 不同 —— **看期刊的引用格式习惯，别照抄别处**。

#### 模式 D｜材料发现式（老刊、地层/大剖面类）

Fortey & Bruton 1973 (*GSA Bulletin*) 的引言**以一句纯事实开头**：

> ① "Fossiliferous lower Paleozoic rocks were **discovered in 1965** at the top of the Hecla Hoek Series in north Ny Friesland, Spitsbergen."
> ② 工作史 + **本文范围 + 预告后续论文**："Part of the section was measured and collected in 1967, and a preliminary account … was given by Vallance and Fortey (1968) … In 1971 the field work was extended … **This paper describes the succession and its field relations and discusses its correlation within Spitsbergen and adjacent Arctic regions preliminary to more detailed paleontologic work to be published in the future.**"
> ③ 地质背景 —— **含对自身局限的坦陈**："The Cambrian rocks are, however, **incompletely exposed**, and are only present in the northern area; complete knowledge of this part of the section is unlikely."

🔴 **模式 D 有一个常被忽略的优点**：**引言里就写明材料局限**（"incompletely exposed"）。
这在通用模板里很少见，但**审稿人最想知道的正是这个**。

#### 模式 E｜铺垫 → 目的 → **单独一段声明新意**

Robinson & Haslett 1995：

> 铺垫三段（海绵骨针的成分/分类/沉积行为）之后：
> "Sponge spicules, and in particular siliceous sponge spicules, are readily fossilized due to their durability, resistance to dissolution, and to the great numbers produced, making them a common component of marine sedimentary rocks throughout the Phanerozoic. **In this study, we report on a siliceous microsclere assemblage from the mid-Early Miocene Dos Bocas Formation of Ecuador.**"
> 然后**另起一段**只写一句新意："**This assemblage is of particular interest as it comprises species previously unknown in the fossil record.**"

🔴 **模式 E 的关键动作**：**目的句与"新意声明"分成两段** ——
目的句说"我做了什么"，下一段说"为什么这个值得看"。

#### 🔴 四种模式的共同底线

| 无论哪种模式 | 具体要求 |
|---|---|
| 首句 | 给**事实**（领域事实或材料事实），不是"本文要研究 X" |
| 目的句 | **独立成句**；位置随模式而变（第 1–3 段都有），**不必强行放首句，也不必放末段** |
| 目的句内容 | **必须带具体对象与产地**（层位、区带、类群名），并常带图号交叉引用 |
| 缺口 | 可以是"remains unclear"，但**更常见的是数量化的知识空白**（"only 19 occurrences …"）或**具体的未研究对象**（哪个层/哪个区/哪个类群） |
| 新意 | 目的句之后**最好单独一段**说明"为什么这个结果值得看" |
| 局限 | **材料/数据局限可以直接写进引言**（"incompletely exposed"），不必藏到方法或讨论里 |

### 9.2 Discussion：**三段骨架 + 四种起手 + 四种收尾**

**精读 Robinson & Haslett 1995 的 Discussion 全文**，其骨架是：

> **① 直接给出比较对象**："The sponge microsclere assemblages encountered in this study are **directly comparable with** Holocene reef sponge communities off the coast of Belize and in the Gulf of Mexico, and with an Upper Jurassic microsclere assemblage."
> **② 引入已有工作并逐类群对照**："Haslett (1992) describes a microsclere assemblage from the Portlandian of southern England in which reniform microscleres … occur in association with spherical and oval-cylindrical microscleres … This Portlandian assemblage is very similar in composition with that of JW 199, in which reniform microscleres are represented by *Placospongia carinata*, spherical microscleres by *Geodia neptuni* and the oval-cylindrical microscleres by *Conciliaspongia rarus* Gen. et sp. nov."
> **③ 指出差异并推进结论**："The assemblages **only differ by** the absence in the Jurassic assemblage of a stellate microsclere, such as *Chondrilla nucula* Schmidt. This similarity appears to imply some kind of faunistic …"

🔴 **讨论的核心动作是"逐项对照"，不是"逐句罗列文献"**：
把本文的组合**按形态类型一项一项**（reniform / spherical / oval-cylindrical / stellate）去对已有组合，
最后用"只差 X"收口。**这是与通用模板最大的差别**——通用模板教你在讨论里逐条引用文献。

**四种起手（语料逐字）**：

| 起手 | 逐字例句 |
|---|---|
| **A 直接进入比较对象** | "The sponge microsclere assemblages encountered in this study are directly comparable with Holocene reef sponge communities …" |
| **B 用数据锁定时代/环境** | "The occurrence of well-known species such as *Dictyomitra formosa*, *Diacanthocapsa euganea* … undoubtedly determine the Noni Formation as having an early Late Cretaceous age (Cenomanian–Turonian)." |
| **C 先摆领域通说** | "The isotopic paleoecologics of planktonic foraminifera can be used to gain insight into the dynamics of stratification in the upper water column." |
| **D 证据 → 推论** | "**Because** the Figueroa fossils are hosted by massive sulfides and associated with basaltic pillow lavas and radiolarian cherts, **we propose that** this assemblage represents part of an Early Jurassic high-temperature hydrothermal vent community." |

🔴 **B 与 D 是本领域最值得抄的两种**：B 先用**标志性种**把时代/环境钉死（地层学论文的看家本领）；
D 用 **"Because …, we propose that …"** 一句话把**证据与推论**焊在一起。

**四种收尾（语料逐字）**：

| 收尾 | 逐字例句 |
|---|---|
| **A 让步并限定结论** | "However, some of these species occur in high latitudes where silica depletion is less pronounced than other regions of the oceans thus lessening the strength of the silica-depletion hypothesis as a major driving force in their evolution." |
| **B 明确指出后续工作** | "More detailed research of the Gufeng Formation is needed for the proper understanding of rocks from the oceanic and platformal facies." ／ "To discuss this issue, further study is required to correct the fossil data such as the Aalenian ammonoid occurring in these intervals." |
| **C 归因收尾** | "The latter result is likely due to the high factor scores of *C. d. davisiana*, a species …" |
| **D 地层/演化陈述收尾** | "Arc magmatism continued well into Late Triassic time along the Sukhothai Terrane in Thailand until its collision with the Loei Terrane during Norian time." |

🔴 **四种收尾没有一种是"未来展望 / future research will…"** ——
本领域讨论段的尾声是**限定、归因、或地质陈述**，不是展望。

### 9.3 章节顺序：**Geological setting 前置、Results 常被合并**

从 PDF 书签（224 篇）与精读全文看到的顺序：

| 主题 | 典型顺序 | 备注 |
|---|---|---|
| 系统描述 / 新类群 | INTRO → **GEO** → METH → **SYS**（逐类群并列小节）→ CONC | **没有独立 Results 段**，结果直接在 SYS 里 |
| 地层 / 生物地层 | INTRO → **GEO** → METH → **GEO/对比** → CONC | 地质背景出现两次：开头的区域背景 + 后面的地层对比 |
| 成因 / 定量 | INTRO → **GEO** → METH → **RES + DISC 合并** → CONC | 合并写法在老刊常见（"RESULTS AND DISCUSSION"） |
| 综述 / 教科书 | INTRO → 逐知识点铺陈 → CONC | 无 GEO/METH |

🔴 **三条硬事实**：
1. **"Geological setting" 几乎必选，且排在 Methods 之前** —— 这个顺序在语料里最常见。
   理由很实际：**"这套化石来自哪个层、哪个区"决定了后面所有的对比与解释**，放在 Methods 后面会颠倒因果。
2. **系统描述类论文没有独立的 Results 段** —— 结果以"逐类群并列小节"呈现。
3. **Results 与 Discussion 合并是老刊常态**（段标题直接写 "RESULTS AND DISCUSSION"），
   新刊则普遍分开。

### 9.4 交稿前自查（结构部分）

- [ ] 引言首句是**事实**，不是"本文要研究 X"？
- [ ] 引言里有**明确的目的句**（独立成句、带具体对象与产地）？
- [ ] 缺口是**具体的或数量化的**（哪个层/哪个区/多少处记录），而不是空泛的 "remains unclear"？
- [ ] 目的句之后**另有一段说明新意**（"of particular interest as …"）？
- [ ] 有 **Geological setting**，且排在 **Methods 之前**？
- [ ] 系统描述类：每个类群一个**并列小节**（Holotype→Paratype→Description→Discussion），**且没有独立 Results 段**？
- [ ] 讨论是**逐项对照**（按形态类型/属种一项一项比），而不是逐条罗列文献？
- [ ] 讨论里**标志性种**用来锁定时代/环境？
- [ ] 推论与证据之间是 **"Because …, we propose that …"** 的显式焊合？
- [ ] 讨论收尾是**让步 / 需进一步研究 / 归因 / 地质陈述**之一，而不是"未来展望"？
- [ ] 材料或数据局限**在引言里就坦陈**（而不是藏到方法或讨论里）？

## 八、来源与可回查

| 来源 | 提供什么 |
|---|---|
| 本地语料 `D:/数据集/PDF_Radiolaria`（8162 篇） | 全部比例数字、1139 条图注、376 张图的配色统计 |
| Aitchison et al. 1999, *Micropaleontology* 45(2): 138–162 | TEXT-FIGURE 制式、黑白花纹地质图、插图定位图、图例分块 |
| Basílio-Dantas et al. 2019 | 灰度环形图与 nMDS：形状编码 + 凸包轮廓 + 图例框 |
| Biard et al. 2022, *Environ Microbiol* | 彩色系统树（灰条外群 / 灰色分组框 / "?" 不支持节点）、Box 1 侧栏、面板级引用 |
| Adl et al. 2019, *J. Eukaryot Microbiol.* | 分类学论文把"分类"写成**编号命题**（(1)…(7)）的写法 |
| APP `instruction.html`、PE `contributor instructions`（见 `multi-journal-style-guides.md`） | 图注必含 authority/date/age/locality；文件名 ISO 9660 |

⚠️ **Micropaleontology 的官方作者指南页受 cookie 墙拦截**，本文件关于该刊的证据
全部来自**已刊论文本身**（属一手出版物证据），**不是官方指南原文**；
引用其格式条款前请回官方页确认。
