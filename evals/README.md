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

M01 摘要 · M02 引言 · M03 文献综述 · M04 方法 · M05 结果 ·
M06 讨论 · M07 结论 · M08 去 AI 化 · M09 期刊投稿 · M10 审稿回复
