"""Typed Bing client for the Crawlora hosted API."""

from .platform import BingClient, AsyncBingClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = BingClient
AsyncClient = AsyncBingClient
__version__ = '0.1.0'
DISPLAY_NAME = 'Bing'
PLATFORM = 'bing'
CONTRACT_REVISION = 'sha256:73cc910f0df40739a5161642e71d8dfcb316ce168baa08a43e8513a5349bd40c'

__all__ = [
    "BingClient", "AsyncBingClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
