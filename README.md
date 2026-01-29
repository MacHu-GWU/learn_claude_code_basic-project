# Understanding Context

> Learn what context is, why it matters, and how to manage it effectively to get better results from Claude Code.

## Why This Matters

Imagine you're chatting with Claude Code about designing a nutrition plan. You discuss different foods, their health benefits, calorie counts, and make decisions together. The conversation spans 20+ exchanges.

Then, in the same session, you ask Claude a completely unrelated question: "How do I debug this Python error?"

You notice Claude's answer feels... off. Less detailed. Less helpful than usual. It's not that Claude got dumber. It's that Claude's attention is being divided.

Every word you type, every response Claude gives, every file you reference — they all add up. At some point, Claude has so much information to juggle that the really important stuff gets buried.

This is about **context** — the total information Claude is working with at any moment.

## What Is Context?

**Context** is everything Claude can "see" right now:

- Your previous questions in this conversation
- Claude's previous answers
- Files you've asked Claude to read
- System prompts (from slash commands)
- Any text you've pasted

Think of it like your brain's working memory. You can hold a lot of information in your head, but there's a limit. If you keep adding more and more, something gets forgotten.

## The Context Window

Claude has a **context window** — the maximum amount of information it can process at once.

Think of it like RAM on a computer:
- Limited size
- Everything you're actively using takes up space
- When it fills up, performance degrades

Claude's context window is large (200,000 tokens), but it's not infinite. And each conversation uses it up.

## What Consumes Context?

Everything in your session counts toward your context:

```
+--------------------------------------+
| System Prompt (slash commands)       | ~500 tokens
+--------------------------------------+
| Your first question                  | ~50 tokens
| Claude's first answer                | ~200 tokens
+--------------------------------------+
| Your second question                 | ~60 tokens
| Claude's second answer               | ~180 tokens
+--------------------------------------+
| File you asked Claude to read        | ~1,000 tokens
+--------------------------------------+
| Your third question                  | ~70 tokens
| Claude's third answer                | ~220 tokens
+--------------------------------------+
| Total in use: ~2,280 tokens          |
| Remaining: ~197,720 tokens (98%)     |
+--------------------------------------+
```

Every exchange adds up. Small contributions become big problems.

## Problems with Long Context

### Problem 1: Context Pressure and Compression

When your context gets close to the limit, Claude automatically compresses the history. It tries to keep the most important information and condense the rest.

But here's the catch: **Claude doesn't know what's important to you.**

It might compress away the one crucial detail you needed. The result? Claude gives you incomplete answers because it forgot key context.

### Problem 2: Token Waste

Each exchange costs tokens. If your session is huge but your new question is unrelated to the old discussion, you're paying the price for information you're not using.

Example:
- You spent 10,000 tokens discussing database design
- Now you ask about CSS styling
- Claude still has to process all 10,000 tokens from the database discussion
- Cost: ~10,000 tokens for context that's irrelevant

That's like paying to have someone read you the entire history book when you only needed one chapter.

## Why Managing Sessions Matters

This is why the **Managing Sessions** tutorial is important. Sessions let you:

- **Start fresh** — New session = clean context
- **Stay focused** — One conversation = one problem
- **Recover when needed** — Use `-c` or `-r` to go back if you need old context

Sessions are your tool for managing context effectively.

## The Solution: Documentation Strategy

Here's the key insight: **Don't keep context — extract it.**

Instead of relying on your session history, create a document:

1. Have a focused conversation with Claude
2. When done, ask Claude to summarize the key points into a **concise document**
3. Save that document to your project
4. In future sessions, reference the document instead of relying on history

Example:
```
You: Based on our discussion about nutrition, I think the key points are:
- Low-calorie options that taste good
- Easy preparation methods
- My chosen foods to try

Please create a concise markdown document (300-500 words) summarizing the key
recommendations and the foods I decided to try. Format it nicely so I can save
it as docs/nutrition-plan.md.

Claude: [Generates concise summary markdown]
```

In the next session:
```
cat docs/nutrition-plan.md
[Continue with clean context, no history baggage]
```

## How Manual Context Compression Works

You can take control of compression instead of letting Claude do it automatically:

1. **Identify what matters** — Tell Claude: "Which parts of our discussion are most important?"
2. **Ask for condensing** — "Please write a 200-word summary focusing on [specific aspects]"
3. **Reference the summary** — In future sessions, just reference the document

Claude doesn't need to re-read everything. It can read the condensed version and stay focused.

## When You Need Long Context

Not every task requires a short context. Long context is valuable when:

- **Building complex systems** — You need the full architecture visible
- **Consistent narrative** — The story needs continuity (like writing a novel)
- **Debugging tangled problems** — You need to see all the code interactions
- **Collaborative design** — Multiple decisions depend on each other

In these cases, use a longer session. But even then, consider:
- Breaking it into focused phases (one session per phase)
- Maintaining a `docs/` folder with key decisions
- Periodically asking Claude to summarize progress

## Hands-on Exercise: Create Your First Documentation

Let's practice the documentation strategy in one complete exercise.

**The Task: Food Recommendations**

1. **Start a Claude Code session:** `claude`

2. **Have a casual conversation** (5-8 exchanges):
   - Ask: `I want to eat healthier. Can you recommend some low-calorie foods that taste good? I like [your food preferences].`
   - Ask follow-up questions about nutrition, taste, preparation
   - Discuss the recommendations
   - Make a decision about which foods to try

3. **Ask Claude to create documentation** (one complete prompt):
   ```
   Based on our discussion, I think the most important points are:
   - Low-calorie foods that actually taste good
   - Easy preparation methods
   - The specific foods I decided to try

   Please create a concise markdown document (300-500 words) that summarizes:
   1. The key food recommendations we discussed
   2. Why these foods are good choices
   3. The specific foods I chose to try

   Format it nicely because I'll save it as docs/my-nutrition-plan.md
   ```

4. **Copy Claude's response** and save it as `docs/my-nutrition-plan.md` in your project

5. **Send the document link to your mentor** as proof you completed the exercise

   Example: "I completed the exercise. Here's my documentation: docs/my-nutrition-plan.md"

**What you're practicing:**
- Having a meaningful conversation
- Recognizing when to convert history into a document
- Creating reusable, context-efficient documentation
- Preparing for a new session (old context is gone, but the document remains)

## Quick Reference

- **Context** — Everything Claude is currently processing
- **Context Window** — Maximum capacity (~200,000 tokens for Claude)
- **Context Pressure** — When context gets full, Claude compresses (risking information loss)
- **Session Management** — Keep conversations focused, use `-c` or `-r` to switch
- **Documentation** — Extract key points from conversations into reusable documents
- **Manual Compression** — Ask Claude to condense important information into concise summaries

## Mentor's Note: Building Sustainable Workflows

Early in my work with AI, I'd have these long, sprawling conversations. "I'll keep all this in context," I thought. Then I'd realize I couldn't remember what we decided, and Claude couldn't either — it was buried in 30,000 tokens of chat history.

I learned the hard way: **context is not memory. Documents are.**

The shift in thinking: Instead of asking "How do I keep this in context?", ask "How do I extract the value from this conversation into something I can reuse?"

It changed everything:
- Conversations became more focused
- I built a knowledge base of documented decisions
- New sessions were clean and fast
- Future me could reference past work without re-discussing it

The best engineers I know practice this ruthlessly. They don't accumulate context; they compress it. They don't rely on memory; they document systematically.

This one habit — converting conversations into documentation — will serve you in every tool, not just Claude Code.

## Further Reading

- [Claude Context Window Documentation](https://docs.anthropic.com/en/docs/about-claude/models/overview)
- [Prompt Engineering Best Practices](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering)
