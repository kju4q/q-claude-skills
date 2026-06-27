# A Claude that rewrites its own rules

most people's AI never gets smarter. it's exactly as good on day 200 as it was on day 1, because every chat starts from zero and nothing it learns ever gets written down.

this is the opposite. it's a small loop that lets Claude read its own results, find where its rules are out of date, and edit the file that governs its own behavior. you stop hand-updating your setup. it updates itself.

i run this on my content system. every week Claude reads which posts performed, compares that to the rules it's been following, and rewrites those rules to match what actually worked. i'm not running the version of the system i wrote months ago. it wrote the current one.

heads up: this looks scary ("AI editing its own instructions") and it isn't, because of three guardrails below. read those before you run it.

---

## the idea in one line

give Claude write access to ONE rules file, plus ONE signal that tells it what's working, and a loop that turns the signal into edits. that's it. instructions stop being config you set once and become something the system maintains.

## the three pieces you need

1. **a rules file** the one file that governs how Claude does a recurring task. for me it's `hooks-library.md` (the rules for what makes a good content hook). for you it could be your writing-style guide, your code-review checklist, your outreach playbook. one file, plain markdown.

2. **a signal file** the evidence Claude reads to decide what to change. for me it's `performance-log.md` (which posts hit, which flopped). for you it could be a results log, a feedback file, a list of what shipped vs what got reverted. if there's no signal, there's nothing to learn from, this is the part people skip and it's the whole point.

3. **the self-review skill** (`self-review.md` in this folder) the loop that reads both, proposes specific edits with reasoning, writes them to the rules file, and logs every change.

## the three guardrails (this is why it's safe)

1. **it edits ONE file, never your whole repo.** the skill names the exact rules file. it has no permission to touch anything else.
2. **every edit is logged with a reason.** it appends to `self-edits.md`: what it changed, what evidence drove it, what it expects to improve. nothing changes silently.
3. **everything is in git.** if an edit is wrong, `git revert` undoes it in one command. the system proposes, git is your undo button.

so the worst case is: it makes a change you disagree with, you read the one-line reason in the log, you revert it. that's the floor.

---

## setup

### 1. pick your rules file and your signal file

you almost certainly already have a rules file (a style guide, a checklist, a CLAUDE.md section). if you don't have a signal file yet, make one. it can start as simple as:

```
# results.md
- 2026-06-20: shipped the short-hook version, got 3x the saves of the long version. short wins.
- 2026-06-22: the "if I were starting over" framing outperformed the feature-list framing.
```

the signal doesn't have to be analytics. "this worked, this didn't, here's why" in your own words is enough for Claude to learn from.

### 2. install the skill

drop `self-review.md` into `.claude/skills/` in your repo, or paste its contents into your CLAUDE.md under a "self-review" heading. (`example-rules.md` in this folder shows the shape of a rules file Claude can actually edit cleanly.)

### 3. run it

type `self-review` in Claude Code (or Cowork). it will:

1. read your rules file and your signal file
2. find the places where the rules no longer match the evidence
3. show you each proposed edit with the reason and the evidence behind it
4. apply the edits to the rules file
5. append an entry to `self-edits.md`

review the proposed edits the first few times. once you trust it, let it run on a schedule.

### 4. (optional) put it on a schedule

this is where it stops being a command you run and becomes a system that maintains itself. in Cowork, create a scheduled task (weekly is a good start) with the prompt:

```
run self-review.
read the rules file and the signal file named in .claude/skills/self-review.md.
propose and apply edits to the rules file based on the evidence.
log every change to self-edits.md with the reason.
then give me a short summary of what you changed and why.
```

now you wake up to a setup that's a little sharper than it was last week, and a log telling you exactly what it learned.

---

## what makes this actually useful and not a gimmick

the gimmick version is "look, AI edited a file." useless.

the useful version is the loop: real evidence in, a specific rule change out, logged so you can trust it, reversible so you're never stuck. the value isn't that it can edit a file. it's that your rules stop rotting. most people's playbooks are written once and never updated against what actually happened. this one can't drift, because it re-grounds itself in the evidence every time it runs.

start with one rules file and one signal. make it yours.
