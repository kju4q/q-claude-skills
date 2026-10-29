---
name: thinking
description: Use this skill when the user needs to understand a problem before solving it. Activate for complex situations where the answer is not clear, where assumptions need surfacing, or where the user feels stuck or overwhelmed. This skill helps map what is actually happening before any action is taken.
---

# Q Thinking

A set of techniques for understanding problems deeply before trying to solve them. Most people jump to solutions. These techniques slow that down in a useful way.

## When to use this skill
- The problem feels overwhelming or unclear
- You have tried solving it and keep hitting the same wall
- You need to understand what is actually driving a situation
- You want to find what you are missing before committing to a direction

## Techniques

### Belief Updater
Maintains three competing hypotheses and updates their probability as new evidence comes in. Use when you are uncertain and need to reason through multiple possible explanations.

### Blind Spot Finder
Finds what is missing from your thinking entirely. Not a critique of what you said but a map of what you did not say. Use when you want to surface assumptions and gaps before moving forward.

### Complexity Mapper
Maps all the moving parts of a problem, how they connect, and which single lever would create the most change. Use when everything feels urgent and connected and you do not know where to start.

### The Unsaid Layer
Surfaces what each person walked away from a conversation believing, and where those beliefs quietly contradict each other. Use after an important conversation to find the gap that never got named and turn it into the script for the next one.

### The Constraint That Becomes the Strategy
Turns your biggest limitation into a competitive position by finding the moves your constraint forces that a well-resourced competitor could not copy. Use when you are frustrated by a limitation and want it to become a moat.

### The Model Underneath the Breakdown
Finds the wrong mental model under a recurring conflict or a process that keeps failing. Use when something keeps breaking the same way and you keep solving it the same way, so you can update the model instead of managing the mood.

## Chains

Each of these is a chain of three prompts run in order in the same conversation. Every prompt reacts to the answer before it, so do not skip ahead or start a new chat between steps. The user pastes the material named in the first prompt, and the next two use only what the chain has produced so far.

### The Failure Script
Command: `fail`
The user pastes their project first. Use when a plan feels safe and you want to find the slow, reasonable path to failure that is already underway.
1. "Here is my project: [paste]. Write the sequence of decisions that would guarantee it fails within a year, where every decision looks smart on the day it's made. Number them."
2. "Which of these have I already made? Be specific."
3. "For the ones I've made, what's the cheapest way to reverse each?"

### The Taste Test
Command: `taste`
The user pastes ten things in their field they love and ten they can't stand. Use when you know what good looks like to you but cannot say why, or your current work feels off and you cannot name the problem.
1. "Here are ten things in my field I love: [list]. Ten I can't stand: [list]. Write the rules I follow without knowing I follow them, as rules, not observations."
2. "Here is what I'm building now: [paste or point at the folder]. Where am I breaking my own rules?"
3. "Which rule, if I followed it here, changes the most?"

### What Would Have To Be True
Command: `true`
The user pastes their plan first. Use before committing time or money, to find the one assumption the whole plan quietly depends on.
1. "My plan: [paste]. List everything that would have to be true for this to work, ranked by how unlikely each one is."
2. "Which one can I check this week, and how, in one step?"
3. "If the most unlikely one is false, what's the plan?"

### The Flip
Command: `flip`
Runs after any answer, so the user pastes nothing new. Use when an answer sounds convincing and you want to know whether it is right or just well argued.
1. "Argue the opposite exactly as hard as you argued that."
2. "Which of the two arguments did you have to stretch more to make, and where?"
3. "What evidence would settle it?"

### The Bio
Command: `bio`
The user pastes their last thirty days: calendar, git log, notes. Use when how you describe yourself and how you spend your time may have drifted apart.
1. "Here are my last thirty days: [calendar, git log, notes]. Write the one-line bio of the person who lived this month, from the evidence only, not from how I describe myself."
2. "Write the same line for a year from now if nothing changes."
3. "Which single week, changed, moves the second line the most?"
