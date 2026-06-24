from __future__ import annotations

from http import HTTPStatus
from typing import TYPE_CHECKING

from tests.extension_test_case import ExtensionTestCase


if TYPE_CHECKING:
    from requests import Response


class ExampleProjectTest(ExtensionTestCase):
    """Worked example exercising the generic temporary-project lifecycle.

    ``tests/run.py`` creates the temporary "example" project before the suite runs and tears it
    down afterwards. This test asserts the project exists in between.

    TEMPLATE: this is a good first check that the harness can reach Polarion and provision a
    project. Add your own ``test_*.py`` modules (each subclassing ``ExtensionTestCase``) for the
    extension-specific behaviour.
    """

    def test_example_project_exists(self) -> None:
        # The temporary project was created by tests/run.py; a 200 here confirms it exists.
        response: Response = self.polarion_api().get_project(self.project_id)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.json()["data"]["id"], self.project_id)
