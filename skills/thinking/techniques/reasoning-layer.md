# Reasoning Layer

## What this technique does

Forces Claude past its default safe answer into its actual committed thinking. Most responses are optimized for the most statistically likely helpful answer. This technique breaks that pattern by running through three cognitive layers.

## When to use

- User wants a genuine opinion not a balanced overview
- User is making an important decision and needs real analysis
- User feels like they are getting generic answers
- User wants to challenge their own thinking on a topic

## How to apply

When this technique is triggered respond in three layers:

**Layer 1 — The safe answer**
Give the most expected helpful response to the question as you normally would.

**Layer 2 — The self critique**
Explain specifically why that answer might be completely wrong. What assumptions does it rely on. What does it miss. Where could it fail.

**Layer 3 — The committed answer**
Give the answer you would give if you had to bet your reputation on it. This should be meaningfully different from layer 1. Be direct. Do not hedge.

**The reframe**
After the three layers ask: what is the question the user should actually be asking that they are not asking? This often produces the most valuable insight of the whole exercise.

## Gotchas

- Layer 2 must be genuinely critical not just a mild caveat. If layer 2 does not make layer 1 feel incomplete it is not working.
- Layer 3 must take a position. Vague or balanced answers defeat the purpose.
- The reframe question is not optional. It is often where the real insight lives.
- Do not skip directly to layer 3. The contrast between layers is what creates the value.

## Example prompt that triggers this technique

"I want your actual committed thinking on this, not just the safe answer."
