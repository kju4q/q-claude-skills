# Write a skill once, run it in every agent

## What a skill is

A skill is a folder with a file called SKILL.md in it. The top of the file says what the skill is and when to use it. The rest is the procedure. Agents read only the top until a task matches, then load the whole thing.

The format is an open standard, documented at [agentskills.io](https://agentskills.io). Anthropic donated it to the Agentic AI Foundation on [October 22, 2026](https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation).

## The folder shape

```
your-skill/
├── SKILL.md       required
├── scripts/       optional, code the agent can run
└── references/    optional, longer docs the agent reads when it needs them
```

SKILL.md starts with frontmatter. Two fields are required.

```yaml
---
name: your-skill
description: What it does and when to use it.
---
```

The [spec](https://agentskills.io/specification) is strict about `name`: lowercase letters, numbers and single hyphens, up to 64 characters, and it must match the folder name. Some agents let a mismatch slide. Cursor and claude.ai uploads don't, so match it.

The description is the part that matters most. At startup the agent loads only the name and description of every skill, and decides from that alone whether yours applies. Say what it does and when it should run, and use the words someone would actually type. "Helps with packages" never fires. "Before cloning or installing any package or repo" does.

The body is plain words. Keep it under 500 lines. Anything longer goes in references/.

## The five parts

A good SKILL.md has five parts. [audit-package](../skills/audit-package/SKILL.md) is the example.

1. **When it runs.** The exact triggers. For audit-package that's every install command, every clone, and any pasted package name.
2. **Hard rules.** What the agent must never do, written as never. Never install before reporting. Never run code from the package.
3. **The steps, with how to do each.** Not "check the maintainer". The command that checks it, and what to do when the check can't be done.
4. **The output format.** Fixed, so you can scan it. audit-package always ends in the same five-row table and a one-line verdict.
5. **What to do after.** What happens when you answer. For audit-package, "go" means install exactly as decided, then check that what landed matches what was audited.

## Install it

Same folder, different place per agent. I checked each of these against the agent's own docs.

| Agent | Project skills | Personal skills |
| --- | --- | --- |
| [Claude Code](https://code.claude.com/docs/en/skills) | `.claude/skills/<name>/` | `~/.claude/skills/<name>/` |
| [Codex](https://learn.chatgpt.com/docs/build-skills) | `.agents/skills/<name>/`, in any folder from where you are up to the repo root | `~/.agents/skills/<name>/` |
| [Cursor](https://cursor.com/docs/context/skills) | `.agents/skills/` or `.cursor/skills/` | `~/.agents/skills/` or `~/.cursor/skills/` |
| [Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/create-skills) | `.github/skills/`, `.claude/skills/` or `.agents/skills/` | `~/.copilot/skills/` or `~/.agents/skills/` |

A few things worth knowing:

- `~/.agents/skills/` is shared by Codex, Cursor and Copilot CLI. It isn't in Claude Code's list, so for Claude Code use `~/.claude/skills/`.
- Cursor also loads skills from the Claude and Codex folders.
- Codex has a built-in installer. `$skill-installer <name>` adds a skill.
- Copilot CLI can add one with `copilot skill add <file, URL or folder>`. After copying a folder in by hand, run `/skills reload`.
- Cursor picks up new skills when it starts.

**claude.ai.** Zip the skill folder. Go to Customize, then Skills, click +, then Create skill, then Upload a skill. Anthropic's [help article](https://support.claude.com/en/articles/12512180-using-skills-in-claude) has the details. Skills turned on there also sync into Claude Code.

**Claude Desktop.** I couldn't verify this one. Anthropic's skills article only describes the claude.ai upload and doesn't mention the desktop app. If you try it, check that the skill shows up before you rely on it.

## Three mistakes

**Writing a prompt instead of a procedure.** "You are an expert security reviewer" is a prompt. "Run `npm view <pkg> time --json` and flag anything published in the last 7 days" is a procedure. A skill is the procedure.

**No output format.** If the output looks different every run, you can't compare runs and you can't scan them. Fix the shape.

**No stop condition.** Say where the skill ends. audit-package ends with "Waiting for you." and stops. Without that line, nothing stops the agent from finishing the audit and going straight on to the install.

## Start from the example

[skills/audit-package](../skills/audit-package/) has the SKILL.md and two worked examples using real packages. Copy the shape, change the job.

Built by [@qendresahhoti](https://instagram.com/qendresahhoti), more at [github.com/kju4q](https://github.com/kju4q)
