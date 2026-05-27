# /goal command template

The `/goal` command exists in Claude Code, Codex, and Hermes. The format below is the one I use across all three. Three parts. The third part is the one most people skip and it's why their goals drift for hours and burn cash.

## What /goal does

`/goal` runs an agentic loop until a validator decides the goal is met. You set the goal once, the agent loops without you, and stops when the end state is reached or you stop it.

Before /goal, you were the loop, reading output, deciding, prompting again, approving, repeating. After /goal, a small validator model does that for you.

## The format

```
/goal [task] until [end state] without [constraints]
```

- **task**: what you want built or done. Specific verbs, not vague intent.
- **end state**: how you'll know it's done. Measurable, observable, the test the agent can run against itself.
- **constraints**: what the agent isn't allowed to touch, change, or pull in. The boundary that keeps it from drifting.

If your end state isn't measurable, the agent doesn't know when to stop. If your constraints are missing, the agent decides for you. Lock both before you walk away.

## The exact /goal from the video

I ran this in this repo on the morning I recorded the /goal video. Set the goal, walked away, made coffee. By the time I came back the script was built, tested, and documented. The artifact is at [`scripts/skill-stats.py`](../scripts/skill-stats.py), the test is at [`scripts/test_skill_stats.py`](../scripts/test_skill_stats.py), and the report it produced is at [`skill-stats-report.md`](../skill-stats-report.md).

```
/goal in the q-claude-skills repo, build a script called skill-stats that scans every skill folder, reads the SKILL.md frontmatter, and outputs a markdown report showing each skill's name, description, last modified date, and a flag for any skills missing required frontmatter fields. until the script executes end-to-end, produces a valid markdown report saved to ./skill-stats-report.md, includes a passing test that runs on the report output, and is documented in a brief README section. without modifying any existing skill files, without adding dependencies outside the python or node stdlib.
```

Three parts in that prompt:

- **task**: build a script called skill-stats that scans every skill folder, reads SKILL.md frontmatter, outputs a markdown report
- **end state**: script runs end-to-end, produces `./skill-stats-report.md`, has a passing test, has a README section
- **constraints**: no existing skill files modified, no dependencies outside python or node stdlib

The constraints are what kept the agent from rewriting half the repo while solving the task. Without them, /goal can loop on a vague target until you stop it.

## Shape templates for other categories

Same three-part shape, applied to different kinds of work. Adapt to your context. These are templates to start from, not goals I've personally run. The skill-stats one above is the real run.

### Refactor

```
/goal in [repo], refactor [file or module] so [behaviour change]. until [the change passes the existing test suite], [new behaviour is covered by at least one new test], and [the failure mode is handled]. without touching [adjacent flow], without changing [public surface], without adding new dependencies.
```

### Research

```
/goal pull the [N] most-cited papers from the last [time window] on [topic], summarize each one in [length], and identify the [N] common threads. until the output is a single markdown file with one section per paper, one section for the cross-cutting threads, and a working source link for every paper. without inventing citations, without including papers cited by fewer than [threshold] other works.
```

### Docs

```
/goal write a quickstart for [repo] that gets a new reader from [start state] to [first working result] in under [time]. until a smart friend can follow it step by step on a fresh machine, [setup file] is updated with the gotchas, and a "what to do if it breaks" section covers the failure modes. without rewriting the existing README, without changing the file structure.
```

### Content

```
/goal draft a [platform] caption for [video topic] that takes the [angle] perspective. until the caption is [voice rules], under [N] characters, and hits [specific required beats]. without repeating the script's opening line, without using em dashes.
```

## Tips that came from running this badly first

- Start small. Run /goal on a 30-minute task before you set it loose on a multi-hour build. The loop is expensive and a vague goal can iterate for hours before realising it's lost.
- Always set a clear end state. The agent's stop condition lives in the "until" clause. Without it the agent runs until you do.
- Check your spend before walking away. Most providers expose a token or dollar usage display. Look at it.
- If your constraints are longer than the task, the goal is too big. Break it up. Multiple small /goals beat one sprawling one.
- Watch the first 30 seconds. If the agent's first move feels off, kill it and tighten the prompt before it spirals.

## Gotchas

- A vague end state means the agent runs until you stop it. Make the "until" clause something the agent can check against itself.
- Constraints aren't optional. Without them, the agent will touch things you didn't intend to touch.
- /goal is for tasks with a checkable end state. It's not the right tool for ambiguous research where the answer shape isn't known.
- Cost compounds. The validator runs every loop. Long-running /goals can spend more than you expect.
