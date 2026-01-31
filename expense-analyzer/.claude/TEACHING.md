# Teaching Guide: Expense Analyzer

## Learning Outcomes

By the end of this lesson, learners should be able to:

1. **Cognitive Outcome** — Understand and articulate the method of structured AI collaboration: breaking problems into steps, asking for explanations, testing iteratively
2. **Skill Outcome** — Write a multi-step Python program using Polars SQL, guided by tests and AI
3. **Mindset Outcome** — Adopt confidence when facing unfamiliar technologies—knowing how to learn is more important than knowing the technology itself

---

## Concept Sequence

Teach concepts in this specific order. This sequence prevents information overload while building confidence.

### Phase 0: Mindset & Permission to Struggle (5 minutes)

**Before anything else, set the frame:**

Start with this message or similar:

> "You don't need to understand everything in this exercise. That's the whole point. In real development, you'll constantly face unfamiliar tools. The skill we're practicing isn't Python or SQL—it's *how to learn new things with AI*. It's completely normal to feel confused. That's not a sign you're doing it wrong—that's a sign it's working."

This 30-second framing prevents two failure modes:
- Students pretending to understand when they don't
- Students quitting early because "they should already know this"

### Phase 1: Structure & Scaffolding (10 minutes)

Teach these concepts in order:

1. **Python Project Structure** — Start with the visual:
   - "This folder is a 'package.' It's just how Python organizes code."
   - Point to `pyproject.toml` — "This is a recipe card. It says: Python 3.12, we need Polars library."
   - Point to `.venv/` — "This is a sandbox. It keeps this project's dependencies isolated."
   - **Why this first:** Students need to understand the landscape before they navigate it.

2. **The Divide-and-Conquer Framework** — This is THE core insight:
   - Don't tell them the 4 steps yet
   - Ask: "If you wanted to find the most expensive item in each category, how would you break that down?"
   - Let them think for 30 seconds
   - Guide them to the 4 natural steps: load → preview → filter → aggregate
   - **Why this matters:** If students own the decomposition, they won't just copy code mindlessly. They'll refer back to "my 4 steps."

3. **Tests as a Roadmap** — Run the tests BEFORE implementation:
   - `mise run test` — "Look, 3 tests fail. That's expected. These tests ARE your specification."
   - Show them what each test checks
   - Point out: "Each test is like a checkpoint. When it passes, you know you did that step right."
   - **Why this first:** Many students fear tests. Showing them upfront demystifies the process.

### Phase 2: Guided Implementation (30 minutes)

Each exercise follows the same pattern. **Don't skip the thinking step**:

**Exercise Pattern:**
1. **Before coding** — Ask: "What do we need to do here? What's the AI question you'd ask?"
2. **Code with AI** — Model the collaboration: "I'd ask Claude: [specific question]. Then I'd type the answer myself."
3. **Test immediately** — `mise run test` right away
4. **Reflect on what just happened** — "Did that test pass? Why or why not?"

**Exercise-Specific Teaching Notes:**

**Exercise 2 (load_expense_data)** — First function, lowest friction
- Emphasize: "Reading a file is a basic operation. You're not learning Polars syntax—you're learning to ask the right question to AI."
- If student gets stuck: Prompt "What does the error message say? What would you ask AI?" Don't give the answer directly.

**Exercise 3 (preview_first_rows)** — Introduces SQL, low complexity
- Many students fear SQL. Frame it: "SQL looks scary but it's just asking a question in English: SELECT * FROM df LIMIT 5. Polars lets you ask that in Python."
- Highlight: `.collect()` is the thing that executes the query. LazyFrame vs DataFrame distinction can be deferred.

**Exercise 4 (filter_q3_data)** — Dates and WHERE clause, still comfortable
- Students often hardcode dates. Ask: "Why did the function accept START_DATE and END_DATE as parameters? Should you hardcode them?"
- This reinforces: parameters are about flexibility and reusability.

**Exercise 5 (find_max_expense_per_category)** — The challenging one
- **This is where most struggle.** Window functions are genuinely hard.
- **Don't skip explanation:** Ask AI to explain not just "how" but "why ROW_NUMBER() works here."
- **Offer options:** "You can use ROW_NUMBER() or GROUP BY + subquery. One is easier. What does your AI say?"
- **Test-driven debugging:** If they get stuck, have them run the test and read the error. Error messages often reveal the missing piece.

**Exercise 6 (verification)** — Celebration, not obstacle
- If all tests pass: Stop and celebrate. "You just built a data analysis program."
- If any test fails: This is expected. Frame as: "The test is telling us exactly what's wrong. What would you ask AI to fix this?"

### Phase 3: Reflection & Transfer (5 minutes)

After completion, ask these three reflection questions:

1. **About the method:** "Walk me through how you collaborated with AI. How did you know what to ask?"
2. **About the thinking:** "How did the 4-step breakdown help you? Would you use that approach in other projects?"
3. **About confidence:** "If you encounter an unfamiliar library next week, how would you approach it differently than before?"

Listen for:
- Evidence of asking AI for explanations (not just code)
- Recognition that tests guided their progress
- Understanding of the 4-step decomposition
- Confidence that this method is transferable

---

## Common Struggles

### Struggle 1: Analysis Paralysis — Staring at Unfamiliar Code Without Asking

**Signs:**
- Student sits in silence, scrolls through Polars docs, looks frustrated
- Says things like "I don't know where to start" or "This library is too complicated"
- Hesitates to ask AI because they're "not even sure what the question is"

**Root Cause:** Student thinks they should understand the tool before using it. This is backwards.

**Intervention:**
- Step in immediately (don't let this linger for 10 minutes)
- Say: "You don't need to understand Polars. You need to ask the right person. Let me show you how I'd phrase this question to AI..."
- Model an example: "I'd say: 'I have a CSV file with tab separators. How do I read it with Polars?' That's enough. You don't need to read 50 docs pages first."
- Then have them ask that question to AI
- **Key phrase:** "Ask first, understand later. That's the method."

### Struggle 2: Copy-Paste Trap — Just Copying from impl_example.py

**Signs:**
- Suspicious similarity between their code and reference implementation
- No iteration (they didn't run tests in between)
- When asked to explain a function, they struggle
- Code appears on first try (no debugging visible)

**Root Cause:** Student thinks the goal is passing tests, not learning.

**Intervention (Gentle, Not Accusatory):**
- Don't say "You cheated"
- Instead say: "I notice your code looks very similar to the reference implementation. Did you really type this yourself, or did you just copy it? I'm asking because... the goal here isn't to make tests pass. It's to *understand* what each line does."
- Then ask: "Can you explain what this line does? Why is it there?"
- If they can't explain, say: "That's okay. Let's go back and understand it. Delete this and type it again, but this time, after each line, ask yourself: what's this doing? Why do I need it?"
- **Key phrase:** "Understanding is the goal, not just passing tests. Type it yourself so you own it."

### Struggle 3: Black Box Approach — Running Code Without Understanding

**Signs:**
- Student writes a SQL query but can't explain what it does
- Copies window function syntax they don't understand
- Says "It works" when test passes, but can't debug if something breaks

**Root Cause:** Student in a hurry, wants quick success, skips the "why" step.

**Intervention:**
- Before accepting a solution that "works," ask: "Explain this query to me. What does `ROW_NUMBER()` do? Why `PARTITION BY category`?"
- If they struggle: "Let's ask AI to explain it to you, not just write it for you. Ask: 'Why would ROW_NUMBER() with PARTITION BY category find the max expense per category?'"
- Have them explain back to you once they understand
- **Key phrase:** "We need to understand the 'why,' not just make the test pass."

### Struggle 4: Test Confusion — Not Understanding Test Failures

**Signs:**
- Test fails, student looks panicked or gives up
- Doesn't read the error message
- Makes random changes to code hoping to fix it
- Says "I don't know why it's failing"

**Root Cause:** Student hasn't been taught how to read error messages; tests seem magical/scary.

**Intervention:**
- Sit next to them when they run the test
- Point to the error message: "Read this. What's it telling you?"
- Model the thought process: "The test says it expected a dictionary but got None. That means our function is returning None. Why? Because we haven't implemented it yet. That's our next step."
- Have them read the test code and the error together: "The test is literally telling you what you forgot."
- Run through once more with their next error
- **Key phrase:** "Error messages are your friend. They tell you exactly what's wrong. Let's read it together."

### Struggle 5: Quitting Too Early — "I Should Already Know This"

**Signs:**
- Student expresses frustration: "I feel stupid" or "This is too hard"
- Suggests giving up: "Maybe this isn't for me"
- Compares themselves to others: "Everyone else probably knows this"
- Overwhelmed by unfamiliar terminology

**Root Cause:** Imposter syndrome + unfamiliar context. Student internalizes confusion as personal failure.

**Intervention (Emotional, Not Technical):**
- Normalize the struggle: "Everyone who's a good programmer faces unfamiliar tech. They don't all know Python. They know HOW to learn. That's what we're practicing."
- Point out progress: "Look at what you did: you read the error, asked AI, understood the answer, fixed it. You just did what real programmers do every day."
- Reframe the timeline: "We're not in a race. We're building a skill that takes a lifetime. This 30-minute exercise is one data point. You're doing great."
- **Key phrase:** "Feeling stuck means you're learning. That's supposed to happen."

---

## Teaching Tips

- **Normalize "I don't know"** — Use it yourself: "I don't remember Polars syntax either. Let me ask AI." Model the behavior you want.

- **Celebrate iteration, not perfection** — When a student gets a test wrong, fixes it, and passes: "That's real programming. That's not a failure—that's learning."

- **Use the divide-and-conquer as a thinking tool** — When a student is stuck, ask: "Which of the 4 steps are we on? What's the next step?" Break it down.

- **Make the 4-step decomposition visible** — Physically draw it or have student write it on paper/whiteboard. Ownership matters.

- **Ask "why" more than "how"** — When student implements something, don't ask "how did you do it?" Ask "why did that work? What would happen if you changed X?"

- **Don't fix code; ask questions** — Instead of "you forgot to add .collect()", ask "why did the error say LazyFrame? What do we need to do?"

- **Tie back to the learning goal frequently** — Remind them: "This isn't about learning Polars. It's about learning to work with AI on unfamiliar problems. Notice what you just did: asked, iterated, understood. That's the skill."

- **Create safe space for questions** — Some students won't ask unless you explicitly say: "Ask anything. There's no stupid question here. If you're confused, that's the whole point of having an AI to help."

- **Check understanding through explanation** — Have them explain their code to you or another student. If they can't explain it, they don't understand it yet.

- **Encourage peer explanation** — If two students are learning together, have them explain to each other. Teaching each other is the best way to solidify understanding.

---

## Assessment Ideas

### During the Exercise

**Formative checks (not grades, just understanding):**

1. **After divide-and-conquer step:** "Tell me the 4 steps we broke this into. Why did we break it that way?"
   - Look for: Student owns the decomposition, can explain why each step is necessary

2. **After each exercise:** "Run the test. Tell me what passed and why. What do you think the test is checking?"
   - Look for: Student reads and interprets the test output, understands the connection between code and test

3. **During Exercise 5 (hardest one):** "Explain what this SQL query does. What would happen if you removed PARTITION BY?"
   - Look for: Student understands the logic, not just copying syntax

4. **Use the "explain back" technique:** "I'm listening. Tell me what you did and why."
   - Look for: Confidence, understanding, ability to articulate the thinking

### Final Assessment (Post-Exercise)

**Grading Rubric (match TICKET.md criteria):**

1. **Implementation Quality** — Code is implemented, not hardcoded, not directly copy-pasted
   - Check: Open impl.py, compare with impl_example.py, look for differences (especially variable names, comments, personal style choices)
   - If identical: Gently prompt "Did you really type this? Remember, the goal is learning."

2. **All Tests Pass** — Run `mise run test`, all 3 tests pass
   - Check: Full test output, all green
   - If failure: Have student debug with AI, iterate

3. **Learning & Understanding** — Student can explain:
   - The method they used to collaborate with AI
   - How the 4-step breakdown helped
   - What they'd do differently next time they see an unfamiliar tool
   - Check: Have a 3-minute conversation about these points

### Reflection Questions for Your One-on-One Debrief

1. "Walk me through your collaboration with AI. How did you decide what to ask?"
2. "Which exercise was hardest? What made it hard?"
3. "Looking back, would you approach it differently knowing what you know now?"
4. "If you encountered a new Python library next week, what would you do? How is that different from what you did here?"
5. "What's one thing you learned about learning from this exercise?"

**Listen for signs of transfer:** If they say things like "I'd ask AI first," "I'd break it down," "I'd run tests after each step," they've internalized the method. That's the win.

---

## Why This Teaching Approach Works

**The balance:** This approach gives just enough scaffolding (the 4 steps, the tests, the mindset frame) without overwhelming. Then it lets students **do** the work—reading errors, asking AI, iterating. The doing is where learning happens.

**The psychology:** By normalizing confusion and celebrating iteration, we flip the script from "I should know this" to "I'm learning how to learn." That mindset shift is the real outcome.

**The transfer:** A student who leaves this exercise thinking "I can handle unfamiliar tech if I break it down and iterate" has learned something worth far more than knowing Polars syntax.