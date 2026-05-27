# Q Claude Skills

A growing collection of Claude skills built around one idea: stop prompting AI and start building systems with it.

Every skill in this repo comes from a real workflow I use or teach. Each one is designed to be installed once and used forever. As I make new content I add new skills here.

## Who this is for

Anyone who uses Claude and wants to get more out of it. No coding experience needed.

## What's inside

### Thinking
For when you need to understand a problem before you try to solve it.

- Belief Updater — maintains three competing hypotheses and updates them as new evidence comes in
- Blind Spot Finder — finds what is missing from your thinking entirely, not a critique of what you said but a map of what you did not say
- Complexity Mapper — maps all the moving parts of a problem and finds the single lever that creates the most change

### Decision Making
For when you need to choose a path and you are too close to see it clearly.

- Parallel Conversations — runs the same idea through three completely different perspectives simultaneously
- Assumption Audit — surfaces every assumption your thinking is based on and stress tests each one
- Time Machine — shows you what your future self would think about this decision in 6 months, 1 year, and 5 years

### Research
For when you need to validate an idea or understand a space before committing to it.

- Adversarial Room — builds the strongest possible case against your idea so you find the fatal flaw before it costs you
- Premortem — assumes the project already failed and works backwards to explain why
- Steelman — builds the strongest possible version of any argument so you engage with what is actually true

### Building
For when you are ready to execute and need a system not just a plan.

- Weekly Planning — builds a complete weekly plan from your actual context, not generic time blocks
- Agent Setup — designs a full agent workflow covering system prompt, tools, and how to know if it is working
- Research Workflow — turns a research question into a structured workflow with a clear stopping condition

## How to install — Claude Desktop and Claude.ai

1. Click the blue Code button on this page
2. Click Download ZIP
3. Unzip the downloaded file
4. Open the unzipped folder and go inside the skills folder
5. Find the folder for the skill you want to install
6. Right-click it and compress it into a ZIP file
7. Open Claude Desktop or claude.ai
8. Go to Settings, then Capabilities, then Skills
9. Click the plus button
10. Select Upload a skill
11. Upload the ZIP file
12. The skill will appear in your Skills list; toggle it on

## How to install — Claude Code

npx skills add https://github.com/kju4q/q-claude-skills.git

## More coming

Every video I make adds a new skill to this repo. Follow along on [Instagram](https://www.instagram.com/qendresahhoti) and [TikTok](https://www.tiktok.com/@qbuilder).

## skill-stats

`scripts/skill-stats.py` scans every folder under `skills/`, reads the YAML frontmatter from each `SKILL.md`, and writes a markdown report to `./skill-stats-report.md` with each skill's name, description, last-modified date, and a flag for any missing required fields (`name`, `description`). Python stdlib only — no install step.

```sh
python3 scripts/skill-stats.py            # writes ./skill-stats-report.md
python3 scripts/test_skill_stats.py       # runs the test suite against the report
```

Optional flags: `--skills-dir <path>` to scan a different tree, `--output <path>` to write elsewhere.
