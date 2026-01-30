# Learn to Understand and Manage Context in Claude Code

## Objective

Learn what context is, why it matters, and how to manage it effectively through documentation strategies. Understand that context has limits and how to work within those limits to maintain Claude's performance.

Read the tutorial: [Understanding Context](https://github.com/MacHu-GWU/learn_claude_code_basic-project/tree/06-understanding-context/)

## Actionable Items

1. Read the tutorial in `README.md`

2. **Complete the Exercise: Create Your First Documentation**

   **Part A: Have a Conversation (5-8 exchanges)**
   - Start Claude Code: `claude`
   - Ask for food recommendations: "I want to eat healthier. Can you recommend some low-calorie foods that taste good? I like [your food preferences]."
   - Have a casual conversation:
     - Ask follow-up questions about nutrition, taste, preparation
     - Discuss the recommendations
     - Ask Claude to explain the reasoning behind recommendations
     - Make a decision about which foods to try

   **Part B: Extract to Documentation**
   - Ask Claude with one complete prompt:
     ```
     Based on our discussion, I think the most important points are:
     - Low-calorie foods that actually taste good
     - Easy preparation methods
     - The specific foods I decided to try

     Please create a concise markdown document (300-500 words) that summarizes:
     1. The key food recommendations we discussed
     2. Why these foods are good choices
     3. The specific foods I chose to try

     Format it nicely because I'll save it as docs/my-nutrition-plan.md
     ```
   - Copy Claude's response
   - Save it as `docs/my-nutrition-plan.md` in your project directory
   - Create the `docs/` directory if it doesn't exist

   **Part C: Submit Your Work**
   - Open a new session: `claude -c` or just `claude`
   - Verify your document exists: `cat docs/my-nutrition-plan.md`
   - Take a screenshot or copy the output showing the document was created
   - Leave a comment on this ticket with:
     - "Exercise completed"
     - A link/reference to your `docs/my-nutrition-plan.md` file
     - Brief reflection: "What did I learn about context and documentation?"

**Estimated time:** 20-30 minutes

## Key Concepts to Understand

- **Context** — Everything Claude is currently processing (history, files, prompts)
- **Context Window** — The maximum amount Claude can process at once (~200,000 tokens)
- **Context Pressure** — When context gets full, Claude compresses history (important info might be lost)
- **Documentation Strategy** — Convert conversations into reusable documents instead of relying on history
- **Manual Compression** — Ask Claude to condense important information into concise summaries
- **When to Use Long Context** — Complex systems, consistent narratives, debugging
- **When to Use Short Context** — Independent queries, focused problems

## Checklist

- [ ] **Read tutorial** - Finished reading 05-understanding-context.md
- [ ] **Started exercise** - Began casual conversation about food recommendations in Claude Code
- [ ] **Had full conversation** - Completed 5-8 exchanges discussing recommendations and made a decision
- [ ] **Generated documentation** - Asked Claude to summarize into markdown format
- [ ] **Saved document** - Successfully saved to `docs/my-nutrition-plan.md`
- [ ] **Verified creation** - Confirmed document exists in a new session
- [ ] **Submitted work** - Left comment with documentation link and reflection
- [ ] **Sent to mentor** - Shared the GitHub link to `docs/my-nutrition-plan.md` with your mentor
- [ ] **Understood the benefit** - Know how documentation replaces the need to keep context

## Reflection Questions (Optional)

After completing the exercise, consider:
- How did the conversation flow naturally from one question to the next?
- Would this conversation have been harder if Claude had dozens of other conversations in its context?
- How does having a 300-500 word summary compare to having to re-read the entire conversation?
- When might you use this documentation strategy in your real work?
