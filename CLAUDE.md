# CLAUDE.md

- **This is a repository template** for the system tests of Polarion Java extensions. Keep the
  scaffolding minimal and generic — do not add real, extension-specific test logic. The scaffold's
  worked example creates a temporary `example` project, asserts it exists, and tears it down (it
  has no dedicated extension under test; `EXTENSION_NAME` points at `test-data`). The spots a
  downstream repository must change are marked with `TEMPLATE`.
- Use `uv` for all Python tooling (`uv run tox`, `uv run python tests/run.py`, `uv sync`) — never `pip`, `python -m pip`, or bare tool invocations.
- GitHub Actions workflows from `SchweizerischeBundesbahnen/*` are intentionally pinned to `@main`, not hash-pinned. This is enforced by `zizmor.yml`. Do not change these to hash pins.
- CI uses `uv sync --frozen` (not `--locked`). Do not change back to `--locked`.
- `==` pins in `pyproject.toml` are for Renovate — `ruff`, `mypy`, `types-requests` use exact pins so Renovate creates PRs that go through CI. Do not relax these to ranges. Range-pinned deps are upgraded by `uv lock --upgrade`.
- **System-test repositories are not published**, so there is no Release Please / build-and-publish step and `version` in `pyproject.toml` is a static placeholder. Do not add release automation.
- **Python version is hardcoded in multiple places** — `.tool-versions` is the source of truth, but `pyproject.toml` (`requires-python`, ruff `target-version`, mypy `python_version`) and `sonar-project.properties` must be updated manually. Only `ci.yml` reads from `.tool-versions` automatically.
- **mypy `python_version = "3.14"` is intentional** — forward-compatibility checking even though the runtime is 3.13. Do not "fix" this to match `requires-python`.
- **System tests run in two places.** GitHub Actions (`system-tests.yml`) is the PR merge gate and runs against a containerized Polarion. The `Jenkinsfile` runs the same suite nightly against a long-lived Polarion environment. Keep these two paths in sync when changing test invocation or dependencies.
- **The Jenkins job is a multibranch pipeline.** Scheduled/manual stages in the `Jenkinsfile` MUST be guarded with `when { branch 'main' }` (combined with the `triggeredBy` checks) — otherwise the suite runs on every feature and PR branch.
- **The PR merge gate is the GitHub Actions `system-tests` check, not Jenkins.** Because Jenkins only runs system tests nightly on `main`, it does NOT post a per-PR status — so the required status check must stay the GitHub Actions `system-tests` job. If you rename that job or workflow, update the required-status-check context in the branch-protection ruleset in the same change, or PRs will be ungated or blocked.
