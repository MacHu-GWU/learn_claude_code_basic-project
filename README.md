# Using Slash Commands

> Learn how slash commands let you quickly execute pre-built prompt templates without typing long instructions every time.

## Why This Matters

Imagine you frequently need to do the same task — convert currencies, review code, write documentation, or analyze data. Each time, you'd need to paste the same detailed instructions to Claude Code.

What if you could just type a quick command and Claude would automatically use the right prompt?

That's what slash commands do. They're like shortcuts for your most common workflows — saving you time and reducing repetition.

## What Are Slash Commands?

Think of a slash command as a **prompt template shortcut**. It's a quick way to inject pre-written system prompts without typing them manually.

Here's the basic idea:

1. A slash command contains a **system prompt** — detailed instructions for Claude
2. You type `/command-name arguments` in Claude Code
3. Claude automatically loads the system prompt and processes your arguments

**Important:** You don't need to memorize slash commands. When you type `/` and start typing, Claude Code shows you a list of available commands. You can select one with just a few keystrokes.

## Understanding System Prompts with an Example

Let's look at a real example. The `convert-currency` command has a system prompt that teaches Claude how to convert between currencies.

You can view it by running:

```bash
cat .claude/skills/convert-currency/SKILL.md
```

This shows you the entire prompt, which includes:
- **Metadata** (name, description, argument-hint) — tells Claude Code about the command
- **System prompt** — the actual instructions Claude will follow

Here's what it looks like:

```
---
name: convert-currency
description: Convert currency amounts between USD, EUR, GBP, CNY, and JPY using current exchange rates.
argument-hint: "[amount] [from-currency] to [to-currency]"
---

You are a currency conversion assistant. Your task is to convert currency amounts accurately...
```

## The $ARGUMENTS Placeholder

The key concept in any system prompt is **$ARGUMENTS**. This is a placeholder that gets replaced with whatever you type after the command.

For example:
- Command: `/convert-currency How much is $180 USD in Euro?`
- `$ARGUMENTS` becomes: `How much is $180 USD in Euro?`

This is how the same command can handle different user inputs — the prompt adapts to whatever you pass in.

## Hands-on Exercise: Practice 1 (Manual Way)

Let's first do this the long way to understand what's happening.

Copy the text below (the system prompt part, NOT the metadata) and paste it into Claude Code with your question. Replace `$ARGUMENTS` with your actual question:

```
You are a currency conversion assistant. Your task is to convert currency amounts accurately using the provided exchange rates.

## Exchange Rates (base currency: USD)

- United States Dollar (USD): 1.00
- Euro (EUR, official common currency of the Eurozone): 0.92
- British Pound Sterling (GBP): 0.79
- Chinese Yuan Renminbi (CNY): 7.22
- Japanese Yen (JPY): 155.50

## Instructions

When the user asks: How much is $180 USD in Euro?

1. Parse the amount and currencies from the user's request
2. Convert the amount using the provided exchange rates:
   - If converting FROM USD: multiply the amount by the target currency rate
   - If converting TO USD: divide the amount by the source currency rate
   - If converting between non-USD currencies: convert to USD first, then to the target currency
3. Provide the result with clear formatting, showing:
   - The original amount and currency
   - The converted amount and currency
   - The calculation used (optional, for transparency)

## Example

Input: "$763.45 USD to EUR"
Output: $763.45 USD = 702.37 EUR (calculation: 763.45 × 0.92 = 702.374)

Be precise with decimal places and round to 2 decimal places for currency amounts.
```

**Your task:** Copy the above, paste into Claude Code, and see how Claude converts the currency.

This is what happens behind the scenes with slash commands — but you had to copy and paste manually.

## Hands-on Exercise: Practice 2 (Using Slash Command)

Now experience the convenience of a slash command.

In Claude Code, simply type:

```
/convert-currency How much is $180 USD in Euro?
```

Compare this to Practice 1:
- Practice 1: Copy a large block of text, paste it, run it (**lots of work**)
- Practice 2: Type a short command (**minimal effort**)

That's the power of slash commands — same result, fraction of the effort.

## How Slash Commands Work Behind the Scenes

When you type `/convert`, Claude Code:

1. Searches for all available commands matching "convert"
2. Shows you a list (in this case, `/convert-currency`)
3. You select it or finish typing the full name
4. Claude loads the system prompt from `.claude/skills/convert-currency/SKILL.md`
5. Your arguments get inserted where `$ARGUMENTS` appears
6. Claude processes the request with the complete context

This is why **you don't need to memorize command names**. Start typing and Claude Code's autocomplete helps you find what you need.

## Why We're Starting Simple

You might have heard the term "Skills" in Claude Code. That's the full power of this system. But slash commands are just 10% of what Skills can do. For now, think of them as convenient prompt shortcuts.

Later, we'll explore:
- Creating custom skills
- Building complex workflows
- Integrating with tools and APIs

But for today, focus on understanding: slash commands = faster access to your favorite prompts.

## Quick Reference

- **Autocomplete:** Type `/` to see available commands; you don't need to memorize them
- **Syntax:** `/command-name arguments`
- **View a skill:** `cat .claude/skills/[skill-name]/SKILL.md`
- **Concept:** Slash commands = prompt templates + quick access
- **Benefit:** Execute complex workflows with minimal typing

## Mentor's Note: Automating Repetitive Workflows

Early in my career, I'd write the same instructions over and over. "Here's how I want you to analyze code..." or "Please convert this using exchange rates..."

The repetition was tedious, but worse, it was error-prone. I'd forget details, make typos, or phrase things slightly differently each time.

Once I realized I could automate these workflows, everything changed. Instead of context-switching between typing instructions and waiting for responses, I could focus on the actual task.

This is a core principle of good engineering: **automate what repeats**. Slash commands are a simple way to practice this — and the habit transfers to everything you build.

## Further Reading

- [Claude Code Skills Documentation](https://code.claude.com/docs/en/skills)
- [Prompt Engineering Best Practices](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering)
