"""Constants for the extension system tests.

TEMPLATE: keep this module for values shared across test modules (the extension bundle
id, timeouts, thresholds, feature names, ...). Replace the placeholders below.
"""

from typing import Final


# Bundle id of the extension installed into the Polarion test container, as registered in
# Polarion. It is the name used in the REST base path /polarion/<EXTENSION_NAME>/rest and to
# build the extension API client, and it is the bundle the test container installs
# (ch.sbb.polarion.extension.<EXTENSION_NAME>).
#
# TEMPLATE: this template's worked example only exercises the generic project lifecycle, so it
# has no dedicated extension under test. It points at "test-data" - the SBB extension that
# powers temporary-project provisioning and is required by the harness anyway. Replace this
# with your extension's bundle id (e.g. "diff-tool", "xml-repair") and add extension-specific
# test_*.py modules.
#
# Final keeps the literal type, so create_extension_api(EXTENSION_NAME) returns the specific API class
# that ExtensionTestCase is parameterized with (a plain str would only give PolarionGenericExtensionApi).
EXTENSION_NAME: Final = "test-data"

# Timeouts and polling for asynchronous Polarion jobs (tune per extension).
POLL_INTERVAL_SECONDS: float = 1.0
