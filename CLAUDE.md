# CLAUDE.md

Guidance for Claude Code (and humans) working in this repository.

## What this project is

`cvxball` computes the smallest enclosing sphere (minimum enclosing ball) of a
set of points. The library lives in `src/cvxball/` and exposes two solvers:

- `min_circle_cvx` — models the problem in CVXPY and dispatches to a backend
  (default CLARABEL).
- `min_circle_clarabel` — assembles the second-order-cone program directly and
  calls Clarabel, skipping CVXPY canonicalisation.

## Ownership split: locally-owned vs Rhiza-synced

This repo syncs its dev infrastructure from the
[`jebel-quant/rhiza`](https://github.com/jebel-quant/rhiza) template. The pinned
template version and platform profile live in `.rhiza/template.yml`; the exact
machine-generated list of synced files is the `files:` block of
`.rhiza/template.lock`. When assessing or changing this repo, keep the two sides
distinct — fix locally-owned code here, fix synced infrastructure upstream in
Rhiza (then re-sync).

### Locally owned (change these here)

- `src/cvxball/` — the library source.
- `tests/` — the project's own test suite (`tests/test_solver.py`).
- `pyproject.toml` — project metadata, dependencies, and local tool config
  (`[tool.deptry]`, `[tool.mypy]` overrides, `[tool.ty]`).
- `README.md` and any project-specific documentation.
- `.rhiza/template.yml` — selects the template version (`template-branch`) and
  platform profile (`profiles`). This file is *configuration you own*, even
  though it lives under `.rhiza/`.
- Any `stubs/` type stubs added to type third-party dependencies.

### Rhiza-owned (do not edit in place — change upstream and re-sync)

Everything listed in `.rhiza/template.lock`'s `files:` block, including:

- `.github/workflows/*` — CI, release, CodeQL, scorecard, benchmark, etc.
- `Makefile` and `.rhiza/make.d/*.mk`, `.rhiza/rhiza.mk` — the build/quality targets.
- `.pre-commit-config.yaml`, `pytest.ini`, `.bandit`, `.editorconfig`.
- `.rhiza/requirements/*.txt`, `.rhiza/utils/*`, `.rhiza/tests/*` — the template's
  own tooling and self-tests.
- `.claude/commands/*` — the synced slash commands.

Editing a synced file locally causes `make validate` to report drift. To change
Rhiza-owned behavior, open a PR against `jebel-quant/rhiza`, cut a template
release, then bump `template-branch` in `.rhiza/template.yml` and run `make sync`.

## Quality gates

Run individual gates with bare `make <target>` (matches the allow-listed rule):

| Target | Checks |
|---|---|
| `make fmt` | pre-commit hooks (ruff format/check, markdownlint, bandit, actionlint, …) |
| `make typecheck` | `ty check` + `mypy --strict` over `src/` (and `.rhiza/utils`) |
| `make docs-coverage` | interrogate docstring coverage (100% required) |
| `make deptry` | unused/missing/misplaced dependency analysis over `src/` |
| `make security` | pip-audit + bandit |
| `make validate` | project structure vs the Rhiza template |
| `make test` | full test suite with its coverage gate (`COVERAGE_FAIL_UNDER`, ≥90%) |

The project test suite (`tests/`) covers `src/cvxball/` at 100%. `make validate`
separately runs the Rhiza template self-tests (`.rhiza/tests/`); those are
Rhiza-owned.
