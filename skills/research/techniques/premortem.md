# Premortem

## What this technique does
Assumes the project or idea has already failed and works backwards to explain why. Most people do post mortems after something fails. This technique runs that same analysis before you start. It surfaces risks that optimism blinds you to and finds the failure modes most likely to actually happen.

## When to use
- You are about to commit significant time or money to something
- You feel too confident and want a reality check
- You want to find the most likely ways this could go wrong
- You are planning something complex with many dependencies

## How to apply

When this technique is triggered do not evaluate whether the idea is good. Assume it already failed and explain why.

**Step 1 — Set the scene**
It is 12 months from now. The project failed. Not a minor setback but a real failure. The user is looking back trying to understand what happened.

**Step 2 — Generate failure stories**
Generate three to five specific, plausible stories of how the failure unfolded. Each story should be different. Cover different failure modes — execution failures, market failures, people failures, timing failures, assumption failures.

**Step 3 — Find the most likely failure**
Identify which failure story is most probable given what you know about the situation. Explain why this one is more likely than the others.

**Step 4 — The prevention question**
For the most likely failure ask: what is the earliest warning sign that this failure is starting to happen. What would you see in week 2 or month 1 that tells you you are on this path.

## Gotchas
- Do not be gentle. The value of this technique disappears if the failure stories are not specific and plausible.
- Do not generate generic failures. Every failure story must be specific to what the user actually shared.
- Do not offer solutions after the premortem unless the user asks. The failure analysis is the output.
- The earliest warning sign question is the most practical part. Do not skip it.

## Trigger prompt
"Assume this already failed. It is 12 months from now and we are looking back. What happened?"
