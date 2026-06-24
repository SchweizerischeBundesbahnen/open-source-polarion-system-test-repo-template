from __future__ import annotations

from typing import TYPE_CHECKING

from python_sbb_polarion.testing.generic_test_case import GenericTestCase

from tests.constants import EXTENSION_NAME


if TYPE_CHECKING:
    from python_sbb_polarion.core.base import PolarionGenericExtensionApi
    from python_sbb_polarion.testing.temp_project import TempProject


class ExtensionTestCase(GenericTestCase):
    """Base test case for the extension system tests.

    Provides the extension API client and a shared temporary Polarion project that the
    individual test modules build on. Put extension-specific helper methods here (settings
    initialization, conversion helpers, assertions, ...).

    TEMPLATE: this base is intentionally minimal. As your suite grows, add helpers here so
    the individual ``test_*.py`` modules stay focused on the behaviour under test.
    """

    example_project: TempProject

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.extension_api = cls.create_extension_api(EXTENSION_NAME)

    @classmethod
    def set_example_project(cls, example_project: TempProject) -> None:
        cls.example_project = example_project

    def setUp(self) -> None:
        self.project_id: str = self.__class__.example_project.temp_project_id
        self.scope: str = f"project/{self.project_id}/"

    def api(self) -> PolarionGenericExtensionApi:
        return self.extension_api
