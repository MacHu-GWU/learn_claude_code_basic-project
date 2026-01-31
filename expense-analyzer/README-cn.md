# Expense Analyzer：练习 AI 辅助开发

> 学习如何与 AI 协作，完成一个使用 Python 和 SQL 的数据分析项目。

## 概述

这是一个动手练习，旨在练习 **AI 辅助开发技能**。你将构建一个小型消费分析器，从交易数据集中找出每个类别中最高的消费。

这里用到的技术（Python、Polars、SQL）对大多数学习者来说可能不太熟悉。**这是故意的。** 目标不是掌握这些工具——而是练习一种可以应用于*任何*陌生技术的方法。

**完全不理解是正常的。** 重点是体验与 AI 的交互式学习——通过对话和迭代，从"我不懂"走向"我理解了"。

## 学习目标

在实际的软件开发中，你会不断遇到陌生的技术、库和代码库。快速理解和使用新工具的能力——通常借助 AI 辅助——正变得越来越重要。

这个练习正好把你放在那个场景中：面对一个陌生的技术栈（Python + SQL），学习如何有效地与 AI 协作来应对它。

完成这个练习后，你将：

1. **练习向 AI 清晰描述任务** — 包括输入格式、约束条件和预期输出
2. **学会向 AI 请求解释** — 不只是拿到代码，还要理解它
3. **体验测试驱动的迭代** — 用失败的测试来指导你的实现
4. **应用分而治之的思想** — 把复杂问题拆分成可管理的步骤

## 前置要求

- 基本的命令行操作能力（运行命令）
- 一个 AI 助手（Claude Code、Cursor 等）
- 愿意尝试和提问的心态

**不需要 Python 或 SQL 经验。** 这正是本练习的意义所在。

## 你将构建什么

一个 Python 函数，它会：
1. 从 TSV 文件读取消费数据
2. 筛选 2025 年第三季度（7-9 月）的数据
3. 找出每个类别中金额最大的消费
4. 返回一个字典，映射类别到 transaction ID

---

## 核心概念

在开始写代码之前，让我们先理解项目结构和工具。如果有些内容感觉陌生也不用担心——随时问你的 AI 助手来解释。

### Python 项目结构

当你查看这个项目时，你会看到一些可能看起来很神秘的文件夹和文件：

- **`expense_analyzer/`** — 这个文件夹包含你的实现代码。在 Python 中，我们把代码组织成 "packages"（包含代码的文件夹）。今天你很幸运——只有一个文件。在更大的项目中，里面可能有很多模块。

- **`tests/`** — 包含用于验证你的代码是否正确工作的测试文件。

- **`pyproject.toml`** — 项目的"配方卡"。它定义了：
  - 项目名称和版本
  - 所需的 Python 版本（3.12+）
  - 依赖项（你的项目需要的外部库）

- **`.venv/`** — 一个"虚拟环境"，它将这个项目的依赖项与你机器上其他 Python 项目隔离开来。

### 使用 uv 进行包管理

Python 项目需要外部库（比如 Polars）。我们使用 **uv** 来管理这些——它快速又现代。关键命令是：

- `mise run venv-create` — 创建虚拟环境（底层运行 `uv venv`）
- `mise run inst` — 安装所有依赖（底层运行 `uv sync --all-extras`）

### Polars：现代数据分析

**Polars** 是本地数据分析最强大的两个库之一（另一个是 DuckDB）。我们使用 Polars 是因为：
- 它非常快（用 Rust 编写）
- 它有干净的 SQL 接口
- 使用体验比其他替代品好得多

了解更多，请查看官方文档：https://docs.pola.rs/

### Polars SQL 接口

Polars 允许你使用熟悉的 SQL 语法通过 `pl.sql()` 查询 DataFrame。这对于了解 SQL 或想学习 SQL 的学习者来说非常完美：

```python
result = pl.sql("""
    SELECT category, amount
    FROM df
    WHERE amount > 100
""").collect()
```

文档：https://docs.pola.rs/user-guide/sql/intro/

### 使用 pytest 进行测试

我们不用写 print 语句然后用眼睛检查输出，而是使用 **pytest**——Python 的标准测试框架。命令是：

```bash
mise run test        # 运行: .venv/bin/pytest tests
```

测试的美妙之处：**如果测试通过，你的代码（大概率）是正确的。** 这让你有信心快速迭代。

### 分而治之：拆解问题

这是本练习的关键洞察。在写任何代码之前，先思考如何把这个问题拆分成步骤：

**任务：** 找出 2025 年第三季度每个类别的最大消费。

**你会怎么拆解？** 在继续阅读之前先想想。

自然的分解是：

1. **加载数据** — 将 TSV 文件读入内存
2. **预览数据** — 了解我们在处理什么
3. **筛选数据** — 只保留 2025 年第三季度的记录
4. **聚合并找最大值** — 按类别分组，找出最高金额

这就是**分而治之**——一种基本的问题解决方法。每一步都很小且可测试。`main()` 函数将所有四个步骤整合在一起。

---

## 练习

### 练习 1：设置你的环境

**目标：** 让项目运行起来，准备好开发。

**要做的事：**

1. 创建虚拟环境：
   ```bash
   mise run venv-create
   ```
   （这会运行 `uv venv` 来创建一个隔离的 Python 环境）

2. 打开 `pyproject.toml`，查看 dependencies 部分。你会看到 `polars` 列在那里。

3. 安装依赖：
   ```bash
   mise run inst
   ```
   （这会运行 `uv sync --all-extras` 来安装所有包）

4. 运行测试，看看哪些失败了：
   ```bash
   mise run test
   ```

**你会注意到：**

测试会失败，因为 `impl.py` 里有返回 `None` 的占位函数。这是预期的——你接下来会实现它们。

> **关键洞察：** 先运行测试可以清楚地看到需要做什么。失败的测试就是你的路线图。

---

### 练习 2：实现 `load_expense_data()`

**目标：** 将 TSV 文件读取到 Polars DataFrame 中。

**要做的事：**

1. 打开 `expense_analyzer/impl.py`，找到 `load_expense_data()` 函数

2. 阅读 TODO 注释和 docstring 来理解需要做什么

3. 问你的 AI 助手：
   > "/teach-code 我需要用 Polars 读取一个 TSV 文件。文件使用 tab 作为分隔符。怎么做？"

4. 实现这个函数。**自己敲代码——不要复制粘贴。**

5. 运行测试：`mise run test`

**提示：** 如果卡住了，可以参考 `impl_example.py` 里的参考实现，但先尝试自己搞定。

> **关键洞察：** 使用 `separator="\t"` 的 `pl.read_csv()` 就是你需要的全部。简单吧？

---

### 练习 3：实现 `preview_first_rows()`

**目标：** 使用 SQL 从 DataFrame 中选择前 N 行。

**要做的事：**

1. 在 `impl.py` 中找到 `preview_first_rows()` 函数

2. 问你的 AI：
   > "/teach-explain 在 Polars 中如何使用 pl.sql() 选择 DataFrame 的前 5 行？"

3. 实现这个函数。记住：**自己写。**

4. 运行 `mise run test` 检查进度

**你会注意到：**

如果你懂 SQL，SQL 语法会很熟悉：`SELECT * FROM df LIMIT 5`。Polars 允许你在 SQL 中直接引用 DataFrame 变量名。

> **关键洞察：** `pl.sql()` 返回一个 LazyFrame——你需要 `.collect()` 来执行查询并获得 DataFrame。

---

### 练习 4：实现 `filter_q3_data()`

**目标：** 将数据筛选为仅包含 2025 年第三季度（7 月 1 日 - 9 月 30 日）。

**要做的事：**

1. 找到 `filter_q3_data()` 函数

2. 问你的 AI：
   > "/teach-explain 如何使用 SQL 筛选 Polars DataFrame，只包含 '2025-07-01' 和 '2025-09-30' 之间的日期？"

3. 实现这个函数

4. 运行 `mise run test`

**提示：** 查看函数参数——开始和结束日期已经提供了。

> **关键洞察：** 当日期是 ISO 格式（YYYY-MM-DD）时，SQL 的 `WHERE` 子句配合 `>=` 和 `<=` 可以自然地处理日期筛选。

---

### 练习 5：实现 `find_max_expense_per_category()`

**目标：** 找出每个类别中金额最大的交易。

**要做的事：**

1. 找到 `find_max_expense_per_category()` 函数

2. 这是最棘手的部分。让你的 AI 解释各种选项：
   > "/teach-explain 我需要在 SQL 中找出每个 'category' 中 'amount' 最大的那一行。有哪些方法？"

3. 有多种方法：
   - 使用 `ROW_NUMBER()` 配合 `PARTITION BY`
   - 使用子查询配合 `GROUP BY` 和 `MAX()`

4. 选择一种方法并实现它。**让你的 AI 解释它是怎么工作的。**

5. 将结果转换为字典（category → transaction_id）

6. 运行 `mise run test`

**你会注意到：**

这需要更高级的 SQL。在这里需要帮助是正常的——这正是 AI 辅助开发的意义所在。

> **关键洞察：** 像 `ROW_NUMBER() OVER (PARTITION BY category ORDER BY amount DESC)` 这样的窗口函数是在分组中找到"最佳"行的强大工具。

---

### 练习 6：运行所有测试并验证

**目标：** 确保所有东西一起工作。

**要做的事：**

1. 运行完整的测试套件：
   ```bash
   mise run test
   ```

2. 所有 3 个测试都应该通过：
   - `test_main_returns_dict` — main() 返回一个字典
   - `test_main_has_all_categories` — 包含所有 6 个类别
   - `test_main_correct_max_expenses` — 找到正确的 transaction ID

3. 如果有测试失败，把错误信息分享给你的 AI，迭代直到通过

**你会注意到：**

`main()` 函数将你所有的实现串联在一起。每一步都为下一步提供输入——这就是分而治之的力量。

---

## 反思：我们学到了什么？

让我们退后一步，思考你练习了什么：

**AI 协作技能：**
- 带着上下文清晰描述任务（文件格式、列名、预期输出）
- 请求解释，而不只是代码
- 用错误信息迭代

**问题解决方法：**
- 将复杂任务拆分成 4 个简单步骤
- 分别测试每个步骤
- 通过通过的测试建立信心

**技术接触：**
- Python 项目结构（packages、pyproject.toml）
- 现代包管理（uv）
- 用 Polars 进行数据分析
- 在 Python 中使用 SQL 查询

技术细节会淡化，但方法会留在你身上。

---

## 导师寄语

**为什么这个练习很重要：**

我设计这个练习，故意让你稍微走出舒适区。当你面对陌生技术时，你的本能可能是感到不知所措，或者只是不断复制粘贴代码直到它能用。

但有更好的方法：**与 AI 进行结构化协作**。

你在这里练习的方法适用于任何技术：

1. **清晰描述** — 给 AI 完整的上下文：输入、输出、约束条件
2. **问"为什么"** — 不只是拿代码；要理解它
3. **迭代测试** — 让失败的测试指导你的进度
4. **分而治之** — 把大问题拆分成小的、可测试的部分

**关键洞察：**

- 4 步拆解（load → preview → filter → aggregate）才是真正的课程。这种分而治之的思维到处都适用。
- 测试不只是用来检查正确性的——当你探索陌生领域时，它们是你的路线图。
- 不知道是可以的。重要的是知道如何找出答案。

**下一步：**

把这个方法应用到你遇到的下一个陌生库或框架上。注意当你有效地与 AI 协作时，你能多快地变得高效。

---

## 快速参考

**设置命令：**
```bash
mise run venv-create   # 创建虚拟环境 (uv venv)
mise run inst          # 安装依赖 (uv sync --all-extras)
mise run test          # 运行测试 (.venv/bin/pytest tests)
```

**关键文件：**
- `expense_analyzer/impl.py` — 你的实现（你要编辑的文件）
- `expense_analyzer/impl_example.py` — 参考实现（只在卡住时查看）
- `tests/test_impl.py` — 验证你实现的测试
- `expense.tsv` — 示例数据文件

**Polars 资源：**
- Polars 文档：https://docs.pola.rs/
- SQL 接口指南：https://docs.pola.rs/user-guide/sql/intro/

---

## 参考实现

如果你完全卡住了，可以查看 `expense_analyzer/impl_example.py` 获取一个可工作的解决方案。

**但是请：**
- 先尝试自己实现每个函数
- 在查看解决方案之前先问你的 AI 要提示
- 自己敲代码——不要复制粘贴
- 确保你理解*为什么*每一行代码都能工作

目标是学习，而不只是完成练习。
