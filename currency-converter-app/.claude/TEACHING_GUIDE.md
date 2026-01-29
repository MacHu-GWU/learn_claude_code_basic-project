# Teaching Guide: Currency Converter App

## Overview

This mini-project teaches **"vibe coding"** — the art of communicating clearly with AI to get high-quality results. It's NOT about learning Python or Streamlit syntax; it's about understanding why **clarity of thought drives output quality**.

Students will experience a powerful progression: building the same app three different ways (vague request → clear spec → interview technique) and observing how dramatically the quality changes based on how well they communicate what they want.

**Core insight:** The bottleneck in AI-assisted development isn't "how to implement"—it's "what to implement." Students learn to clarify their ideas through conversation before asking AI to build.

---

## Learning Outcomes

By the end of this lesson, students will:

1. **Understand the clarity-quality relationship** — vague input produces unpredictable output; clear input produces precise output
2. **Experience three different approaches** — quick experiment, following a spec, using the interview technique
3. **Learn the interview technique** — how to use AI to clarify their own ideas when they don't know what they want
4. **Use Claude Code effectively** — including practical tips like `claude -c` (continue) and `claude -r` (resume) to not lose work
5. **Recognize that clarity can be discovered** — you don't need perfect requirements upfront; you can discover them through conversation

---

## Concept Sequence: What to Teach First, Second, etc.

### Phase 1: Set Expectations & See the Target (5 min)

**Before students start:**

1. Run `streamlit run app-example.py` together so they see what "done well" looks like
2. Point out the key features: clean UI, proper error handling, correct currencies, instant feedback
3. Say: "This is the reference implementation. Keep this in mind as you go through the exercises."

**Why:** Students need a visual anchor for "quality." Without it, they won't know if their Exercise 1 result is mediocre or not.

### Phase 2: Exercise 1 — The Vague Approach (10 min)

**Guide them through:**

1. Start a fresh Claude session: `claude`
2. Give a vague prompt: "I need a currency converter tool. Help me build it."
3. Let Claude ask questions or make assumptions
4. Have them run the resulting app

**Teaching moves:**

- Don't interrupt — let them experience the unpredictability
- After it works, ask: "How does this compare to `app-example.py`? What's different?"
- They'll notice: maybe wrong currencies, missing features, different UI approach, etc.
- Say: "This isn't Claude's fault. Claude built exactly what you asked for — which wasn't very specific."

**Key insight to plant:** Input clarity → Output quality

### Phase 3: Exercise 2 — The Clear Spec Approach (15 min)

**Before they start:**

1. Have them review `app-spec.md`
2. Ask: "What makes this requirement document clear? Point out specific details."
3. They should notice: currencies listed, UI elements defined, conversion formula given, error handling specified

**Guide them through:**

1. Start a new session: `claude` (or `/clear` if same session)
2. Use the prompt: "READ app-spec.md to understand the currency converter app requirement, then write the python app at app.py, and teach me how to run it."
3. Watch Claude reference the spec and build to match it exactly
4. Have them run the app

**Teaching moves:**

- This is the "aha moment" — the result is dramatically better and more predictable
- Ask: "How is this different from Exercise 1? What made the difference?"
- They should recognize: detailed requirements → better implementation
- Say: "Notice what didn't change — Claude's capability is the same. What changed is the clarity of your request."

**Key insight to solidify:** Good requirements aren't complicated—they're just specific.

### Phase 4: Exercise 3 — The Interview Technique (20 min)

**Set it up:**

1. Start a new session: `claude`
2. Explain: "Most people can't write a clear spec like `app-spec.md` from scratch. That's normal! But you don't need to. Let AI help you discover what you want."
3. Use this prompt:

```
I want to build a currency converter app that converts amounts between different currencies based on exchange rates. I want to build it in Python and run it locally.

Please help me figure out the detailed spec by asking me questions to define this requirement in detail. After a few rounds of Q&A (like an interview), write my final decisions to app-spec.md for future reference.
```

4. Have them answer Claude's questions naturally
5. Review the generated spec together

**Teaching moves:**

- This reveals the true superpower: students can use AI twice—first to clarify their thinking, then to implement
- Ask: "Did Claude ask questions you wouldn't have thought of?"
- Ask: "Is the generated spec close to the official one? Where are the differences?"
- Emphasize: "You just created clear requirements without knowing how to write one upfront!"

**Key insight to reveal:** Clarity can be discovered through conversation.

### Phase 5: Reflection & Comparison (10 min)

**Have them compare:**

1. Run all three versions side-by-side (Exercise 1, Exercise 2, Exercise 3)
2. Show the apps running and compare:
   - UI quality
   - Currency selection
   - Error handling
   - Responsiveness

**Debrief questions:**

- "Why did Exercise 2 match `app-example.py` so closely?"
- "How was Exercise 3's generated spec different from the official one? Why?"
- "Which exercise would you use if you were building something for a real user?"
- "What's the pattern you see here?" (→ Input quality determines output quality)

**Final insight:** Clear communication is more valuable than coding syntax in the age of AI.

---

## Concept Map

```
VIBE CODING (Core Skill)
│
├─ Clarity of Thought
│  └─ Can you describe what you want?
│
├─ Clear Communication
│  ├─ Written (specs, detailed prompts)
│  └─ Conversational (interview technique)
│
└─ Input → Output Relationship
   └─ Vague input → Unpredictable output
   └─ Clear input → Precise output
   └─ Iterative discovery → Personalized output

SUPPORTING SKILLS
├─ Using Claude Code CLI effectively
│  ├─ `claude` — start session
│  ├─ `/clear` — reset conversation
│  ├─ `claude -c` — continue last session
│  └─ `claude -r` — resume from history
│
└─ Reading & Understanding Requirements
   └─ What makes `app-spec.md` effective?
```

---

## Common Student Struggles & Interventions

### Struggle 1: "My Exercise 1 result works fine. Why do I need to do Exercise 2?"

**Why it happens:** Students see functional output and don't recognize mediocrity.

**Intervention:**

1. Show them `app-example.py` running
2. Run their Exercise 1 app next to it
3. Ask: "Which one would you want to use? Why?"
4. Point out specifics: UI polish, error handling, currency support
5. Say: "A working app and a *well-designed* app are different things. Exercise 2 teaches you the difference."

### Struggle 2: "I lost my work by pressing Ctrl+C. Now I have to start over."

**Why it happens:** Students don't know Claude Code remembers conversation history.

**Intervention:**

1. Teach them immediately: `claude -c` continues the last session (same context)
2. Teach them: `claude -r` opens a menu to pick from recent sessions
3. Say: "Claude Code remembers your conversations. You don't lose anything by pressing Ctrl+C. Just use `-c` or `-r` to get back."
4. Emphasize: "This is especially useful if you're exploring and want to go back to a previous version."

### Struggle 3: "I don't know what I want. I can't write a spec like `app-spec.md`."

**Why it happens:** Most people can't write clear requirements from scratch.

**Intervention:**

1. Normalize it: "That's totally normal. Most people can't write specs."
2. Point them to Exercise 3: "You don't need to know upfront. Use the interview technique."
3. Walk through Exercise 3 with them if they're stuck
4. Show: "Claude asked questions you wouldn't ask yourself. That's the power of this technique."

### Struggle 4: "Exercise 1 gave me a CLI app but I wanted a web app. Whose fault is that?"

**Why it happens:** Students blame AI instead of recognizing unclear communication.

**Intervention:**

1. Reference the Mentor's Note in README: "AI is like a mirror. It reflects the clarity of your thinking."
2. Ask: "Did you tell Claude you wanted a web UI? Did you mention Streamlit? Did you describe what the interface should look like?"
3. Say: "Claude made reasonable assumptions based on what you told it. The lesson here isn't 'AI is broken'—it's 'clarity matters.'"
4. Show Exercise 2: "When you're specific, Claude delivers exactly what you describe."

### Struggle 5: "I did all three exercises but I don't understand what I learned."

**Why it happens:** Students completed tasks without reflecting on the pattern.

**Intervention:**

1. Force the comparison: "Let's run all three versions at the same time. What do you notice?"
2. Ask directly: "In Exercise 1, your request was ___. In Exercise 2, your request was ___. How different were they?"
3. Point to the pattern: "You gave Claude less information in Exercise 1. Claude had to guess. In Exercise 2, you were specific. Claude delivered exactly that."
4. Generalize: "This pattern applies to everything you build with AI. Clearer input → Better output. Always."

---

## Teaching Tips

### The "Aha Moment"

The biggest learning happens **between Exercise 1 and Exercise 2**, when they see the dramatic quality difference. Don't rush this. Take time to point out specifics:

- "Look at the error handling. Exercise 2 handles this case, Exercise 1 doesn't."
- "See how the UI is organized? Exercise 2 is cleaner."
- "The conversion result shows more precision in Exercise 2."

This is where the insight from intellectual understanding into felt understanding.

### Use `app-example.py` as a Visual Reference

Before and after each exercise, have them run:

```bash
streamlit run app-example.py
```

Use it as the "north star" for quality. Questions like "How close is your version to this?" are much more concrete than "Is your app good?"

### The Interview Technique is a Superpower

Don't gloss over Exercise 3. This is where students discover they can use AI to think. Point out:

- "Claude asked about error handling. Did you think about that?"
- "Claude asked about currency selection. You didn't mention it, but now your spec does."
- "The generated spec is YOUR spec now. Claude helped you clarify, but you made the decisions."

This reframes AI from "tool that implements" to "tool that helps you think."

### Session Management Matters

Teach `claude -c` and `claude -r` early:

- Show: "You pressed Ctrl+C. Your work isn't lost."
- Demo: "Look, `claude -c` got us back to where we were."
- Explain: "This is why you can experiment. You can always go back."

This reduces friction and lets students explore without fear.

### Don't Teach Python or Streamlit

Explicitly tell students: "You're not learning Python today. You're learning how to communicate with AI. Python and Streamlit are just the tools Claude uses—not the lesson."

If students ask about the code in `app.py`, redirect: "Sure, Claude can explain that. But for this lesson, focus on the bigger pattern: clarity → quality."

---

## Common Misconceptions to Address

### "AI can read my mind if I ask nicely"

**Wrong.** AI can only work with what you explicitly tell it. Politeness doesn't make vague requests precise.

**Correct:** "AI is very good at what you ask it to do. Your job is to ask clearly."

### "Good requirements require programming knowledge"

**Wrong.** You don't need to know how to code to describe what you want.

**Correct:** "Good requirements are just specific. They describe what the user sees and does. You can be specific without knowing code."

### "If the result isn't what I want, the AI is bad"

**Wrong.** The AI didn't fail; the communication was unclear.

**Correct:** "The AI is reflecting back the clarity (or confusion) of your request. Better input = better output."

### "I can only ask Claude for what I already know I want"

**Wrong.** You can ask Claude to help you figure out what you want.

**Correct:** "The interview technique (Exercise 3) is for exactly this. You don't need clarity upfront—you can discover it through conversation."

---

## Assessment Ideas

### Quick Checks (During the Lesson)

1. After Exercise 1: "Compare your result to `app-example.py`. What's the same? What's different?"
2. After Exercise 2: "Why do you think Exercise 2 matched the spec so well? What changed?"
3. After Exercise 3: "Looking at Claude's generated spec, which questions surprised you?"

### Deeper Assessment (End of Lesson)

1. **Reflection Write:** "In 3-4 sentences, explain the relationship between clarity and output quality. Use examples from the three exercises."

2. **Transfer Task:** "You want to build a simple todo list app. Would you start with Exercise 1, 2, or 3 approach? Why?"

3. **Comparison:** "Compare the official `app-spec.md` with the one Claude generated in Exercise 3. Where are they the same? Where are they different? Why?"

4. **Self-Assessment:**
   - Can I identify when my request to AI was too vague?
   - Do I know how to use `claude -c` and `claude -r` to recover work?
   - Can I explain why Exercise 2's result was better than Exercise 1's?
   - Do I understand the interview technique and when to use it?

---

## Troubleshooting

### "Students finish Exercise 1 and want to stop"

Push them forward: "The real learning is in the comparison. Do Exercise 2 and then we'll look at them side-by-side."

### "Students are confused about which session to use for which exercise"

Start fresh with `/clear` or `claude` for each exercise. The goal is to show three different approaches, so mixing contexts defeats the purpose. Make it explicit: "We're starting fresh now to compare."

### "Students' Exercise 3 generated spec is very different from the official one"

This is fine! Point it out: "See? You made different choices than the official spec. That's the point—your spec reflects what YOU want. Both are valid. This shows why the interview technique is powerful."

### "Students ask technical questions about the code"

Redirect gently: "Claude can explain that. For now, focus on the lesson: clarity of communication. The code is just an implementation detail."

---

## Extensions & Next Steps

If students finish early or want to go deeper:

1. **Exercise 4:** "Now build your own small app using the three-approach workflow. What did you learn?"

2. **Spec Analysis:** "Read `app-spec.md` and identify: What makes this spec clear? What would make it clearer?"

3. **Interview Retrospective:** "In Exercise 3, which questions that Claude asked were most helpful? Why?"

4. **Real-World Application:** "Think of a project you want to build. Draft a spec for it. Use the interview technique if you get stuck."

---

## Key Takeaways for Teachers

- **The lesson is about communication, not code.** Don't get pulled into Python/Streamlit explanations.
- **The aha moment is Exercise 1 → 2.** Spend time on the comparison.
- **Session management matters.** Teach `claude -c` and `claude -r` early so students aren't afraid to experiment.
- **The interview technique is the superpower.** Make sure students feel how powerful it is to have AI help them think.
- **Clarity can be discovered.** Emphasize that students don't need perfect upfront knowledge; they can discover clarity through conversation.

---

## Resources for Teachers

- **For context on vibe coding:** See README.md "Mentor's Note" section
- **For reference implementation:** Run `streamlit run app-example.py`
- **For spec analysis:** See `app-spec.md` for examples of clear requirements
- **For technical setup:** See `.claude/PROJECT.md` for environment details
