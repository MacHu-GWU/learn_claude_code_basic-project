---
description: Intelligently generate or update multiple course materials based on instructor request
---

Use the `lesson-smith` agent skill to analyze the instructor's request and determine which files need to be created or updated.

**Available files:**
- `README.md` - Tutorial document (project root)
- `TICKET.md` - Actionable task card (project root)
- `.claude/PROJECT.md` - Project overview
- `.claude/TEACHING_GUIDE.md` - Instructor notes

**Context to read first:**
- All existing files listed above
- Project source files if needed for understanding

**User request:** $ARGUMENTS

**Your task:**
1. Analyze the instructor's request
2. Determine which files need to be created or modified
3. Only modify files that are relevant to the request
4. Follow the templates defined in lesson-smith skill
5. Ensure all content is in English
6. Report what was created/modified and what was skipped (with reason)
