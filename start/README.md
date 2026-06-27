# Start here: the way I'd use Claude if I were starting over

If I deleted my whole Claude setup today, these are the three things I'd build back
first. Not better prompts. The three things that turn Claude from a chatbot you talk to
into a platform you build on.

Each one is real, each one is something I actually run, and each link below goes to a
working starter you can install. Pick one and build it this week.

---

## 1. A Claude that rewrites its own rules

Give Claude write access to one rules file plus one signal that tells it what's working,
and it reads its own results and updates its own instructions. Your setup stops rotting.
It gets sharper every week instead of staying frozen on day one.

Safe by design: it edits one named file, logs every change with a reason, and everything
is in git so any edit is one `git revert` away.

**Starter:** [`/self-improving`](../self-improving) (README + the self-review skill + an example rules file)

## 2. One prompt that splits into a fleet of agents

Stop asking one Claude one question. Give one instruction and it fans out into a dozen
sub-agents, each working a different piece in its own memory, then merges everything into
one answer. The rule: don't make one Claude do twelve things, make twelve Claudes do one
thing each. Parallel isolated contexts beat one long chat that forgets its own beginning.

**Starter:** [`/commands/workflow-starter-pack.md`](../commands/workflow-starter-pack.md) (3 ready-to-run dynamic workflows)

## 3. An agent that lives on your machine and texts you

Claude doesn't have to be a place you go. This one runs on your own laptop, watches
GitHub and what's moving in AI, and texts you in Telegram when it finds something worth
building. Give it somewhere to run, a way to reach you, and a job, and it comes to you.

**Starter:** [q-signal-to-build](https://github.com/kju4q/q-signal-to-build) (the full agent: SKILL.md, setup, run script)

---

## How they fit together

One fixes itself, one clones into a team, one lives in your pocket. Together they're the
difference between using Claude and building on it. Start with whichever one solves a
problem you have this week, get it working, then add the next.

Build your own version, change it, break it, make it yours.
