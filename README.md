[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=SchweizerischeBundesbahnen_open-source-polarion-system-test-repo-template&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=SchweizerischeBundesbahnen_open-source-polarion-system-test-repo-template)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=SchweizerischeBundesbahnen_open-source-polarion-system-test-repo-template&metric=bugs)](https://sonarcloud.io/summary/new_code?id=SchweizerischeBundesbahnen_open-source-polarion-system-test-repo-template)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=SchweizerischeBundesbahnen_open-source-polarion-system-test-repo-template&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=SchweizerischeBundesbahnen_open-source-polarion-system-test-repo-template)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=SchweizerischeBundesbahnen_open-source-polarion-system-test-repo-template&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=SchweizerischeBundesbahnen_open-source-polarion-system-test-repo-template)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=SchweizerischeBundesbahnen_open-source-polarion-system-test-repo-template&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=SchweizerischeBundesbahnen_open-source-polarion-system-test-repo-template)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=SchweizerischeBundesbahnen_open-source-polarion-system-test-repo-template&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=SchweizerischeBundesbahnen_open-source-polarion-system-test-repo-template)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=SchweizerischeBundesbahnen_open-source-polarion-system-test-repo-template&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=SchweizerischeBundesbahnen_open-source-polarion-system-test-repo-template)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=SchweizerischeBundesbahnen_open-source-polarion-system-test-repo-template&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=SchweizerischeBundesbahnen_open-source-polarion-system-test-repo-template)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=SchweizerischeBundesbahnen_open-source-polarion-system-test-repo-template&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=SchweizerischeBundesbahnen_open-source-polarion-system-test-repo-template)

# System Tests Repository Template for Polarion Extensions

This repository is a **template** for the system-test repositories of SBB Polarion Java extensions
(`ch.sbb.polarion.extension.*`). It provides the scaffolding to run black-box system tests against a
Polarion instance using the [`python-sbb-polarion`](https://github.com/SchweizerischeBundesbahnen/python-sbb-polarion)
test harness, plus the CI/CD wiring (GitHub Actions and Jenkins).

## Using this template

1. Create a new repository from this template (e.g. `ch.sbb.polarion.extension.<name>.st`).
2. Replace the example values (the scaffold ships a minimal worked example that creates a temporary
   `example` project, asserts it exists, and tears it down; search for `TEMPLATE` to find each spot):
   - `tests/constants.py` — set `EXTENSION_NAME` to your extension's bundle id.
   - `tests/run.py` — set the project id / name / template and the template location.
   - `pyproject.toml` — set `name` and `description`.
   - `sonar-project.properties` — set `sonar.projectKey`/badges to your repository.
   - `.github/workflows/system-tests.yml` — pin `TC_*` versions and images for your extension.
3. Add your project template and baselines under `test-data/` (see `test-data/project-template/README.md`).
4. Write `tests/test_*.py` modules subclassing `ExtensionTestCase` (`tests/test_example_project.py` is an example).

## CI

This project uses dual CI:

- **GitHub Actions**
  - `ci.yml` — linting, type checking, and SonarCloud analysis (static checks; no Polarion required).
  - `system-tests.yml` — system tests against a Polarion instance running in a Docker container. This
    is the pull request merge gate (the `system-tests` check is required on `main`), so merging does
    not depend on the availability of a persistent Polarion instance.
- **Jenkins** (`Jenkinsfile`) — the same system tests run on a nightly schedule against a persistent
  Polarion instance, on the `main` branch only. Jenkins is not part of the
  per-pull-request merge path.

## 1. Run tests against a prepared Polarion server (local or remote)

In this mode, the tests run against a running Polarion server specified by `app_url` and authenticated
with `app_token`.

| Parameter | Default value | Mandatory for external Polarion | Description                          |
|-----------|---------------|---------------------------------|--------------------------------------|
| app_url   | -             | yes                             | Base URL of external Polarion server |
| app_token | -             | yes                             | Authentication token                 |

### IntelliJ
- install the Python plugin
- import the project
- add and configure a Python SDK in the project settings
- run as a normal unit test

### Command line example
```
uv run python tests/run.py --app_url BASE_POLARION_URL --app_token AUTH_TOKEN
```

## 2. Run tests against a local Polarion test container

In this mode a Polarion container is created on the fly from a Docker image and the tests run against
it.

### Prerequisites
- Docker runtime must be available on the machine
- A Polarion Docker image with the specified name must exist locally or in a remote registry

### Command line example
```
uv run python tests/run.py --tc_polarion_image_name=polarion:2606-0
```

### Parameters
| Parameter                        | Default value | Mandatory for test containers | Description                                                                                              |
|----------------------------------|---------------|-------------------------------|----------------------------------------------------------------------------------------------------------|
| tc_polarion_image_name           | -             | yes                           | Polarion Docker image name. This parameter triggers test-containers mode                                  |
| tc_extension_version             | latest        | no                            | Version of the extension under test. By default the latest version from the local Maven repo is used      |
| tc_additional_bundles            | -             | no                            | Comma-separated list of additional bundles to install, in the form group_id:artifact_id:version           |
| tc_admin_utility_version         | -             | no                            | Version of the admin-utility extension used to initialize the instance and prepare test data              |
| tc_weasyprint_service_image_name | -             | no                            | WeasyPrint service Docker image name (only for extensions that depend on the WeasyPrint service)          |

All parameters can also be specified as environment variables (the upper-cased `TC_*` form).
