---
description: Generate or update TICKET.md (actionable task card) using lesson-smith skill
---

Use the `lesson-smith` agent skill to craft the **TICKET.md** file.

**Context to read first:**
- `.claude/PROJECT.md` - for project overview
- `README.md` - for tutorial content reference
- Existing `TICKET.md` - if updating

**User request:** $ARGUMENTS

**Output requirements:**
- Follow the three-part structure: Objective, Actionable Items, Checklist
- Include GitHub link to the tutorial (project root directory)
- Use markdown task list format: `- [ ]`
- All content in English
- Place file at project root: `./TICKET.md`
