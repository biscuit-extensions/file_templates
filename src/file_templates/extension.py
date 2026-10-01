from __future__ import annotations

import typing

from biscuit.extensions import Extension

if typing.TYPE_CHECKING:
    from biscuit.api import ExtensionsAPI


class FileTemplates(Extension):
    """Boilerplate code templates for new classes and modules"""

    def __init__(self, api: "ExtensionsAPI") -> None:
        super().__init__(api)
        self.api = api
        self.api.logger.info("File Templates extension initialised.")

    def install(self) -> None:
        """Run when extension is loaded."""
        self.api.logger.info("File Templates installed successfully.")
