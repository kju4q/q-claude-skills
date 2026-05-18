# 3 Claude Automations

three automations that connect claude.ai, claude code, and cowork through github. the philosophy is simple: stop prompt engineering, start context engineering. your AI gets better when the files it reads about you compound, not when your prompts get cleverer.

what's inside:

1. the scheduled task that runs my weekly performance review automatically
2. the save command that turns one export block into 8 organized files in github
3. the skill-router.sh script that loads the right rules based on what i'm typing

heads up, parts of this assume you have cowork (anthropic's desktop product for agentic tasks) and claude code (terminal). if you don't, the patterns still translate, just adapt to your stack.

---

## 1. the scheduled task

### what it does

every sunday at 10am, cowork opens a session by itself, reads my CLAUDE.md and performance-log.md, uses claude in chrome to pull this week's analytics from IG, TikTok, LinkedIn, X, files them into performance-log.md, surfaces top performers and patterns.

i wake up sunday and the prep is done.

### setup

1. open cowork, go to scheduled tasks in the sidebar
2. create a new task with this prompt:

```
it's sunday morning. run my weekly performance review.

steps:
1. read CLAUDE.md for my system context
2. read content/performance-log.md for prior weeks
3. use claude in chrome to read this week's analytics from IG, TikTok, X, LinkedIn. for each post capture: views, comments, manychat keyword commenters, saves, shares, follows attributed
4. file into content/performance-log.md using the weekly review template at the bottom of the file
5. identify the top performer + why, identify the underperformer + why, surface 1-3 patterns across multiple posts this week
6. suggest 1-3 hooks to repeat next week and 1-3 to avoid
7. give me a clean summary i can scroll through with coffee
```

3. set the schedule: weekly, sunday, 10am (or your time)
4. click "Run now" once to pre-approve tool use, especially claude in chrome, otherwise future runs pause on permission prompts

### prerequisites

- CLAUDE.md in your repo that explains your context
- performance-log.md with a weekly review template at the bottom
- claude in chrome installed, logged into your analytics platforms

---

## 2. the save command

### what it does

i draft videos in claude.ai, the output is an export block with sections (SCRIPT, SCREEN, HOOKS, CAPTIONS, TRENDY, LINKEDIN, X, NEWSLETTER, THOUGHTS), i paste that block into cowork, type `save: monday slug-name`, and cowork parses each section into a separate .md file, creates a folder, updates my weekly log, commits to git, and pushes to github.

seconds later, the content is filed, version-controlled, available in claude code on my laptop.

### setup

add this to your CLAUDE.md or create a save.md skill in cowork:

```
When the user types `save: [day] [slug]`, do the following:
1. Take the most recent === Q-OS SAVE === block from the chat history.
2. Parse each === SECTION === header into a separate file:
   - SCRIPT → script.md
   - SCREEN → screen.md
   - HOOKS → hooks.md
   - CAPTIONS → captions.md
   - TRENDY → trendy.md
   - LINKEDIN → linkedin.md
   - X → x.md
   - NEWSLETTER → newsletter.md
   - THOUGHTS → thoughts.md
3. Create meta.md with frontmatter from the header (day, date, slug, pillar, status).
4. Place all files in: content/scripts/{week-range}/{day-date-slug}/ where week-range is the current week formatted like "18-24-may-2026"
5. Append a new row to content/weekly-log.md under the current week's planned content table.
6. Run: git add -A && git commit -m "save: {slug}" && git push
```

### the export block format

use this in claude.ai when you finish drafting:

```
=== Q-OS SAVE ===
day: [day]
date: [date]
slug: [slug]
pillar: [pillar]
status: [drafted | ready-to-record]

=== SCRIPT ===
[content]

=== HOOKS ===
[content]

...other sections as needed

=== END ===
```

---

## 3. skill-router.sh

### what it does

a bash script that hooks into claude code's UserPromptSubmit event, reads what you're typing, checks for keywords, auto-loads the relevant SKILL.md file as additional context. ask about scripts or hooks, content SKILL.md loads with all your content rules. ask about offers, business SKILL.md loads instead.

you don't switch modes, the router does it from your keywords.

### setup

1. download `skill-router.sh` from this folder
2. drop it at `.claude/skill-router.sh` in your repo
3. make it executable: `chmod +x .claude/skill-router.sh`
4. register the hook in `.claude/hooks.json`:

```json
{
  "UserPromptSubmit": {
    "command": ".claude/skill-router.sh"
  }
}
```

5. create the SKILL.md files in each domain folder (content/SKILL.md, business/SKILL.md, products/SKILL.md) with the rules for that domain

### customization

- the keyword lists in the script are MY vocabulary (content, script, offer, client, etc), swap for whatever vocabulary you actually use, that's the whole point
- add more domains if your work has more than 3 areas
- keyword matching uses `grep -w` for whole-word matching, modify if you want fuzzier matches

---

## one more thing

these three automations work because they share state through github. claude.ai when planning, claude code when building, cowork when reviewing, all reading from the same repo. work in one surface, it shows up in the others. that's the whole setup.

build your own version, change it, break it, make it yours.
