# Belief Updater

## What this technique does

Turns Claude into a live reasoning engine that maintains multiple competing hypotheses and updates them as new evidence comes in. Instead of asking for answers you run a dynamic model that gets more accurate over time. This is how scientists think. This is how the best investors think.

## When to use

- User is working through a problem with multiple possible explanations
- User has new information and wants to update their understanding
- User is making a decision under uncertainty
- User wants to track competing theories as evidence builds
- User is doing research or analysis where the answer is not yet clear

## How to apply

When this technique is triggered set up and maintain three competing hypotheses:

**Setup**
Ask the user what problem or question they are working through if not already clear. Then define three competing hypotheses that could each explain the situation or answer the question. Make them genuinely different from each other — not variations of the same idea.

**For each hypothesis state:**

- What it claims
- Current probability it is true based on available evidence
- What evidence would increase its probability
- What evidence would completely destroy it

**As new evidence comes in**
Update the probability of each hypothesis. Be explicit about what changed and why. Remove a hypothesis if evidence destroys it and replace it with a better one if needed. Keep the model alive and honest.

**The output**
Always show the current state of all three hypotheses with their probabilities after each update. Make it easy for the user to see how their understanding is evolving.

## Gotchas

- Do not let dead hypotheses survive. If evidence destroys one remove it immediately.
- Probabilities do not need to add up to 100. Each hypothesis is evaluated independently.
- Do not collapse to one hypothesis too early. The value is in maintaining genuine uncertainty until the evidence is strong enough.
- Do not make all three hypotheses variations of the same idea. They should represent genuinely different explanations.
- The question "what evidence would destroy this hypothesis" is the most important question in the whole technique. Do not skip it.

## Example prompt that triggers this technique

"Maintain three competing hypotheses about this. Update them as I give you new information."
