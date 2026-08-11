# Check Your App

Three checks for the three holes that show up in almost everything built with AI. Together they take about fifteen minutes.

None of this is because AI is careless. You described a feature and it built the feature, and the part that keeps strangers out was never in the description, which is why the same three holes turn up over and over.

**This assumes your code is open in Claude Code or Cursor,** so that whatever you are running the prompts in can actually read your project files. If you built on Lovable, Bolt, or Replit and have never opened the code, you can still do the manual check in each section, since those need nothing but your live site and a browser.

Run the prompts one at a time and read the answers properly rather than skimming for a green tick.

---

## 1. Is your database open?

Your app stores what your users type. That store comes with rules about who is allowed to read it, and those rules are off by default on every major service. Nobody turns them on, because turning them on was never part of building the feature.

**Run this:**

```
Look at this project and tell me how it talks to its database or storage.

Then answer these one at a time:
1. Which service is it (Supabase, Firebase, or something else)?
2. For every table or storage bucket, is there a rule restricting who can
   read and write it, or can any visitor read everything?
3. Show me the exact file and line where each rule is defined, or tell me
   plainly that no rules exist anywhere in this project.
4. If a stranger opened my app, pulled the connection details out of it,
   and queried the database directly, what could they read?

Do not reassure me. If you cannot tell, say you cannot tell and say why.
```

Question four is the one that matters, because it forces a real answer instead of a box being ticked.

**Then check the dashboard, because the code cannot tell you this.** Rules often live in the service rather than in your repo, so Claude reading your project genuinely cannot see them. In Supabase, open Table Editor and look for the row level security indicator on each table. In Firebase, open Rules and look at whether they read `allow read, write: if true`, which means anyone.

**What a bad answer looks like:** any table with no rule, any storage bucket that is public when it holds anything a user uploaded, or Claude telling you it cannot find rules anywhere.

**The fix is a setting, not a rebuild.** Turn row level security on, then add a policy saying a user can only see their own rows. Ask Claude to write the policy for your specific table and paste it into the dashboard.

---

## 2. Is a real secret sitting in your frontend?

This is where most checklists get it wrong, so read the distinction before you panic.

Some keys are meant to be public. A Supabase anon key and a Firebase config are designed to sit in the browser, and they are safe **only** because the rules from check one are supposed to be doing the actual protecting. Other keys are catastrophic in the browser and there is no version of it being fine.

| Safe in the browser | Never in the browser |
|---|---|
| Supabase `anon` key, if RLS is on | Supabase `service_role` key |
| Firebase config, if Rules are set | Database password or connection string |
| Publishable Stripe key (`pk_`) | Secret Stripe key (`sk_`) |
| | OpenAI or Anthropic API keys |

**The ten second version.** Open your live site, right click, View Page Source, then search the page for `service_role`, `sk-`, `sk_live`, `password`, and `secret`. Anything in the right hand column above showing up here is a problem right now, not a theoretical one.

**Run this for the thorough version:**

```
Search this project for credentials that get sent to the browser.

For each one, tell me:
1. The file and the line.
2. Exactly which key it is. A Supabase anon key or a Firebase config are
   meant to be public. A service_role key, a database password, or an
   OpenAI, Anthropic or Stripe secret key are not.
3. Whether it ends up in code the visitor downloads, or only in code that
   stays on the server.
4. Whether any of them are committed to git, including in older commits
   that are no longer in the current files.

Sort them worst first. Do not tell me a key is fine just because it is
common to see it there.
```

Point four catches the one people miss. Deleting a key from a file does not remove it from your git history, and history is public on a public repo.

**The fix.** Move real secrets to server side environment variables so they never reach the browser. If a secret was ever committed, rotate it, because removing it from the code does not un-share it.

---

## 3. Does anything check who is asking?

Your app has doors. One to sign up, one to load a profile, one to pull records. AI builds the doors reliably. What it does not always build is the part that checks whether the person walking through is allowed through that particular one.

There are two separate checks here and most code only has the first. Being logged in is not the same as being allowed to see this specific record.

**Run this:**

```
List every route, endpoint, or server function in this project.

For each one, tell me:
1. Does it check that the caller is logged in?
2. Does it check that the caller owns the specific record they are asking
   for, or does it just trust an ID that came in with the request?
3. What happens if someone logged in as user A changes the ID in the
   request to user B's?

Those are two different checks. Show me the ones that have neither first,
then the ones that only have the first.
```

**The manual version, on your own app only.** Make two test accounts. Log in as the first, find a URL or a request with an ID in it, and change that ID to the second account's. If you can see the second account's data while logged in as the first, that door is open. Use accounts you created, on software you own, and nothing else.

**The fix.** Every query that fetches a record should filter by the logged in user's id on the server, rather than trusting an id that arrived from the browser.

---

## If you find something

Fix the database rules first. It is usually one setting, it is the one with the worst outcome if ignored, and it is often what makes an exposed key harmless.

Then rotate any secret that reached the browser or the git history, then close the doors.

Do not paste your findings anywhere public, including into a post about how you fixed it, until it is actually fixed.

---

## What this does not cover

Three checks is not a security review. This will not find cross site scripting, out of date dependencies with known vulnerabilities, missing rate limits, or an endpoint that calls a paid API with no cap and quietly runs up a bill.

It covers the three that account for most of what goes wrong in apps built quickly, which is a good afternoon's work and not a certificate.

If your app handles payments, health information, or identity documents, get someone who does this professionally to look at it. The stakes are different and so is the standard.

---

These are not bugs. AI built exactly what you described, and you described what you wanted to happen rather than what you wanted to stop.
