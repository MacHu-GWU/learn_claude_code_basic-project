# 练习：用 AI 辅助完成一个数据分析小项目

## 这个练习是什么？

在前面的学习中，你已经：

1. 通过 Currency Converter App 体验了 **Vibe Coding** 的感觉
2. 学会了在 AI 辅助下学习开发项目的 **最佳实践**

现在，是时候用一个小项目来**巩固这套方法**了。

这个练习故意选了两个你可能不太熟悉的技术：**Python 数据处理** 和 **SQL 查询**。目的不是让你"学会" Python 或 SQL——而是让你练习：

- 如何向 AI 描述一个你不熟悉的任务
- 如何让 AI 帮你写代码，然后理解它
- 如何在 AI 辅助下调试和验证

**记住：重点不是技术本身，而是你和 AI 协作的方式。**

---

## 任务背景

你会收到一个消费记录文件 `expenses_2025.tsv`，包含某人 2025 全年的消费数据。

你的任务是写一个函数，找出 **2025 年 7-9 月（Q3）每个消费类别中金额最大的那笔交易**。

技术要求：
- 用 **Polars** 读取 TSV 文件
- 用 **Polars SQL**（`pl.sql()`）完成数据分析

---

## 数据说明

**文件格式：** TSV（Tab 分隔）

| 列名 | 说明 | 示例 |
|------|------|------|
| `transaction_id` | 交易 ID | `TXN-2025-001` |
| `date` | 日期（ISO 格式） | `2025-07-15` |
| `category` | 消费类别 | `Dining` |
| `merchant` | 商家 | `Chipotle` |
| `amount` | 金额 | `12.50` |
| `description` | 备注 | `Lunch` |

**类别共 6 种：** `Dining`, `Transport`, `Shopping`, `Entertainment`, `Groceries`, `Utilities`

---

## 函数要求

**函数名：** `find_max_expense_per_category`

**输入：** `file_path`（字符串，TSV 文件路径）

**输出：** 字典，格式如下：

```python
{
    "Dining": "TXN-2025-XXX",
    "Transport": "TXN-2025-XXX",
    ...
}
```

**逻辑：**
1. 只看 2025-07-01 到 2025-09-30 的数据
2. 每个类别找金额最大的那笔
3. 返回对应的 `transaction_id`

---

## 如何用 AI 完成这个任务

### 第一步：安装依赖

先让 AI 帮你确认环境：

> "我需要用 Polars 做数据分析，请告诉我怎么安装。"

### 第二步：描述任务

用你自己的话向 AI 描述任务。比如：

> "我有一个 TSV 文件，包含消费记录。我需要用 Polars 读取它，然后用 pl.sql() 写 SQL 查询，筛选 2025 年 7-9 月的数据，找出每个 category 里 amount 最大的那笔，返回它的 transaction_id。"

**关键点：** 把你知道的信息都告诉 AI——文件格式、列名、筛选条件、输出格式。

### 第三步：理解代码

当 AI 给你代码后，**不要直接复制粘贴**。问它：

> "请解释这段 SQL 在做什么，特别是 [你不懂的部分]。"

如果解释太复杂，继续追问：

> "能用更简单的方式解释吗？假设我完全不懂 SQL。"

### 第四步：运行测试

```bash
pytest test_expense_analyzer.py -v
```

如果测试失败，把错误信息发给 AI：

> "测试报错了：[粘贴错误信息]。帮我看看哪里出问题了。"

### 第五步：迭代修复

根据 AI 的建议修改代码，再次运行测试。重复直到通过。

---

## 文件结构

```
expense-analyzer/
├── expenses_2025.tsv          # 数据（提供）
├── expense_analyzer.py        # 你的代码（你写）
└── test_expense_analyzer.py   # 测试（提供）
```

你的 `expense_analyzer.py` 应该包含：

```python
import polars as pl


def find_max_expense_per_category(file_path: str) -> dict:
    """
    找出 Q3 每个类别的最大支出。
    
    必须使用 pl.sql() 完成分析逻辑。
    """
    # 你的代码
    pass
```

---

## 检查清单

- [ ] 安装了 `polars`
- [ ] 用 `pl.read_csv(separator="\t")` 读取 TSV
- [ ] 用 `pl.sql()` 写 SQL 查询
- [ ] 日期筛选正确（2025-07-01 到 2025-09-30）
- [ ] 返回的是字典，value 是 `transaction_id`
- [ ] `pytest` 测试全部通过
- [ ] 能向导师解释你的 SQL 在做什么

---

## 这个练习的意义

完成这个练习后，你应该更熟练地掌握了：

✅ **如何向 AI 清晰描述任务** — 包括输入、输出、约束条件
✅ **如何让 AI 解释代码** — 不只是拿代码，还要理解它
✅ **如何用测试验证结果** — 客观检验代码是否正确
✅ **如何迭代调试** — 把错误信息给 AI，协作修复

这套方法适用于任何你不熟悉的技术。以后遇到新的库、新的框架、新的语言，都可以用同样的方式快速上手。