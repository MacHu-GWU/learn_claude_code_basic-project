# Editing Long Messages

> Learn how to compose and edit long messages efficiently using a markdown file instead of the chat input box.

## Why This Matters

Imagine you're working on a complex task. You need to write a detailed prompt to Claude Code — maybe referencing multiple files, explaining context, or listing several requirements. You start typing in the chat input box...

Then you realize you made a typo three lines up. Or you want to reorganize your thoughts. Or you accidentally pressed Enter and sent an incomplete message.

The chat input box is great for quick questions, but it's terrible for composing longer, thoughtful prompts. There's no easy way to scroll, edit, or organize your thoughts.

The solution? Write your messages in a markdown file first, then copy and paste into Claude Code. This gives you the full power of your editor — syntax highlighting, easy navigation, undo/redo, and the ability to save your prompts for reference.

## The Message File Approach

Instead of typing directly in Claude Code, create a file called `.claude/claude-code-messages.md` in your project. This file serves as your "drafting space" for prompts.

The file is excluded from git (via `.gitignore`), so it won't clutter your repository. It's purely for your convenience.

Here's how it works:

1. Write your message in the file
2. Copy the message
3. Paste it into Claude Code
4. Claude responds
5. When you have another message, write it in the file and repeat

You can keep a history of your prompts by separating them with horizontal lines (`----`). This creates a personal log of what you've asked, which can be helpful for reference.

## Writing from Top to Bottom

Here's a practical tip that will save you time: **write new messages at the top of the file**.

Why? When you open a file in most editors, the cursor starts at the top. If you keep your latest message at the top, you can quickly see what you last asked without scrolling. Your conversation history reads naturally — newest first, oldest last.

Your file structure should look like this:

```markdown
------------------------------------------------------------------------------

------------------------------------------------------------------------------

------------------------------------------------------------------------------
(your latest message here - write new ones above this line)
------------------------------------------------------------------------------
(newer message here)
------------------------------------------------------------------------------
(older message here)
------------------------------------------------------------------------------
```

## Referencing Files in Your Messages

One of the most common reasons to use the message file is when you need to reference specific files in your project.

When you tell Claude Code to look at a file, you should use the **absolute path** — the full path from the root of your filesystem. This removes any ambiguity about which file you mean.

In GitHub Codespaces or VS Code, getting the absolute path is easy:

1. Find the file in the Explorer panel (left sidebar)
2. Right-click on the file name
3. Select "Copy Path" (not "Copy Relative Path")

You'll get something like:

```
/workspaces/my-project/src/config.json
```

Then in your message, you can write:

```
Please review the configuration in /workspaces/my-project/src/config.json
and suggest improvements.
```

This is much easier to do in a file editor where you can see what you're typing, rather than in a small chat input box.

## Clearing the Chat Input

Sometimes you start typing in Claude Code's chat input and want to start over. Here's what you need to know:

- Press **Ctrl+C once** to clear the current input
- Press **Ctrl+C twice** to exit Claude Code entirely

This is useful when you've pasted something and want to clear it, or when you changed your mind about what to ask.

## Hands-on Exercise

Let's practice what you've learned.

**Your task:** Use the message file to ask Claude Code a question.

First, open `.claude/claude-code-messages-example.md` in your editor. You'll see it already has a sample message at the bottom:

```
Help me understand what I need to know from README.md
```

Copy this line and paste it into Claude Code. Watch how Claude reads the README and summarizes the key points for you.

Now try writing your own message in the file. Add a new section at the bottom (below a `----` line) and write a question about any file in this project. Copy and paste it into Claude Code.

## Common Issues

**Accidentally sent an incomplete message**

This is exactly why we use the message file approach. If you compose in the file first, you can review and edit before sending. For now, just continue the conversation — Claude will understand if you add more context.

**Not sure which path to use**

Always use "Copy Path" (absolute path), not "Copy Relative Path". The absolute path starts from the root (`/`) and includes the full directory structure.

**File changes aren't reflected**

Make sure you save the file before copying. Most editors show an unsaved indicator (like a dot) in the tab.

## Mentor's Note: Thoughtful Communication

When I first started using AI assistants, I would type questions stream-of-consciousness style — just thinking out loud. The results were hit or miss.

Over time, I learned that the quality of AI responses directly correlates with the quality of your prompts. Taking a moment to compose your thoughts, organize your request, and provide clear context makes a huge difference.

The message file approach isn't just about convenience — it's about building a habit of thoughtful communication. This skill transfers to everything: writing emails, documentation, code comments, and even conversations with colleagues.

The few seconds you spend organizing your thoughts often save minutes of back-and-forth clarification.

## Quick Reference

- Message file location: `.claude/claude-code-messages.md`
- Separator between messages: `----` (horizontal line)
- Copy file path: Right-click → "Copy Path" in VS Code/Codespaces
- Clear chat input: Ctrl+C (once to clear, twice to exit)
- Write new messages at the top of the file

## Further Reading

- [Prompt Engineering Best Practices](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering)
