# Agent Setup

## What this technique does
Helps you design and set up an agent workflow for a specific task. Most people prompt agents the same way they prompt a chatbot and wonder why the results are inconsistent. This technique covers what the agent needs to know, what tools it needs, how to prompt it correctly, and how to know when it is actually working.

## When to use
- You want to automate a repeating task with an agent
- You are setting up a workflow that runs without your involvement
- You want to connect multiple tools and have Claude orchestrate them
- You have tried prompting an agent and the results are unreliable

## How to apply

When this technique is triggered do not just write a prompt. Design the full agent system.

**Step 1 — Define the task precisely**
What exactly does the agent need to do. What is the input. What is the output. What does success look like in a single measurable outcome. Vague tasks produce vague agents.

**Step 2 — Identify the tools**
What does the agent need access to in order to complete this task. List every tool, connector, and data source. If a tool is missing the agent will hallucinate or fail silently.

**Step 3 — Write the system prompt**
A good agent system prompt has four parts:
- Role: who the agent is and what it is optimizing for
- Context: everything the agent needs to know about the situation
- Constraints: what the agent must never do
- Output format: exactly what the finished output looks like

**Step 4 — Define the failure modes**
What does a bad output look like. How will you know if the agent is going off track. Build in a check before any irreversible action.

**Step 5 — Test before automating**
Run the agent manually three times before scheduling it. If the output is inconsistent the system prompt needs work not the schedule.

## Gotchas
- Do not automate before testing. A bad agent running on a schedule causes more damage than a bad agent you run once.
- Vague system prompts produce vague outputs every time. Be specific about what good looks like.
- Missing tools are the most common failure mode. Map every tool the task needs before writing a single line of prompt.
- The failure mode definition is not optional. If you do not know what bad looks like you will not catch it when it happens.

## Trigger prompt
"Help me design a complete agent setup for this task. Cover the system prompt, tools needed, and how to know if it is working."
