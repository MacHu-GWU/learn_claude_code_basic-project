# Learn to Manage Sessions

## Objective

Learn how Claude Code sessions work, how to manage conversation history, and how to use session commands (`-c` and `-r`) to resume or browse past conversations.

Read the tutorial: [Managing Sessions](https://github.com/MacHu-GWU/learn_claude_code_basic-project/tree/05-managing-sessions/)

## Actionable Items

1. Read the tutorial in `03-managing-sessions.md`
2. **Practice 1 (Understanding Session Isolation):**
   - Start Claude Code normally: `claude`
   - Tell Claude: `Let me tell you: my favorite food is cheese burger`
   - Ask: `What's my favorite food?` (Claude answers correctly)
   - Exit Claude Code
   - Start Claude Code again: `claude`
   - Ask: `What's my favorite food?` (Claude doesn't remember)
   - Reflect: Notice the session isolation

3. **Practice 2 (Resuming with -c):**
   - Start Claude Code: `claude`
   - Tell Claude: `Let me tell you my favorite programming language is Python`
   - Exit Claude Code
   - Resume with: `claude -c`
   - Ask: `What programming language do I like?` (Claude remembers)

4. **Practice 3 (Browsing with -r):**
   - Exit Claude Code
   - Browse sessions: `claude -r`
   - Select one of your past sessions
   - Verify the context is restored by asking a question about what you discussed

5. Leave a comment on this ticket to let your mentor know you've completed it

**Estimated time:** 15-20 minutes

## Key Concepts to Understand

- A **session** is a single conversation with all context saved
- Sessions are **isolated** by default (new session = blank slate)
- **`-c`** continues your last session
- **`-r`** lets you browse and pick from past sessions
- **`/clear`** clears context in the current session but doesn't create a new session file
- Sessions are stored automatically; you don't need to do anything to save them

## Checklist

- [ ] **Read tutorial** - Finished reading 03-managing-sessions.md
- [ ] **Practice 1** - Experienced session isolation (context lost after exit)
- [ ] **Practice 2** - Used `-c` to resume a session and verified context was restored
- [ ] **Practice 3** - Used `-r` to browse sessions and re-entered a past session
- [ ] **Understand the concept** - Know the difference between sessions and context clearing
- [ ] **Notify mentor** - Left a comment saying "Done" or describing what you learned
