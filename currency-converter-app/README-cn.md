# 货币转换应用

> 你的第一次 "vibe coding" 体验：不用自己写代码就能构建一个真实的应用。

![Currency Converter App](./img/currency-converter.png)

## 概览

恭喜！你刚刚安装了 Claude Code。现在呢？

在这个练习中，你将构建一个完整功能的货币转换应用 — 是的，一个真实的应用，有 UI 可以在浏览器中运行。最令人兴奋的是：**你不需要懂如何编码**。

但等等，这不是魔法。AI 为你构建什么取决于**你如何与它沟通**。这是你今天要学到的最重要的课程。

把 AI 想象成一位刚加入你团队的超级人才。他们能做出令人惊艳的工作，但前提是你给出清晰的 instructions。说 "给我做点酷的东西"，你会得到……什么都可能。说 "这是我确切需要的东西，包括所有细节"，你会得到正是你想象的东西。

## 学习目标

在完成这个练习后，你将：

1. **体验 "vibe coding" 的力量** — 通过描述你想要的东西来构建应用
2. **理解为什么 clear requirements 很重要** — 通过动手对比实验
3. **学习实用技巧** — 当不确定要什么时，如何让 AI 帮助你理清自己的想法

> **注意：** 这个练习不是关于学习 Python 或 Streamlit。而是关于学习如何有效地与 AI 工具协作。

## 前置条件

- Claude Code 已安装且可用（你应该能在 terminal 中运行 `claude`）
- 对使用 terminal 有基本熟悉度（cd、ls 等）
- 就这些！不需要任何编程经验。

## 你将构建什么

一个简单但功能完整的货币转换器，可以：
- 让你输入金额（如 100）
- 选择源 currency（如 USD）
- 选择目标 currency（如 EUR）
- 立即显示转换结果

这是一个小应用，但它是一个**真实的应用** — 对初学程序员来说需要花费数小时甚至数天才能完成的那种。你将在几分钟内让它运行起来。

---

## 练习

### 练习 1：一句话方法

**目标：** 看看当你给 AI 一个模糊 request 时会发生什么。

**怎么做：**

1. 打开 terminal，navigate 到这个 project folder
2. 输入 `claude` 启动 Claude Code
3. 输入这个 prompt（或用你自己的话类似地表达）：

```
I need a currency converter tool. Help me build it.
```

4. 让 Claude 开始工作。它可能会：
   - 问你一些问题，或者
   - 直接根据假设开始构建

5. **观察结果。** 问自己：
   - 它是否构建了你想象的东西？
   - 它是否使用了你预期的 technology？
   - UI 是否看起来像你想象的那样？
   - 是否包含你关心的 currencies？

**你可能会注意到：**

结果……还可以。它能用。但可能不完全是你想的。也许它是一个 command-line tool，而你想要一个 web app。也许它只支持 USD 和 EUR。也许 interface 看起来和你想的不一样。

这不是 Claude 的错。**Claude 确实构建了你要求的东西 — 只是你的 request 不够 specific。**

> **关键洞察：** Vague input = 不可预见的 output。AI 很强大，但读不了你的心思。

---

### 练习 2："Clear Spec" 方法

**目标：** 看看当你提供 clear requirements 时会有多大的差异。

**怎么做：**

1. 启动一个**新的** Claude Code session（再输入一次 `claude`，或用 `/clear` 重置）
2. 这次，使用这个 prompt：

```
READ app-spec.md to understand the currency converter app requirement, then write the python app at app.py, and teach me how to run it.
```

3. 观看 Claude 工作。它会：
   - 读取 spec file（其中包含详细 requirements）
   - 根据这些确切 specifications 构建应用
   - 解释如何运行它

4. **运行应用**，使用 Claude 给你的命令（可能是 `streamlit run app.py`）

5. **与练习 1 比较结果：**
   - 是否更接近上面截图中看到的？
   - 是否包含所有 5 种 currencies（USD、CNY、EUR、GBP、JPY）？
   - UI 是否符合 spec？

**你会注意到：**

结果更加 polished 和 predictable。它完全符合 spec。UI elements 在应该的位置。currencies 正确。转换 formula 按预期工作。

> **关键洞察：** Clear requirements = high-quality results。你花在思考想要什么上的时间永远不会浪费。

**随意探索 `app-spec.md`** — 打开它，看看什么样的 requirement document 是好的。不复杂，只是 clear 和 specific。

---

### 练习 3：让 AI 帮你思考

**目标：** 学习当不确定想要什么时如何理清自己的想法。

这里的关键是：大多数人无法从零开始写出像 `app-spec.md` 这样 clear 的 spec。这完全正常！**在和 AI 交谈之前，你不需要确切知道你想要什么。**

有更好的方法：**让 AI interview 你**。

**怎么做：**

1. 启动一个**新的** Claude Code session
2. 使用这个 prompt：

```
I want to build a currency converter app that converts amounts between different currencies based on exchange rates. I want to build it in Python and run it locally.

Please help me figure out the detailed spec by asking me questions to define this requirement in detail. After a few rounds of Q&A (like an interview), write my final decisions to app-spec.md for future reference.
```

3. **回答 Claude 的问题。** 它可能会问：
   - "Which currencies do you want to support?"
   - "Do you want a command-line interface or a web UI?"
   - "Should exchange rates be hardcoded or fetched from an API?"
   - "What should happen if the user enters invalid input?"

4. **做出决定。** 不要想太多 — 根据你的偏好直接回答。

5. **审查生成的 spec。** Claude 会根据你的回答写入一个 `app-spec.md` file。检查它是否 capture 了你讨论的内容。

**你会学到：**

你刚刚创建了一份 clear requirement document，而不知道怎样写！AI 问了 right questions，你提供了 domain knowledge（你想要什么）。一起，你们创建了两者单独都做不了的东西。

> **关键洞察：** 如果你无法写 spec，让 AI 通过对话帮你发现你想要什么。Interview technique 有效是因为 AI 知道该问什么 questions，而你知道你倾向的答案。

---

## 反思：我们学到了什么？

让我们退一步，思考刚才发生了什么：

| 方法 | Input Quality | Output Quality |
|------|--------------|----------------|
| 练习 1 | Vague（一句话） | Unpredictable，"good enough" |
| 练习 2 | Clear（detailed spec） | Precise，符合预期 |
| 练习 3 | Started vague，became clear（通过 Q&A） | High quality，个性化 |

**模式很清楚：** Better input = Better output。

但这里是真正的洞察：**你不必从 perfect requirements 开始**。你可以：
1. 从粗略想法开始
2. 让 AI 通过 questions 帮你改进
3. 记录改进后的 requirements
4. 使用这些 requirements 来构建伟大的东西

这是 effective AI collaboration 的本质。AI 增强了你带来的东西。带来 clarity（或发现 clarity 的意愿），你会得到惊人的结果。

---

## Mentor 的话

**为什么这个练习重要：**

我见过数百人与 AI 工具的痛苦过程，90% 的时候，问题不在 AI — 而在于人们怎样与它沟通。他们输入一些 vague 的东西，得到平庸 results，然后得出结论 "AI 没那么有用"。

但这是真相：**AI 像一面镜子。它反映了你思维的 clarity（或 confusion）。**

真正的技能不是关于创作 perfect "prompt"（那个词被过度使用了）。而是关于 **clear communication** — 你能否描述：

1. **你想构建什么** — goal、features、behavior
2. **你期望它如何工作** — files 应该去哪里，使用什么 technology，output 应该是什么样的

这听起来简单，但很难！它要求你成为一个**清晰的思考者**。这里是令人不适的真相：大多数人在开始和 AI 交谈前还没想清楚他们真正想要什么。他们脑子里有个 vague 想法，期望 AI 读心术。

**但你不必天生就是一个"clear thinker"**

这是今天最重要的课程：**你可以用 AI 来帮助你清晰思考**。

Interview technique（练习 3）是秘密武器。当你请 AI interview 你关于 requirements 时，魔法发生了：

- AI 问出 structured 的 questions，你自己想不到
- 你被迫做出你一直在回避的决定
- 你的 vague 想法变成了 concrete requirements
- 最后，你有了 clear spec — 即使你最初无法从零开始写

这是真正的绝招：**用 AI 成为清晰的思考者，然后用这种 clarity 从 AI 获得更好的结果**。

**你体验过的三种方法：**

| 方法 | 何时使用 |
|------|---------|
| Direct request（练习 1） | Quick experiments，low-stakes tasks |
| Clear spec（练习 2） | 你已经确切知道想要什么 |
| Interview technique（练习 3） | 你有想法但还没想清楚细节 |

大多数现实 tasks 属于第三类。你有粗略想法，但细节 fuzzy。不要假装否则 — embrace 它，让 AI 帮你理清。

**关于 "vibe coding" 的几句话：**

"Vibe coding" 这个词很俏皮，但技能是真实的。在 AI 时代，清晰表达你想要什么的能力 — 用 natural language — 变得比死记 syntax 更有价值。

这不意味着编程知识无用。理解软件如何工作帮助你更好地与 AI 沟通。但 bottleneck 已转变：**最难的部分不再是 "how to implement" — 而是 "what to implement"。**

你的工作是清晰地思考问题（或让 AI 帮你清晰思考）。AI 的工作是 implement solutions。当双方都做好自己的工作时，魔法发生。

**后续步骤：**

现在你体验过了这个 workflow，尝试将它应用于你自己的 projects：

- 有学校 project？不要直接把作业丢给 AI。首先，理清你想构建什么。
- 不确定想要什么？使用 interview technique。请 AI 帮你想清楚。
- 得到平庸 results？不要怪 AI。问自己："我真的沟通清楚我想要什么了吗？"

欢迎来到构建软件的未来。进入 barrier 从未如此之低 — 但**你清晰思考和沟通的能力比以往任何时候都更重要**。

---

## 快速参考

**启动 Claude Code：**
```bash
claude
```

**运行应用（Claude 构建后）：**
```bash
streamlit run app.py
```

**重置对话：**
```
/clear
```

**关键文件：**
- `app-spec.md` — requirement document（阅读以了解好的 spec 是什么样的）
- `app.py` — app code（由 Claude 生成）
- `rates.json` — exchange rate data（由 Claude 生成）

---

## 参考实现：先看最终目标

在开始练习之前，运行参考实现来看看一个精致、设计良好的应用是什么样的：

```bash
streamlit run app-example.py
```

这是**导师的参考实现** — 这个项目的黄金标准。用它作为视觉参考来对比：

- UI 看起来有多干净
- 错误处理如何工作
- 界面如何组织
- currencies 如何显示

**为什么先做这个？** 如果看不到最终目标，你不会知道你的练习 1 结果是平庸还是优秀。用 `app-example.py` 作为"做得好"的样子的参考。

完成每个练习后，再运行一次，问自己："我的结果与这个参考实现有多接近？"
