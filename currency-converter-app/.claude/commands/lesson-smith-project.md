---
description: Generate or update PROJECT.md (project overview) using lesson-smith skill
---

Use the `lesson-smith` agent skill to craft the **PROJECT.md** file.

**Context to read first:**
- Existing `.claude/PROJECT.md` - if updating
- Project files to understand structure and setup

**User request:** $ARGUMENTS

**Output requirements:**
- Follow the PROJECT.md template defined in lesson-smith skill
- Include development environment details
- Include key commands table
- All content in English
- Place file at: `.claude/PROJECT.md`
