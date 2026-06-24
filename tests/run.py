"""Test runner for system tests.

This module discovers and runs all system tests. It supports both an external
Polarion server and an on-the-fly Docker test container.

Test modes:
    - External server: requires APP_URL and APP_TOKEN (env vars or --app_url/--app_token).
    - Docker container: requires TC_POLARION_IMAGE_NAME; the container is created on the fly.

Example:
    Run against an external Polarion server::

        $ uv run python tests/run.py --app_url https://<POLARION_URL> --app_token <TOKEN>

    Run with a Docker test container::

        $ uv run python tests/run.py --tc_polarion_image_name polarion:<POLARION_VERSION>

TEMPLATE: replace the placeholder extension name, project id/name/template and the
template location below with the values for your extension. See test-data/project-template.
"""

import sys
import unittest

import xmlrunner
from python_sbb_polarion.testing.temp_project import TempProject
from python_sbb_polarion.testing.testcontainers_helper import TestContainersHelper
from python_sbb_polarion.util import abs_path, abs_path_str

from tests.constants import EXTENSION_NAME
from tests.extension_test_case import ExtensionTestCase


# find and load tests
loader = unittest.TestLoader()
suite = loader.discover(abs_path_str("."))

# Create the Polarion test container only when TC_POLARION_IMAGE_NAME is set; otherwise
# tests run against the external server given by APP_URL/APP_TOKEN.
testcontainers_helper = TestContainersHelper()
testcontainers_helper.create_test_container_if_required(EXTENSION_NAME)

# TEMPLATE: a temporary Polarion project is created from the template under test-data and
# torn down at the end of the run. Adjust the ids/name and the template folder to your project.
example_project = TempProject(
    "example",
    "Example Project",
    "example_st",
    abs_path("../test-data/project-template/example_st"),
)
ExtensionTestCase.set_example_project(example_project)

try:
    # run tests
    result = xmlrunner.XMLTestRunner(verbosity=2).run(suite)
    # Exit with non-zero status if tests failed or had errors
    if not result.wasSuccessful():
        sys.exit(1)
finally:
    example_project.tear_down()
    testcontainers_helper.tear_down()
