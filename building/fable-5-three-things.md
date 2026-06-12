# 3 things inside Fable 5

You commented FABLE, so here's everything from the video, written out so you can try all three right now.

One thing first: Fable 5 is not the default model. Update Claude Code and switch to it:

```
claude update
```

Then inside a session:

```
/model fable
```

Press Enter to save it as your default. Confirm with `/status`. You need Claude Code v2.1.170 or later and a paid plan.

---

## 1. Friend mode

Launch Claude Code with the default system prompt wiped:

```
claude --model fable --system-prompt "."
```

The period is there because the quotes can't be empty. What you get is Fable with no coding persona: a thinking partner instead of an assistant. Use it to talk through decisions, stress test ideas, or get an honest second opinion.

Good first prompts to try:

- "I'm deciding between two options, poke holes in both: ..."
- "Give me a brutally honest take on this idea: ..."
- "Argue me into picking one: ..."

Know this: the flag strips the work instructions too, so use it for conversations, not for serious agent tasks. For real work, launch Claude Code normally.

## 2. Watch it think

Fable is always reasoning on every step, and you can't turn that off. By default Claude Code hides it.

Press **Ctrl+O** during any task.

The gray italic text that appears is Fable reasoning in real time: why it picks a file, what it's worried about, what it's about to try. Press Ctrl+O again to hide it.

Why keep it on: when Fable does something weird, the reasoning tells you why. When it does something brilliant, the reasoning shows you what context it used, which teaches you how to write better prompts.

If you press Ctrl+O and the thinking looks empty, add this to `~/.claude/settings.json` and restart the session:

```
"showThinkingSummaries": true
```

## 3. The effort dial

Type this in any Claude Code session:

```
/effort
```

This is the only dial Fable has, and it changes how the model behaves, not just how hard it thinks. Lower effort means fewer tool calls and straight-to-the-point answers. Higher effort means planning, exploring, more tool calls, and sometimes changes you never asked for.

How to use it:

- **Low**: quick fixes and questions
- **Medium**: your daily driver for real work
- **Max**: only for the problem you've been stuck on for days

Max isn't better. Max is more. Set the dial on purpose instead of leaving the default, and you'll get faster answers and burn through your usage limits slower.

---

That's all three. If you build something with any of these, tag me, I genuinely want to see it.

More breakdowns and skills live in this repo, look around.

Qendresa
TikTok @qbuilder · Instagram @qendresahhoti
