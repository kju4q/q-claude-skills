# Self-Modifying Instructions

## What this technique does
Adds a line to a Claude project's instructions that makes Claude propose edits to its own setup at the end of each substantive session, based on what it observed about the user. The setup improves itself instead of going stale.

## When to use
- The user has a Claude project they use regularly
- The user wants their setup to keep improving without having to remember what to update
- The user wants Claude to notice patterns about them and act on them

## How to apply

This is a one-time addition to project instructions. Add this line:

"At the end of every substantive session, before signing off, propose 1 to 3 specific edits to my project instructions, memory files, or skills based on what you observed about me this session. Format them as diffs i can approve or reject. Include reasoning for each."

After that, every substantive session ends with Claude proposing edits. The user approves or rejects each one. Over time the setup becomes genuinely tuned to how the user actually works.

## Gotchas
- Generic proposals ("add more detail about your work") mean the session was not substantive enough, or the instruction needs tightening
- The user has to actually approve or reject. Ignoring the proposals defeats the loop
- Approve sparingly. The setup should sharpen, not bloat
- The best proposals are ones the user would not have thought to make themselves

## Trigger prompt
"At the end of every substantive session, before signing off, propose 1 to 3 specific edits to my project instructions, memory files, or skills based on what you observed about me this session. Format them as diffs i can approve or reject. Include reasoning for each."
