# Currency Converter App: Your First Vibe Coding Experience

## Objective

Learn the fundamental skill of AI-assisted development: **clear communication**. Through three hands-on exercises, you'll discover how the quality of your input directly determines the quality of AI's output, and learn a powerful technique to clarify your ideas when you're unsure what you want.

**Key Insight:** The bottleneck in AI-assisted development isn't "how to implement" — it's "what to implement." Your ability to think clearly and communicate precisely is now more valuable than knowing how to code.

**Read the full tutorial:** [Currency Converter App](https://github.com/MacHu-GWU/learn_claude_code_basic-project/tree/07-currency-converter-app-local-dont-push/currency-converter-app)

---

## Actionable Items

1. **Run the reference implementation** — Execute `streamlit run app-example.py` to see what a polished, well-built app looks like. Take 2-3 minutes to observe the UI design, how currencies are displayed, and how the conversion works.

2. **Complete Exercise 1: Vague approach** — Start Claude Code with `claude`, then use `/teach-code` and give a one-liner request like "I need a currency converter tool. Help me build it." Observe how Claude fills in gaps with assumptions. Note what's different from the reference implementation.

3. **Complete Exercise 2: Clear spec approach** — Start a new Claude Code session. Use `/teach-code READ app-spec.md to understand the currency converter app requirement, then write the python app at app.py, and teach me how to run it.` Run the resulting app with `streamlit run app.py` and verify it matches the reference implementation.

4. **Complete Exercise 3: Interview technique** — Start a new Claude Code session. Use `/teach-brainstorm I want to build a currency converter app that converts amounts between different currencies based on exchange rates. I want to build it in Python and run it locally. Help me figure out the detailed spec by asking me questions.` Answer Claude's questions thoughtfully, then review the generated decision document.

5. **Compare all three approaches** — Reflect on the differences between Exercise 1, 2, and 3. Can you articulate why "better input = better output"? Which approach felt most natural to you, and why?

6. **Verify your completed work** — Run `/teach-check` to validate that you've completed all exercises and have a working `app.py` file. Address any items that didn't pass verification.

---

## Checklist

- [ ] Ran reference implementation: `streamlit run app-example.py`
- [ ] Completed Exercise 1 (vague one-liner request with `/teach-code`)
- [ ] Completed Exercise 2 (clear spec approach with `app-spec.md`)
- [ ] Completed Exercise 3 (interview technique with `/teach-brainstorm`)
- [ ] Can explain why "better input = better output" in your own words
- [ ] Have a working `app.py` file that runs without errors
- [ ] App has basic currency conversion functionality
- [ ] Ran `/teach-check` to verify all items passed

---

## Verification & Submission

### How to Verify Your Work

Use the `/teach-check` command to validate that you've completed all requirements:

```
/teach-check
```

This command will:
- Verify you've completed all items in the checklist above
- Confirm you have a working `app.py` file
- Test that the app runs with Streamlit without errors
- Ensure basic currency conversion functionality works

### Submission Steps

1. **Complete all exercises** — Finish Exercise 1, 2, and 3 as described above
2. **Run `/teach-check`** — Verify all items in the checklist are complete
3. **Address any issues** — If verification fails, complete any missing items and run `/teach-check` again
4. **Share your work** — Provide your `app.py` file to your instructor for review

### What Instructors Will Verify

When reviewing your submission:
- App runs without errors: `streamlit run app.py`
- Basic currency conversion functionality works correctly
- Code structure is reasonable and readable
- Evidence that you completed all three exercises (review conversation history or generated files)

### Session Recovery Tips

If you accidentally exit Claude Code or lose your session:
- **Continue last session:** `claude -c`
- **Resume from history:** `claude -r`
- **Start fresh:** `claude`

---

## Learning Outcomes

By completing this project, you will have:
1. Experienced the power of "vibe coding" — building a real app by describing what you want
2. Discovered through hands-on comparison why clear requirements matter
3. Learned the interview technique to clarify vague ideas through conversation
4. Understood that communication clarity is now as valuable as coding skills
5. Built a working app without writing a single line of code yourself

**Estimated time:** 15-30 minutes
