# Expense Analyzer: Practice AI-Assisted Development

> Learn how to collaborate with AI to complete a data analysis project using Python and SQL.

## Overview

This is a hands-on exercise designed to practice **AI-assisted development skills**. You'll build a small expense analyzer that finds the highest spending in each category from a transaction dataset.

The technologies (Python, Polars, SQL) are intentionally unfamiliar to most learners. **This is by design.** The goal isn't to master these tools—it's to practice a method you can apply to *any* unfamiliar technology.

**It's completely normal to not understand everything.** The point is to experience interactive learning with AI—going from "I don't know" to "I understand" through conversation and iteration.

## Learning Objectives

In real-world software development, you'll constantly encounter unfamiliar technologies, libraries, and codebases. The ability to quickly understand and work with new tools—often with AI assistance—is becoming essential.

This exercise puts you in that exact situation: facing an unfamiliar stack (Python + SQL) and learning to navigate it effectively with AI as your collaborator.

By the end of this exercise, you will:

1. **Practice describing tasks clearly to AI** — including input format, constraints, and expected output
2. **Learn to ask AI for explanations** — not just getting code, but understanding it
3. **Experience test-driven iteration** — using failing tests to guide your implementation
4. **Apply divide-and-conquer thinking** — breaking a complex problem into manageable steps

## Prerequisites

- Basic command line familiarity (running commands)
- An AI assistant (Claude Code, Cursor, etc.)
- Willingness to experiment and ask questions

**No Python or SQL experience required.** That's the whole point.

## What You'll Build

A Python function that:
1. Reads expense data from a TSV file
2. Filters to Q3 2025 (July-September)
3. Finds the maximum expense in each category
4. Returns a dictionary mapping category to transaction ID

---

## Key Concepts

Before diving into code, let's understand the project structure and tools. Don't worry if some of this feels unfamiliar—ask your AI assistant to explain anything that's unclear.

### Python Project Structure

When you look at this project, you'll see folders and files that might seem mysterious:

- **`expense_analyzer/`** — This folder contains your implementation code. In Python, we organize code into "packages" (folders with code). Today you're lucky—there's only one file. In larger projects, there could be many modules inside.

- **`tests/`** — Contains test files that verify your code works correctly.

- **`pyproject.toml`** — The project's "recipe card." It defines:
  - Project name and version
  - Python version required (3.12+)
  - Dependencies (external libraries your project needs)

- **`.venv/`** — A "virtual environment" that isolates this project's dependencies from other Python projects on your machine.

### Package Management with uv

Python projects need external libraries (like Polars). We use **uv** to manage these—it's fast and modern. The key commands are:

- `mise run venv-create` — Creates a virtual environment (runs `uv venv` underneath)
- `mise run inst` — Installs all dependencies (runs `uv sync --all-extras` underneath)

### Polars: Modern Data Analysis

**Polars** is one of the two most powerful libraries for local data analysis (the other being DuckDB). We're using Polars because:
- It's blazing fast (written in Rust)
- It has a clean SQL interface
- It's a joy to work with compared to alternatives

To learn more, check the official documentation: https://docs.pola.rs/

### Polars SQL Interface

Polars lets you query DataFrames using familiar SQL syntax with `pl.sql()`. This is perfect for learners who know SQL or want to learn it:

```python
result = pl.sql("""
    SELECT category, amount
    FROM df
    WHERE amount > 100
""").collect()
```

Documentation: https://docs.pola.rs/user-guide/sql/intro/

### Testing with pytest

Instead of writing print statements and checking output by eye, we use **pytest**—Python's standard testing framework. The command is:

```bash
mise run test        # Runs: .venv/bin/pytest tests
```

The beauty of tests: **if they pass, your code is (probably) correct.** This gives you confidence to iterate quickly.

### Divide and Conquer: Breaking Down the Problem

Here's the key insight for this exercise. Before writing any code, think about how to break this problem into steps:

**The task:** Find the max expense per category for Q3 2025.

**How would you break this down?** Think about it before reading further.

The natural decomposition is:

1. **Load data** — Read the TSV file into memory
2. **Preview data** — Understand what we're working with
3. **Filter data** — Keep only Q3 2025 records
4. **Aggregate and find max** — Group by category, find the highest amount

This is **divide and conquer**—a fundamental problem-solving approach. Each step is small and testable. The `main()` function orchestrates all four steps together.

---

## Exercises

### Exercise 1: Set Up Your Environment

**Goal:** Get the project running and ready for development.

**What to do:**

1. Create the virtual environment:
   ```bash
   mise run venv-create
   ```
   (This runs `uv venv` to create an isolated Python environment)

2. Open `pyproject.toml` and look at the dependencies section. You'll see `polars` listed.

3. Install dependencies:
   ```bash
   mise run inst
   ```
   (This runs `uv sync --all-extras` to install all packages)

4. Run the tests to see what's failing:
   ```bash
   mise run test
   ```

**What you'll notice:**

The tests will fail because `impl.py` has stub functions that return `None`. This is expected—you'll implement them next.

> **Key insight:** Running tests first shows you exactly what needs to be done. Failing tests are your roadmap.

---

### Exercise 2: Implement `load_expense_data()`

**Goal:** Read the TSV file into a Polars DataFrame.

**What to do:**

1. Open `expense_analyzer/impl.py` and find the `load_expense_data()` function

2. Read the TODO comments and docstring to understand what's needed

3. Ask your AI assistant:
   > "/teach-code I need to read a TSV file using Polars. The file uses tab as separator. How do I do this?"

4. Implement the function. **Type it yourself—don't copy-paste.**

5. Run the tests: `mise run test`

**Hint:** The reference implementation is in `impl_example.py` if you get stuck, but try to figure it out first.

> **Key insight:** `pl.read_csv()` with `separator="\t"` is all you need. Simple, right?

---

### Exercise 3: Implement `preview_first_rows()`

**Goal:** Use SQL to select the first N rows from a DataFrame.

**What to do:**

1. Find the `preview_first_rows()` function in `impl.py`

2. Ask your AI:
   > "/teach-explain How do I use pl.sql() to select the first 5 rows from a DataFrame in Polars?"

3. Implement the function. Remember: **write it yourself**.

4. Run `mise run test` to check progress

**What you'll notice:**

The SQL syntax is familiar if you know SQL: `SELECT * FROM df LIMIT 5`. Polars lets you reference the DataFrame variable name directly in SQL.

> **Key insight:** `pl.sql()` returns a LazyFrame—you need `.collect()` to execute the query and get a DataFrame.

---

### Exercise 4: Implement `filter_q3_data()`

**Goal:** Filter the data to only Q3 2025 (July 1 - September 30).

**What to do:**

1. Find the `filter_q3_data()` function

2. Ask your AI:
   > "/teach-explain How do I filter a Polars DataFrame using SQL to only include dates between '2025-07-01' and '2025-09-30'?"

3. Implement the function

4. Run `mise run test`

**Hint:** Look at the function parameters—the start and end dates are already provided.

> **Key insight:** SQL's `WHERE` clause with `>=` and `<=` handles date filtering naturally when dates are in ISO format (YYYY-MM-DD).

---

### Exercise 5: Implement `find_max_expense_per_category()`

**Goal:** Find the transaction with the highest amount in each category.

**What to do:**

1. Find the `find_max_expense_per_category()` function

2. This is the trickiest part. Ask your AI to explain options:
   > "/teach-explain I need to find the row with the maximum 'amount' for each 'category' in SQL. What are my options?"

3. There are multiple approaches:
   - Using `ROW_NUMBER()` with `PARTITION BY`
   - Using a subquery with `GROUP BY` and `MAX()`

4. Pick one approach and implement it. **Ask your AI to explain how it works.**

5. Convert the result to a dictionary (category → transaction_id)

6. Run `mise run test`

**What you'll notice:**

This requires more advanced SQL. It's okay to need help here—that's the point of AI-assisted development.

> **Key insight:** Window functions like `ROW_NUMBER() OVER (PARTITION BY category ORDER BY amount DESC)` are powerful tools for finding "the best" row within groups.

---

### Exercise 6: Run All Tests and Verify

**Goal:** Ensure everything works together.

**What to do:**

1. Run the full test suite:
   ```bash
   mise run test
   ```

2. All 3 tests should pass:
   - `test_main_returns_dict` — main() returns a dictionary
   - `test_main_has_all_categories` — all 6 categories are present
   - `test_main_correct_max_expenses` — the correct transaction IDs are found

3. If any test fails, share the error message with your AI and iterate until it passes

**What you'll notice:**

The `main()` function chains all your implementations together. Each step feeds into the next—that's the power of divide and conquer.

---

## Reflection: What Did We Learn?

Let's step back and think about what you practiced:

**AI Collaboration Skills:**
- Describing tasks clearly with context (file format, column names, expected output)
- Asking for explanations, not just code
- Iterating with error messages

**Problem-Solving Approach:**
- Breaking a complex task into 4 simple steps
- Testing each step individually
- Building confidence through passing tests

**Technical Exposure:**
- Python project structure (packages, pyproject.toml)
- Modern package management (uv)
- Polars for data analysis
- SQL queries within Python

The technical details will fade, but the method stays with you.

---

## Mentor's Note

**Why this exercise matters:**

I designed this exercise to put you slightly outside your comfort zone—on purpose. When you face unfamiliar technology, your instinct might be to feel overwhelmed or to just copy-paste code until it works.

But there's a better way: **structured collaboration with AI**.

The method you practiced here works for any technology:

1. **Describe clearly** — Give AI the full context: inputs, outputs, constraints
2. **Ask "why"** — Don't just take code; understand it
3. **Test iteratively** — Let failing tests guide your progress
4. **Divide and conquer** — Break big problems into small, testable pieces

**Key insights:**

- The 4-step breakdown (load → preview → filter → aggregate) is the real lesson. This divide-and-conquer thinking applies everywhere.
- Tests aren't just for checking correctness—they're your roadmap when exploring unfamiliar territory.
- It's okay to not know. What matters is knowing how to find out.

**Next steps:**

Apply this method to the next unfamiliar library or framework you encounter. Notice how quickly you can become productive when you collaborate with AI effectively.

---

## Quick Reference

**Setup commands:**
```bash
mise run venv-create   # Create virtual environment (uv venv)
mise run inst          # Install dependencies (uv sync --all-extras)
mise run test          # Run tests (.venv/bin/pytest tests)
```

**Key files:**
- `expense_analyzer/impl.py` — Your implementation (the file you edit)
- `expense_analyzer/impl_example.py` — Reference implementation (look only if stuck)
- `tests/test_impl.py` — Tests that verify your implementation
- `expense.tsv` — Sample data file

**Polars resources:**
- Polars documentation: https://docs.pola.rs/
- SQL interface guide: https://docs.pola.rs/user-guide/sql/intro/

---

## Reference Implementation

If you get completely stuck, you can look at `expense_analyzer/impl_example.py` for a working solution.

**But please:**
- Try to implement each function yourself first
- Ask your AI for hints before looking at the solution
- Type the code yourself—don't copy-paste
- Make sure you understand *why* each line works

The goal is learning, not just completing the exercise.
