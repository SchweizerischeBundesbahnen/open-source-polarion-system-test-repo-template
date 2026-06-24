# Test data

This folder holds the static test data the system tests run against.

## Layout

- `project-template/` — Polarion project template(s) used to create a temporary project for the
  duration of a test run. `tests/run.py` instantiates a `TempProject` from a template folder here,
  and tears it down afterwards.
- `expected/` — expected/baseline artifacts that tests compare their output against (kept under
  version control).
- `output/` — artifacts produced during a run (generated files, rendered pages, diffs). This folder
  is created at runtime and is git-ignored.

## Adding your project template

1. Export the Polarion project you want to test against (the on-disk project layout: `.polarion/`,
   `modules/`, `_wiki/`, ...) into a folder under `project-template/`, e.g.
   `project-template/example/` (the worked example ships exactly this).
2. Point `tests/run.py` at that folder when constructing `TempProject` (the `template_location`
   argument), and set the project id / name / template id to match.

The placeholder name `example` in `tests/run.py` is illustrative — replace it with a name that
reflects your extension and project.
