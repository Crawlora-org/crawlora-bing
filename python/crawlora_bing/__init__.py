"""Typed Bing client for the Crawlora hosted API."""

from .platform import BingClient, AsyncBingClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = BingClient
AsyncClient = AsyncBingClient
__version__ = '0.2.0'
DISPLAY_NAME = 'Bing'
PLATFORM = 'bing'
CONTRACT_REVISION = 'sha256:0c1aae283aa17db66ba7f542134d6b983351857e5d153e22cbf40c4fb6506eb0'

__all__ = [
    "BingClient", "AsyncBingClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
