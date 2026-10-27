# Make your own Claude Code skill

A skill is a reusable ability you teach Claude Code once and invoke with one command. I built one called slides, I type /slides in any repo and it turns that project into a presentation. That one lives in its own repo at https://github.com/kju4q/slides if you want to see a finished skill in the wild. Here's how to build yours.

## What a skill actually is

One folder with one file inside called SKILL.md. The file starts with a small header that names the skill and says when to use it, and the rest is instructions written like you'd brief a person. That's the whole thing, no code required.

The skills in this repo also keep extra reference files in a techniques/ folder next to SKILL.md. That's optional, start with just the one file.

## Build your first one in five steps

1. Pick one job you keep asking Claude for in different words. That repetition is your skill.

2. Make a folder named after the job, lowercase, no spaces, for example skills/your-job/. Inside it, create SKILL.md.

3. Start the file with this header, filling in your own:

   ```yaml
   ---
   name: your-skill-name
   description: Use this skill when the user wants X. Activate when Y.
   ---
   ```

   The name is what you invoke, and it must match the folder name. That's the rule in [the spec](https://agentskills.io/specification), and Cursor and claude.ai uploads enforce it. In this repo the skill named thinking lives in skills/thinking/. The description is how Claude decides when to use it, so say when, not just what.

4. Below the header, write the instructions: what to do step by step, what the output should look like, what to never do. Be specific, this file is the skill.

5. Install it and say the job. In Claude Code, skills from this repo install with `npx skills add https://github.com/kju4q/q-claude-skills.git`, or drop your folder into your own skills setup. Then just ask for the job, or invoke it by name.

## How you know it works

Run it on a real case. If the output misses, don't rewrite your request, rewrite the SKILL.md, that's the difference between prompting and building. Every fix makes the skill permanently better.

## Start from a working example

Every skill in this repo is a working example. Open any folder under skills/, read its SKILL.md, copy the shape, change the job.

Stuck? Ask me in the comments on my videos, that's what they're for.

Built by [@qendresahhoti](https://instagram.com/qendresahhoti), more at [github.com/kju4q](https://github.com/kju4q)
