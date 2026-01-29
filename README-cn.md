# 使用斜杠命令

> 学习如何使用斜杠命令快速执行预先构建的提示词模板，而不是每次都输入冗长的指令。

## 为什么这很重要

想象你经常需要做同样的任务 — 转换货币、审查代码、编写文档或分析数据。每一次，你都需要粘贴同样的详细指令到 Claude Code 中。

如果你只需要打一个快速命令，Claude 就自动使用正确的提示词，会怎样呢？

这正是斜杠命令做的事情。它们像是你最常见工作流的快捷方式 — 节省时间并减少重复。

## 什么是斜杠命令？

把斜杠命令想象成一个**提示词模板快捷方式**。它是一种快速注入预先编写的系统提示词而无需手动输入的方式。

基本思想是：

1. 斜杠命令包含一个**系统提示词** — Claude 的详细指令
2. 你在 Claude Code 中输入 `/command-name arguments`
3. Claude 自动加载系统提示词并处理你的参数

**重要提示：** 你不需要记住斜杠命令。当你输入 `/` 并开始输入时，Claude Code 会展示可用命令的列表。你可以用几个按键选择一个。

## 用例子理解系统提示词

让我们看一个真实的例子。`convert-currency` 命令有一个系统提示词，教 Claude 如何在货币之间转换。

你可以通过运行以下命令来查看它：

```bash
cat .claude/skills/convert-currency/SKILL.md
```

这会显示完整的提示词，包括：
- **元数据**（name、description、argument-hint）— 告诉 Claude Code 关于这个命令的信息
- **系统提示词** — Claude 将遵循的实际指令

它看起来像这样：

```
---
name: convert-currency
description: Convert currency amounts between USD, EUR, GBP, CNY, and JPY using current exchange rates.
argument-hint: "[amount] [from-currency] to [to-currency]"
---

You are a currency conversion assistant. Your task is to convert currency amounts accurately...
```

## $ARGUMENTS 占位符

任何系统提示词中的关键概念是 **$ARGUMENTS**。这是一个占位符，会被替换为你在命令后输入的内容。

例如：
- 命令：`/convert-currency How much is $180 USD in Euro?`
- `$ARGUMENTS` 变成：`How much is $180 USD in Euro?`

这就是同一个命令如何处理不同的用户输入的方式 — 提示词适应你传入的任何内容。

## 动手练习：练习 1（手动方式）

让我们先用手动的方式来理解发生了什么。

复制下面的文本（系统提示词部分，不是元数据），粘贴到 Claude Code 中，带上你的问题。替换 `$ARGUMENTS` 为你的实际问题：

```
You are a currency conversion assistant. Your task is to convert currency amounts accurately using the provided exchange rates.

## Exchange Rates (base currency: USD)

- United States Dollar (USD): 1.00
- Euro (EUR, official common currency of the Eurozone): 0.92
- British Pound Sterling (GBP): 0.79
- Chinese Yuan Renminbi (CNY): 7.22
- Japanese Yen (JPY): 155.50

## Instructions

When the user asks: How much is $180 USD in Euro?

1. Parse the amount and currencies from the user's request
2. Convert the amount using the provided exchange rates:
   - If converting FROM USD: multiply the amount by the target currency rate
   - If converting TO USD: divide the amount by the source currency rate
   - If converting between non-USD currencies: convert to USD first, then to the target currency
3. Provide the result with clear formatting, showing:
   - The original amount and currency
   - The converted amount and currency
   - The calculation used (optional, for transparency)

## Example

Input: "$763.45 USD to EUR"
Output: $763.45 USD = 702.37 EUR (calculation: 763.45 × 0.92 = 702.374)

Be precise with decimal places and round to 2 decimal places for currency amounts.
```

**你的任务：** 复制上面的内容，粘贴到 Claude Code 中，看看 Claude 如何转换货币。

这就是斜杠命令幕后发生的事情 — 但你必须手动复制和粘贴。

## 动手练习：练习 2（使用斜杠命令）

现在体验斜杠命令的便利。

在 Claude Code 中，只需输入：

```
/convert-currency How much is $180 USD in Euro?
```

与练习 1 比较：
- 练习 1：复制一大块文本，粘贴它，运行它（**很多工作**）
- 练习 2：输入一个简短命令（**最小的工作量**）

这就是斜杠命令的力量 — 相同的结果，一小部分工作量。

## 斜杠命令如何在幕后工作

当你输入 `/convert` 时，Claude Code：

1. 搜索所有与"convert"匹配的可用命令
2. 显示一个列表（在这个例子中，`/convert-currency`）
3. 你选择它或完成完整的名称
4. Claude 从 `.claude/skills/convert-currency/SKILL.md` 加载系统提示词
5. 你的参数被插入到 `$ARGUMENTS` 出现的地方
6. Claude 用完整的背景信息处理请求

这就是为什么**你不需要记住命令名称**。开始输入，Claude Code 的自动完成会帮助你找到需要的内容。

## 为什么我们先从简单开始

你可能听说过 Claude Code 中的术语"Skills"。这是这个系统的全部力量。但斜杠命令只是 Skills 能做事情的 10%。现在，把它们想象成方便的提示词快捷方式。

以后，我们将探索：
- 创建自定义 skills
- 构建复杂的工作流
- 与工具和 API 集成

但今天，重点是理解：斜杠命令 = 更快访问你最喜欢的提示词。

## 快速参考

- **自动完成：** 输入 `/` 查看可用命令；你不需要记住它们
- **语法：** `/command-name arguments`
- **查看一个 skill：** `cat .claude/skills/[skill-name]/SKILL.md`
- **概念：** 斜杠命令 = 提示词模板 + 快速访问
- **好处：** 用最少的输入执行复杂的工作流

## 导师的话：自动化重复的工作流

在我职业生涯的早期，我会一遍遍写同样的指令。"这是我想让你分析代码的方式……"或"请用汇率转换这个……"

重复很乏味，但更糟的是，它容易出错。我会忘记细节、打错字或短语的方式略有不同。

一旦我意识到我可以自动化这些工作流，一切都改变了。我不再在输入指令和等待响应之间切换上下文，而是可以专注于实际的任务。

这是好工程的核心原则：**自动化重复的东西**。斜杠命令是实践这一点的简单方式 — 这个习惯会转移到你构建的一切。

## 进一步阅读

- [Claude Code Skills 文档](https://code.claude.com/docs/en/skills)
- [提示工程最佳实践](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering)
