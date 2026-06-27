# GitHub Growth Kit

Use this checklist to make the GitHub repo easier to discover, evaluate, and contribute to.

## Repository Topics

Add these topics in GitHub repository settings:

```text
python
dotenv
cli
devtools
developer-tools
environment-variables
configuration
config
fastapi
django
ci
github-actions
open-source
```

## Labels

Create these labels:

| Label | Color | Description |
| --- | --- | --- |
| `good first issue` | `7057ff` | Small, well-scoped contribution for new contributors |
| `help wanted` | `008672` | Useful contribution from the community |
| `feedback wanted` | `fbca04` | Needs real-world project feedback |
| `false-positive` | `d876e3` | envgap warned about a valid project pattern |
| `framework:pydantic` | `1d76db` | Pydantic or pydantic-settings support |
| `framework:django` | `092e20` | Django settings support |
| `area:docs` | `0075ca` | README, examples, docs, launch material |
| `area:ci` | `5319e7` | CI, exit codes, annotations, automation |
| `area:parser` | `c5def5` | dotenv, Python AST, or future config parsers |
| `needs reproduction` | `d93f0b` | Needs a smaller example to debug |
| `roadmap` | `0e8a16` | Planned feature or milestone item |

## Starter Issues

### 1. Add Pydantic BaseSettings detection

Labels: `help wanted`, `roadmap`, `framework:pydantic`

```markdown
envgap should detect required environment variables declared through Pydantic Settings classes.

Initial scope:

- detect classes inheriting from `BaseSettings`
- read annotated fields
- required when a field has no default
- optional when a field has a default
- map `database_url` to `DATABASE_URL`
- include file and line number in findings
- add tests and a FastAPI/Pydantic example

Later scope, not required here:

- aliases
- `env_prefix`
- nested settings
- Pydantic v1/v2 edge cases
```

### 2. Add Docker Compose env detection

Labels: `help wanted`, `roadmap`, `area:parser`

```markdown
envgap should understand common Docker Compose environment patterns so it can explain local-vs-container drift.

Useful first scope:

- parse `compose.yml`, `docker-compose.yml`, and `docker-compose.yaml`
- detect `environment:` keys
- detect `env_file:`
- report variables used by Docker but missing from `.env.example`
- avoid reading secrets from unrelated files

This should stay diagnostic: envgap should explain what it found, not mutate compose files.
```

### 3. Improve typo detection examples and false-positive coverage

Labels: `good first issue`, `feedback wanted`, `false-positive`

```markdown
envgap currently detects likely typo pairs such as `DB_URL` vs `DATABASE_URL`.

This issue is for collecting and testing real-world examples:

- helpful matches that envgap should catch
- false positives it should avoid
- abbreviations to support, such as `cfg` -> `config`

Please add tests for any behavior change.
```

### 4. Add GitHub Actions annotation output

Labels: `help wanted`, `area:ci`, `roadmap`

```markdown
In CI, envgap could optionally print GitHub Actions annotations so missing keys appear inline in pull request logs.

Possible command:

```console
envgap check --format github
```

Initial scope:

- emit `::error file=...,line=...::...` for errors with locations
- emit `::warning file=...,line=...::...` for warnings with locations
- keep existing terminal and JSON output unchanged
- add tests for escaping annotation text
```

### 5. Add a comparison docs page

Labels: `good first issue`, `area:docs`

```markdown
Add a short docs page explaining how envgap differs from:

- python-dotenv
- pydantic-settings
- django-environ
- secret scanners

The key message: those tools load, validate, or protect config; envgap diagnoses drift between code, docs, local files, and shell env.
```

## Suggested Milestones

- `v0.2 Pydantic/FastAPI`
- `v0.3 Docker and CI`
- `v0.4 Django`

## GitHub Description

Use this repository description:

```text
Find gaps between .env, .env.example, shell variables, and Python code.
```

## Website

Use the PyPI URL or README until a docs site exists:

```text
https://pypi.org/project/envgap/
```
