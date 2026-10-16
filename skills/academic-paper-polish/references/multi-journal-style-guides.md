# 多期刊官方 Style Guide 汇总（地学 / 古生物 / CV）

> **核验日期：2026-10-16。** 全部取自官方 guide-for-authors 或官方 author-kit，非二手转述。
> 每份标注**获取状态**：✅ 官方原文全量 ｜ 🟡 官方原文部分（其余域被 CF/网络拦截）｜ 📌 官方 URL 待查

---

## 目录

| # | 期刊 / 会议 | 出版社 | 状态 | 对你研究的价值 |
|---|---|---|---|---|
| 1 | **Earth-Science Reviews** | Elsevier | ✅ | ⭐⭐⭐ 综述顶刊 |
| 2 | **Nature** | Springer Nature | ✅ | ⭐⭐ 篇幅/图表最严 |
| 3 | **PNAS** | NAS | ✅ | ⭐⭐ Significance Statement 独有 |
| 4 | **CVPR / ICCV / 3DV** | CVF | ✅ | ⭐⭐⭐ 放射虫图像方向 |
| 5 | **Palaeoworld** | Elsevier | ✅ | ⭐⭐⭐ 含 Systematic palaeontology 格式 |
| 6 | **Paleobiology** | Cambridge | ✅（用户提供） | ⭐⭐⭐ 化石标本照相 |
| 7 | **Acta Palaeontologica Polonica** | 波兰科学院 | ✅ | ⭐⭐⭐ ZooBank 强制 + 图件精确参数 |
| 8 | **Palaeontologia Electronica** | OA | ✅ | ⭐⭐ 无页限无版面费 |
| 9 | **PalZ** | Springer | 🟡 | ⭐⭐⭐ Systematic Palaeontology 格式范例 |
| 10 | **Elsevier 微体古生物系**（Revue de Micro / Marine Micro / Geobios） | Elsevier | ✅ | ⭐⭐⭐ 放射虫直接对口 |

**未获取（网络阻断）**：*Palaeontology*（Wiley，403）· *Journal of Vertebrate Paleontology*（T&F，403）· *Journal of Paleontology*（Cambridge，429 限流）

---

# 一、Earth-Science Reviews（ESR）

**投稿入口**：`submit.elsevier.com/EARTH`｜**同行评审**：single anonymized，至少 2 名审稿人

## 1.1 收录边界（🔴 最容易被 desk-reject 的地方）

**本刊只发综述。** 以下**不予考虑**：
- 常规研究论文（仅在 occasional special issue 中收录）
- **Bibliometric studies**（文献计量学研究）—— 若综述必须含文献计量数据，该部分**只能放 SI**
- 无显著综述成分的 meta-analysis
- 生物学、生态学、土壤与农业科学、地质工程主题 → 应投相应领域期刊

> "Submissions that aggregate previous literature and do not integrate and build on existing knowledge are unlikely to be accepted."

## 1.2 字数与要素限制

| 项 | 要求（原文） |
|---|---|
| 综述论文 | 无严格上限，但 **>20,000 词**须先邮件与编辑讨论（抄送 timothy.horscroft@elsevier.com） |
| Discussion | **≤3,000 词**；须在原文发表后 **6 个月**内提交 |
| Reply | **≤3,000 词**；须在收到通知后 **1 个月**内提交 |
| **Abstract** | 🔴 **≤250 词**，**且必须写成单一段落** |
| **Highlights** | **3–5 条**，每条 **≤85 字符**（含空格）；作为**单独可编辑文件**提交，文件名含 "highlights" |
| **Keywords** | **1–7 个**；英文；避免含 and/of 的多词组合 |

## 1.3 文件格式

- Word 用 `.doc/.docx`，LaTeX 用 `.tex`；🔴 **PDF 不是可接受的源文件**
- Word 用**单栏**排版；双栏仅限 LaTeX
- 删除所有删除线与下划线（除科学必要性）
- 🔴 **所有稿件须含连续行号**

## 1.4 结构

- 章节须清晰编号：`1` → `1.1` → `1.1.1` → `1.2`
- 交叉引用须用编号格式，不得只写 "the text"
- 摘要不纳入章节编号
- 顺序含 Theory and calculation、Acknowledgements（**置于参考文献列表前的独立部分**）、**Author contributions: CRediT**、Appendices（A, B…；Eq. (A.1)；Table A.1, Fig. A.1）

## 1.5 图表

| 图像类型 | 格式 | 分辨率 |
|---|---|---|
| Vector drawings | EPS, PDF | 嵌入字体或将文字存为图形 |
| Photographs | TIFF, JPG, PNG | **300 dpi**（单栏最小宽 **1063 px**；全页 **2244 px**） |
| Bitmapped line drawings | TIFF, JPG, PNG | **1000 dpi**（单栏 **3543 px**；全页 **7480 px**） |
| Charts / 大表格 | XLS, XLSX | 清晰可读 |
| Annotated images | PPT, PPTX | 内嵌图 ≥300 dpi |

- 每图作为**单独文件**，命名如 `Figure_1`、`Figure_2`
- 🔴 **不可提交**：多图合并为一个文件（为互相比较而准备的图可例外）
- 🔴 **图注须置于图下方，并同时放入单独文件，且置于图像区域之外**

> **Aims & scope 特有要求**：插图必须是**实际图件**（地图、剖面、图、照片），**不能是文字的图形化重复**。所有图注——尤其图来自文献时——**必须说明该图要传达的信息（the message of the figure）**，而非仅描述其内容。

## 1.6 其他

- **单位**：必须用 SI；提及其他单位须给 SI 等值
- **公式**：可编辑文本，非图片；变量斜体；e 的幂用 `exp`；小分数用 `/`
- **表格**：可编辑文本；表注置于表体下方；**避免竖线与单元格底纹**
- **参考文献**：按第一作者字母序，同作者再按年代；**摘要中引用的文献须完整给出**；尽量给 DOI
- **数据**：Option C —— 必须存入数据仓库、在文中引用链接、或说明为何不能共享
- **生成式 AI**：须在参考文献列表前加 "Declaration of generative AI and AI-assisted technologies" 章节
- **语言**：美式或英式，**不可混用**
- **校样**：🔴 **两天内**返回
---

# 二、Nature

**官方页**：`nature.com/nature/for-authors`（Formatting guide / Initial submission / Final submission）

## 2.1 Article 篇幅（🔴 按"印刷页"算，不按字数）

| 项 | 要求 |
|---|---|
| 物理科学 | 平均**不超过 6 个印刷页** |
| 生物/临床/社科 | 平均**不超过 8 个印刷页** |
| 6 页文章 | 约 **2,500 词**正文 + 4 个 modest display items |
| 8 页文章 | 约 **4,300 词**正文 + 5–6 个 modest display items |
| "modest" display item | 含图注约占 **1/4 页**（≈270 词） |
| 复合图 | 约占 **1/2 页**（≈600 词） |
| 不间断一页正文 | 约 **1,250 词** |

## 2.2 Summary paragraph（🔴 Nature 独有，替代传统 Abstract）

- **完全引用的 summary paragraph**，理想 **≤200 词**
- 与正文**分开**；**避免数字、缩写、首字母缩写词、计量单位**（除非必要）
- 面向**本学科之外的读者**
- **结构（四步，原文）**：
  1. **2–3 句**学科基础介绍
  2. 工作背景与原理的简要说明
  3. 主要结论陈述（**用 "Here we show" 或等价表述引出**）
  4. **2–3 句**把主要发现放入更广语境，说明结果如何推动了领域前进

## 2.3 Title

- 🔴 **不超过两行印刷宽度 = 75 字符**（含空格）
- 通常**不含数字、首字母缩写、缩写或标点**
- 须有足够细节便于检索，又要宽到领域外读者能理解

## 2.4 References

- 🔴 **Article 主文通常 ≤50 条**（Methods / SI 的额外文献不计入此数）
- 每条编号只能列**一篇**出版物
- **编号按出现顺序**，正文中为上标（不用括号，除非易与上标数字混淆）
- 作者全部列出，**超过五人只列第一作者 + et al.**
- 文章标题**必填**，用正体（非斜体），首词大写，结尾加句号
- 书名斜体全大写；**期刊名斜体并按惯例缩写**；**卷号粗体**
- 只收已发表/已被具名刊物接受/已上认可预印本服务器的文献；**papers in preparation 只能在正文提及**
- 🔴 **不要用链接域（EndNote 等产生）** —— 保存前用 EndNote 的一键按钮去掉代码

## 2.5 Methods

- Methods 在正文文件中，**位于图注之后**；出现在 PDF 与在线 HTML，**不出现在印刷版**
- 🔴 通常**不超过 3,000 词**
- 已发表方法的详细描述应避免 —— 给参考文献号即可，只说明新增或改动处
- 🔴 **Methods 不能含图或表**
- 鼓励把协议存到 protocols.io（Springer Nature 免费服务）

## 2.6 Figures

- 标准尺寸：**单栏 90 mm / 双栏 180 mm**；页面全深 **170 mm**
- 图内字母**小写**，首字母大写，无句点
- 单位与数值间**一个空格**；千位用逗号（1,000）
- 🔴 **用比例尺（scale bars）而非放大倍数**
- 避免在阴影/纹理区上直接排字、避免反白字
- 图例文字尽量放图例而非图上
- **Extended Data**：纯在线，通常**最多 10 个** display items
- 🔴 Nature **不鼓励使用或改编已发表的 display items**

## 2.7 Tables

- 每表**单独一页**，**竖版**（非横版）， upright
- 表题为**一行粗体**
- 符号与缩写在表下方定义

## 2.8 其他关键

- **双倍行距**；拼写按 *Oxford English Dictionary*
- 首选 **12 号 Times New Roman**；数学符号用普通文本或 Symbol 字体
- **End notes**：Acknowledgements 应简短，**不得感谢匿名审稿人和编辑**，不得用 "excellent" / "insightful" 等词
- 🔴 **通信作者不一定资深作者**，发表其名不暗示资历
- 数据与材料**发表时必须公开**
- 含 SI 的须写："Supplementary Information is available for this paper."
- 生命科学与行为社科 Article **必须提交 Reporting Summary**

---

# 三、PNAS

**官方页**：`pnas.org/author-center`｜**投稿**：PNAScentral

## 3.1 文章类型与篇幅（🔴 按"排版页"算）

| 类型 | 篇幅 | 参考文献 |
|---|---|---|
| **Research Reports** | 优选 **6 页**，最多 **12 页**；6 页 ≈ **4,000 词** + 50 refs + 4 个中等图表 | ~50 |
| **Brief Reports** | 🔴 **3 页** ≈ **1,600 词**（含 manuscript text、title page、abstract、figure legends） | **15** |
| **Letters to the Editor** | **500 词**；2 个图表；**10 refs**；须在原文在线发表后 **6 个月**内 | 10 |
| **Opinions** | **1,500–2,000 词**（不含 refs）；不需 abstract；by invitation only | — |
| **Perspectives** | 最多 **10 页**；by invitation | — |
| **Author Responses** | **500 词**；2 个图表；11 refs | 11 |

## 3.2 🔴 Significance Statement（PNAS 独有，最易误解）

- **仅 Direct and Contributed Submissions** 需要
- 🔴 **≤120 词**（Overleaf 模板写 "between 50 and 120 words"）
- 写给**本领域外的本科教育水平科学家**
- **不是结果摘要** —— 是解释工作为何重要
- Brief Reports **不**需要

## 3.3 Abstract

- 🔴 **≤250 词**，**单一段落**
- 向普通读者解释主要贡献
- 🔴 **摘要中引用的文献必须在摘要内完整给出，且正文中也须引用**

## 3.4 Title

- **<135 字符**（或三行以内）
- **不得以问句形式出题**
- 避免数字、缩写、标点、双关语
- 须包含所研究的生物（organism）

## 3.5 稿件顺序

```
title page → abstract → significance statement → main text
(Introduction → Results → Discussion → Materials and methods)
→ Acknowledgments and funding → References → Figure legends
```

- 从 title page 开始编号所有页面
- 图表与稿件**分开上传**
- 🔴 初始投稿**格式中立**（format-neutral），不强求期刊排版

## 3.6 图表技术规格

| 项 | 要求 |
|---|---|
| 格式 | TIFF, EPS, PDF, or PPT；3D 用 PRC/U3D 且须另附 2D |
| 尺寸 | Small ≈ **9×6 cm**；Medium ≈ **11×11 cm**；Large ≈ **18×22 cm** |
| 灰度/彩图**无文字** | **300 ppi/dpi** |
| 灰度/彩图**含文字** | **600–900 ppi/dpi** |
| **Line art** | **1000–1200 ppi/dpi** |
| 字号 | 缩小后**不小于 6 pt（2 mm）**，**不大于 12 pt（6 mm）**；同图内一致 |
| 色彩模式 | **RGB** |
| 复合图 | 须预先拼合（preassemble） |
| 文字 | 避免把文字嵌入图形 |

**Figure legends**
- 多面板图：第一句为 brief overview，并**至少一次明确引用并描述每个面板**
- 所有 error bars 须明确标注并在 legend 中描述
- 用 ± 须说明是 SEM 还是 SD
- 适用时给 *P* value、magnification 或 scale bar
- 🔴 **须在 legend 中注明独立数据点数 N**
- 🔴 **所有 graph 的数值轴须从 0 开始**（log 轴除外）

**Tables**：可编辑 Word/RTF/LaTeX；表题在上、脚注在下；🔴 **避免 multipart tables**（如 Table 1A/1B）

## 3.7 数据与代码

- 🔴 **投稿时即须提交 data sharing plans**
- 🔴 **正文必须能独立成立**（不依赖 SI）
- SI Appendix：单个 PDF；Datasets：XLSX/RTF/PDF/CSV/GZ/TXT；Movies：AVI/MOV/WMV/GIF/MPEG，**≤10 MB**
- SI 图表编号从 S1, S2 开始；SI 内引用**独立编号**，不与正文交叉
- 若文章核心是新 method/technique，**methods 须在正文完整描述**

## 3.8 其他

- 🔴 通信作者**投稿时须提供 ORCID**；不得在 proofs 阶段补加
- 初评须提至少 **three** Editorial Board members / NAS members / qualified reviewers
- 返修须在收到决定后 **2 个月**内提交，否则视为 new submission；须含 **point-by-point response**；强烈建议交 tracked-changes 文件
- LaTeX 用 PDFLaTeX；须上传 .cls/.sty/.bib/.bst/.bbl/.ldf 为 "LaTeX Support File"；🔴 **禁止 nesting、cross-referencing、input 命令**
- 封面图：**21.59 cm × 27.94 cm**；EPS 或 TIFF（RGB）；附 **50–60 词** lay-language caption；**不得用 Stock photography**；**主要内容若由生成式 AI 生成则不符合资格**
- 参考文献：按出现顺序编号；期刊名用 MEDLINE/PubMed 缩写；作者超五人列第一作者 + et al.；须给卷号或 DOI

---

# 四、CVPR / ICCV / 3DV（CVF）

**官方源**：`github.com/cvpr-org/author-kit`（LaTeX 模板）｜**投稿**：CMT
⚠️ **自 2024 起不再支持 Microsoft Word 版模板**（Word 版停在 CVPR2024-v3）

## 4.1 版面（官方 `sec/2_formatting.tex` 原文数字）

| 项 | 要求 |
|---|---|
| 栏数 | 🔴 **必须双栏** |
| 印刷区总宽 | **6⅞ in（17.46 cm）** |
| 印刷区总高 | **8⅞ in（22.54 cm）** |
| 每栏宽 | **3¼ in（8.25 cm）** |
| 栏间距 | **5/16 in（0.8 cm）** |
| 主标题距页顶 | **1⅜ in（3.49 cm）**，居中 |
| 后续页距页顶 | **1 in（2.54 cm）** |
| 底边距（8.5×11 in 纸） | **1⅛ in（2.86 cm）** |
| 底边距（A4 纸） | 约 **1⅝ in（4.13 cm）** |
| 页码 | 页脚居中，距页底 **¾ in**；**review 版有页码，camera-ready 版不显示页码** |

## 4.2 字体

| 元素 | 规格 |
|---|---|
| MAIN TITLE | **Times 14 pt 粗体**；名词/代词/动词/形容词/副词首字母大写；冠词/并列连词/介词小写（除非句首）；标题后空两行 |
| AUTHOR NAME(s) / AFFILIATION(s) | **Times 12 pt 非粗体**，居中于标题下；后空两行 |
| MAIN TEXT | **Times 10 pt，单倍行距**；🔴 **不要双倍行距**；段首缩进 **1 pica**（≈1/6 in 或 0.422 cm）；**全文两端对齐**；**段间不加空行** |
| 图表题注 | **9 pt Roman**；短题注居中；**表题在表上方，图题在图下方** |
| Callouts | **9 pt Helvetica 非粗体** |
| 一级标题 | **Times 12 pt 粗体**，左对齐，仅首词大写；前后各一空行 |
| 二级标题 | **Times 11 pt 粗体**，左对齐，仅首词大写；前后各一空行 |
| 三级标题 | **Times 10 pt 粗体**，左对齐，后接句点，文字接排同行（**不鼓励使用**） |
| 脚注 | **Times 8 pt 单倍行距**；置于所引用页该栏底部；**尽量少用** |
| 参考文献 | **Times 9 pt 单倍行距**，列于文末 |

## 4.3 Abstract

- 位于左栏顶部、作者与单位信息之下
- "Abstract" 标题：**12 pt Times 粗体**，相对该栏居中，仅首词大写
- 摘要正文：**10 pt 单倍行距**
- 摘要后空两行，然后开始正文
- 社区惯例上限 **≤200 词**（官方原文只说"参考往年 CVPR 摘要感受风格与长度"）

## 4.4 引用

- 参考文献**按文末编号**，正文引用用**方括号**：`[1]`、`[2-5]`
- 一次引用多篇须**按数字顺序**
- 官方 `.bst`：`ieee_fullname`（2024 前）/ `ieeenat_fullname`（2025+）
- 交叉引用用 `\cref{}` / `\Cref{}` 自动插入标签

## 4.5 插图

- 所有图形**居中**；🔴 LaTeX 中**不要用 `center` 环境**（会加多余空白），改用 `\centering`
- 🔴 **确保任何要点在印刷版可辨** —— 读者可能打印，不能假设能缩放看细节
- 图中字号须与正文字号相称；线宽须在印刷中有效
- `\includegraphics[width=0.8\linewidth]{myfile.pdf}` 形式指定宽度

## 4.6 🔴 色盲友好（CVPR 特有）

> 大量审稿人与读者有彩色视觉缺陷，**红绿色盲最常见**。
> **避免仅靠颜色作为区分特征**（如红线 vs 绿线），**须加第二重区分特征**。

## 4.7 篇幅（社区惯例）

- 主文 **8 页**（camera-ready 可延至 **9 页**）
- 参考文献**不计入**主文页数
- 补充材料单独 PDF/zip，不限量
- 🔴 **双盲评审**：提交 PDF **不得含任何身份信息**；有严格反去匿名化规则

---

# 五、Palaeoworld

**出版社**：Elsevier（代中科院南京地质古生物研究所）｜**邮箱**：`palaeoworld@nigpas.ac.cn`
**版面费**：🔴 **无版面费（no page charges）**｜**APC**（OA）：USD 3,260

## 5.1 收录边界

接受：Palaeoworld Perspectives · Rapid Communication · Original technical research papers and case studies · **Review articles（normally invited）** · Special theme collections · Letters to the Editors · Book reviews

> 🔴 **不符合 house style、写作或准备不佳的稿件将在送审前退回修改。**

## 5.2 篇幅

- 一般不超过 **30 个印刷页**（Palaeoworld 格式）
- 更长者须投稿前联系 Editor-in-Chief
- 相关论文间重复内容应最小化

## 5.3 结构

章节编号 `1` → `1.1` → `1.1.1` → `1.2`；交叉引用用编号；摘要不入编号
建议顺序：Introduction（明确目标，**避免详细文献综述或结果摘要**）→ Methods（足够细节以独立重复）→ Results（清晰简洁可重复）→ Discussion（探讨意义，**避免大量引用文献**）→ Conclusion（可独立成节或并入 Discussion / Results and Discussion）→ Theory and calculation → Acknowledgements（**置于参考文献列表前的独立章节，不得放标题页**）→ **Author contributions: CRediT**（14 类角色）→ Appendices（A, B…；Eq. (A.1)；Table A.1, Fig. A.1）

## 5.4 摘要与关键词

- **Abstract ≤250 词**；摘要中引用的文献须完整给出
- **Keywords 1–6 个**，英文，避免含 and/of 的多词组合

## 5.5 命名法与单位（🔴 古生物核心）

- 必须遵循 **ICBN** 与 **ICZN** 现行版
- 🔴 所有描述和图示的化石**必须注册并存放于具永久保存能力的正规公立机构**；登记号须在文中给出（通常在 systematic palaeontology 部分和图题中）
- 所有分类单元的作者名和日期须在**首次使用后**给出；作者名**完整拼写，不得用 "et al."**
- 格式：*Hongshanosaurus houi* You, Xu and Wang, 2003.
- 同物异名列表用 Matthews (1973) 符号；附加信息置括号内；同义名列表仅注文献首页，但**所有图版和图版号须列入**
- **Open nomenclature**：*Luciniola* cf. *pumila* (Goldfuss, 1840)（**非** *Luciniola* cf. L. *pumila*）；*Luciniola*? sp.（**非** ? *Luciniola* sp.）
- **小数点**（不用逗号）；千位以上用**空格**分隔
- 拉丁文来源表达（*in vivo, et al., per se*）**不斜体**
- **属名缩写**：首次全称；之后可缩写为词首大写字母加句点（如 *H.*）；句首及与 "sp." 连用时须全称；**种及亚种名不得缩写**

## 5.6 🔴 Systematic palaeontology 标题顺序（★ 分类学论文必读）

**新属（new genus）**：
1. Genus name + "n. gen."
2. *Figures*（仅在未含物种正式描述时提供）
3. *Synonymy list*（含图版和插图引用），可选
4. *Etymology*，**必需**
5. *Type species*，**必需**，注明指定方式（original designation 或 subsequent designation by Author (year, p. xx)）
6. *Other species*（不完整时）或 *Included species*（完整时），推荐
7. *Diagnosis*，**必需**，**电报式文体**
8. *Description*，推荐
9. *Remarks*，推荐
10. *Occurrence*，推荐

**新种（new species）**：
1. Species name + "n. sp."
2. *Figures*，**必需**
3. *Synonymy list*，如适用则必需
4. *Etymology*，**必需**
5. *Types*，**必需**：type designations、repository acronyms、catalogue numbers、含模式地层的地层划分与地质年代、模式产地地理位置（正模与副模分别列出）；测量数据置于 Description 后单独标题 "*Measurements*"
6. *Other material examined*，如适用则必需
7. *Diagnosis*，**必需**
8. *Description*，**必需**（脊椎动物或植物可按解剖部位分小节）
9. *Measurements*，至少提供模式标本测量数据
10. *Remarks*，推荐
11. *Occurrence*，**必需**

## 5.7 图表

| 图像类型 | 格式 | 分辨率 |
|---|---|---|
| Vector drawings | EPS, PDF | 嵌入字体或文字存为图形 |
| Photographs | TIFF, JPG, PNG | **300 dpi**（单栏最小宽 **1063 px**；全页 **2244 px**） |
| Bitmapped line drawings | TIFF, JPG, PNG | **1000 dpi**（单栏 **3543 px**；全页 **7480 px**） |
| Charts / 大表格 | XLS, XLSX | 清晰可读 |
| Annotated images | PPT, PPTX | 内嵌图 ≥300 dpi |

- 每图单独文件，命名 `Figure_1`、`Figure_2`
- 🔴 **不得提交多图合并文件**（为对比目的准备的前/中/后照片可例外）
- 🔴 **不得增强、遮蔽、移动、移除或引入图像中任何特征**
- 亮度/对比度/色彩平衡调整不得遮蔽或消除原始信息
- **非线性调整（如 gamma）须在图题中声明**
- 🔴 **禁止使用 AI 工具创建或修改代表原始观测/实验数据的图像**
- 表格：**避免竖线与单元格底纹**；表注置于表体下方
- 附加材料单文件最大 **150 MB**，总计最大 **1 GB**

## 5.8 其他

- **投稿信必须附**，书面声明未发表且不同时投他处，说明科学意义与广泛吸引力
- 两名及以上作者的稿件，**所有作者须发 author agreement**
- 参考文献：正文引用 "作者（不含首字母）+ 年份"，按时间序；表按作者姓氏字母序；非英文文献加注 "(in Russian)" 等
- Word 用 `.doc/.docx`，LaTeX 用 `.tex`；🔴 **不接受 PDF 作源文件**；Word 用**单栏**

---

# 六、Acta Palaeontologica Polonica（APP）

**官方页**：`app.pan.pl/instruction.html`（最后更新 2024-01-03）｜**投稿**：`e-system.app.pan.pl`
**许可**：**CC BY**｜**篇幅**：收 moderate length 稿件；>100 排版页者以 Palaeontologia Polonica 增刊出版

## 6.1 稿件类型与篇幅

| 类型 | 篇幅 |
|---|---|
| 常规 Articles | moderate length |
| **Brief reports** | **2,000–3,000 词**，约 12 个双倍行距页（含插图） |
| **Comments / Discussions** | **1,000–1,500 词**，约 6 个双倍行距页 |
| **Prefaces** | **500–1,500 词**，约 3 页 |
| **Monographs** | **50,000–75,000 词**，约 300 个双倍行距页 |

Brief reports 结构：title → **加粗首段（提供工作原理并总结主要结果）** → main text → acknowledgements → references → 邮件地址与 ORCID

## 6.2 格式（🔴 与 Paleobiology 高度相似）

- 🔴 **全稿双倍行距**（含摘要、正文、参考文献、表格、图注、附录）
- **Times New Roman，12 号**
- 从 title page 开始**编号所有页**
- 🔴 **不右对齐、不在右边界断词**
- 图表在正文中**按连续顺序**引用
- 一般**不超过三级标题**

## 6.3 图件（🔴 参数极精确，古生物刊中最细）

| 项 | 要求 |
|---|---|
| 双栏宽 | **183 mm** |
| 单栏宽 | **89 mm** |
| 最大长 | **237 mm** |
| 字体 | 推荐 **Calibri 8 pt** |
| 线粗细 | **0.2 mm** |
| 比例尺 | **0.7 mm** |
| 分辨率 | line art（位图）**400 dpi**；照片 **≥400 dpi at final size**，**非插值、不压缩**（如不用 JPEG） |
| 格式 | 照片 AI / PSD / CDR / TIFF（layered）；线绘 CorelDraw（≤2021）/ Illustrator（≤CS5）/ EPS |

- 🔴 **字母从左上到右下连续**；同一标本多视角用同字母加数字下标（A₁, A₂, A₃）
- 🔴 **放大用比例尺表示**
- 标注用**全称**而非缩写（线绘必用，照片有空间时也用）
- **照片须黑背景**；对象边缘须清晰；白背景可接受但最亮区不得全白
- 复杂解剖物体**推荐立体照片对**，配解释性线绘；立体对**并排**（非上下），间距**最大 65 mm**
- 🔴 插图须交**可编辑文件**（CDR/AI/layered TIFF/PSD），标注在**单独图层**；或交两版（有标注/无标注）—— **终版字母与符号由编辑部添加以保证 APP 风格一致**
- 线绘图须**紧密裁切**

## 6.4 🔴 ZooBank / IPNI 强制注册（★ 新分类单元必做）

> 自 APP issue 64(1) 起，**在 APP 发表的命名行为必须在在线出版前注册 ZooBank**，并**在 Systematic palaeontology 部分提供 ZooBank 号**。新植物分类单元注册 IPNI。

## 6.5 Systematic palaeontology 组织

**新属**：Etymology（新属必需）→ Type species（含 authority, locality, age）→ Species included（新属必需）→ Diagnosis（新属必需）→ Remarks（可选）→ Stratigraphic and geographic range（新属必需）

**新种**：Species name → Figures → Etymology → Type material（Holotype, Paratypes）→ Type locality → Type horizon → Material → Diagnosis → Description（可按解剖部位或发育阶段分小节）→ Remarks（**与其他分类单元的比较放这里**）→ Stratigraphic and geographic range

**已描述种**：Species name → Figures → **Synonymy** → Material（必需）→ Description → Remarks → Stratigraphic and geographic range（除 open nomenclature 外**必需**）

**同义名格式范例**：
```
1956 Martellia ichangensis sp. nov.; Wang 1956: 11, pl. 2: 1-5.
1974 Martellia ichangensis Wang, 1956; Xu et al. 1974: 148, pl. 65: 5-7.
```

🔴 **分类单元作者名是名称的一部分，不是引用**。若需引用源出版物，须恰当表述（如 "... Pallas (1778) based (*Lepus europaeus*) on..."）。**不把出版物合著者与分类单元名称作者混同**（依 ICZN）。

## 6.6 命名法与地层学术语

- 🔴 **新分类单元在正文全篇用 "sp. nov." 和 "gen. nov."**
- 属名在句首及与 "sp." 连用时**拼全称**；在同一主要标题内首次全称后可缩写；*Agenus* cf. *A. species* 组合可缩写；**种及亚种名不得缩写**
- 两位分类单元作者间用 **&** 而非 "and"（与常规引用不同）
- 🔴 **正式承认的时间与岩石地层单位大写**（Middle Ordovician, Late Cretaceous），**非正式的不大写**（late Paleozoic, middle Pliocene）
- 🔴 **已发表工作引用用过去时**（"Kowalski (1900) noted that..."）
- 问号与属名间**不加空格**：*Homo*?（问属级归属）· *Homo sapiens*?（问种级）· ?*Homo sapiens*（问整个鉴定）
- 句中列项用**小写罗马数字**：(i)…; (ii)…; (iii)…
- 生物带名：APP **两部分均大写**（"Conodont Zone"）；也允许 *Gracilis* Zone 无斜体写法；岩性术语可不斜体（*Posidonia* Shales）

## 6.7 其他

- **Abstract**：**结构化**，min 100 / max 300 词；**所有新描述分类单元须在摘要中给出名称**；除异常情况外摘要不引文献
- **Keywords**：从投稿表列表选题，另可建议 **3–8 个**；含地层与地理信息；高级分类单元用拉丁名
- **Introduction**：简洁，专业古生物/地质学者可读；**提供最少背景**；**不做文献综述**
- 机构缩写按字母序列出（缩写, 机构名, 城镇, 国家）
- 所有图示和描述的化石**须存于合适博物馆**，引用馆藏号并前置机构缩写
- **Discussion**：聚焦解释与意义；陈述启示与局限；**含未来研究可能性**
- **Conclusions**：不得含新数据或发现；若 Discussion 与 Conclusions 合并，须命名 **Concluding remarks**
- **Cover letter**：**不超过 A4 一面（≤300 词）**；首段解释为何需要该研究并清晰陈述研究问题
- **数据**：Joint Data Archiving Policy —— 数据须作 SOM 或归档至 Dryad / MorphoBank / GenBank；可 embargo 至多一年
- 篇幅费：**10 个排版页内免费**（约 30 个双倍行距页）；超出每页 **EUR 22**（含 VAT）；**彩色图自 issue 69(1) 起免费**
- ⚠️ **缅甸琥珀**：2017 年起收集的缅甸琥珀论文不予发表（SVP 建议，2020-04-23 生效）
- **Proefs**：PDF 形式，**最好 48 小时内**返回；**只允许必要更正**，过度更改费用由作者承担

---

# 七、Palaeontologia Electronica（PE）

**官方页**：`palaeo-electronica.org/content/contributor-instructions`（Contributor Instructions 2023-current）
**性质**：最古老的开放获取同行评审电子古生物期刊｜**无页限、无版面费**

## 7.1 稿件结构（终稿顺序）

```
1. title page   2. author page   3. abstract   4. translated abstracts（可选）
5. plain language summary   6. body of the text   7. acknowledgements
8. references   9. figure/table/appendix captions
```

- Figures、tables、appendices **必须作为单独文件**提交
- 单文件 **≤50 MB**；总计 **≤200 MB**

## 7.2 格式

- 🔴 **全稿双倍行距**（含摘要、正文、参考文献、图表附录说明）
- 🔴 **右边界不对齐**（do not justify）
- 图表附录按正文引用顺序编号
- 🔴 **不用脚注**

## 7.3 标题页与作者页

- **独立标题页**；标题简短、左对齐、**仅首字母大写**（专有名词除外）
- 最多 **6 个关键词**；描述新分类单元时用 "new species" / "new genus" 而**不给出具体名称**
- **独立作者页**：列所有作者与全部联系信息；第一作者非通信作者须注明；**该页在送审前会被移除**
- 每位作者须提供**简短传记与照片**（照片 **72 ppi、至少 300 px 宽**），在 PEMSATS 单独录入，**不放入稿件正文**

## 7.4 摘要与通俗摘要（🔴 PE 独有双摘要）

- **ABSTRACT** 大写、左对齐于页顶；次行摘要 **≤250 词**
- 摘要应提供研究与结论的相关细节；避免 "will be discussed herein" 类表述；**不含参考文献**
- 🔴 **必须提供 plain language summary** —— 用非专业人士可理解的语言描述研究背景与主要发现

## 7.5 标题层级

| 层级 | 格式 |
|---|---|
| 一级 | **全大写，居中** |
| 二级 | 左对齐顶格，**粗体大小写混排**，独立一行 |
| 三级 | 粗体大小写混排，后接**句点+空格**，文字接排同行 |

## 7.6 图件（🔴 PE 参数）

| 项 | 要求 |
|---|---|
| 宽度 | **175 mm 或 84 mm**，**300 ppi 或更高**（首次 PDF 投稿可 **150 ppi**） |
| 字号 | **8 pt 或更大**（按印刷尺寸） |
| 色彩模式 | 🔴 **RGB，不用 CMYK** |
| 照片格式 | **TIFF 或 PSD** |
| 矢量格式 | **AI（Illustrator CS6）或 EPS** |
| 终稿 | 🔴 **不要用 Word 或 PDF 交终稿图** |
| 图部件编号 | 🔴 **用字母不用数字**：1A, 1B, 1C（**非** 1.1, 1.2, 1.3） |
| 部件 | 须与图注所列一致 |

**其他图件要求**
- 🔴 **照片图须在图内有比例尺**，或在图注中标明标本/物体/视野尺寸
- 图像对比与密度**均匀**
- 线绘、plot、sketch **背景白色**；照片背景**白或黑**；黑背景用 RGB `0,0,0` 或 CMYK `C75 M68 Y67 K90`
- 🔴 **提交前须打印所有图**（无论彩色或黑白）检查纸上效果；**彩色图也须印成黑白**检查灰度值是否足够区分
- 若色调重要，须用校准显示器，并在图中加**灰阶条**供读者校准
- 动画：MOV（QuickTime）或 GIF，约 **512 px**；每个动画须提供一张静态图用于印刷版
- 作者照片：**72 ppi，至少 300 px 宽**

## 7.7 图注

- 图注写在稿件 Word/RTF 文件内，格式同新投稿件
- 每条以 **FIGURE / TABLE / APPENDIX**（大写）+ 编号 + 句点（粗体）开头，图注文字用常规体
- 例：`FIGURE 1. Location map of studied exposures.`

## 7.8 🔴 文件命名（ISO 9660 约束，极易踩坑）

**只允许**：小写字母 · 数字 0-9 · 下划线 `_` · 句点 `.`
**禁止**：
- 超过 **8 个字符**的主文件名
- 超过 **3 个字符**的扩展名
- **空格**
- 任何其他字符（`~!@#$%^&*()+=-?><,;:'"[]{}` 等）

---

# 八、PalZ（Paläontologische Zeitschrift）

**出版社**：Springer｜**ISSN**：0031-0220 (print) / 1867-6812 (online)｜**创刊**：1913
**官方期刊**：Paläontologische Gesellschaft（德国古生物学会）｜**投稿**：`editorialmanager.com/paze`
**投稿指南**：`springer.com/journal/12542/submission-guidelines`｜**IF**：1.5（2025）

## 8.1 Systematic Paleontology 格式（官方专门文件）

> 官方有单独 PDF 说明 Systematic Paleontology 排版（Michael Rasser, 2022-11-14 / 2024-07 更新）
> `media.springer.com/.../12542_PalZ-Format_Syst_Pal_July_2024.pdf`

| 规则 | 要求 |
|---|---|
| 分类单元名称 | **粗体** |
| 层级与作者 | **常规字体** |
| 空行 | **仅在属级与种级分类单元前后**（**不在种名与图引用之间**） |
| 子标题 | **斜体**，后接**句点**；标题**前**加一空行 |
| 同义名列表 | 🔴 **每隔一行缩进（hanging indent）**；缩进行须**垂直对齐** |
| 作者与年份间逗号 | 🔴 **加逗号**（注意：**这与正文引用不同**，正文引用不加逗号） |

**范例结构（官方示例，节选）**：
```
Systematic Paleontology
Order Palaeocopida Henningsmoen, 1953
Suborder Palaeocopina Henningsmoen, 1953
Superfamily Beyrichiacea Matthew, 1886
Family Beyrichiidae Ulrich, 1894
Genus Zygobeyrichia Ulrich, 1916

Type species. Zygobeyrichia apicalis Ulrich, 1916.

Important diagnostic features. Large trilobate beyrichiacean ostracodes,
according to Ulrich (1916) characterised by a [....]

Zygobeyrichia subcylindrica (Richter, 1863)
Figures 10, 11

1863 Beyrichia Kloedeni M'Coy — Richter: p. 671, pl. 19, figs. 7, 8, 9,
    10 and 11.
1863 Beyrichia subcylindrica n. sp. — Richter: p. 671–672, pl. 19,
    figs. 12, 13, 14 and 15.
1968 Zygobeyrichia subcylindrica (Richter, 1853) — Zagora: p. 13–15,
    text-figs. 4, 5, pl. 1, figs. 1, 2 and 3 (with synonymy)

Remarks. The species was revised by Zagora (1968) due to new material from
the latest Emsian of Thuringia. [….]
```

> ⚠️ 注意 PalZ 与 APP 的一处**关键差异**：PalZ 的 taxonomic authority **加逗号**（`Henningsmoen, 1953`），而 APP/Paleobiology 系的分类单元名称后**不加逗号**。

## 8.2 收录范围

古生物学全谱：Palaeozoology · Palaeobotany · Palaeoecology · Palaeogeography · Geobiology · 理论与方法 · 相关领域（如生物学）贡献
接受高质量 original research papers 与 review articles；可提议 topical volumes

---

# 九、Elsevier 微体古生物系（放射虫直接对口）

以下期刊**共用 Elsevier 标准 guide-for-authors 模板**（与 ESR 同源），期刊间差异仅在 Aims & Scope 与 APC：

| 期刊 | 范围 | 与你研究方向 |
|---|---|---|
| **Revue de Micropaléontologie** | 微体古生物全领域；鼓励微体化石组合数据（含壁化学成分）与地层/古环境问题结合 | ⭐⭐⭐ 放射虫直接对口 |
| **Marine Micropaleontology** | 海洋微体古生物 | ⭐⭐⭐ 放射虫直接对口 |
| **Geobios** | 古生物与地层学（里昂） | ⭐⭐ |
| **Comptes Rendus Palevol** | 古生物与演化（法国自然历史博物馆） | ⭐⭐ |

**Elsevier 通用硬约束**（详见 ESR 一节，各刊一致）：
- Abstract **≤250 词**
- Keywords **1–7 个**
- Word `.doc/.docx` / LaTeX `.tex`；🔴 **PDF 非源文件**；Word **单栏**
- 🔴 **连续行号**
- 照片 **300 dpi**；线绘 **1000 dpi**
- 表格**避免竖线与底纹**
- 图注置于图下方 + 单独文件
- **CRediT** 作者贡献
- 数据 Option C（存仓库 + 引用链接，或说明原因）
- 校样 **两天内**返回
- 🔴 **不得增强/遮蔽/移动/移除/引入图像特征**；非线性调整须在图注声明；**禁止 AI 生成或修改代表原始数据的图像**

**APC 参考**：Palaeoworld USD 3,260

---

# 十、横向对比（选刊决策用）

## 10.1 摘要 / 前置要素

| 期刊 | 摘要上限 | 特殊前置要素 | Keywords |
|---|---|---|---|
| **ESR** | **250 词** | — | 1–7 |
| **Nature** | **200 词**（summary paragraph） | 四步结构，禁数字/缩写 | — |
| **PNAS** | **250 词** | 🔴 **Significance Statement ≤120 词** | — |
| **Paleobiology** | **300 词** | 🔴 **Non-technical Summary ≤300 词** | <6 |
| **Palaeoworld** | **250 词** | — | 1–6 |
| **APP** | **100–300 词**，**结构化** | 新分类单元须在摘要给出名称 | 3–8 |
| **PE** | **250 词** | 🔴 **plain language summary** | ≤6 |

> 🔴 **三门"双摘要"要求各不相同**：Nature=summary paragraph（四步结构）｜PNAS=Significance Statement（讲重要性不讲结果）｜Paleobiology=Non-technical Summary｜PE=plain language summary。**同一篇论文换个刊就要重写前置部分，别偷懒复用。**

## 10.2 图表参数对比

| 期刊 | 照片 dpi | 线绘 dpi | 单栏宽 | 双栏宽 | 最大高 | 字号下限 | 线宽下限 |
|---|---|---|---|---|---|---|---|
| **ESR / Palaeoworld / Elsevier 系** | **300** | **1000** | — | — | — | — | — |
| **PNAS** | 300（含文字 600–900） | **1000–1200** | ~9 cm | ~18 cm | ~22 cm | **6 pt** | — |
| **Paleobiology** | **600** | **1200** | **9 cm** | **18 cm** | **24 cm** | **8 pt** | **0.3 pt** |
| **APP** | **400** | **400** | **89 mm** | **183 mm** | **237 mm** | **8 pt** | **0.2 mm** |
| **PE** | **300**（可 150 首投） | **300** | **84 mm** | **175 mm** | — | **8 pt** | — |
| **CVPR** | — | — | 8.25 cm（栏宽） | 17.46 cm（区宽） | 22.54 cm | — | — |
| **Nature** | — | — | **90 mm** | **180 mm** | 170 mm（页全深） | — | — |

> 🔴 **同是"化石照片"， Paleobiology 要 600 dpi，APP 要 400 dpi，PNAS 要 300 dpi（含文字则 600–900）。** 按最高标准（600 dpi）准备最安全。

## 10.3 图件提交方式

| 期刊 | 图是否嵌入正文 | 单独文件 | 命名要求 |
|---|---|---|---|
| **Nature** | 初投鼓励放一起 | 终稿分开 | — |
| **Paleobiology** | 🔴 **不嵌入** | ✅ | `Fig1_2col.tif`（含栏宽） |
| **APP** | 终稿标位置 | ✅ | 可编辑格式，标注单独图层 |
| **PE** | 🔴 **不嵌入** | ✅ | 🔴 **ISO 9660：≤8 字符，仅小写/数字/`_`/`.`** |
| **Elsevier 系** | — | ✅ | `Figure_1`、`Figure_2` |
| **CVPR** | LaTeX `\includegraphics` | — | — |

## 10.4 篇幅与参考文献

| 期刊 | 篇幅 | 参考文献 |
|---|---|---|
| **ESR** | 综述无上限（>20,000 词先商量） | — |
| **Nature** | 6–8 印刷页；2,500–4,300 词 | 🔴 **≤50** |
| **PNAS** | 6 页（最多 12）；Brief Report 3 页 / 1,600 词 | ~50（Brief Report **15**） |
| **Paleobiology** | — | — |
| **Palaeoworld** | **≤30 印刷页** | — |
| **APP** | Brief report 2,000–3,000 词 | — |
| **PE** | 🔴 **无页限** | — |
| **CVPR** | 主文 **8 页**（camera-ready 9 页） | 不计入页数 |

## 10.5 Systematic palaeontology 格式差异（★ 分类学论文换刊必改）

| 项 | **Paleobiology** | **Palaeoworld** | **APP** | **PalZ** |
|---|---|---|---|---|
| 分类单元名称后逗号 | 无 | 无 | 无 | 🔴 **有** |
| 名称字体 | 斜体 | 斜体 | 斜体 | **粗体** |
| 层级/作者字体 | — | — | — | 常规 |
| 同义名列表缩进 | — | Matthews (1973) 符号 | 每行独立 | 🔴 **hanging indent，隔行缩进** |
| 空行 | — | — | — | 仅属级/种级前后 |
| 子标题 | — | *斜体* + 必需/推荐标注 | — | **斜体** + 句点 |
| 命名注册 | — | 存公立机构 | 🔴 **ZooBank 强制** | — |

> 🔴 **这是换刊成本最高的一块。** PalZ 要粗体名称 + authority 加逗号 + 隔行缩进；Paleobiology/APP 系要斜体名称 + 不加逗号。**同一套 systematic palaeontology 文本不能直接搬。**

## 10.6 通用红线（所有刊一致，最易违反）

1. 🔴 **照片不得改动** —— 除色调、对比度、加标注/轮廓线；非线性调整（gamma）须在图注声明
2. 🔴 **标本照片必须带比例尺 + 数值说明**，**不可用 ×40 等放大倍数代替**（终版可能缩放）
3. 🔴 **禁止 AI 生成或修改代表原始观测/实验数据的图像**（Elsevier / Palaeoworld 明令）
4. 🔴 **化石须存公立机构并给登记号**
5. 🔴 **不得直接复制已发表图**（除 OA / 已获许可）；修改后必标来源
6. 🔴 **新分类单元命名须注册**（ZooBank / IPNI）
7. 🔴 **摘要与结论中不应出现参考文献**（PNAS 例外：摘要引用须在摘要内完整给出）
8. 🔴 **SI / 补充材料的文献不计入主 Literature Cited**
9. 🔴 **图表按正文出现顺序编号**，不用图注排位（Paleobiology 明令 no figure call outs）
10. 🔴 **字体须嵌入**（矢量图）
11. 🔴 **Ga/Ma/ka = 年代，Gyr/Myr/kyr = 跨度**；**upper/middle/lower = 岩石地层单位，early/late = 时间单元**
12. 🔴 **Elsevier 校样 2 天内返回；APP 48 小时内**

---

# 十一、给你的选刊建议（放射虫化石图像提取方向）

## 11.1 期刊梯队

| 梯队 | 期刊 | 理由 |
|---|---|---|
| **首选** | **Paleobiology** | 化石图像方法学接受度高；图件规范明确支持标本照相；已有官方 style guide 在手 |
| **首选** | **Revue de Micropaléontologie** / **Marine Micropaleontology** | 放射虫直接对口；Elsevier 模板已掌握 |
| **次选** | **Palaeoworld** | 无版面费；中科院南京院所办，国内放射虫成果接受度高；含 Systematic palaeontology 完整规范 |
| **次选** | **APP** | 图件参数最明确；CC BY；ZooBank 注册流程成熟 |
| **冲刺** | **Nature / PNAS** | 若方法有跨学科突破；但篇幅/前置要素约束最严 |
| **综述** | **ESR** | 若做"计算机视觉在微体化石分类中的应用"综述 —— **这正是你课程报告的主题** |

## 11.2 立即可做的三件事

1. **按最高标准备图** —— 化石照片统一做到 **600 dpi at final size**，可同时满足 Paleobiology(600)/APP(400)/PNAS(300)/Elsevier(300)
2. **若含新分类单元** —— 现在就注册 **ZooBank**（APP 强制，Nature 也要求 LSID），别等到 proof 阶段
3. **论文同时准备两版前置部分** —— 学术摘要（≤250 词）+ 通俗摘要（≤300 词），覆盖 Paleobiology / PNAS / PE 三家的双摘要要求

## 11.3 待补的网络阻断项

以下期刊官方 guide 因 CF/网络阻断未取到，需要时用浏览器手动打开：

| 期刊 | 官方 URL | 阻断原因 |
|---|---|---|
| *Palaeontology*（Palaeontological Association） | `palass.org/publications/palaeontology/` | Wiley 403 |
| *Journal of Vertebrate Paleontology* | `tandfonline.com/journals/ujvp20` | T&F 403 |
| *Journal of Paleontology*（CUP） | `cambridge.org/core/journals/journal-of-paleontology` | Cambridge 429 限流 |
| *PalZ* 完整 submission guidelines | `springer.com/journal/12542/submission-guidelines` | `media.springer.com` 连接失败（已通过搜索取得 Systematic Palaeontology 部分） |

> 本机连通性：**Nature / Springer / palaeo-electronica.org / app.pan.pl / elsevier.com(仅跳转) / github.com 可达**；
> **sciencedirect.com / pnas.org / wiley.com / tandfonline.com / geoscienceworld.org 被 CF 拦截**；
> **media.springer.com 连接失败**。
