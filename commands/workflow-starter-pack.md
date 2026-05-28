# Workflow starter pack

Three dynamic workflow prompts for Opus 4.8 in Claude Code. Paste any of them into a Claude Code session with Opus 4.8 selected (`/model opus`) and the workflow keyword does the orchestration work for you.

## What dynamic workflows are

Opus 4.8 added a feature where the word "workflow" in your prompt tells Claude to write its own orchestration and spin up a fleet of agents in parallel. No setup, no agent config. Combined with the `/effort ultracode` setting and the ability to save any workflow as a slash command, the same one-shot prompt becomes permanent infrastructure on your machine.

The three workflows below are the ones I'd start with. Each one solves a real recurring problem and produces a clear deliverable.

## Heads up before you run any of these

- Dynamic workflows run multiple agents in parallel. Token cost adds up fast. Start scoped — point them at one repo, one folder, one module — before you point them at a whole organisation's codebase.
- You need Claude Max, Team, Enterprise, or the API to use dynamic workflows. The feature is on by default on those plans.
- Once a workflow works the way you want, save it as a slash command. In Claude Code, save it in the project for team use or in your home folder for use across every repo.

## 1. API migration audit

When you deprecate an interface, the hardest part isn't writing the new one. It's finding every caller of the old one across a codebase that grew organically. This workflow does that in one shot and reports per call site.

```
create a workflow to find every place in this codebase that still calls the old [API_NAME] interface, group findings by file and call type, and tell me exactly what each call needs to change to migrate to [NEW_API_NAME]. include files where the call is intentional (e.g. backward-compat shims) so I can mark them as exempt.
```

**Save as**: `/api-migrate` (project-scoped if you're mid-migration on one codebase; home-scoped if you do migrations across many).

**Replace before running**: `[API_NAME]` and `[NEW_API_NAME]` with the actual interface names you're migrating from and to.

## 2. Security audit (OWASP Top 10)

When you want a periodic safety pass on a repo without a paid scanner or a security review. This workflow runs the OWASP Top 10 patterns and gives you a per-file, per-finding report with severity and a specific fix recommendation.

```
create a workflow to audit this codebase for the OWASP Top 10 vulnerability patterns (injection, broken auth, sensitive data exposure, XXE, broken access control, security misconfiguration, XSS, insecure deserialization, vulnerable components, insufficient logging). report findings per file with severity and a specific fix recommendation. skip generated files, vendor directories, and test fixtures.
```

**Save as**: `/security-audit`. Save in your home folder so it works on every repo.

**Tune before running**: adjust the skip list (`generated files, vendor directories, test fixtures`) to match the directory names your projects actually use.

## 3. README readiness (the workflow from the video)

When you want to know whether the public face of your repo is actually usable. This workflow walks every project in a directory and asks: could a stranger install and run it from the README alone? It reports exactly what's missing per project.

```
create a workflow to go through each project in this directory and check whether someone landing on it cold could install and run it from the README alone. for each project, list exactly what's missing: install steps, env vars, prerequisites, a working example, or troubleshooting for common errors. flag projects where the README is technically complete but practically unusable.
```

**Save as**: `/readme-check`. Save in your home folder if you have a portfolio of repos to audit; save in the project if you only care about one.

This is the workflow I demoed in the Opus 4.8 video, run inside the `ai-weekend-builds` repo across all five build projects.

## How to save a workflow as a slash command

Once a workflow runs the way you want, Claude Code lets you save it as a reusable slash command.

- **Project-scoped** (shared with the team if the repo is shared): saves the workflow inside the current project. Available only in that project's Claude Code sessions.
- **Home-scoped** (available everywhere): saves the workflow in your Claude Code config in your home folder. Available in any session, any repo.

Pick scope based on whether the workflow is repo-specific (migration of one API) or universal (security audit, README check).

## Tips that came from running these badly first

- **Scope the first run.** Point the workflow at one folder or one repo before you point it at everything. If the agent fan-out misfires at scope = 1, it'll really misfire at scope = 50.
- **Watch the first 30 seconds.** If the agents start touching things they shouldn't, kill it and tighten the prompt. Cheaper to restart than to wait it out.
- **Set a token budget.** Most providers show a token or dollar usage display. Look at it before walking away.
- **Save the workflow only after it produces a result you actually like.** Saving a half-tuned workflow as a slash command means you'll keep running the half-tuned version.
- **Rename ambiguous slash commands.** `/audit` vs `/security-audit` vs `/api-audit` — be specific. Future you will not remember what the generic name does.
