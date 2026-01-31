# Expense Analyzer: Complete the AI-Assisted Development Exercise

## Objective

Build a Python expense analyzer that finds the highest spending in each category from Q3 2025 transaction data.

Read the tutorial: [Expense Analyzer Exercise](https://github.com/MacHu-GWU/learn_claude_code_basic-project/tree/08-expense-analyzer/expense-analyzer)

The goal is not just to make tests pass—it's to practice **AI-assisted development skills**: describing tasks clearly, asking for explanations, iterating with tests, and applying divide-and-conquer thinking.

## Actionable Items

1. **Set up your environment** — Run `mise run venv-create` and `mise run inst` to create a virtual environment and install dependencies

2. **Implement the four core functions in `expense_analyzer/impl.py`** — Work through each function one by one:
   - `load_expense_data()` — Read the TSV file into a Polars DataFrame
   - `preview_first_rows()` — Use SQL to display the first N rows
   - `filter_q3_data()` — Filter data to Q3 2025 using SQL
   - `find_max_expense_per_category()` — Find the max expense per category using SQL

3. **Test your work** — Run `mise run test` after each function to verify correctness and iterate

4. **Verify all tests pass** — Ensure `test_main_returns_dict`, `test_main_has_all_categories`, and `test_main_correct_max_expenses` all pass

## Checklist

- [ ] **Environment set up** — Virtual environment created and dependencies installed
- [ ] **`load_expense_data()` implemented** — Reads TSV file and returns a Polars DataFrame
- [ ] **`preview_first_rows()` implemented** — Uses SQL to select first N rows from DataFrame
- [ ] **`filter_q3_data()` implemented** — Uses SQL to filter data to Q3 2025 date range
- [ ] **`find_max_expense_per_category()` implemented** — Uses SQL to find max expense per category and returns a dictionary
- [ ] **All tests pass** — Run `mise run test` and verify all 3 tests pass
- [ ] **Learning complete** — You understand what each function does and can explain the AI collaboration method you used

## Submission & Verification

When you're done, run `/teach-check` to verify your work against the checklist. Say "ship it" when complete to generate RESULT.md, then share the RESULT.md file GitHub link with your instructor.

## Grading Rubric

> **For instructors and /teach-check assistant** — Students may skip this section.

**Criterion 1: Implementation Quality (No Hardcoding)**
- Review `expense_analyzer/impl.py` for all four functions
- Verify functions are implemented (not just returning placeholder values like `None`)
- Check for any hardcoded return values—implementations should use actual logic
- Compare with `expense_analyzer/impl_example.py` to ensure it's not a direct copy-paste
- **Note:** If code appears to be copy-pasted from reference implementation, do NOT mark as failed. Instead, prompt the student with: "I notice your implementation looks very similar to the reference. Did you really type this yourself? Remember, the goal is learning—understanding the code is more important than just making tests pass."

**Criterion 2: All Tests Pass**
- Run `mise run test`
- Verify all 3 tests pass:
  - `test_main_returns_dict` — `main()` returns a dictionary
  - `test_main_has_all_categories` — all 6 expense categories are present
  - `test_main_correct_max_expenses` — correct transaction IDs are returned for each category
- If any test fails, provide the error output and ask student to debug with AI assistance

**Criterion 3: Learning & Communication**
- Student demonstrates understanding of the AI collaboration method used
- Can explain their approach to breaking down the problem
- Mentions asking AI for explanations (not just code)
- Shows evidence of test-driven iteration
