---
description: Generate or update README.md (tutorial document) using lesson-smith skill
---

Use the `lesson-smith` agent skill to craft the **README.md** file.

**Context to read first:**
- `.claude/PROJECT.md` - for project overview
- `.claude/TEACHING_GUIDE.md` - for teaching focus (if exists)
- Existing `README.md` - if updating

**User request:** $ARGUMENTS

**Output requirements:**
- Follow the README.md template defined in lesson-smith skill
- Must include "Mentor's Note" section
- All content in English
- Place file at project root: `./README.md`
