# Agent or Workflow?

The one question: **can you write the steps down in advance?**

If you can write step 1, step 2, step 3 on a sticky note and they never change, you need a workflow. If the next step depends on what the AI finds along the way, you need an agent.

## The sticky note test

Ask yourself: could I write the exact steps before running this, and would they be the same every single time?

- Yes: workflow. Faster, cheaper, predictable. Boring is a feature.

- No, the AI has to look at something and decide what to do next: agent.

## Everyday examples

| Task | Which one | Why |
|---|---|---|
| Summarize my inbox every morning | Workflow | Same steps daily: read, filter, summarize, send |
| Find me a flight under $400, try other dates or airports if needed | Agent | Next step depends on what it finds |
| Post my weekly recap every Friday | Workflow | Read the week, summarize, send. Never changes |
| Figure out why my post underperformed | Agent | Has to dig, notice something, then investigate based on what it noticed |
| Turn every new invoice into a spreadsheet row | Workflow | Same extraction, same destination, every time |
| Research a topic and decide which sources are worth reading deeply | Agent | Judgment calls at every step |

## Prompt for building a workflow

```
I want to automate this task: [describe task].
The steps are the same every time:
1. [step]
2. [step]
3. [step]
Help me set this up as a simple repeatable workflow. Do not add
decision-making or branching. It should do exactly these steps
in this order, every time.
```

Fastest way to run one: claude.ai/code/routines. Type the task, pick daily, set the time. The inbox summary from the video took under a minute to set up there.

## Prompt for building an agent

```
I want an agent for this task: [describe task].
I cannot write the steps in advance because the next step depends
on what you find. Here is the goal: [goal].
Here is what you are allowed to do: [allowed actions].
Here is what you must never do without asking me: [limits].
Before acting, tell me your plan for the first step.
```

Notice the agent prompt includes limits. An agent makes its own decisions, so you decide the boundaries before it runs, not after it surprises you. The agent in the video lives on Telegram, but the same structure applies anywhere: goal, allowed actions, limits, plan first.

## The rule of thumb

Start with a workflow. Upgrade to an agent only when the workflow keeps breaking because the task genuinely needs judgment. An agent you did not need is just a workflow that costs more and surprises you at random.
