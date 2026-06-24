"""Constants for the extension system tests.

TEMPLATE: keep this module for values shared across test modules (the extension bundle
id, timeouts, thresholds, feature names, ...). Replace the placeholders below.
"""

# Bundle id of the extension under test, as registered in Polarion. This is the name used
# in the REST base path /polarion/<EXTENSION_NAME>/rest and to build the extension API
# client. Examples: "pdf-exporter", "docx-exporter", "xml-repair".
EXTENSION_NAME: str = "myextension"

# Timeouts and polling for asynchronous Polarion jobs (tune per extension).
EXPORT_TIMEOUT_SECONDS: int = 100
POLL_INTERVAL_SECONDS: float = 1.0
