# Managing Sessions

> Learn how Claude Code sessions work and how to manage conversation history across multiple conversations.

## Why This Matters

Imagine you're working on a project and chatting with Claude Code about it. You share context — file paths, requirements, your preferences. Claude understands everything.

Then you close Claude Code and come back tomorrow. You ask Claude the same question... and it has no idea what you were talking about.

This isn't a bug — it's how sessions work. Each time you start Claude Code, you get a fresh conversation. That's good for keeping things organized, but what if you want to continue a previous conversation or review what you discussed before?

That's where session management comes in. Claude Code lets you:
- **Resume** a previous session (continue where you left off)
- **Browse** past sessions (find and replay old conversations)
- **Keep organized** conversation history

## What Are Sessions?

A **session** is a single conversation with Claude Code. It's a complete record of everything you said and everything Claude responded with.

Think of it like notebooks:
- Each time you start Claude Code, you open a **new notebook**
- Everything in that conversation goes in that notebook
- When you exit, the notebook is saved
- Next time you start Claude Code, you get a **blank notebook** (new session)

This separation is useful because:
1. **Organization** — Each project/task can have its own session
2. **Privacy** — Sessions are isolated from each other
3. **History** — You can go back to any past session anytime

## Understanding Session Persistence

By default, Claude Code works like this:

**Session 1:**
```
                        Let me tell you: my favorite food is pizza
Got it.

                        What's my favorite food?
Your favorite food is pizza.
(Exit Claude Code - Session saved)
```

**Session 2:** (New session, fresh start)
```
                        What's my favorite food?
I don't know what your favorite food is. We haven't discussed this.
```

Claude has no memory of Session 1 during Session 2. This is intentional — each session is independent. But Claude Code saves every session. You can access them later using session commands.

## Session Commands

Claude Code provides two commands to manage sessions:

### `-c` — Continue Previous Session

```bash
claude -c
```

This **continues** the last session you were in. All the context from your previous conversation comes back. It's like opening the same notebook you had before.

### `-r` — Resume from Session History

```bash
claude -r
```

This shows you a list of all your past sessions. You can pick which one you want to resume. It's like browsing your notebook collection and picking the one you want to open.

## Hands-on Exercise 1: Understanding Session Isolation

Let's learn how sessions work by experiencing the isolation.

**Part A: Create context in a session**

1. Start Claude Code normally: `claude`
2. Tell Claude about your preferences: `Let me tell you: my favorite food is cheese burger`
3. Verify Claude remembers: Ask `What's my favorite food?`
4. Claude should answer: "Your favorite food is cheese burger"

**Part B: Exit and start fresh**

5. Exit Claude Code (Ctrl+C twice)
6. Start Claude Code again normally: `claude`
7. Ask the same question: `What's my favorite food?`
8. Claude responds: "I don't know what your favorite food is"

**What happened?**

You created two separate sessions. Session 1 had your food preference. Session 2 started fresh with no context. The information wasn't lost — it's stored — but Session 2 can't see it because they're separate conversations.

This is why managing sessions matters. Without tools to resume or review, you'd lose important context.

## Hands-on Exercise 2: Resuming with `-c`

Now let's use the `-c` flag to continue a previous session.

**Part A: Create a new session with context**

1. Start Claude Code: `claude`
2. Tell Claude something: `Let me tell you my favorite programming language is Python`
3. Exit Claude Code

**Part B: Resume the session with -c**

4. Run: `claude -c`
5. Claude Code should show: "Resuming session..." or similar
6. Ask a question: `What programming language do I like?`
7. Claude responds: "Your favorite programming language is Python" (remembers!)

**What happened?**

The `-c` flag resumed your last session. All the context from that conversation came back. It's like reopening the same notebook instead of getting a new one.

## Hands-on Exercise 3: Browsing Sessions with `-r`

Now let's use the `-r` flag to select from multiple past sessions.

**Setup (if you haven't done Exercises 1 & 2):**
- Make sure you have at least 2 past sessions with different context
- Exercise 1 has one session about food
- Exercise 2 has one session about programming languages

**The Practice:**

1. Exit Claude Code (if you're in one)
2. Run: `claude -r`
3. You'll see a list of past sessions (with timestamps or summaries)
4. Select one of your earlier sessions (e.g., the one about food or programming)
5. You're now in that session — all context restored
6. Ask: `What did we discuss?` or reference the information you shared
7. Claude remembers the context from that specific session

**What happened?**

The `-r` flag let you browse your entire session history and pick which one to resume. This is powerful when you have many conversations and want to continue a specific one, not just the most recent.

## Quick Reference

- **New session:** `claude` (default behavior)
- **Continue last session:** `claude -c`
- **Browse and pick a session:** `claude -r`
- **Session storage:** Sessions are automatically saved; you don't need to do anything
- **Context isolation:** Each session starts fresh unless you resume
- **Alternative to -c:** `/clear` clears the current session's context but doesn't create a new session file

## Common Scenarios

**Scenario 1: You're working on a project and want to come back to it tomorrow**

Use `claude -c` to resume where you left off. All your context is there.

**Scenario 2: You've had many conversations and can't remember which one had important information**

Use `claude -r` to browse sessions and find the one you need.

**Scenario 3: You want to start completely fresh without the previous context, but keep the old session saved**

Just start Claude Code normally with `claude`. A new session is created, and your old one is preserved for later.

## Mentor's Note: Organizing Your Thinking

Early in my career, I'd lose important conversations. "Wait, which session did I discuss the architecture in?" or "What were the requirements we agreed on?"

I learned that session management is like project management for your conversations. Each focused conversation gets its own session. When you come back to it, everything is there.

The real skill is knowing when to start a new session. Here's my pattern:
- **New session for each project/task** — Different goals deserve different notebooks
- **Don't switch sessions mid-task** — Finish your current session before starting a new one
- **Review old sessions when stuck** — Look back at how you solved similar problems

Over time, your session history becomes a personal knowledge base. You can trace your thinking, see how you approach problems, and even learn from mistakes.

## Further Reading

- [Claude Code Documentation](https://code.claude.com/docs)
- [Workflow Best Practices](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering)
