from tests.extension_test_case import ExtensionTestCase


class VersionTest(ExtensionTestCase):
    """Smoke tests for the standard /version endpoint exposed by every SBB Polarion extension.

    TEMPLATE: this example exercises the shared /version endpoint and is a good first check
    that the extension is deployed and reachable. Add your own ``test_*.py`` modules (each
    subclassing ``ExtensionTestCase``) for the extension-specific behaviour.
    """

    def test_version_get(self) -> None:
        # run_test_get_version() (from GenericTestCase) asserts the common version contract:
        # vendor "SBB AG", an automaticModuleName of ch.sbb.polarion.extension.<name>, and
        # well-formed version/build-timestamp fields.
        self.run_test_get_version()

    def test_version_get_with_invalid_token(self) -> None:
        self.run_test_get_version_with_invalid_token()
