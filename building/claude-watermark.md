# Claude's Text Watermark

Claude now weaves an invisible mark into the text it writes. This is what it actually is, what it can and cannot prove, and the three things worth doing about it.

Everything here comes from [Anthropic's announcement](https://www.anthropic.com/news/claude-text-watermark). Where I have added an opinion, it says so.

## What it actually is

When Claude writes, there are constant moments where several words fit equally well and the sentence works whichever one it takes. Those choices used to be settled with randomness. Now they are settled using a hidden key combined with the words that came before, so the choice looks random from the outside but is determined, and over enough text the pattern becomes findable by anyone holding that key.

The method is a version of SynthID-Text, published by Google DeepMind in Nature in 2024, so it is a documented approach rather than something invented privately.

The most important thing to understand is that **the mark is not a hidden character and it is not metadata buried in the file. It is the word choices themselves.** Every other property follows from that. It survives copying and pasting into anything. It degrades as you rewrite the sentences. It barely works on short passages, because a handful of words does not provide enough decisions to be confident about.

It carries no information about you, your account, or your conversation. It has no effect on speed, cost, or token usage.

## What is marked and what is not

| Marked | Barely or not marked |
|---|---|
| Text Claude generates from scratch | Text you wrote that Claude only proofread |
| Long passages, where there are enough choices | Short passages, too few choices to be confident |
| Text you copy and paste elsewhere | Code where an exact output is required |
| | Factual passages with only one correct phrasing |
| | Anything you rewrite substantially in your own words |

Images work on a completely different mechanism. Supported file types get signed provenance metadata attached to the file rather than anything hidden in the picture, which means it comes off the moment somebody screenshots or re-encodes it.

## Which models, which products

This applies to **Claude models launched on or after 2 August 2026**. Models released before that date are not covered, which is a detail most coverage has skipped.

It applies across claude.ai, the Claude Platform API, Claude Code, Cowork, Claude Tag, and Claude accessed through AWS, Google Cloud and Microsoft Foundry.

The trigger is Article 50 of the EU AI Act, which became enforceable on the same date and requires providers to embed machine-readable marks in generative AI output. Anthropic signed the accompanying Code of Practice along with roughly 190 other organisations, so this is an industry-wide obligation rather than one company's decision.

## What it proves, and what it does not

It tells you Claude was probably involved somewhere in producing that text. That is the whole claim.

It cannot tell the difference between Claude writing something from scratch and Claude lightly editing something you wrote, because both come back carrying the same kind of signal. A mark is not proof a machine wrote something. The absence of a mark is not proof a human did, since a full rewrite removes it and any other tool leaves nothing.

This matters because employers, clients and institutions are already treating detector output as settled proof of authorship, and it was never built to carry that weight. A detection API is listed as coming soon, which means more people will be running these checks shortly.

## Three things to do

### 1. Change where Claude sits in your work

The mark measures how much of the wording came from Claude. Anthropic's own carve-out is that text you wrote yourself and Claude only proofread has generally been lightly edited, so it carries little or no mark.

So the practical move is to stop having Claude produce your sentences and start having it pressure test them. Let it argue with your draft, find what you left out, and tell you which assumption is weakest, then you write the words.

That is a better way to work regardless of watermarking, which is the part worth sitting with. The mark did not create this trade-off, it just made it visible.

### 2. Say how you work before anybody asks

One line, somewhere people can see it. A stated process turns a future detector result from an accusation into something you already disclosed.

Adapt one of these rather than pasting it as is, because it should be true of you specifically:

> I use AI to pressure test and edit. The words are mine.

> Research and structure are AI assisted. Drafting and final copy are mine.

> This was drafted with AI assistance and edited by me.

Put it where the work lives. A site footer, an about page, a proposal template, a contract clause, a repo README.

If you are a student, this does not substitute for your institution's rules. Find their actual policy and follow that, because it will be more specific than anything general.

### 3. Know the limits well enough to say them

If this ever gets raised about your work, the accurate things to say are that the mark indicates involvement rather than authorship, that it cannot distinguish generated text from edited text, and that it is unreliable on short passages.

That is not a way to talk your way out of something. If AI wrote your words, the answer is the disclosure in step two, not a clever line. The reason to know the limits is so that a weak signal does not get treated as a strong one, in either direction.

## What this does not cover

This is one company's watermark. Other providers have made different choices, third party detectors are a separate and much less reliable category, and none of this tells you anything about text produced before August 2026.

If your work carries real professional or legal exposure, get advice specific to your situation rather than relying on a summary.

## Sources

- [How Claude's text watermark works](https://www.anthropic.com/news/claude-text-watermark), Anthropic
- SynthID-Text, Google DeepMind, published in Nature, 2024
- EU AI Act Article 50, enforceable 2 August 2026

---

This does not change how to use AI well. It just makes it visible whether you were.
