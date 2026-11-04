# AI/ML 方法类地学论文的写作实证（v2.16.0 新增）

> **本文件解决什么问题**：`fulltext-reading-evidence.md` 的 164 篇语料**全部是描述类系统学论文**
> （新种描述、属级修订），**没有一篇是「用机器学习/深度学习做一项地学研究」的论文**。
> 本文件补上这个空白：把「AI 方法类地学论文**实际怎么写**」逐条取证。
>
> **证据来源**：`D:\文档\硕士\论文\artificial intelligence in taxonomical classification\参考文献`
> 共 225 篇 PDF（本机收集的「AI × 分类学」专题文献）。
> 225 篇全部抽取正文并**逐字精读其中 77 篇**（分层见 §一），
> 另有 **225 篇全部**做机器层的声明块/章节链统计。
>
> 🔴 **本文件的语料不是随机样本**（是「AI × 分类学」专题的人选文献），
> 因此**结论一律写成「在本批 N 篇中观察到」，不写成领域规律**；
> 分级口径见 `fulltext-reading-evidence.md` §12（A/B/C 级）。

## 一、阅读口径与分层（先说清楚能兑现什么）

| 口径 | 数值 | 说明 |
|---|---|---|
| 目录下 PDF 总数 | **225** | 全部英文 |
| 正文抽取成功 | **225 / 225** | 无一失败 |
| 正文可逐字读（≥3000 字符） | **224** | 1 篇为 0 字符（扫描件） |
| 正文合计 | 约 **1650 万字符** | 已切除参考文献列表 |
| **逐字精读** | **77 篇** | 分 25 个分片，每篇由独立子 Agent 读到文件末尾 |
| 机器层统计 | **225 篇全部** | 章节链、声明块、逐字声明块抽取 |
| 语种 | 全英文 | **无中文/俄文对照** |

### 1.1 分层判据（机器执行，可复现）

按「论文自己的研究对象是不是化石/微体化石」+「有没有用 AI/ML 方法」两轴分层：

| 层 | 判据 | n | 处理 |
|---|---|---|---|
| **A 组** | **标题含化石/微体化石类群词** + 摘要/引言含 AI/ML 方法词 | **50** | **逐字精读（主证据）** |
| **B 组** | 标题不含、但摘要/引言对象是化石 + 用 AI | **29** | **逐字精读（次证据）** |
| **C 组** | 用 AI，但研究对象不是化石 | **113** | **不逐字精读**；只用于声明块句式库 |
| **D 组** | 其他 | 21 | 不读 |
| **X 组** | 历史文献（Darwin 1859 / Linne 1759 等）或文本层不可读 | 12 | 不读 |

> A 组 50 篇覆盖放射虫、有孔虫、硅藻、牙形石、菊石、孢粉、纺锤虫、浮游有孔虫、
> 双壳类/腕足、钙质超微化石、鱼牙微体化石等 —— **与本 skill 的目标领域完全对齐**。

### 1.2 这批语料的三个已知缺陷（必须随结论一起声明）

1. **文件名不可信**：已发现文件名与正文不符的实例 ——
   `Beaufort_2004_coccolith_neural_net.pdf` 的正文实际是
   Boeckel & Baumann 2004（*Marine Micropaleontology* 51:301–320），
   全文**既无 Beaufort 也无 neural network**，用的是经典多元统计（DCA/CCA/聚类）。
   → **本文件所有「逐字精读」结论均以正文实际作者/期刊为准，不以文件名为准。**
2. **全英文，零中文对照**：本文件的结论**不能**直接套到中文刊（对照 `fulltext-reading-evidence.md` §8.11 的中文刊骨架）。
3. **专题偏倚**：语料由人选收集，偏向「AI 用于分类/识别」，**不能**用于估计「AI 论文占地学论文多少比例」这类频率。

## 二、范式对照：描述类 vs 方法类（机器统计，同口径）

这是本文件存在的理由。两条语料用**同一套机器判据**统计：

| 维度 | 描述类语料（旧，n=164） | **方法类语料（新，A 组 n=50）** |
|---|---|---|
| 有独立 Discussion 段 | **约 35%**（65% 无） | **48%**（24/50） |
| 有独立 Conclusion 段 | 有（两种形态） | **52%**（26/50） |
| **Discussion 与 Conclusion 并存** | — | **38%**（19/50） |
| 有独立 Results 段 | 描述类**没有** | **46%**（23/50） |
| 有独立 Methods 段 | 三档详略（完整式/一句式/写进摘要式） | **62%**（31/50） |
| 有独立 Systematic 段 | **描述类的核心** | **0%**（0/50） |
| 有 Repository 段 | 描述类必备 | **0%**（0/50） |
| 有 Geological setting 段 | 描述类几乎必选 | **0%**（0/50） |
| 有 Acknowledgements 段 | — | **50%**（25/50） |

→ 🔴 **两类论文的骨架不可混用**。描述类论文的「无独立 Discussion/Results、有 Repository/Geological setting」
  这些结论**只在描述类成立**；方法类论文恰恰相反。
  → 写「微体古生物 + AI」的论文时，**不要**套用描述类的骨架（那是新种描述的骨架）。

## 三、声明块：现代地学/古生物论文必写的六块

> 本节的百分比来自 **225 篇机器统计**（标题锚定 + 行内标题两种匹配，取最长连续块），
> 逐字原文来自 A/B 组 79 篇。**每个分母都写明。**

### 3.1 出现频率（分母 = 该层篇数）

| 声明块 | A 组（化石+AI, n=50） | B 组（n=29） | C 组（纯 AI, n=113） | D 组（n=21） |
|---|---|---|---|---|
| **Data availability** | **54%**（27/50） | 31%（9/29） | 28%（32/113） | 10%（2/21） |
| **Competing interest** | **52%**（26/50） | 41%（12/29） | 21%（24/113） | 5%（1/21） |
| **Author contributions** | **46%**（23/50） | 38%（11/29） | 23%（26/113） | 5%（1/21） |
| **Funding** | 38%（19/50） | 28%（8/29） | 27%（30/113） | 14%（3/21） |
| **Code availability** | **24%**（12/50） | 10%（3/29） | 5%（6/113） | 0%（0/21） |
| **Ethics / IRB** | 4%（2/50） | 3%（1/29） | 8%（9/113） | 0%（0/21） |
| **AI 使用声明** | 0%（0/50） | 0%（0/29） | 1.8%（2/113） | 0%（0/21） |

> ⚠️ **v2.16.1 口径补充（原文保留）**：上表 **Funding 38%（19/50）** 是**机器层标题匹配**口径，
> 实际包含「正文提到资助、但没有独立 Funding 标题」的论文。人工层合并 8 个分片后，
> **有独立 Funding 标题的只有 1/10（10.0%）**。读这行时请按「正文提到资助」理解。详见 §9.9。

→ 🔴 **化石类 AI 论文的声明块显著强于纯 AI 论文**：Data availability 54% vs 28%，
  Code availability 24% vs 5%（**4.5 倍**）。
  → 原因可推断但**不写死**：地质学刊普遍要求标本可溯源 + 数据可复现（**推断，无直接原句**）。
→ 🔴 **AI 使用声明几乎不存在**（225 篇中仅 2 篇命中）——
  这批论文（2024–2026 为主）**尚未普遍声明 AI 使用情况**。

### 3.2 Data availability 的五种实际写法（逐字原文）

**① 公共仓库 + DOI（本领域主流）**

> “Data are available online at: osf.io/j3q67/” —— Foxon 2021, `PCI Paleo`

> “The raw data associated with this work are available online through the SEANOE repository
> https://doi.org/10.17882/108821 (Hayat et al., 2025a). The full CNN training-image dataset is
> deposited on Zenodo at https://doi.org/10.5281/zenodo.17965134 (Hayat et al., 2025b).”
> —— Hayat et al. 2026, `J. Micropalaeontology`

> “Data available from the Dryad and Zenodo digital repositories: https://doi.org/10.5061/
> dryad.51c59zwb0, https://doi.org/10.5281/zenodo.6333970.” —— Liu et al. 2023, Fossil Image Dataset

**② 标本存藏 + 数据集 DOI（微体古生物的特有写法：两件都要交代）**

> “Microscopic slides are prepared and stored at UMR 8198 – Evo-Eco-Paleo of the University of Lille,
> France. The datasets (https://doi.org/10.57745/8KBOFP, Pinto et al. 2023) have been archived in the
> repository of the University of Lille at Recherche Data Gouv.” —— Carlsson 2023, 放射虫博士论文

> “All analyzed slides are stored at the Institute of Geological Sciences, National Academy of
> Sciences of Armenia (Yerevan), and the remaining shale samples are curated by the paleontology
> team at the University of Lille (France).” —— Lokteva et al. 2026, 泥盆纪孢子

→ 🔴 **这一条是本领域与纯 AI 论文最大的差别**：微体古生物论文必须交代
  **实物标本（玻片/岩石）在哪里**，光给数据 DOI 不够。

**③ 机构库（非 Zenodo）**

> “The Airyscan images used in this study were submitted to the Illinois Databank
> (https://doi.org/10.13012/B2IDB-8817604˙V1).” —— Adaime et al. 2024, PNAS Nexus

> “…are available in Harvard’s Dataverse public repository at
> https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi%3A10.7910%2FDVN%2FYHKWMR.”
> —— Cifuentes-Alcobendas & Domínguez-Rodrigo 2019, Scientific Reports

> “The datasets presented in this study can be found in online repositories. The names of the
> repository/repositories and accession number(s) can be found below: https://www.scidb.cn/s/RbeqIj.”
> —— Duan 2023, Frontiers in Earth Science

**④ 补充材料内含数据/代码**

> “The radiolarian dataset “SO32” used in this study is available in supplementary material 2.
> The program codes are available on GitHub (https://github.com/masora1030/CVPR2022-Pretrained-ViT-Pytorch).”
> —— Mimura et al. 2025

> “The code to collect the data used in figures is distributed as part of the Supplementary Material.”
> —— Hou et al. 2023, Ecological Informatics

**⑤ 「录用后可提供」（最弱的一档，但在化石类中确实存在）**

> “The data can be supplied by authors after acceptance of the article.” —— Gorur et al. 2023

> “Code Availability The source codes can be supplied by authors after acceptance of the article.”
> —— Gorur et al. 2023

→ ⚠️ **「录用后提供」在审稿时是可接受的最低限度**，但与 ①②③ 差一个量级。

### 3.3 Code availability 的实际写法

> “The test dataset is publicly available at the KAUST Research Repository [12]. The full training
> and validation datasets, code, and trained models are available at
> https://github.com/A-Halimi/3D_Fossil_Project.” —— Halimi & Osman 2025, ForamDeepSlice

> “The dataset and code are available at Zenodo: https://doi.org/10.5281/zenodo.17608881”
> —— Plavetić et al. 2025, J. Micropalaeontology

> “The code is available at Zenodo: https://doi.org/10.5281/zenodo.18032045 (Lokteva et al., 2025b).”
> —— Lokteva et al. 2026

> “The ParticleTrieur software program, which was used to manually label the training set and
> automatically classify foraminifera images, is available … with tutorials from
> http://particle-classification.readthedocs.io … The latest version of the Python scripts
> (https://doi.org/10.5281/zenodo.3996358, Marchant, 2020b) to train the CNNs in this paper are
> available from http://www.github.com/microfossil/particle-classification”
> —— Marchant et al. 2020, J. Micropalaeontology

> “The ML code and related files are archived at https://github.com/brberis/djtensor”
> —— MacFadden et al. 2026

> “The codes are available at https://archive.softwareheritage.org/browse/directory/…”
> —— Carlsson 2023（法国 HAL + Software Heritage 双归档，**已发表论文中最彻底的一例**）

→ 🔴 **代码发布的三个层次**（本批实证）：① 只给 GitHub 链接；
  ② GitHub + Zenodo DOI（带版本）；③ Zenodo + Software Heritage 永久归档（可引用、可复现）。
  → 化石类论文里 **② 已成主流**，③ 仅见 1 例（Carlsson）。

## 四、数据集、模型与评估：方法类论文的实际写法

> 本节逐字原文来自 A/B 组 77 篇的精读笔记；每条结论标注样本量。

### 4.1 数据集怎么交代（必备六件）

在本批 A 组中，数据集交代**几乎总是**包含以下六项，缺一项就会在审稿时被追问：

| 项 | 本批实际写法（逐字原文） | 出处 |
|---|---|---|
| **来源与检索式** | 检索式写明分类群名 + 下载日期：“taxon/taxa name ‘Ammonoidea’”，下载日期 “10 November, 2020” | Foxon 2021 |
| **初样本 → 清洗规则 → 终样本** | 明确写两步剔除：“Outlying cases or samples that contain very few coccoliths … have been removed from the analyses.”；菊石类写“缺 dm1/ww1/wh1/uw 的剔除；该种标本数 < 50 的剔除”，最终 11 个种、N = 781 | Boeckel & Baumann 2004；Foxon 2021 |
| **每类样本量** | 进表逐类列出（Table 1），并给占比列 | Duan 2023；Marchant 2020 |
| **标注方式** | “manually cropped and labeled by an expert diatomist” | Bueno et al. 2017 |
| **划分方式与比例** | “a 10-fold cross-validation has been applied” / “~85% / ~15%” / “80% / 10% / 10%” | Bueno 2017；Duan 2023；Kahanamoku 2024 |
| **不平衡的显式承认 + 补偿手段** | “The conodont dataset collected in this study has two problems: the dataset is small and imbalanced.”，并用加权损失 “Weighti = 1 − ni/N” 补偿 | Duan 2023 |

→ 🔴 **数据量小是本领域的常态，不是缺陷** —— A 组普遍是几百到几万张图。
  本批实测：牙形刺 613 张 / 9 种；菊石 781 标本 / 11 种；硅藻 24,000 张 / 80 类；
  浮游有孔虫 34,640 张 / 35 种。**写方法时必须交代这个量级，否则显得不可信。**

### 4.2 模型怎么写：五种交代粒度（实测）

| 粒度 | 做法 | 代表 |
|---|---|---|
| **① 架构点名 + 图** | “Figure 4. Overview of the convolutional neural network used and its procedures in the experiment.” | Duan 2023 |
| **② 架构点名 + 超参表** | 超参表同时承担「模型对比表」职责：K1–K10 十折准确率 + lr + epo + lw + aver | Duan 2023 |
| **③ 网格全列** | “每个分类器的超参搜索网格完整列于 Table 3”，且写明验证设计为 **5×5 嵌套交叉验证**（内层 grid search 选参，外层估无偏泛化性能） | Foxon 2021 |
| **④ 环境版本全写** | “All models were trained using an NVIDIA GeForce RTX 2070 graphics card, and the operating system version was Windows 10 Professional. Python version 3.7.0 was used, along with PyTorch version 1.10.0 and CUDA version 10.2.” | Duan 2023 |
| **⑤ 消融式对照** | 冻结策略逐条列：c1 从零训练 / c2 冻结全部卷积 / c3、c4 只冻前 7 层或前 26 层 / c5–c9 冻卷积只训全连接 | Duan 2023 |

→ 🔴 **④（环境版本）是化石类论文里最少被写、但审稿人最常要的一项** ——
  本批只有个别论文写全 Python/PyTorch/CUDA/GPU 四件套。
→ 🔴 **超参写在正文散文里是常见做法**，不是都要进表
  （如 “a bagging tree with 200 learners and 30 splits provided the best results”）。

> ⚠️ **v2.16.1 口径更正（原文保留）**：上条方向正确，但**漏了第三种主流**——
> 只列架构 / 分类层 / 输入尺寸而不列学习率（110 的 Table 3 属于这一类，不能算超参表），
> 以及**直接声明沿用默认配置**（220）。合并 8 个分片 21 篇口径，
> **有独立超参表的只有 2 篇（9.5%）**，只有 Foxon 2021（Table 3 网格）与 Duan 2023（Table 2）。
> 详见 §9.1 / §9.2。

### 4.3 评估怎么写：指标清单实测

本批 A 组出现的指标（按出现篇数排序，机器统计口径见 §5）：

- **accuracy**（几乎必报）
- **precision / recall / F1-score**（逐类给）
- **AUC / ROC**（类别不平衡时的主指标）
- **macro-average**（“The macroaverage AUC value for the classiﬁer on the test dataset was 0.90.”）
- **Caliński-Harabasz / Variance Ratio Criterion / NMI / Fowlkes-Mallows**（聚类类指标）

🔴 **类别不平衡时必须说明为何不用 accuracy** —— Duan 2023 在 3.4 节先讲指标定义，
指出不平衡下 accuracy 会失效，再把 AUC 定为主指标。这是本批唯一明确写出这一点的论文。

### 4.4 基线对比：三种强度（实测）

| 强度 | 做法 | 逐字原文 |
|---|---|---|
| **弱：无基线** | 只报自己的结果 | — |
| **中：内部对照** | 用自己的变体互比（从零训练 vs 迁移学习、ResNet18 vs ResNet50、CBAM vs SE 注意力模块） | Duan 2023 |
| **强：显式朴素基线 + 外部横向比较** | “the simplest baselines … are given by using transfer learning via ImageNet-initialised off-the-shelf CNN architectures”；菊石类直接写出多数类基线 **148/781 ≈ 0.190** | Karaderi 2022；Foxon 2021 |

→ 🔴 **写出朴素基线（多数类、随机）是一种强信号**：审稿人立刻能看出提升幅度。
  本批仅 Foxon 2021 一例写到数字。

### 4.5 局限性怎么写：三段式与专节制（实测）

**专节制（本批最规范的一例）**：Duan 2023 设 “5.2 Threats to validity and areas for future work”，
用编号 1) 2) 3) 列三条自陈局限：

> “In general, the intelligent recognition of conodont species had several challenges: 1) the dataset was small and
> unbalanced; 2) some conodonts were incomplete, and this natural defect was not found in common datasets; and
> 3) the original textures of some conodont were damaged during the experimental process, leading them to be
> missing some key features.”

**逐条嵌入讨论（最常见）**：Foxon 2021 设独立 **Strengths** 与 **Limitations** 两段，全文以 Limitations 收尾；
Bueno 2017 把局限写在各实验节末尾，分四类：

> “Precise segmentation is a critical point for the whole classification process. This is a limitation for
> handcrafted feature approaches.”

> “Automation methods may be a tool to help both the expert and the non-expert, but in difficult cases, it should
> always be the expert who makes the final decision.”

→ 🔴 **本批的局限写法有一个共同点：局限一律指向「数据/对象本身」而非「模型不够强」** ——
  标本残缺、纹理破坏、类别不平衡、寿命期形态差异、视角差异。
  → 这是描述类论文没有的维度（描述类论文的局限是「材料暴露不全」这类地层学局限）。

## 五、图件与表格：方法类论文画什么（实测）

### 5.1 独有图件类型（描述类论文里不存在的）

| 图件类型 | 本批实测出现情况 | 代表 |
|---|---|---|
| **混淆矩阵（热图）** | 本批方法类论文的**标配**；图注句式高度固定：“行=真值、列=预测、单元格为百分比、对角线=100 %” | Duan 2023；Kahanamoku 2024；Mimura 2022 |
| **ROC 曲线** | 与 AUC 配套出现 | Duan 2023 |
| **t-SNE / UMAP 特征可视化** | 展示网络最后一层特征（“visualize the last layer of features after training on the original data”）；本批仅 1 篇用 t-SNE | Duan 2023 |
| **网络架构示意图** | “Overview of the convolutional neural network used and its procedures in the experiment.” | Duan 2023 |
| **类别样本网格** | “Examples of the 80 diatom taxa classiﬁed in this study.” / “Example illustrations of each species of the conodont genus Hindeodus in the dataset.” | Bueno 2017；Duan 2023 |
| **分割掩膜对照** | “Segmented diatoms and their binary mask” | Bueno 2017 |
| **训练/数据流程示意** | “Schematic diagram of Stratiﬁed K-fold cross validation.” | Duan 2023 |
| **误差案例图** | “Some incomplete fossil samples [(A), the part enclosed by the white oval dotted line] and samples with surfaces attached to colloids (B).” | Duan 2023 |

> ⚠️ **v2.16.1 口径更正（原文保留）**：上表「混淆矩阵（热图）= 方法类论文的**标配**」**不成立**。
> 合并 8 个分片 24 篇口径，**有混淆矩阵的只有 11 篇（45.8%）**，严格只算主文图是 10/24（41.7%）；
> **近一半的方法类论文用逐类 F1 / Precision / Recall 表替代**（如 Foxon 2021 Table 6），
> 分片 05 的 4 篇一篇都没画。详见 §9.1 / §9.2。

→ 🔴 **与描述类论文的差别**：描述类论文的图几乎全是
  「标本照片 / 图版 / 地层柱状图 / 分布图」；方法类论文的图是
  「混淆矩阵 / ROC / 特征空间 / 架构图 / 误差案例」。**两类不能混用。**

### 5.2 人工 vs 自动的双数据源叠绘（一个高频做法）

本批方法类论文在结果图上普遍采用**同一测量的两种来源叠绘**，并在图注里用文字点明颜色含义：

> 地质结果图一律双数据源叠绘（人工 vs 自动），颜色用文字点明。

→ 这与 skill 现有的语义色字典（人工=红 #D30203 / AI=紫 #75489A）**正好吻合**，
  说明「颜色语义要写进正文，不能只写在图注里」这条规则在方法类论文里同样成立。

### 5.3 表注与表的两种职责

| 职责 | 本批实际做法 | 代表 |
|---|---|---|
| **数据集统计表** | 逐类样本量 + 训练/测试划分 + 占比列 | Duan 2023 Table 1；Marchant 2020 |
| **超参表兼模型对比表** | 一表同时给 K1–K10 十折准确率 + lr + epo + lw + aver | Duan 2023 Table 2 |
| **超参搜索网格表** | 每个分类器的网格取值范围逐行列出 | Foxon 2021 Table 3 |
| **逐类指标表** | 逐种 F1 / Precision / Recall（代替混淆矩阵的表格替代方案） | Foxon 2021 Table 6 |

🔴 **表注一律含「最佳值加粗」声明 + 脚注式脚标**（a/b 说明输入尺寸等）；
   且本批多篇把「训练时间/推理时间」与精度指标**并列为列** ——
   即**把算力开销当作与精度同等的报告维度**。

### 5.4 数据/代码可用性区块的固定位置

本批实测的声明块顺序（各刊不同，但同一刊内一致）：

```text
… 正文 / Conclusion
→ Data availability（+ Code availability / Data Records）
→ CRediT author contributions
→ Declaration of competing interest
→ Acknowledgments
→ References
```

→ 另一常见变体（Elsevier 系）：Author contributions → Funding → Acknowledgements →
  Declaration of competing interest → Data availability。
→ 🔴 **顺序因刊而异**，但**同一刊内必须一致**；投稿前应查目标刊最近 3 篇的实际顺序。

## 六、引言 / 讨论 / 结论：方法类论文的写法

> 本节对照 `fulltext-reading-evidence.md` §八（描述类论文的实测写法），
> 只写**方法类论文实测做了什么**，不写应当如何。

### 6.1 引言：起手与缺口

**方法类引言的固定四步**（本批实测）：

1. **对象的地学意义**（不是「本文做了什么」）—— 与描述类引言**同**，
   如牙形刺：“牙形刺在地质研究中的作用”；硅藻：“Diatoms are a major group of algae…”
2. **传统方法的痛点（量化）** —— 描述类论文没有这一步。
   Bueno 2017 直接引法规给出工作量基线：
   “in order to compute an index score, the identification of a minimum of 400 valves per sample is required”
3. **既有技术进展的缺口** —— 不是「没人研究过 X」，而是「已有方法在 Y 维度不够」。
   如 Duan 2023 的缺口是**粒度**：此前数据多跨属/科，本文做**属内细粒度**。
4. **本文做法 + 用途声明**

**贡献声明的四种形态**（本批实测）：

| 形态 | 原文 | 出处 |
|---|---|---|
| **编号 (a)(b)** | “The main contributions of this work are: (a) big database collection… and (b) the study of the main handcrafted features…” | Bueno 2017 |
| **编号问句式** | 引言末尾用编号问句列研究问题 | 与描述类同（见 `fulltext-reading-evidence.md` §八） |
| **一句话带过** | “In this study, we use…” | Duan 2023 |
| **专设小节** | 引言内设 **“Paper Contributions.”** 加粗小节 | Karaderi 2022 |

🔴 **章节导航句是方法类论文的常见件**，描述类论文较少见：

> “In order to extract the main diatom features, we propose in Section 3 a segmentation…
> In Section 4, a complete list of descriptors is provided… Sections 5 and 6 describe classification
> strategies and some classifiers. Experimental results are presented in Section 7 where an overall
> accuracy of 98.11% is presented… Finally, Section 8 concludes the paper addressing unresolved
> challenging problems.” —— Bueno et al. 2017

→ **这段话把「结构」「每节做什么」「核心数字」「收尾」四件事一次说完**，
  是本批最完整的引言收尾写法之一。

### 6.2 讨论：三种形态

| 形态 | 做法 | 代表 |
|---|---|---|
| **① 独立 Discussion + 专节「威胁效度」** | “5.2 Threats to validity and areas for future work”，编号列局限 | Duan 2023 |
| **② 独立 Strengths + Limitations 收尾** | 无独立 Discussion 标题，全文以 Strengths 一段 + Limitations 长段结束 | Foxon 2021 |
| **③ 讨论嵌入结果节末尾** | 每节按「实验 → 解释 → 与文献比较 → 对本领域意义」四步走 | Bueno 2017 |

**讨论里的一类特殊动作：把失败案例归因到对象本身**

> “Segmentation faults, including omissions, misidentifications and incomplete segmentations, were rarely
> seen and mostly occurred in poor-preserved fossils.” —— Huang et al. 2024（纺锤虫数据集）

→ 🔴 **这是化石类 AI 论文与纯 AI 论文的最大区别**：
  误差归因必须落到**化石保存状态/形态变异**上，而不是「模型能力不足」。

### 6.3 结论：三种形态

| 形态 | 做法 | 代表 |
|---|---|---|
| **段落式（回扣引言）** | 3 段：①回扣引言主张 ②回扣方法与核心数字并解释为何可接受 ③给可迁移性判断 | Duan 2023 |
| **贡献前置式** | 首句即 “(a)… (b)…” 的贡献总述，再接精度目标回扣，再接未解问题 | Bueno 2017 |
| **编号清单式** | 与描述类同（见 `fulltext-reading-evidence.md` §5.2） | — |

**方法类结论的一个高频句式：给「在什么条件下这个方法才成立」**

> “The optimal classiﬁer, c6, obtained an AUC value of 0.9 on the test set. This was a good result for the
> classiﬁcation of a conodont species, especially considering that the model was trained in the low data
> regime, and some conodont images have natural defects (e.g., some parts of the fossil were missing and
> the surface of the fossil was covered by colloid).” —— Duan 2023

> “Machine learning models and outputs should be used with caution in studies where quantification of the
> abundance of rare species is a central goal, as the models we show…” —— Kahanamoku et al. 2024

→ 🔴 **结论里必须写「适用边界」** —— 这在描述类论文里不存在
  （描述类论文的结论是「发现了什么」，方法类论文的结论还要说「什么时候不能用」。
  **「不是所有任务都适合用 AI」这句话在本批论文里反复出现，是领域共识。**）

## 七、与描述类论文的对照速查表（写稿时按体裁判）

**先判定体裁，再选骨架。这两张表不能混用。**

| 骨架件 | 描述类（新种/修订） | **方法类（AI/数据）** |
|---|---|---|
| Geological setting | **几乎必选，且在 Methods 之前** | 0/50（**没有**） |
| Repository（标本存藏） | **必备**，单列一节或写在系统描述段第一句 | 0/50（无此段，但内容并入 Data availability） |
| Systematic（类群块） | **核心**，逐类群并列 | 0/50（**没有**） |
| Results | 通常**无独立段** | **46% 有独立 Results 段** |
| Methods | 三档详略（完整式/一句式/写进摘要式） | **62% 有独立 Methods 段**，且必含数据集交代 |
| Discussion | 65% 无独立段（讨论在 Remarks 里） | **48% 有独立 Discussion 段** |
| Conclusion | 两种形态（连续散文 / 编号清单） | **52% 有独立 Conclusion 段**，多为段落式 |
| Data availability | 描述类语料中未单列 | **54% 有**（A 组 27/50） |
| Code availability | 无 | **24% 有**（A 组 12/50） |
| Author contributions | 无 | **46% 有** |
| Competing interest | 无 | **52% 有** |
| 图件主类 | 标本照片 / 图版 / 柱状图 / 分布图 | **混淆矩阵 / ROC / 特征空间 / 架构图 / 误差案例** |
| 局限的类型 | 材料暴露不全、地层对比不确定 | **数据量与不平衡、标本残缺、纹理破坏、形态变异** |
| 结论的落点 | 「发现了什么」 | 「发现了什么」+ **「什么时候不能用」** |

### 7.1 写「微体古生物 + AI」论文的检查表

按本批 50 篇 A 组论文的实测共性，**以下各项在 A 组中出现的篇数见括号**：

1. **先说清楚数据从哪来、怎么清洗、剩多少**（数据集交代六件：来源检索式 / 初样本→清洗规则→终样本 / 每类样本量 / 标注方式 / 划分比例 / 不平衡如何处理）
2. **说清楚运行环境**（Python / PyTorch / CUDA / GPU 型号 —— 本批仅个别论文写全）
3. **给朴素基线**（多数类基线或随机基线 —— 本批仅 1 例写明数字）
4. **交代分类不平衡，并说明为何不以 accuracy 为主指标**（本批仅 1 例明确写）
5. **误差归因落到化石保存状态与形态变异**，而不是模型能力
6. **Data availability 交代两件事：实物标本在哪 + 数据集 DOI**（这是本领域与纯 AI 论文的差别）
7. **Code availability 给到 GitHub + Zenodo DOI**（能到 Software Heritage 永久归档更好）
8. **结论里写适用边界**（什么情况下不该用 AI 分类）
9. **混淆矩阵用固定句式**：行=真值、列=预测、单元格=百分比、对角线=100 %
10. **表注写「最佳值加粗」**，并把训练/推理时间与精度并列为列

> ⚠️ 以上 10 条是**本批 A 组 50 篇的共性清单**，不是规范。
  括号内篇数见 §8；**任何一条都要按目标刊的最近 3 篇实际做法再核对**。

## 八、本文件的局限（必须如实说明）

1. **语料非随机**：225 篇是「AI × 分类学」专题的人选文献，**不能**用于估计任何比例。
2. **全英文**：本文件**不能**直接套到中文刊（中文刊骨架见 `fulltext-reading-evidence.md` §8.11）。
3. **文件名不可信**：已发现文件名与正文不符实例（`Beaufort_2004_coccolith_neural_net.pdf` 实为
   Boeckel & Baumann 2004 的多元统计论文，无神经网络）→ **所有结论以正文为准**。
   （**v2.16.1 补**：完整清单见 **§9.8** —— 实际 **9 例完全不符**，9/225 = 4.0%，另有 1 例取了编辑姓名。）
4. **A 组只有 50 篇**：按 `fulltext-reading-evidence.md` §12 的分级，本文件多数结论属
   **B 级（10–29 篇）**，涉及单一刊或单一作者群的具体写法属 **C 级**。
5. **章节链统计有抽取缺陷**：PDF 一级标题行常在抽取中丢失，
   「有无独立 Discussion 段」等判断**部分依赖子 Agent 从上下文补出的标题**，
   已在各篇 ⚠️ 中逐条标注；引用具体篇数前应回查该篇 ⚠️。
6. **声明块百分比是机器标题匹配**：
   标题行锚定 + 行内标题两种模式并取，**可能漏掉没有标准标题的散文式声明**；
   逐字原文以 A/B 组精读笔记为准。
7. **图件类型统计来自图注文本，未开图**：本批未渲染 PNG 实际看图
   （与 `figure-conventions-evidence.md` 的 449 张实看不同）——
   **本文件关于图的结论只到「图注写了什么」，不到「图画成什么样」**。
8. **引文回源**：本批笔记中的引文已用**词袋覆盖判据**回源核对（692 条中 0 条真实缺失，
   全部可验证）；但**词袋判据不能证明词序**，
   因此「逐字」指的是词完整而非字符级一致（双栏 PDF 抽取本身会打断行序）。

> 📌 **增量追加说明（v2.16.1）**：按本 skill 自 v2.15.0 起的惯例，新内容一律**追加**在既有章节之后，
> **不改动原句**。下面新增的 **§九** 是「8 个分片 31 篇」的横向观察二次汇总，
> 其中对 **§4.2 / §5.1 / §3.1 / §8 第 3 条** 四处表述给出了口径更正（汇总见 **§9.2**）。
> 引用本文件时请一并读 §九；四处原句旁已各自加了「v2.16.1 口径更正」的限定注。


## 九、横向观察二次汇总：8 个分片 31 篇的交叉统计（含对前文的口径更正）

> **本节按增量追加原则新增**（v2.16.1），§一–§八任何原句**未改动**，更正一律以「加限定注 + 本节说明」的方式给出。
>
> 数据来自 25 个分片中**写出了显式「本分片横向观察/小结」的 8 个分片**
> （shard_ai_04 / 05 / 06 / 07 / 16 / 17 / 24 / 25），分母 = 各分片自己声明的篇数之和 = **31 篇**。
> 复现脚本：`ai_verify_sec9.py`（合并计数）、`ai_kappa_probe.py`（kappa 回源）、`ai_title_probe.py`（文件名回源）。
>
> 🔴 **读下面的数字前必须先接受三条口径**：
> 1. **这 31 篇不是随机样本**，是「子 Agent 恰好写了横向观察」的分片，占 77 篇逐字精读的约 40%。
> 2. **分母 31 篇 ≠ §3.1 的 225 篇**，两者**不可直接相减**。
> 3. **分片的分母含非方法类论文**：shard_06 自己写明「5 个文件里只有 4 篇是地学/方法类」，
>    shard_17 写明「5 篇里只有 2 篇真做机器学习建模」。
>    → 凡是本节给的比例，都是**「该分片全部篇数」口径**，天然被综述、观点、数据论文、
>    非地学论文稀释；读者若只要纯方法类，需按分片说明自行扣除。

### 9.1 四条硬数字：混淆矩阵不是「标配」，超参表是例外

| 现象 | 合并口径 | 占比 | 分片分解（分片号 = 该分片计数 / 该分片篇数） |
|---|---|---|---|
| **混淆矩阵** | 11 / 24 | **45.8%** | 04 3/4 · 05 0/4 · 06 2/4 · 07 3/3 · 16 2/5 · 24 1/4 |
| 混淆矩阵（严格口径：只算主文图） | 10 / 24 | 41.7% | 07 由 3/3 降为 2/3（123 的错分只在 Supplementary Table S2） |
| **独立超参表** | 2 / 21 | **9.5%** | 04 2/4 · 05 0/4 · 06 0/4 · 16 0/5 · 24 0/4 |
| **统计检验** | 5 / 30 | **16.7%** | 04 1/4 · 05 0/4 · 06 2/4 · 07 1/3 · 16 1/5 · 17 0/5 · 24 0/4 · 25 0/1 |
| **训练 / loss 曲线图** | 3 / 22 | **13.6%** | 05 2/4 · 06 1/4 · 16 0/5 · 17 0/5 · 24 0/4 |

→ 🔴 **混淆矩阵不是「标配」**（45.8%，严格口径 41.7%）。**近一半的方法类论文用
  「逐类 F1 / Precision / Recall 表」替代混淆矩阵**（Foxon 2021 的 Table 6 就是逐种 F1/Precision/Recall）。
  分片 05 的 4 篇**一篇都没画**混淆矩阵。
→ 🔴 **独立超参表是例外而非常态**（9.5%）。只有两篇真给了独立超参表：
  Foxon 2021（Table 3 完整搜索网格）与 Duan 2023（Table 2 兼模型对比表）。
  其余 19 篇的写法是**三种**（不是两种）：① 写在正文散文；
  ② **只列架构 / 分类层 / 输入尺寸而不列学习率**（110 的 Table 3 属于这一类，不能算超参表）；
  ③ **直接声明沿用默认配置**（220：“沿用默认配置”）。
→ 🔴 **统计检验是少数派**（16.7%）。出现时用的是 Shapiro–Wilk / Wilcoxon signed-rank /
  Kruskal–Wallis / Welch t / paired t / ANOVA / McNemar / Bland–Altman。
  多数论文改用「**10 次重复运行的 mean ± SD**」代替显著性检验。
→ 🔴 **训练曲线罕见**（13.6%），而且**常被推入补充材料**：
  “The training and validation iterations are given in Supplements 4.2 figure S1, which confirms
  that the data is neither overfit, nor underfit.”

### 9.2 对前文四处表述的口径更正（原文保留，此处说明）

| 前文位置 | 原表述 | 更正 |
|---|---|---|
| §5.1 首行 | 混淆矩阵是方法类论文的「**标配**」 | **不成立**。45.8%（严格 41.7%），近一半用逐类指标表替代。见 §9.1 |
| §4.2 末条 | 「超参写在正文散文里是**常见做法**，不是都要进表」 | 方向正确但**漏了第三种主流**（只列架构 / 直接声明默认配置），且独立超参表实际只有 9.5%。见 §9.1 |
| §3.1 Funding | Funding **38%（19/50）** | 口径不同：这是「**正文提到资助**」，不是「有独立 Funding 标题」。人工层实测独立 Funding 标题只有 **1/10 = 10.0%**。见 §9.9 |
| §8 第 3 条 | 「已发现文件名与正文不符实例」 | 实例不止 1 例，实际 **9 例完全不符**（9/225 = 4.0%）。见 §9.8 |

### 9.3 Cohen’s kappa 的实际情况：一处「词频会骗人」的实证

上一轮草稿里写的是「**Cohen’s kappa 本批从未出现**」。**这句话是错的**，本节给出更正与回源证据：

- **77 篇逐字精读语料中**：kappa 的 **28 处提及全部是否定式**
  （“不报 kappa” / “无 F1/kappa” / “**0 个**使用 Cohen’s kappa”）
  → 精读范围内，kappa **从未作为被报告的指标出现**。
- **225 篇全量正文中**：kappa 字面命中 **4 篇**，逐篇回源后 ——

| 文件 | 实际情况 | 是否真报告 |
|---|---|---|
| `187__Suvorov_2022_LaMa_inpainting.txt` | 损失函数权重系数 `L_final = κ·L_Adv + α·L_HRFPL + β·L_DiscPL + …` | ❌ **假阳性**，与 Cohen’s kappa 无关 |
| `057__Elith_2006_Nordic_society_oikos_Ecography_29_2.txt` | “Kappa (Cohen 1960), which is a chance-corrected measure of agreement”；报 “maximum kappa (KAPPA)” | ✅ 真报告（物种分布模型，presence-absence 预测） |
| `058__Elith_2009_Species_distribution_models.txt` | 综述性提及：“summaries of performance are based on … including kappa, area under the receiver operating characteristic curve (AUC) and correlation coefficients” | ✅ 真提及 |
| `170__Salifu_2022_fruit_fly_morphometrics.txt` | 逐模型报 “Kappa statistic of 0.54 / 0.648 / 0.784 / 0.810 / 0.811 / 0.833”，与 AUC + NIR 并列 | ✅ **真分类论文真报告** |

→ 🔴 **准确表述**：不是「本批从未出现 kappa」，而是
  「**在 77 篇逐字精读的地学 AI 分类语料中未出现；在 225 篇全量中，于 3 篇非精读论文
  （2 篇生态物种分布模型 + 1 篇果蝇形态分类）出现**」。
→ 📌 **本条同时是一条方法论警告**：若只用「grep 全文有没有 kappa」来下结论，
  会同时**误报**（LaMa 的 κ 是权重系数）和**漏报**（Salifu 2022 真报了 kappa）。
  **词的命中不能代替逐篇判读** —— 这与本文档 §8 第 8 条的引文回源口径是同一条纪律。

### 9.4 数据集交代的四种实做（标注方式 / 划分比例 / 不平衡处理）

**① 标注方式实测四种**（不是一种）：

| 标注方式 | 原文 / 出处 |
|---|---|
| 网络爬虫 + 人工复核 | 论文自述经网络爬取后人工复核（shard_07 的 123） |
| 人工标注 + 在线平台画框 | 126 用 RoboFlow 平台画框（shard_07） |
| 专家人工鉴定 + 馆藏号 | 130 的标本逐件由专家鉴定并附馆藏号（shard_07） |
| 多人标注 + 资深专家裁决 gold standard | 103 至少 2 人标注 + 第一作者裁决；110 由 BIIGLE 多人标注 + 资深专家定 gold standard（shard_06） |

→ 另有一条**资历声明**值得抄：
  “categorized into 32 classes … by one of the authors (TI), who has studied radiolarians for more than 30 years”（shard_09）。

**② 划分比例实测十二种写法**（同一批论文内部极不一致）：

| 写法 | 原文 / 出处 |
|---|---|
| ~85% / ~15% | “The images were then split into training (~ 85%) and testing (~ 15%) datasets.”（shard_09；Duan 2023 同） |
| 80 / 10 / 10 | shard_06 的 103 |
| 72 / 18 / 10 + 4-fold + out-of-set 80/20 | shard_06 的 110 |
| 80 / 15 / 5 | shard_07 的 123 |
| 70 / 20 / 10 与 70 / 15 / 15 | shard_07 的 126 |
| 80 / 20 + 固定外部测试集 | shard_07 的 130 |
| 6 : 2 : 2（概率式表述） | “We randomly assigned the multimodal data to the training set, validation set, and test set with a probability of 6:2:2”（shard_15 的 219） |
| 2.47 : 1 → 74 / 30 图 | shard_05 的 Johansen |
| **复用他人已发布的 withheld test set** + 27,731 训练 + 另有 5-fold | shard_06 的 105 |
| **只写集合构成、不写比例** | 162：训练集 = 外部集 + 本集（本文集占比 < 3%）、验证集 = 仅本集图像（shard_24） |
| **只有 K 折、没有比例** | 107：“Ten-fold cross-validation”（shard_06） |
| **根本没有划分概念** | Strydom（shard_05）；Apostol 的测试集来自训练集内部交叉验证（shard_17） |

→ 🔴 **给目标刊投稿前，不要照抄任何一篇的比例** —— 本批十二种写法互不相同，
  且唯一带「复用他人 withheld test set」的做法会引入**跨文献数据异质性**（shard_06 的 105）。

**③ 类别不平衡的五种处理**（实测）：

| 处理 | 原文 / 出处 |
|---|---|
| 加权损失补偿 | “Weight_i = 1 − n_i/N”（Duan 2023）；“损失函数按类样本量倒数加权”（shard_09） |
| 下采样并写出下采样后的数字 | “Objects representing the diatom Fragilariopsis kerguelensis, which in the raw data accounted for nearly 40% of all specimens, were randomly subsampled to 660 specimens to reduce imbalance.”（shard_06 的 110） |
| 重采样 | “we applied a resampling technique to process the dataset to alleviate imbalanced sample distribution across different categories in the training set”（shard_15 的 219） |
| 剔除样本数过少的类 | 该种标本数 < 50 的整种剔除（shard_06）；移除只有 1、2 个样本的类（shard_15） |
| **不处理，但把不平衡归一化为行业常态** | “individual classes were covered by ca. 40–400 specimens each. This represents an amount of imbalance that is not uncommon in taxonomic classification.”（shard_06 的 105） |

→ 🔴 第五种写法值得注意：**主动承认不平衡、同时声明它是本领域的常态**，
  是比「不提」更稳的写法（审稿人一定会问），但**不能替代**给出具体数字。

### 9.5 可解释性图件：三条路线并存

| 路线 | 实测写法 | 代表 |
|---|---|---|
| **① Grad-CAM / CAM** | “the weighted activation heatmap (Grad-CAM) (Servaraju et al., 2017) generated from the runs with the 3-class dataset showed that the analytical focus of the network was centered around the thoracic and abdominal walls of the specimens”（shard_02 的 CH3，**放在补充材料 Fig 3.S2**） | shard_07 的 123（Fig.7–9 三联图）；shard_10 的 graptolite 注意力图；shard_13 的 206（Fig. 11）；shard_17 的 [5]；shard_18 的 Fig.3 / Fig.4 |
| **② saliency map** | 单独设二级标题 “Saliency Maps”，工具写明 tf-keras-vis v0.87 + Sobel 滤波增强边缘 | shard_07 的 130（单例图解 + 5 个误识别标本的「照片 + saliency map」对照） |
| **③ 完全不用** | 4 篇地学方法类全无（shard_06）；3 篇全无（shard_20）；3 篇全无（shard_19）；126 完全没有可解释性图 | 多篇 |

→ 🔴 **可解释性图件不是必需项**：三条路线并存，「完全不用」的论文数量并不少。
  若要用，**Grad-CAM 是主流写法**；它与混淆矩阵是**两回事**，不要指望用混淆矩阵替代可解释性论证。
→ 📌 一条易被忽视的操作细节：**正文放补充材料**是常见做法
  （shard_02 的 CH3 / CH4-1：“训练曲线与 Grad-CAM 都被推入补充材料”）。

### 9.6 局限自陈的七种句式（实测，可直接套用）

| # | 句式类型 | 逐字原文 | 出处 |
|---|---|---|---|
| 1 | “It is worth noting that…” | “It is worth noting that…” | shard_02 的 CH2；shard_06 的 103（指向死亡群集 ≠ 活体群集） |
| 2 | 单句点名 | “The limitation of the proposed method is the lack of…” | shard_06 的 107 |
| 3 | **警示句式** | “Machine learning models and outputs should be used with caution in studies where…” | shard_06 的 103 |
| 4 | 条件句式 | “If the initial metaweb is too narrow…” | shard_05 的 Strydom |
| 5 | 先扬后抑 + 专设编号小节 | `4.1 Future Research` | shard_05 的 Johansen |
| 6 | **「因为做不到 X 所以不采用 Y」** | 散落在数据处理小节 | shard_05 的 Huang |
| 7 | **方法论权衡句式**（每小节先优势后局限） | “the major advantage…” → “the major limitation…” | shard_24 |

→ 另有两种**归因句式**，因写得太好而单独列出：

> **域偏移的并列归因**（把两种可能并列，不下断言）：
> “The still remaining small shift might represent either a slight residual methodological drift,
> or genuine biological signal…” —— shard_06 的 110

> **承认域外后把责任归给训练数据**：
> “As the CNN training… and accuracy are independent from the camera itself” —— shard_24 的 192

→ 🔴 与 §4.5 一致：**七种句式指向的仍然是数据 / 对象本身**，
  只有第 3 种（警示句式）与第 7 种（权衡句式）会顺带说到「何时不该依赖本方法」。

### 9.7 章节链小标题的三套体系，以及「无 Discussion 标题」≠「无讨论内容」

| 体系 | 实测写法 | 出处 |
|---|---|---|
| **① 层级编号** | 一级 + 二级编号到 2.1 / 2.2 / 3.1 / 3.2 / 4.1 / 4.2 | shard_07 的 126 |
| **② 行内粗体小标题**（Cambridge 体例） | “Data.—” / “Training.—” / “Performance Analysis.—” 等 **11 个**，全文不用层级编号 | shard_07 的 123 |
| **③ 三级混排** | 一级标题 + 二级标题 + 行内小标题（11 个二级 + 4 个行内） | shard_07 的 130 |
| ④ 栏目眉 + run-in 小标题（PNAS 体例） | 全文 0 个独立标题（0 Discussion / 0 Conclusion / 0 Results / 0 Abstract） | shard_25 |

→ 📌 **引言贡献点的写法实测为零**：shard_07 的 3 篇中 **0 篇**用「贡献点编号列表」写引言贡献；
  shard_06 的 5 篇中「贡献声明用编号列表」也是 **0/5**（均为散文式）。

→ 🔴 **「没有 Discussion 标题」不等于「没有讨论内容」** —— 这是本批最容易被统计口径误导的一点：

| 论文 | 实际形态 |
|---|---|
| 105 | 讨论用自定义标题 “6 Taxonomic Reflection.” |
| 110 | 讨论由**无标题段**承载 |
| 103 | 讨论由 “Usage Notes” 承载 |
| 192 | Results 与 Discussion **合并成 §3**，再用 §3.4 / §3.5 分节 |
| Strydom | 讨论分布在 §2 / §3 / §5 与 Box 1 / Box 2 |
| 220 / 221 / 001 | 一级标题在 PDF 抽取中**整体丢失**（属抽取缺陷，非论文写法） |

→ 📌 **操作要求**：凡引用「有无独立 Discussion 段 / Conclusion 段」的篇数，
  **必须逐篇回查该篇 ⚠️ 标注**（§8 第 5 条已声明此缺陷，此处给出具体错例）。

### 9.8 文件名误标全量清单：9 例完全不符（9/225 = 4.0%）

以下全部**已从磁盘正文首行回源核对**（`ai_title_probe.py`），非转述：

| # | 文件名指向 | 正文实际（首行原句） | 性质 |
|---|---|---|---|
| 1 | `011__Beaufort_2004_coccolith_neural_net` | “Distribution of coccoliths in surface sediments of the south-eastern South Atlantic Ocean: ecology, preservation and carbonate contribution”（Boeckel & Baumann, *Marine Micropaleontology* 51:301–320） | 同门类但**方法不是神经网络**（多元统计 / 排序） |
| 2 | `051__Dionisio_2020_radiolarian_CNN` | “Habitability of the early Earth: Liquid water under a faint young Sun facilitated by strong tidal heating due to a closer Moon”（Heller et al., arXiv:2007.03423v3） | **完全不符**，且非古生物语境 |
| 3 | `088__Hou_2023_fossil_image_ensemble` | “Graph embedding and transfer learning can help predict potential species interaction networks despite data limitations”（Strydom et al., *PERSPECTIVE*） | **完全不符**，无化石 |
| 4 | `113__Kong_2016_dictionary_pollen` | “Crystal Structure Prediction of Molecular Crystals from First Principles: Are we there yet?”（Pham et al., arXiv:1605.00733v1） | **完全不符**，凝聚态物理 |
| 5 | `139__Mitra_2019_planktic_foraminifera_CNN` | “The genetic diversity, morphology, biogeography, and taxonomic designations of Ammonia (Foraminifera) in the Northeast Atlantic”（Bird et al., *Marine Micropaleontology*） | 同门类但**无 CNN** |
| 6 | `156__Polo_2025_ammonites_Colombia` | “Investigating the application of LLMs to invertebrate palaeontology through the development of automated taxonomy assistants for brachiopod identification” | **完全不符**，是腕足类不是菊石 |
| 7 | `182__Stephenson_2026_LLM_taxonomy_palynology` | **与第 6 例是同一篇论文** | **完全不符**，是腕足类不是孢粉 |
| 8 | `191__Tetard_2020_automated_radiolarian_workflow` | “Million-year-scale alternation of warm–humid and semi-arid periods as a mid-latitude climate mode in the Early Jurassic (late Sinemurian, Laurasian Seaway)”（Munier et al.） | **完全不符**，古气候无 AI |
| 9 | `223__Zhong_2017_foraminifera_classification_comparison` | “Letter Position Encoding in a Neural Framework”（Stokes & Hickok, IEEE 2017） | **完全不符**，认知科学 |

> **9 个文件 = 8 篇不同论文**（第 6、7 例是同一篇被放了两次）→ **9/225 = 4.0%**。
> 另有一例是**取名取了编辑姓名**（论文本身正确）：
> `048__DeBaets_2021_ammonoid_ML` 的正文是 Foxon F 2021，
> 源 PDF 首页写 “Cite as: Foxon F (2021) … / Recommender: Kenneth De Baets”（De Baets 是 PCI Paleo 的推荐人）。
> 合计命名缺陷 **10/225 = 4.4%**。

→ 🔴 **这份清单是 §8 第 3 条的完整版**：此前只写了 Beaufort 一例，实际是 **9 例完全不符**。
  **所有结论以正文实际作者 / 期刊为准，不以文件名为准** —— 这条原则在本批已被 10 次实证。

### 9.9 声明块：机器层与人工层的口径差（Funding 最典型）

| 声明块 | 机器层（§3.1，225 篇，A 组 n=50） | 人工层（8 分片 31 篇，只认**独立段落**） |
|---|---|---|
| **Data availability** | 54%（27/50） | **12/31 = 38.7%** |
| **Code availability** | 24%（12/50） | **4/31 = 12.9%** |
| **Funding** | 38%（19/50） | **1/10 = 10.0%**（仅 shards 06 / 24 / 25 有明确计数） |

→ 📌 **两个口径的分母不同，不能直接相减**（31 篇含综述 / 观点 / 数据论文 / 非地学论文，
  这些天然不写 Data availability）。差异至少有两个来源：
  ① **分母构成不同**；② **机器层把正文中的行内 “Data availability” 字样也计入，人工层只认独立段落**。

→ 🔴 **Funding 的差距最大（38% vs 10%），因为「有资助」和「有独立 Funding 标题」是两件事**：
  shard_24 的 4 篇**没有一篇**有独立 Funding 标题 —— 资助放在致谢首句、
  放在 Acknowledgements 内、或混写在 Authors’ contributions 段内；
  shard_06 的 5 篇中只有 1 篇有独立 “Funding” 标题。
  → **§3.1 的 Funding 38%（19/50）应读作「正文提到资助」，不是「有独立 Funding 标题」。**

→ 📌 **投稿实操建议**：目标刊若要求独立声明段，照 §5.4 的顺序表排版；
  若目标刊只要求「致谢中写明资助」，照本节实测的**散写**写法即可，不必硬造一个 Funding 段。
  但 **Data availability / Code availability 在化石类论文里属于「要写」项**（§3.2 / §3.3 的逐字原文可抄）。
