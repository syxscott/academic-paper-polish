# 图件设计体系（Figure Design System）

> **本文件解决什么问题**：
> `figure-specs.md` 给的是**硬参数**（dpi / 尺寸 / 字号下限）；
> `color-system.md` 给的是**配色决策逻辑**（颜色怎么组织成语义）。
> 本文件给的是**第三层、也是最常被跳过的一层**：**一张新图该长成什么样**、
> **一篇论文的图该按什么顺序串起来**、**每种图必须包含哪些元素**。
>
> **蓝本**：Hayat et al. 2026, *J. Micropalaeontology* **45**: 95–116,
> DOI [10.5194/jm-45-95-2026](https://doi.org/10.5194/jm-45-95-2026)。
> 一篇微体古生物 + 机器学习论文，14 张图覆盖「方法 → 模型 → 验证 → 生态 → 成本」全链路。
> 本文件的每个色号、每条版式规则都**逐像素实测自该文**，不是经验值。
> **🔴 引用规范**：本文件每条规则都锚在**论文原句**上（见下节「蓝本原文锚点」）；**要引用就引原句**，中文转述不算数。

---

## 零、为什么以这篇为蓝本

| 维度 | 实测值 |
|---|---|
| 图数 | **14**（Fig 1–14），分布于正文 15 页 |
| 排版 | Copernicus `copernicus.cls`，**单栏**，版心宽 **177.0 mm**（A4 595.3×785.2 pt） |
| 最大图宽 | 175.0 mm（Fig 4 通栏，几乎占满版心） |
| 图件格式 | 位图 PNG / JPEG，**单图最大 5.07 兆像素**（Fig 10） |
| 图内字体 | 无衬线（matplotlib 默认族），正文层为 LaTeX 衬线 |
| 色系 | **1 组双语义色（红=人工 / 紫=AI）+ 3 个功能色 + 1 套单色阶** |
| 关键优势 | **颜色语义在正文里被明文写出**（"manual (red) versus automated (purple)"），读者零解码成本 |

🔴 **判据**：这篇论文的图**不需要看图注就能读懂颜色** —— 因为同一篇里
"红=人工、紫=AI" 从 Fig 6 一直守到 Fig 12。**这才是「配色成功」的验收标准。**

---

## 🔖 蓝本原文锚点（verbatim，逐句引用）

> 本文件的每条规则都锚在**论文自己的措辞**上。中文只作定位标注；**要引用就引原句**。
> 出处：*J. Micropalaeontology* **45**: 95–116, DOI 10.5194/jm-45-95-2026
> （PDF 图注与正文逐字转录，保留原刊 "colour" / "grey" 等英式拼写）。

| 图 | 原文（verbatim） | 由此得到的规则 |
|---|---|---|
| Fig 1 | "Flowchart depicting the classification and automation workflow of foraminifera. **Blue arrows represent training, and black arrows represent model application.**" | 箭头颜色 = 语义，且**必须写进图注** |
| Fig 3 | "The five classes, including benthic foraminifera, debris, cut, fragment, and planktonic foraminifera, are **bounded by rectangles of different colours**." | 框色 ↔ 类别一一绑定 |
| Fig 4 | "Each cell indicates the percentage of images from the true class (rows) that were predicted as the corresponding class (columns). Perfect classification is indicated by 100 % values along the diagonal, while off-diagonal values reflect misclassifications, indicating inter-class confusion." | 行 = 真值、列 = 预测；对角线 = 100 % |
| Fig 6 | "The numbers on the pie charts show the **number of specimens** of each species." ・ "**Diamonds indicate means.**" ・ "Grey points represent individual samples, while **black points indicate mean differences**." | 环形图写绝对数；均值 = 菱形；均值差 = 黑点 |
| Fig 7 | "Each plot shows samples as **orange dots**, a regression line (black) with the corresponding R2 value, and a **dashed perfect-agreement line**." | 散点单色橙、回归黑实线、1:1 灰虚线 |
| Fig 8 | "Each plot shows samples as orange dots, a regression line (solid black), a dashed perfect-agreement line (black), and the corresponding R2 value." | 同上（Fig 8 把 1:1 虚线写成 black） |
| Fig 9 | "The background of the samples is indicated as **orange (black plate) and grey (Plummer cell) stripes**." | 背景语义带 = 实验底色 |
| Fig 10 | "(a) Box-and-jitter plots for 31 samples showing the distribution of three indices (Evenness index and Shannon (H) and Simpson (1-D) diversity indices) measured using **automated (purple) and manual (red)** methods." ・ "(b) Bland–Altman regression: ... **The dashed line marks zero difference, and the blue line is ordinary least-squares (OLS) fit** of the difference of the mean with the **95 % confidence interval (grey)**. Slopes are small and non-significant, indicating no proportional bias. However, the vertical offset shows systematic differences." | 语义色 + OLS / 零线 / CI 三线制 |
| Fig 12 | "(a) Bray–Curtis dissimilarity-based non-metric multidimensional scaling (nMDS) of foraminiferal assemblages counted **manually (red) and by CNN (purple)**. **Convex hulls represent the spatial distribution of each group in ordination space.** Different symbols indicate different samples." | 色相 = 组别，形状 = 样品，凸包 = 组分布 |
| Fig 13 | "**Green circles are individual samples, the solid green line is the regression line**, and the dashed line shows the **1 : 1 agreement**." | 环境量 = 绿色系；空心圆 = 单样本 |
| Fig 14 | "The time requirement of different steps in the automated identification workflow." | 流程成本单独成图 |

**正文原句 —— 颜色语义被作者写进正文，不只在图注**

> "Figure 10a compares manual (red) versus automated (purple) counting based on three key indices, namely Evenness (Pielou, 1966), Shannon diversity (H) (Shannon, 1948), and Simpson diversity (1-D) (Simpson, 1949), of the same samples."

> "Figure 12a presents a Bray–Curtis-dissimilarity-based nMDS ordination comparing foraminiferal assemblages derived from manual counts (red symbols) versus automated counts (purple symbols)."

🔴 **这一条最关键**：颜色语义写进了**正文**，读者不翻图注也能解码。
凡是要画「方法 A vs 方法 B」的图，**在正文里就用文字把颜色对应关系写一遍**。

**图注的诚实性写法（原文）**

> "Each pair represents one class for the CNN models. **The images in each pair are not of the same foraminifera specimen.**"（Fig 2）

> "**The image in the top-left corner (purple border)** of each composite image is mislabelled according to the model, and it suggests a different name (in purple) based on the surrounding training images."（Fig 5）

---

## 一、🔴 铁律：图序即论证顺序

**图的排列顺序不是编号习惯，是审稿人读你论文的路径。**
把「方法图」排在「结果图」后面，等于让审稿人先看到结论再找依据 —— 顺序错，直接掉分。

### 14 张图的骨架（可复用到任何一篇论文）

| 阶段 | 图 | 原型 | 回答的问题 |
|---|---|---|---|
| **① 方法** | Fig 1 | A 流程图 | 样本从哪来、怎么走到 AI |
| | Fig 2 | B 图像对照版 | 模型到底在学什么长什么样 |
| | Fig 3 | B 图像对照版 | 人工标注分了哪几类 |
| **② 模型** | Fig 4 | C 性能矩阵 | 模型准不准、错在哪对 |
| | Fig 5 | B 图像对照版 | 具体错在哪些样本上 |
| **③ 一致性** | Fig 6 | D 成对比较 | AI 和人工的**量级**一致吗 |
| | Fig 7 | E 回归网格 | AI 和人工的**逐种**一致吗 |
| | Fig 8 | E 回归网格 | 换成相对丰度还一致吗 |
| | Fig 9 | D 成对比较 | **时间序列上**的丰度曲线一致吗 |
| **④ 生态** | Fig 10 | D + E 混合 | 单一指数的分布与系统偏差 |
| | Fig 11 | D 成对比较 | 指数跨样品的走势一致吗 |
| | Fig 12 | E 排序图 | **整个群落**的组成一致吗 |
| | Fig 13 | E 回归网格 | 用 AI 数据算出的**环境指标**还成立吗 |
| **⑤ 成本** | Fig 14 | A 流程图 | 这套系统**省了多少人力** |

🔴 **一条通用公式**（任何学科通用）：

```
方法图 → 数据/对象图 → 模型性能图 → 误差案例图
→ 方法 vs 基准的一致性图（换 3 种量纲各来一次）
→ 生态/业务意义图 → 成本/效率图
```

**「一致性」为什么要三个量纲**：绝对计数（Fig 7）→ 相对丰度（Fig 8）→ 群落结构（Fig 12）。
只放一个，审稿人一定会问「那换成相对比例呢」。**先问自己审稿人会问什么，再决定要画几张图。**

---

## 二、五种图件原型（archetype）

### A. 流程图（Fig 1、Fig 14）

**结构**：上排实物/地图照片链 → 下排算法流程框图。
**两种分工**：
- Fig 1 = **系统全景**（样本来源 → 图像采集 → 模型训练 → 模型应用 → 结果对比）
- Fig 14 = **成本分解**（同一条流水线，标出每步耗时）

🔴 **流程图的三条硬规则**：
1. **箭头颜色必须有语义且写进图注** —— 本文用**蓝箭头=训练路径，黑箭头=模型应用路径**
2. **框体文字用「动词+对象」**，不写名词堆砌（"CVAT training for segmentation"，不是 "CVAT"）
3. **红字标注 = 人的动作**（"Duplicates removal"、"Model application"），
   因为「AI 流程里人还在哪」是审稿人最关心的问题之一

**Fig 14 的 chevron 变体**：流程步骤多、且要给每步配时间/成本时用雪佛龙箭头。
🔴 **每个 chevron 用一个色，但文字与耗时数字用该 chevron 的同色**，
上下交错排布避免文字互相压。

### B. 图像对照版（Fig 2、Fig 3、Fig 5）

**结构**：黑底（或纯色底）上排布图像格 + 每格下方的物种名 + 编号。
**本文的三种用法**：
- **Fig 2**：光学照片（a）与 SEM 照片（b）**成对**，每对 = 一个类别。
  🔴 关键诚实声明：**"The images in each pair are not of the same foraminifera specimen"**
  —— 不声明会被认为是误导。
- **Fig 3**：标注界面截图，**5 个类别用 5 种矩形框色**（绿=有孔虫、白=碎屑、蓝=切割、
  红=碎片、黄=浮游）。框色与类别一一绑定，且**每个框旁直接写类别名**（不靠图例）。
- **Fig 5**：误差案例 —— 左上角那张用**洋红色边框**标出（=模型判错的那张），
  下方给出模型的替代判读（洋红文字）。

🔴 **图像版的铁律**：
- 底色用**纯黑或纯白**，不用浅灰（标本本身颜色即数据）
- **必须有比例尺**，不能用放大倍数代替（Fig 2 用 200 µm 横条）
- **物种名用斜体**，编号用阿拉伯数字并与图注一一对应
- **每个面板字母用粗体大写**（(a) (b) (c)），置于面板左上

### C. 性能矩阵（Fig 4）

**结构**：4 个混淆矩阵 2×2 排布，每个矩阵 = 主热图 + 顶部边际条 + 右侧边际条。

🔴 **本文的关键设计（可整套照抄）**：
- **单色阶（蓝色系）**，不用彩虹色阶 —— 主图、顶部条、右侧条**共用同一蓝色系**
- 深色格内**白字**，浅色格内**黑字**（阈值自动切换）—— 数字必须始终可读
- 每个矩阵**上方写 Overall accuracy + Precision**，各一行
- 行列标签用**斜体物种名**，旋转 90° 排布避免拥挤
- 面板标题（M-1…）用**大号粗体无衬线**，放在面板左上角

### D. 成对比较面板（Fig 6、Fig 9、Fig 10a、Fig 11）

**结构**：同一个「人工 vs AI」对比在多种图元上重复出现，换量纲换视角。

| 组件 | 图元 | 作用 |
|---|---|---|
| 组成比例 | 双**环形图**（donut） | 总量结构是否一致 |
| 分布 | 箱线 + 均值菱形 | 中位数/四分位是否一致 |
| 配对差 | 散点 + 零线 + 均值点 | 差值是否有系统性偏移 |
| 时间序列 | 双折线 + 背景色带 | 逐样品的走势是否一致 |
| 指数跨样品 | 分栏折线 | 指数在每个样品上的走势 |

🔴 **本文的三个细节值得抄**：
1. **环形图把总数直接写在扇区上**（不用百分比），读者一眼看到量级差异
2. **箱线图用空心白底 + 彩色描边**，均值用菱形 —— 空心=中位数区、实心点=均值，双重标记
3. **背景语义色带**（Fig 9）：样品按实验底色（黑板 / Plummer 皿）交替染色，
   🔴 色带**只表类别、不参与数值编码**，且**图例必须单列一块解释**两种底色

### E. 回归与排序图（Fig 7、Fig 8、Fig 10b、Fig 12、Fig 13）

**回归网格（Fig 7 / Fig 8）**：
- **3×3 小倍数阵列**，每个格子一个物种
- 面板标题 = **物种名（粗体斜体）**
- 数据点 = **单一橙色**
- 回归线 = **黑色实线**
- 1:1 完全一致线 = **灰色虚线**
- **R² 写在左上角**，大号字体，不带边框

**Bland–Altman（Fig 10b）**：
- 差值 vs 均值散点，**黑色点**
- **OLS 拟合线用蓝色**，**95% 置信带用灰色**
- 零差异 = **黑色虚线**
- 左下角写 Slope 与 p 值、R²，🔴 **点估计 + p 值必须同时给**

**排序图（Fig 12）**：
- nMDS 散点用**多形状**（圆/方/三角/菱形/叉/加号）区分样品 —— 🔴 **形状承担类别，色相承担组别**
- 两组的**凸包用极浅填充**（粉 `#F2D5D6` / 淡紫 `#ECE8F5`）
- Stress 值用斜体写在右上角

**单变量验证（Fig 13）**：
- **空心圆**（绿色描边）= 单个样品
- 回归线用同色实线，1:1 线用黑色虚线
- 左上角三行大字号：Slope / Intercept / R²

---

## 三、🔴 语义色字典（逐像素实测）

> 下表 HEX **由原图像素统计得出**（取饱和像素的众数），不是目测近似。
> 用法：先按**角色**选角色色，再查表取 HEX。

### 3.1 双语义主色（本文最关键的一对）

| 角色 | 实测 HEX | 色相/饱和 | 在哪些图出现 |
|---|---|---|---|
| 🔴 **人工 / 基准 / Manual** | `#D30203`（群峰）/ `#CD0000` | 0° / 0.99 | Fig 6b、Fig 9、Fig 10a、Fig 11、Fig 12a |
| 🟣 **AI / 自动 / Automated** | `#75489A` | 273° / 0.53 | 同上（与红一一配对） |

🔴 **铁律：双组对比图，全篇只用这一对颜色。**
Fig 6 → Fig 12 跨越 6 张图、5 种图元（箱线、折线、散点、菱形、凸包），
红色永远是人工、紫色永远是 AI，**一次都没有例外**。

⚠️ **别用「红=坏 / 绿=好」的直觉**：本文红=人工（通常视为 ground truth），
所以红绝不能同时承担「错误」含义 —— Fig 5 标「模型判错的那张」用的是**洋红框**，
与 AI 主色紫同族但不同明度，正是为了不与「人工=红」冲突。

### 3.2 功能色（每色一个职责，全篇不越界）

| 职责 | HEX | 出处 |
|---|---|---|
| 单一系列散点 | `#F6A100` | Fig 7、Fig 8 |
| 环境/物理量验证 | `#308E2C` | Fig 13 |
| 拟合线 / 连续色阶 | `#093576` → `#00509D` | Fig 4、Fig 10b |
| 背景语义带（类别一） | `#FEE7CD`（浅橙） | Fig 9 黑板底 |
| 背景语义带（类别二） | `#F3F3F4`（浅灰） | Fig 9 Plummer 皿底 |
| 凸包填充（组一/组二） | `#F2D5D6` / `#ECE8F5` | Fig 12a |
| 差值正/负区域底 | 浅蓝 / 浅粉 | Fig 6c |

### 3.3 地图专用（Fig 1a）

| 要素 | HEX |
|---|---|
| 海洋 | `#67C4D4` |
| 陆地 | `#CD9826` |
| 取样点 | 🔴 **红色五角星**（唯一的高饱和红，与「人工=红」不冲突，因不在数据图内） |

### 3.4 🔴 配色的三条验收

1. **同一色相全篇只承载一个含义** —— 本文中「紫」只可能是 AI
2. **主色对在灰度下仍可区分** —— 红与紫明度接近，
   所以本文**同时用线型/形状/填充**做第二重线索（箱线：红框 + 紫框；
   排序图：多形状 + 凸包）
3. **连续量用单色阶，不用彩虹** —— Fig 4 全蓝单色阶（深蓝=高正确率）

---

## 四、版式与排版规范

| 项 | 规范 |
|---|---|
| 面板字母 | **粗体大写 (a) (b) (c)**，置于每面板左上角，全图一致 |
| 物种名 | **斜体**（属名种名都斜体），面板标题里用**粗体斜体** |
| 坐标轴标题 | 无衬线正体，不加粗 |
| 轴标签单位 | 写在轴标题里（例：Relative abundance (%)），不写进图注 |
| 网格线 | **全部删除**（Fig 7/8/13 无网格，靠 1:1 虚线定位） |
| 图例位置 | 多面板图放**图底居中**（Fig 6、Fig 9、Fig 11），一次讲完，不重复 |
| 边框 | 折线图可加**全框**（Fig 11、Fig 10），散点网格图不加（Fig 7、Fig 8） |
| 字号层级 | 面板字母 > 面板标题 > 统计标注（R²/Slope） > 轴标签 > 刻度 |
| 背景 | 白底；照片类面板用纯黑/纯白底 |

---

## 五、🔴 一图一结论

**每张图只能回答一个问题。** 判据（本文逐图自检）：

| 图 | 一句话结论 |
|---|---|
| Fig 6 | 两种计数在**量级与中位数**上一致 |
| Fig 7 | 逐种绝对计数**高度一致**（R² 多数 > 0.75） |
| Fig 8 | 相对丰度一致但**弱于**绝对计数（R² 最低 0.546） |
| Fig 12 | 群落结构在排序空间**不可区分** |
| Fig 13 | AI 反演的环境量与人工**几乎重合**（R²=0.992） |

⚠️ **Fig 8 的 R² 明显低于 Fig 7，是真实发现不是缺陷** ——
相对丰度把分母也换掉了，误差会放大。**图件要敢展示「没有那么好」的那一面**，
否则审稿人自己算出来，你的可信度就崩了。

---

## 六、图注模板（Copernicus / JM 口径）

Copernicus 官方要求：**图例必须在图内**，图注不重复图内已有信息。
本文的图注统一结构：

```
Figure N. <一句描述性标题>。
(a) <面板 a 做什么>。(b) <面板 b 做什么>。
<必要的统计口径：数据集大小、划分比例、单位、误差棒含义>
<缩写全拼：ResNet50 是什么；CVAT 是什么>
```

🔴 **本文图注里三个值得抄的做法**：
1. **写出样本量与划分比例**："1690 images for M-1 ... with 80 % used for training and 20 % for validation"
2. **诚实声明图的局限**："The images in each pair are not of the same foraminifera specimen"
3. **解释非常规记号**："Diamonds indicate means"、Stress 值、"Slopes are small and non-significant"

---

## 七、交稿前自查（本文逐条过）

- [ ] 图件是否覆盖「方法 → 性能 → 一致性 → 意义 → 成本」全链？
- [ ] 同一语义色在**每张图**里是否都是同一个含义？
- [ ] 双组对比是否**全篇只用一对颜色**？
- [ ] 连续量是否用**单色阶**（且深浅格内文字自动反色）？
- [ ] 每张回归图是否都有 **1:1 参考线** + **R²**？
- [ ] 1:1 线是否**用虚线**（与拟合实线区分）？
- [ ] 统计标注是否给了 **点估计 + p 值**（不只是 R²）？
- [ ] 面板字母是否**全图一致**、粗体、置于左上？
- [ ] 物种名是否**斜体**？
- [ ] 物种照片是否带**比例尺**（不是放大倍数）？
- [ ] 图例是否**在图内**且只用一次？
- [ ] 背景色带是否**只表类别**、且图例单独解释？
- [ ] 图注是否写出**样本量、划分比例、单位**？
- [ ] 图注是否解释了所有非常规记号（菱形、凸包、Stress）？
- [ ] 图内字体是否已换成目标期刊要求的 **Arial / Helvetica**？
- [ ] 全部转**灰度**后，两组是否仍可区分？
- [ ] 用 **Coblis（色觉障碍模拟器）** 过一遍（Copernicus 明确要求）？

---

## 八、来源

| 来源 | 提供什么 |
|---|---|
| **Hayat et al. 2026, *J. Micropalaeontology* 45: 95–116**<br>DOI 10.5194/jm-45-95-2026 | 14 张图的原型库、语义色字典（逐像素实测）、版式规范、图注模板 |
| **Copernicus Publications 投稿说明**（同平台，JM 同用 `copernicus.cls`） | 图例必须入图、Coblis 色觉检查、复合图合并成单文件、300 dpi、矢量优先与字体嵌入 |

⚠️ **口径说明**：Copernicus 图件条款来自同平台期刊官方投稿说明页
（JM 使用同一套 `copernicus.cls` 与同一份图件条款）；
**期刊专属项（字数、篇幅、摘要长度）以 JM 官网 Author guidelines 为准**，
本文件不复述，避免张冠李戴。
