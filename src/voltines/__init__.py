"""The Voltines Python client."""

from importlib.metadata import version, PackageNotFoundError

from .player import watch

try:
    __version__ = version("voltines")
except PackageNotFoundError:
    __version__ = "0.0.0"

__all__ = ["watch", "__version__"]
