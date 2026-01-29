---
description: Generate or update TEACHING_GUIDE.md (instructor notes) using lesson-smith skill
---

Use the `lesson-smith` agent skill to craft the **TEACHING_GUIDE.md** file.

**Context to read first:**
- `.claude/PROJECT.md` - for project overview
- `README.md` - for tutorial content
- Existing `.claude/TEACHING_GUIDE.md` - if updating

**User request:** $ARGUMENTS

**Output requirements:**
- Follow the TEACHING_GUIDE.md template defined in lesson-smith skill
- Include concept sequence (what to teach first, second, etc.)
- Include common struggles and interventions
- All content in English
- Place file at: `.claude/TEACHING_GUIDE.md`
