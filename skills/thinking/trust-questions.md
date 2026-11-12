# Four Questions Before You Trust What Your Agent Built

Addy Osmani's [Cognitive Surrender](https://addyosmani.com/blog/cognitive-surrender/) separates offloading, where I delegate and still own the answer, from surrender, where the agent's output quietly becomes mine.
Between the two I put deferral, where I look at the work but take the agent's word on the parts I didn't check, and all three feed what he calls comprehension debt, the debt I don't notice until I have to change the code.
These are the four questions I run before anything an agent built gets merged, plus the habit under them.

## 1. Expectation first

If I ask before I guess, the agent's answer becomes my expectation and I lose the only thing I had to check it against. So before I ask, I write one line of what I think the answer should be. The gap between my line and its answer is where the review happens, and a gap I can't explain means I don't understand the code yet.

Before asking, I write:

```
I expect: [one line of what I think the answer is]
```

After the agent answers:

```
Compare your answer to this line and say where they differ and why: [my line]
```

## 2. Help me think or think for me

Both are fine. Surrender starts when I didn't choose, when a request I meant as help me think comes back as a finished decision and I accept it. One line at the top of the request makes the choice on purpose, and it tells the agent whether to hand me options or hand me an answer.

```
Help me think: give me the options and the tradeoffs, I'll decide.
```

```
Think for me: decide and do it, I'll review the result.
```

The rule: both are fine as long as I chose.

## 3. What would have to be true for this to be wrong

An agent tests the paths it thought of, and its summary reports those. The bug lives in the path it didn't think of, so I ask for that path by name and then I test it myself instead of asking the agent to.

```
List the three conditions under which this change is wrong, then tell me which one you did not test.
```

I test that one myself.

## 4. Would I defend this to the maintainer

Approving a diff feels like reviewing it. Explaining it out loud is the real test. So before I merge I write two lines, what changed and why, as if I'm saying them to the maintainer's face. If I can't write them, I haven't reviewed it.

```
What changed: [one line]
Why: [one line]
```

## The habit under them

I read the commands the agent ran and their raw output before I read its summary. The summary is the agent's story about the work. The commands and output are the work. A test run that printed 3 failures and a summary that says all tests pass is the exact thing I'm looking for, and I only catch it in the raw output.

In Claude Code, I press Ctrl+O to open the transcript viewer, which shows every tool call with its full input and output. I checked this against the [interactive mode docs](https://code.claude.com/docs/en/interactive-mode) on November 12, 2026. Keybindings can be changed, so if Ctrl+O does nothing for you, check `~/.claude/keybindings.json`.

In Codex, I use the Show details expansion on each command to see what ran and what it printed. I couldn't find that label in the current Codex docs, so check what your version calls it.

Source: [Cognitive Surrender by Addy Osmani](https://addyosmani.com/blog/cognitive-surrender/)
