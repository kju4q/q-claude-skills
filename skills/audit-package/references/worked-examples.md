# Worked examples

Two real npm packages, audited on October 27, 2026 by following the five checks in [SKILL.md](../SKILL.md). Each was downloaded as a tarball into an empty temp folder. Neither was installed, and nothing from either was run.

The dependency counts come from `npm install <pkg> --package-lock-only --ignore-scripts` in an empty project. There was no existing lockfile to compare publishers against, so that part says "could not check". In a real project you'd compare against your own lockfile.

Registry data changes. Run the checks again before you rely on any of this.

## 1. A clean package: picocolors 1.1.1

What I ran:

```
npm view picocolors maintainers repository.url time.created _npmUser dist.integrity
npm view picocolors time --json
npm view picocolors@1.1.0 _npmUser
npm view picocolors dist.tarball
```

The report:

| Check | Finding | Risk |
| --- | --- | --- |
| Maintainer and age | One maintainer, alexeyraspopov. First published 2021-09-27, so about five years old. Repo is github.com/alexeyraspopov/picocolors, the same name as the publisher. | low |
| Publish timing | 1.1.1 published 2024-10-16. The three before it were 2024-09-02, 2024-05-14 and 2021-10-13. All four published by alexeyraspopov. Nothing in the last 7 days. | low |
| Install-time execution | No `scripts` field in package.json. No `binding.gyp`. | low |
| Env and network on load | picocolors.js:1. It reads color settings from env through an alias of `process`. No network, no child processes, no eval, no base64. | low |
| Dependency footprint | 0 dependencies. Publisher comparison against an existing lockfile: could not check, no lockfile. | low |

Verdict: install

Every check is clean, and the one env read is for color settings.

Waiting for you.

Worth noticing: a grep for `process.env` alone finds nothing in this package. The env read on line 1 only shows up when you also search for `.env`, which is why the skill tells you to.

After "go", the check is `npm ls picocolors` showing 1.1.1, and the `integrity` in `package-lock.json` matching `sha512-xceH2snhtb5M9liqDsmEw56le376mTZkEX/jEb/RxNFyegNul7eNslCXP9FDj/Lcu0X8KEyMceP2ntpaHrDEVA==`.

## 2. A package with a postinstall script: esbuild 0.28.2

What I ran:

```
npm view esbuild maintainers repository.url time.created _npmUser scripts dist.integrity
npm view esbuild time --json
npm view esbuild@0.28.1 _npmUser
npm view esbuild dist.tarball
```

The report:

| Check | Finding | Risk |
| --- | --- | --- |
| Maintainer and age | One maintainer account, esbuild. First published 2017-11-26, so about nine years old. Repo is github.com/evanw/esbuild. Versions are published by GitHub Actions through npm trusted publishing, not a personal account. | low |
| Publish timing | 0.28.2 published 2026-08-08. The three before it were 2026-06-11, 2026-04-02 and 2026-04-02. All four published by the same GitHub Actions trusted publisher. Nothing in the last 7 days. | low |
| Install-time execution | `"postinstall": "node install.js"`. install.js reads env (29, 141, 181), runs child processes (103, 121, 187), and has an HTTPS download from registry.npmjs.org (147, 149, 245, 248). | high |
| Env and network on load | lib/main.js: 1709, 1893, 2009, 2023, 2029, 2081, 2088, 2272, 2376, 2384, 2398. It reads its own settings from env and spawns its own binary. The rest are URLs in comments and error messages, and one regex that parses stack traces. | medium |
| Dependency footprint | 26 optional platform packages, all @esbuild/*, all version 0.28.2. Only the one for your platform installs. All 26 published 2026-08-08 by the same GitHub Actions trusted publisher. None in the last 7 days. Publisher comparison against an existing lockfile: could not check, no lockfile. | low |

Verdict: don't

The postinstall script touches both the network and the environment, and the rules say that's a don't, even for a project this established.

Waiting for you.

This is the rule doing its job, not a claim that esbuild is malicious. The download in install.js is a fallback for when the platform package didn't install. Whether that's acceptable is the human's call, made after reading install.js. If they read it and still want it, they can say so and the agent installs it as told.
