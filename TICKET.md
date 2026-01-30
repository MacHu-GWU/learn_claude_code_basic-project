# Learn to Use Slash Commands in Claude Code

## Objective

Learn how slash commands let you quickly execute pre-built prompt templates without typing long instructions every time. Understand that slash commands are autocompleted shortcuts for prompt templates.

Read the tutorial: [Using Slash Commands](https://github.com/MacHu-GWU/learn_claude_code_basic-project/tree/04-using-slash-commands/)

## Actionable Items

1. Read the tutorial in `README.md`
2. View the system prompt: `cat .claude/skills/convert-currency/SKILL.md`
3. **Practice 1 (Manual):** Copy the system prompt from the tutorial, replace `$ARGUMENTS` with "How much is $180 USD in Euro?", and paste into Claude Code
4. **Practice 2 (Slash Command):** Type `/convert-currency How much is $180 USD in Euro?` into Claude Code
5. Compare the two approaches — notice how slash commands reduce typing
6. Leave a comment on this ticket to let your mentor know you've completed it

**Estimated time:** 10-15 minutes

## Key Concepts to Understand

- Slash commands are **shortcuts for prompt templates**
- You don't need to memorize command names — use autocomplete (type `/` and search)
- The `$ARGUMENTS` placeholder gets replaced with your input
- This is 10% of what Skills can do; we'll explore more advanced features later

## Checklist

- [ ] **Read tutorial** - Finished reading the 04-using-slash-commands.md
- [ ] **View skill file** - Ran `cat .claude/skills/convert-currency/SKILL.md` and saw the system prompt
- [ ] **Practice 1 (Manual)** - Copied the system prompt and manually sent a currency conversion request to Claude Code
- [ ] **Practice 2 (Slash Command)** - Used `/convert-currency` command and compared it with Practice 1
- [ ] **Understand the benefit** - Know why slash commands are faster than typing full prompts
- [ ] **Notify mentor** - Left a comment saying "Done" or describing what you learned
