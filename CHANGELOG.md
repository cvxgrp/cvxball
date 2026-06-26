# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com),
and entries are generated from [Conventional Commits](https://www.conventionalcommits.org).

## [1.0.2] - 2026-06-26

### Maintenance
- Chore(deps)(deps): bump starlette from 0.52.1 to 1.0.1 (#260)
- Chore(deps)(deps): bump the github-actions group with 9 updates (#261)
- Chore(deps)(deps): bump the python-dependencies group with 7 updates (#262)
- Add Rhiza Claude commands (#263)
- Chore(deps)(deps): bump the github-actions group with 2 updates

### Other Changes
- Bump rhiza template ref v0.18.4 → v0.19.5
- Sync Rhiza template v0.18.4 → v0.19.5
- Satisfy stricter v0.19.5 gates (ruff ANN, mypy --strict)
- Change copyright from Jebel Quant Research to cvxgrp (#264)
- Remove 'templates' section from template.yml (#265)
- Merge branch 'main' into sync/rhiza-v0.19.5
- Make API docs build in the isolated zensical env (src-layout)
- Use `**kwargs: Any` in min_circle_cvx
- Add property-based and degenerate-input coverage
- Document solver selection (cvx vs clarabel) in README
- Merge pull request #271 from cvxgrp/improve/quality-followups
- Merge pull request #266 from cvxgrp/sync/rhiza-v0.19.5
- Use cp.multiply to avoid deprecated CVXPY *-as-matmul in min_circle_cvx
- Merge pull request #272 from cvxgrp/dependabot/github_actions/github-actions-08d4ebc5fb
- Merge branch 'main' into fix/273-cvxpy-multiply-deprecation
- Merge pull request #274 from cvxgrp/fix/273-cvxpy-multiply-deprecation

## [1.0.1] - 2026-06-04

### Bug Fixes
- *(typecheck)* Suppress ty unresolved-attribute for clarabel extension

### Maintenance
- Chore(deps)(deps): bump the github-actions group with 4 updates (#234)
- Chore(deps)(deps): bump the python-dependencies group with 8 updates (#235)
- *(rhiza)* Sync to v0.10.6 template (#236)
- *(rhiza)* Add github-tests, github-book, github-marimo bundles
- *(rhiza)* Restore missing github-* bundle workflows
- Increase coverage to 100% by testing error paths
- Chore(deps)(deps): bump github/codeql-action in the github-actions group (#238)
- Chore(deps)(deps): bump the python-dependencies group with 3 updates (#239)
- Update via rhiza (#240)
- Chore(deps)(deps): bump pillow from 12.1.1 to 12.2.0 (#241)
- Chore(deps)(deps): bump pygments from 2.19.2 to 2.20.0 (#242)
- Chore(deps)(deps): bump github/codeql-action in the github-actions group (#243)
- Chore(deps)(deps): bump the python-dependencies group with 3 updates (#244)
- Sync .github/workflows and .rhiza/tests from cvxrisk (#246)
- Chore(deps)(deps): bump idna from 3.11 to 3.15 (#247)
- Chore(deps)(deps): bump pymdown-extensions from 10.21.2 to 10.21.3 (#248)
- Update rhiza to v0.15.1 (#250)
- Update rhiza to v0.15.2 (#251)
- Chore(deps-dev)(deps-dev): bump marimo from 0.23.6 to 0.23.8 in the python-dependencies group (#252)
- Update rhiza to v0.17.0 (#253)
- Update rhiza to v0.18.4 (#254)
- Add pip dependabot entry for .rhiza/requirements
- Chore(deps)(deps): bump cvxpy-base in the python-dependencies group (#256)
- Chore(deps)(deps): bump the github-actions group with 8 updates (#255)
- Chore(deps-dev)(deps-dev): bump the python-dependencies group with 3 updates (#259)
- Chore(deps)(deps): bump the github-actions group with 9 updates (#258)

### Other Changes
- Bypass CVXPY: direct Clarabel solver for minimum enclosing ball (#233)
- Mkdocs
- Lock file
- Update mkdocs.yml
- Update template.yml
- Bump version 1.0.0 → 1.0.1

## [1.0.0] - 2026-02-24

### Dependencies
- *(deps)* Lock file maintenance (#172)
- *(deps)* Lock file maintenance (#175)
- *(deps)* Update dependency mosek to v11.1.2 (#177)
- *(deps)* Lock file maintenance (#179)
- *(deps)* Update dependency astral-sh/uv to v0.9.26 (#181)
- *(deps)* Update dependency mosek to v11.1.3 (#182)
- *(deps)* Update ghcr.io/astral-sh/uv docker tag to v0.9.26 (#183)
- *(deps)* Update pre-commit hook astral-sh/ruff-pre-commit to v0.14.13 (#184)
- *(deps)* Lock file maintenance (#185)
- *(deps)* Update pre-commit hook python-jsonschema/check-jsonschema to v0.36.1 (#187)
- *(deps)* Update dependency astral-sh/uv to v0.9.27 (#188)
- *(deps)* Update ghcr.io/astral-sh/uv docker tag to v0.9.27 (#189)
- *(deps)* Lock file maintenance (#190)
- *(deps)* Update pre-commit hook abravalheri/validate-pyproject to v0.25 (#194)
- *(deps)* Update dependency astral-sh/uv to v0.9.28 (#192)
- *(deps)* Update ghcr.io/astral-sh/uv docker tag to v0.9.28 (#193)
- *(deps)* Lock file maintenance (#195)
- *(deps)* Update dependency mosek to v11.1.5 (#197)
- *(deps)* Update dependency astral-sh/uv to v0.10.0 (#198)
- *(deps)* Update pre-commit hook astral-sh/ruff-pre-commit to v0.15.0 (#200)
- *(deps)* Update ghcr.io/astral-sh/uv docker tag to v0.10.0 (#199)
- *(deps)* Update dependency astral-sh/uv to v0.10.1 (#202)
- *(deps)* Update pre-commit hook jebel-quant/rhiza-hooks to v0.2.1 (#204)
- *(deps)* Update pre-commit hook astral-sh/uv-pre-commit to v0.10.1 (#203)
- *(deps)* Lock file maintenance (#205)
- *(deps)* Lock file maintenance (#206)
- *(deps)* Update dependency astral-sh/uv to v0.10.3 (#209)
- *(deps)* Update dependency mosek to v11.1.6 (#210)
- *(deps)* Update pre-commit hook astral-sh/ruff-pre-commit to v0.15.1 (#212)
- *(deps)* Update pre-commit hook python-jsonschema/check-jsonschema to v0.36.2 (#214)
- *(deps)* Update github/codeql-action action to v4.32.3 (#211)
- *(deps)* Update pre-commit hook astral-sh/uv-pre-commit to v0.10.3 (#213)
- *(deps)* Update pre-commit hook rhysd/actionlint to v1.7.11 (#215)
- *(deps)* Update pre-commit hook jebel-quant/rhiza-hooks to v0.3.0 (#216)
- *(deps)* Lock file maintenance (#217)
- *(deps)* Update dependency astral-sh/uv to v0.10.4 (#219)
- *(deps)* Update github/codeql-action action to v4.32.4 (#220)
- *(deps)* Update dependency astral-sh/uv to v0.10.5 (#224)
- *(deps)* Update pre-commit hook astral-sh/uv-pre-commit to v0.10.5 (#222)
- *(deps)* Update pre-commit hook astral-sh/ruff-pre-commit to v0.15.2 (#221)
- *(deps)* Update dependency astral-sh/uv to v0.10.5 (#228)

### Maintenance
- Update via rhiza (#176)
- Sync with rhiza (#186)

### Other Changes
- Delete .rhiza.env (#178)
- Fix CI badge link in README.md
- Fix path for cvxball in soc.py
- Delete tests/test_rhiza directory
- Sync (#201)
- Update template.yml (#208)
- Clean up bumpversion configuration (#225)
- Update template branch to v0.8.3 (#226)
- Add renovate.json (#227)
- Bump version 0.1.0 → 1.0.0

## [0.1.0] - 2026-01-02

### Dependencies
- *(deps)* Update dependency astral-sh/uv to v0.9.21 (#166)
- *(deps)* Update ghcr.io/astral-sh/uv docker tag to v0.9.21 (#167)
- *(deps)* Update pre-commit hook rhysd/actionlint to v1.7.10 (#168)
- *(deps)* Lock file maintenance (#169)

### Maintenance
- Import rhiza templates

### Other Changes
- Shorten the notebook
- Update README
- Rhiza
- Rhiza
- Delete .github/CONFIG.md (#165)
- Migrate
- Remove dependabot
- Convert optional dependencies to dependency groups
- Sync
- Update pyproject.toml
- [WIP] Change structure from cvx/ball/solver to cvxball/solver (#171)
- Update README.md
- Add classifiers and license information
- Fmt
- Current version

## [0.0.24] - 2025-12-18

### Bug Fixes
- *(deps)* Update dependency mosek to v11.0.14 (#141)
- *(deps)* Update dependency mosek to v11.0.16 (#148)
- Fixing tests

### Dependencies
- *(deps)* Update pre-commit hook abravalheri/validate-pyproject to v0.24.1 (#131)
- *(deps)* Update pre-commit hook astral-sh/ruff-pre-commit to v0.11.2 (#132)
- *(deps)* Lock file maintenance (#134)
- *(deps)* Update pre-commit hook python-jsonschema/check-jsonschema to v0.32.1 (#136)
- *(deps)* Update pre-commit hook crate-ci/typos to v1.31.0 (#135)
- *(deps)* Update pre-commit hook crate-ci/typos to v1.31.1 (#137)
- *(deps)* Update ghcr.io/astral-sh/uv docker tag to v0.6.12 (#139)
- *(deps)* Update pre-commit hook astral-sh/ruff-pre-commit to v0.11.3 (#140)
- *(deps)* Update pre-commit hook astral-sh/ruff-pre-commit to v0.11.4 (#142)
- *(deps)* Lock file maintenance (#143)
- *(deps)* Update ghcr.io/astral-sh/uv docker tag to v0.6.13 (#144)
- *(deps)* Update ghcr.io/astral-sh/uv docker tag to v0.6.14 (#146)
- *(deps)* Update pre-commit hook astral-sh/ruff-pre-commit to v0.11.5 (#147)
- *(deps)* Lock file maintenance (#149)
- *(deps)* Lock file maintenance (#151)
- *(deps)* Update pre-commit hook python-jsonschema/check-jsonschema to v0.33.0 (#152)

### Maintenance
- *(config)* Migrate config .github/renovate.json (#150)

### Other Changes
- Update ghcr.io/astral-sh/uv Docker tag to v0.6.10 (#125)
- Lock file maintenance (#126)
- Tschm patch 2 (#128)
- Update ghcr.io/astral-sh/uv Docker tag to v0.6.11 (#129)
- Update renovate.json (#130)
- Update renovate.json (#133)
- Schedule for ci/cd
- Update renovate.json
- Update test_notebooks.py (#154)
- Update README.md
- Makebranch (#155)
- Update __init__.py (#156)
- Update book.yml (#157)
- Remove the age job for the book
- Add GitHub template configuration file (#163)
- Update template.yml
- Delete .github/CODE_OF_CONDUCT.md
- Delete .github/CONTRIBUTING.md
- Update template repository in template.yml
- Update template.yml
- Rhiza
- Add script header with dependencies (#164)
- Remove stuff
- Remove docker
- Remove book
- No server
- Fmt
- Fmt
- Dependencies
- Dependencies
- Dependencies
- Remove 3.14
- Deptry?
- Fmt

## [0.0.23] - 2025-03-21

### Other Changes
- Lock file maintenance (#124)

## [0.0.22] - 2025-03-21

### Other Changes
- Update cvxgrp/.github action to v2.2.7 (#109)
- Update pre-commit hooks (#110)
- Lock file maintenance (#111)
- Update ghcr.io/astral-sh/uv Docker tag to v0.6.6 (#112)
- Update dependency mosek to v11.0.12 (#113)
- Lock file maintenance (#114)
- Lock file maintenance (#115)
- Update dependency mosek to v11.0.13 (#116)
- Update ghcr.io/astral-sh/uv Docker tag to v0.6.7 (#117)
- Update pre-commit hooks (#118)
- Lock file maintenance (#119)
- Update ghcr.io/astral-sh/uv Docker tag to v0.6.8 (#120)
- Update cvxgrp/.github action to v2.2.8 (#121)
- Update ghcr.io/astral-sh/uv Docker tag to v0.6.9 (#122)
- Lock file maintenance (#123)
- Update release.yml

## [0.0.21] - 2025-03-09

### Other Changes
- Fmt
- Release of a docker image (#70)
- No need to explicitly construct flight client (#72)
- Update README.md (#74)
- Update cvxgrp/.github action to v2.2.4 (#73)
- 75 move to marimo (#76)
- Update Dockerfile
- Remove jupyter (#78)
- 79 introduce book (#80)
- Update README.md (#81)
- Update ci.yml
- Update ghcr.io/astral-sh/uv Docker tag to v0.6.2 (#82)
- Update pre-commit hooks (#83)
- Lock file maintenance (#84)
- 85 update client using context (#86)
- Update docker/dockerfile Docker tag to v1.14 (#89)
- Lock file maintenance (#90)
- Support for cloud.google.com (#92)
- Update numpy-flight (#93)
- Update cvxgrp/.github action to v2.2.5 (#94)
- Update pre-commit hooks (#95)
- Lock file maintenance (#96)
- Update ghcr.io/astral-sh/uv Docker tag to v0.6.3 (#97)
- Update dependency mosek to v11.0.9 (#98)
- Lock file maintenance (#99)
- Lock file maintenance (#100)
- Lock file maintenance (#101)
- Update dependency mosek to v11.0.10 (#102)
- Update pre-commit hooks (#103)
- Update ghcr.io/astral-sh/uv Docker tag to v0.6.4 (#104)
- Update dependency mosek to v11.0.11 (#105)
- Update ghcr.io/astral-sh/uv Docker tag to v0.6.5 (#106)
- Lock file maintenance (#107)
- Using ResultData
- Update cvxgrp/.github action to v2.2.6 (#108)

## [0.0.20] - 2025-02-18

### Maintenance
- Build the container in release

## [0.0.19] - 2025-02-18

### Other Changes
- Update release.yml (#69)

## [0.0.18] - 2025-02-18

### Maintenance
- Build the container in release

## [0.0.16] - 2025-02-18

### Maintenance
- Build the container in release

## [0.0.15] - 2025-02-18

### Maintenance
- Build the container in release
- Build the container in release

## [0.0.14] - 2025-02-18

### Maintenance
- Build the container in release

## [0.0.13] - 2025-02-18

### Maintenance
- Testing the server
- Testing
- Testing
- Build the container in release

### Other Changes
- Lock file maintenance (#62)
- 63 bring in server (#64)
- Simplifying the client
- Docker is coming (#66)
- Lean NumpyClient
- Update ghcr.io/astral-sh/uv Docker tag to v0.6.1 (#68)
- Using new numpy-client package
- Update pyproject.toml
- Bring in numpy-flight-server
- Bring in numpy-flight-server
- Remove pyarrow traces
- Remove pyarrow traces
- Remove obsolete dependencies

## [0.0.12] - 2025-02-12

### Other Changes
- Update release.yml
- Update pre-commit.yml (#32)
- Introduce renovate, remove dependabot
- Release without explicit checkout
- Simplifying .github connection
- Update pyproject.toml (#33)
- Update pyproject.toml (#34)
- Update workflows for cvxball
- Deptry and pre-commit update
- Update dependency mosek to v10.2.15 (#37)
- Update ci.yml (#35)
- Update .pre-commit-config.yaml (#41)
- Update dependency mosek to v11 (#40)
- Update pre-commit.yml
- Update release.yml
- Create .editorconfig
- Update release.yml
- Update release.yml
- Lock file maintenance (#44)
- Update pre-commit hook crate-ci/typos to v1 (#43)
- Update pre-commit hooks (#42)
- Update cvxgrp/.github action to v2.1.1 (#39)
- Update release.yml (#45)
- Update dependency mosek to v11.0.6 (#46)
- Update pre-commit.yml
- Update ci.yml (#47)
- Update cvxgrp/.github action to v2.1.2 (#48)
- Update ci.yml (#50)
- Update release.yml (#51)
- Update pre-commit.yml (#52)
- Update pre-commit.yml (#53)
- Update cvxgrp/.github action to v2.2.1 (#49)
- Lock file maintenance (#54)
- Lock file maintenance (#55)
- Update dependency mosek to v11.0.7 (#57)
- Update cvxgrp/.github action to v2.2.3 (#56)
- Update ci.yml (#58)
- Update pre-commit hook astral-sh/ruff-pre-commit to v0.9.5 (#59)
- Lock file maintenance (#60)
- Update dependency mosek to v11.0.8 (#61)

## [0.0.11] - 2025-01-30

### Other Changes
- Bump cvxgrp/.github from 2.0.11 to 2.0.12 (#31)

## [0.0.10] - 2025-01-29

### Other Changes
- Bump cvxgrp/.github from 2.0.9 to 2.0.11 (#30)

## [0.0.9] - 2025-01-28

### Other Changes
- Bump cvxgrp/.github from 2.0.8 to 2.0.9 (#29)

## [0.0.8] - 2025-01-28

### Other Changes
- [pre-commit.ci] pre-commit autoupdate (#28)

## [0.0.7] - 2025-01-27

### Other Changes
- Release without source?

## [0.0.6] - 2025-01-27

### Other Changes
- Release without source?

## [0.0.5] - 2025-01-27

### Other Changes
- Update release.yml

## [0.0.4] - 2025-01-27

### Other Changes
- Bump cvxgrp/.github from 2.0.6 to 2.0.8 (#27)

## [0.0.3] - 2025-01-27

### Other Changes
- Automated release of tags

## [0.0.2] - 2025-01-27

### Other Changes
- 22 make a jupyter notebook for cvxpy (#23)
- Bump cvxgrp/.github from 2.0.3 to 2.0.6 (#24)
- [pre-commit.ci] pre-commit autoupdate (#25)
- Update .pre-commit-config.yaml (#26)
- Automated release of tags

## [0.0.1] - 2025-01-20

### Other Changes
- Initial commit
- Add first set of dependencies
- Add clarabel dependency
- Add 'make test'
- Solver with test-case
- Solver with test-case
- Ignore clarabel for deptry
- Update README.md
- More README
- More README
- Remove book and devcontainer
- Uv lock
- Update README.md
- Uv.lock updates
- Line too long
- Update Makefile
- 1 remove env file (#2)
- Update .pre-commit-config.yaml (#3)
- Update .pre-commit-config.yaml
- 4 add an image in readme (#5)
- Update code fragment in README
- 6 create badges (#7)
- Update README.md
- Update README.md
- Update README.md (#9)
- Update pre-commit.yml
- Update README.md
- Update Makefile
- Release removed (#13)
- 14 experiments with alternative implementations (#15)
- Install mosek as a dev dependency (#17)
- Experiment with mosek (#19)
- Update alter2.py (#20)
- Update alter1.py (#21)

<!-- generated by git-cliff -->
