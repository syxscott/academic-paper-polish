# 评测集（evals）

用于量化本 skill 的触发准确率与输出质量，便于迭代时对比前后效果。

## 文件

| 文件 | 说明 |
|---|---|
| `evals.json` | 用例定义：模块、触发句、期望加载的文件、必须出现的要点、禁止行为 |

## 评分标准

| 等级 | 判定 |
|---|---|
| **pass** | 正确加载对应模块；输出含该模块全部硬规则与关键数字；无编造 |
| **partial** | 加载了模块，但遗漏关键硬规则或数字 |
| **fail** | 未触发 / 触发错误模块 / 编造数字或文献 |

## 用例结构

```json
{
  "id": "M01-abstract",
  "module": "prompts/01-abstract.md",
  "prompt": "帮我压缩一下摘要，投 Earth-Science Reviews",
  "expect": {
    "load": "prompts/01-abstract.md",
    "must_mention": ["300 词", "Highlights", "避免缩写"],
    "must_not": ["编造期刊影响因子"]
  }
}
```

## 运行方式

评测依赖模型执行，本仓库只提供用例与基线定义：

1. 逐条把 `prompt` 喂给加载了本 skill 的 agent
2. 检查它是否读取了 `expect.load` 指定的文件
3. 检查输出是否覆盖 `must_mention`，且未触犯 `must_not`
4. 按规定等级打分，汇总通过率

## 覆盖模块

| 前缀 | 覆盖范围 |
|---|---|
| **M01–M10** | 摘要 · 引言 · 文献综述 · 方法 · 结果 · 讨论 · 结论 · 去 AI 化 · 期刊投稿 · 审稿回复 |
| **R01–R03** | references 层：**配色系统**（R01 通用决策 / R02 热图色阶）· **图件硬参数** |

> `R` 前缀表示评测**按需加载的深度参考**（`skills/academic-paper-polish/references/`），而非固定模块。
> 触发句刻意写成「读者会怎么说」，用于检验渐进披露是否生效 ——
> 即：用户问配色时，应加载 `skills/academic-paper-polish/references/color-system.md`，
> 而不是误加载某个 prompt 模块或直接凭通用知识回答。

### R01 的关键反向断言

R01 的 `must_not` 明确禁止「把『对照冷色/处理暖色』说成铁律」——
该表述在 v2.4.0 曾被误写为铁律，v2.4.1 已降级为「目标期刊惯例」。
此类**曾经犯过的过度概括**都应写成 `must_not` 防回归。
