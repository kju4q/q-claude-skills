---
name: self-review
description: >
  Reads a results/signal file, compares it against a rules file, and rewrites the
  rules file to match what the evidence actually shows. Logs every change. Use when
  the user types `self-review` or asks Claude to update its own rules from results.
---

# self-review

You maintain a set of rules by re-grounding them in evidence. You are allowed to edit
ONE rules file and ONE log file. You may not edit anything else.

## Configure these two paths before first run

- RULES_FILE: `hooks-library.md`        # the file whose rules you may rewrite
- SIGNAL_FILE: `performance-log.md`      # the evidence you read to decide what to change
- LOG_FILE: `self-edits.md`              # where you record every change you make

(Change these three values to match the user's repo. Never edit a file other than
RULES_FILE and LOG_FILE.)

## The loop

When invoked:

1. **Read** RULES_FILE and SIGNAL_FILE in full.

2. **Find mismatches.** Identify places where the rules no longer match the evidence:
   - a rule the evidence now contradicts
   - a pattern that clearly worked but isn't written down as a rule yet
   - a rule stated vaguely that the evidence lets you make specific
   Ignore everything the evidence doesn't speak to. Do not invent changes to look busy.
   If the evidence supports the current rules, say so and change nothing.

3. **Propose each edit** with three things, before writing:
   - the exact change (old text -> new text)
   - the evidence from SIGNAL_FILE that drives it (quote it)
   - what you expect to improve as a result
   Keep edits small and specific. One rule at a time. No rewrites of the whole file.

4. **Apply** the approved edits to RULES_FILE.

5. **Log** every applied edit to LOG_FILE, appending an entry:

   ```
   ## [date] self-review

   - **Changed**: [the rule, before -> after]
   - **Evidence**: [the quote/data from the signal file]
   - **Expected effect**: [what should improve]
   - **Revert with**: git revert of this commit if wrong
   ```

6. **Summarize** in chat: what changed, what evidence drove it, what you left alone and why.

## Hard rules

- Edit ONLY RULES_FILE and LOG_FILE. Nothing else, ever.
- Never delete a rule without logging the evidence that made it obsolete.
- Never make a change the signal file doesn't support. "It seems better" is not evidence.
- Prefer making a vague rule specific over adding a brand-new rule.
- If you are unsure, propose the edit and stop. Let the user decide.
- Everything you write is committed to git, so a wrong edit is always one `git revert` away.
  Mention this in your summary so the user knows the undo path.
