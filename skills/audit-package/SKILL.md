---
name: audit-package
description: Before cloning or installing any package or repo, stop, inspect it, report what it is and what it does, give a verdict, and wait for the human.
---

# audit-package

Installing a package runs someone else's code on this machine. This skill makes that a decision the human takes on purpose, with the facts in front of them.

## When this runs

Run it any time the task would run one of these:

- `npm install`, `pnpm add`, `yarn add`
- `pip install`, `uv add`
- `cargo add`, `go get`
- `git clone`
- `npx <anything>`

Also run it before adding a dependency to a lockfile or manifest by hand, and when the human pastes a package name or repo URL and asks about it.

If the request is to install, do the audit first. Do not install until the human answers.

## Hard rules

- Never run the install or the clone before reporting.
- Never execute anything from the package. No scripts, no binaries, no `npx`, no imports.
- Never print, open, or quote a secret value. If the package reads one, name the variable, not its value.
- Read metadata and source only. Download source as a tarball or file into a new, empty temp folder. Don't clone, and don't use the package manager to fetch it.
- If a check can't be done, write "could not check" and why. Never guess.

## The five checks

Work in a fresh temp folder. Get the source first.

- npm: `npm view <pkg> dist.tarball`, then download that URL with `curl` and extract it.
- PyPI: `https://pypi.org/pypi/<pkg>/json` lists each file's `url` and `digests.sha256`. Download the wheel or sdist with `curl`. Don't use `pip download`. It does the same resolution as `pip install`, and for an sdist that means preparing metadata with the package's build backend.
- GitHub: download the archive for the tag or commit instead of cloning.

### 1. Maintainer and age

- npm: `npm view <pkg> maintainers repository.url time.created _npmUser`.
- PyPI: the JSON above. `info.author`, `info.maintainer` and `info.project_urls`. The age is the earliest upload time in `releases`.
- GitHub: the repo page or `gh repo view <owner>/<repo>`. Owner, creation date, contributors.

Report who publishes it, how long the project has existed, and how many maintainers it has. Say whether the publisher matches the owner of the repo the README points to. A mismatch is not proof of anything, but it goes in the table.

### 2. Publish timing

- npm: `npm view <pkg> time --json` gives every version's publish date. `npm view <pkg>@<version> _npmUser` gives who published each one.
- PyPI: `upload_time_iso_8601` for each file in `releases`. The JSON doesn't say which account uploaded a file. Write "could not check" for the publisher part.

Compare the latest version's date with the cadence of the previous few. Flag:

- anything published in the last 7 days
- a gap pattern that suddenly changed, like a project quiet for two years that ships three versions in a day
- a version published from a different account than the ones before it

### 3. Install-time execution

- npm: the `preinstall`, `install` and `postinstall` keys in `scripts` in the package's `package.json`. Also a `binding.gyp` file, which makes npm run a native build.
- PyPI: a wheel (`.whl`) installs without a build step. An sdist is built on install, which runs its build backend, so read `setup.py`, `pyproject.toml` and any build hooks.
- Cargo: a `build.rs` in the crate root. Cargo compiles and runs it before building the crate.
- Anything else: any script the tool runs on install.

If there is a script, quote the script line itself, like `"postinstall": "node install.js"`. Then read the file it runs and note what it does: network, environment, child processes, writes outside the package folder.

### 4. Environment and network on load

Grep the package source for:

```
process.env  os.environ  .env  environ  fetch  http  net  child_process  subprocess  eval  base64
```

Search for `.env` and `environ` on their own as well, because code often aliases `process` and reads `p.env`. A search for `process.env` alone misses that.

List file and line for each hit, not contents. Then say in plain words what the hits add up to, like "reads color settings from env" or "spawns its own binary". Look for long base64 strings and decode them in your head, not by running anything.

### 5. Dependency footprint

- npm: in an empty temp folder, `npm init -y`, then `npm install <pkg> --package-lock-only --ignore-scripts`. This resolves the full tree into `package-lock.json` without installing anything into `node_modules`. Count the entries under `packages`.
- PyPI: `info.requires_dist` lists direct dependencies. For the full tree, run `uv pip compile --no-build` on a one-line requirements file. It resolves without installing and refuses to build source distributions. If you can't resolve it, say "could not check".

Then:

- count the transitive dependencies
- count how many come from publishers that don't appear anywhere in the human's existing lockfile
- flag any dependency that was itself published in the last 7 days

## The report

Always this format. The human should be able to scan it in ten seconds.

| Check | Finding | Risk |
| --- | --- | --- |
| Maintainer and age | ... | low / medium / high |
| Publish timing | ... | low / medium / high |
| Install-time execution | ... | low / medium / high |
| Env and network on load | ... | low / medium / high |
| Dependency footprint | ... | low / medium / high |

Verdict: install / install with `--ignore-scripts` / don't

One line of why.

Waiting for you.

Then stop. Don't run anything else.

## Verdict rules

**don't** is reserved for these three:

- an install-time script contacts any host other than the package's own official registry
- an install-time script reads an env name that contains KEY, TOKEN, SECRET, PASSWORD, AWS or SSH
- a version was published less than 7 days ago from an account that didn't publish the previous versions

**install with `--ignore-scripts`** if:

- an install script reads env and downloads only from the package's own official registry host, and that behavior is documented in its README or official docs, or
- install scripts exist but look benign, or
- publish timing is odd but everything else is clean

With this verdict, tell the human to read the script before they enable it. If the install behavior isn't documented anywhere, say so in the finding.

**install** if every check is clean.

Timing flags alone never produce "install". They produce `--ignore-scripts`.

`--ignore-scripts` is npm's name. Use the matching option for the tool:

| Tool | How to skip install-time code |
| --- | --- |
| npm | `npm install --ignore-scripts` |
| Yarn 1 | `yarn add --ignore-scripts` |
| Yarn 2 and later | Third-party postinstall scripts are off unless `enableScripts` is set to true. Leave it off. |
| pnpm | Dependency build scripts don't run until approved in `allowBuilds`. Don't approve this one. |
| pip | `pip install --only-binary :all: <pkg>` installs wheels only, so no sdist build runs. It fails if there's no wheel. |
| uv | `uv add --no-build <pkg>` refuses to build source distributions. |
| Cargo | There is no flag to skip `build.rs`. Say so, and the verdict is don't until the human has read it. |

## After the verdict

If the human says "go":

1. Run the install exactly as decided. Same package, same version, same flags.
2. Check that what landed is what you audited:
   - npm: `npm ls <pkg>` for the version, and the `integrity` field for the package in `package-lock.json`. It must equal the `dist.integrity` you saw in `npm view`.
   - uv: the version and `hash` in `uv.lock` against the `sha256` from the PyPI JSON.
   - pip without a lockfile: `pip show <pkg>` for the version. With no lockfile that records hashes, write "could not check" for the hash.
3. Report in one short block: version audited, version installed, hash match yes or no.

If anything doesn't match, say so first, and stop.

If the human says anything other than "go", do what they say. Don't install.

## Examples

Two filled-in reports, one clean package and one with a postinstall script, are in [references/worked-examples.md](references/worked-examples.md).
