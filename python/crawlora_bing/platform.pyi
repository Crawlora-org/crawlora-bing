from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelBingVideosResponseDoc = TypedDict('ModelBingVideosResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelBingVideosResponse],
    'msg': NotRequired[str],
}, total=False)

ModelBingVideosResponse = TypedDict('ModelBingVideosResponse', {
    'pagination': NotRequired[ModelBingSearchPagination],
    'results': NotRequired[list[ModelBingVideoResult]],
}, total=False)

ModelBingVideoResult = TypedDict('ModelBingVideoResult', {
    'age': NotRequired[str],
    'age_timestamp': NotRequired[int],
    'creator': NotRequired[str],
    'duration': NotRequired[str],
    'platform': NotRequired[str],
    'position': NotRequired[int],
    'thumbnail': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
    'views': NotRequired[str],
}, total=False)

ModelBingSearchPagination = TypedDict('ModelBingSearchPagination', {
    'count': NotRequired[int],
    'next_page': NotRequired[int],
    'page': NotRequired[int],
    'previous_page': NotRequired[int],
}, total=False)

ModelBingSuggestResponseDoc = TypedDict('ModelBingSuggestResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelBingSuggestResponse],
    'msg': NotRequired[str],
}, total=False)

ModelBingSuggestResponse = TypedDict('ModelBingSuggestResponse', {
    'query': NotRequired[str],
    'suggestions': NotRequired[list[ModelBingSuggestionResult]],
}, total=False)

ModelBingSuggestionResult = TypedDict('ModelBingSuggestionResult', {
    'entity': NotRequired[ModelBingSuggestionEntity],
    'position': NotRequired[int],
    'query': NotRequired[str],
}, total=False)

ModelBingSuggestionEntity = TypedDict('ModelBingSuggestionEntity', {
    'description': NotRequired[str],
    'image_url': NotRequired[str],
    'name': NotRequired[str],
}, total=False)

ModelBingSearchResponseDoc = TypedDict('ModelBingSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelBingSearchResponse],
    'msg': NotRequired[str],
}, total=False)

ModelBingSearchResponse = TypedDict('ModelBingSearchResponse', {
    'context': NotRequired[ModelBingSearchContext],
    'low_confidence': NotRequired[bool],
    'news': NotRequired[list[ModelBingNewsResult]],
    'pagination': NotRequired[ModelBingSearchPagination],
    'people_also_ask': NotRequired[list[str]],
    'related_queries': NotRequired[list[str]],
    'results': NotRequired[list[ModelBingSearchResult]],
    'videos': NotRequired[list[ModelBingVideoResult]],
}, total=False)

ModelBingSearchResult = TypedDict('ModelBingSearchResult', {
    'age': NotRequired[str],
    'age_timestamp': NotRequired[int],
    'description': NotRequired[str],
    'display_url': NotRequired[str],
    'favicon': NotRequired[str],
    'hostname': NotRequired[str],
    'position': NotRequired[int],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelBingNewsResult = TypedDict('ModelBingNewsResult', {
    'age': NotRequired[str],
    'age_timestamp': NotRequired[int],
    'description': NotRequired[str],
    'position': NotRequired[int],
    'related_count': NotRequired[int],
    'source': NotRequired[str],
    'thumbnail': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelBingSearchContext = TypedDict('ModelBingSearchContext', {
    'attributes': NotRequired[list[ModelBingContextAttribute]],
    'description': NotRequired[str],
    'image': NotRequired[str],
    'subtitle': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelBingContextAttribute = TypedDict('ModelBingContextAttribute', {
    'label': NotRequired[str],
    'value': NotRequired[str],
}, total=False)

ModelBingNewsResponseDoc = TypedDict('ModelBingNewsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelBingNewsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelBingNewsResponse = TypedDict('ModelBingNewsResponse', {
    'pagination': NotRequired[ModelBingSearchPagination],
    'results': NotRequired[list[ModelBingNewsResult]],
}, total=False)

ModelBingImagesResponseDoc = TypedDict('ModelBingImagesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelBingImagesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelBingImagesResponse = TypedDict('ModelBingImagesResponse', {
    'pagination': NotRequired[ModelBingSearchPagination],
    'results': NotRequired[list[ModelBingImageResult]],
}, total=False)

ModelBingImageResult = TypedDict('ModelBingImageResult', {
    'height': NotRequired[int],
    'image_url': NotRequired[str],
    'position': NotRequired[int],
    'source': NotRequired[str],
    'source_url': NotRequired[str],
    'thumbnail': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
    'width': NotRequired[int],
}, total=False)

BingImagesResponse = ModelBingImagesResponseDoc
BingImagesParams = TypedDict('BingImagesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'page': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

BingNewsResponse = ModelBingNewsResponseDoc
BingNewsParams = TypedDict('BingNewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'page': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

BingSearchResponse = ModelBingSearchResponseDoc
BingSearchParams = TypedDict('BingSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'page': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

BingSuggestResponse = ModelBingSuggestResponseDoc
BingSuggestParams = TypedDict('BingSuggestParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'rich': NotRequired[bool],
}, total=False)

BingVideosResponse = ModelBingVideosResponseDoc
BingVideosParams = TypedDict('BingVideosParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'page': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

class BingGroup:
    @overload
    def images(self, **params: Unpack[BingImagesStreamParams]) -> BinaryIO: ...
    @overload
    def images(self, **params: Unpack[BingImagesTextResponseParams]) -> str: ...
    @overload
    def images(self, **params: Unpack[BingImagesDefaultParams]) -> BingImagesResponse: ...
    @overload
    def news(self, **params: Unpack[BingNewsStreamParams]) -> BinaryIO: ...
    @overload
    def news(self, **params: Unpack[BingNewsTextResponseParams]) -> str: ...
    @overload
    def news(self, **params: Unpack[BingNewsDefaultParams]) -> BingNewsResponse: ...
    @overload
    def search(self, **params: Unpack[BingSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[BingSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[BingSearchDefaultParams]) -> BingSearchResponse: ...
    @overload
    def suggest(self, **params: Unpack[BingSuggestStreamParams]) -> BinaryIO: ...
    @overload
    def suggest(self, **params: Unpack[BingSuggestTextResponseParams]) -> str: ...
    @overload
    def suggest(self, **params: Unpack[BingSuggestDefaultParams]) -> BingSuggestResponse: ...
    @overload
    def videos(self, **params: Unpack[BingVideosStreamParams]) -> BinaryIO: ...
    @overload
    def videos(self, **params: Unpack[BingVideosTextResponseParams]) -> str: ...
    @overload
    def videos(self, **params: Unpack[BingVideosDefaultParams]) -> BingVideosResponse: ...

OperationId = Literal[
    'bing-images',
    'bing-news',
    'bing-search',
    'bing-suggest',
    'bing-videos',
]

class CrawloraClient:
    bing: BingGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bing-images'],
        params: BingImagesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BingImagesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bing-news'],
        params: BingNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BingNewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bing-search'],
        params: BingSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BingSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bing-suggest'],
        params: BingSuggestParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BingSuggestResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['bing-videos'],
        params: BingVideosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BingVideosResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['bing-images'],
        params: BingImagesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BingImagesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bing-news'],
        params: BingNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BingNewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bing-search'],
        params: BingSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BingSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bing-suggest'],
        params: BingSuggestParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BingSuggestResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['bing-videos'],
        params: BingVideosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BingVideosResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class BingClient(CrawloraClient):
    def __enter__(self) -> BingClient: ...
    @overload
    def images(self, **params: Unpack[BingImagesStreamParams]) -> BinaryIO: ...
    @overload
    def images(self, **params: Unpack[BingImagesTextResponseParams]) -> str: ...
    @overload
    def images(self, **params: Unpack[BingImagesDefaultParams]) -> BingImagesResponse: ...
    @overload
    def news(self, **params: Unpack[BingNewsStreamParams]) -> BinaryIO: ...
    @overload
    def news(self, **params: Unpack[BingNewsTextResponseParams]) -> str: ...
    @overload
    def news(self, **params: Unpack[BingNewsDefaultParams]) -> BingNewsResponse: ...
    @overload
    def search(self, **params: Unpack[BingSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[BingSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[BingSearchDefaultParams]) -> BingSearchResponse: ...
    @overload
    def suggest(self, **params: Unpack[BingSuggestStreamParams]) -> BinaryIO: ...
    @overload
    def suggest(self, **params: Unpack[BingSuggestTextResponseParams]) -> str: ...
    @overload
    def suggest(self, **params: Unpack[BingSuggestDefaultParams]) -> BingSuggestResponse: ...
    @overload
    def videos(self, **params: Unpack[BingVideosStreamParams]) -> BinaryIO: ...
    @overload
    def videos(self, **params: Unpack[BingVideosTextResponseParams]) -> str: ...
    @overload
    def videos(self, **params: Unpack[BingVideosDefaultParams]) -> BingVideosResponse: ...

class AsyncBingClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncBingClient: ...
    bing: _AsyncBingGroup
    @overload
    async def images(self, **params: Unpack[BingImagesStreamParams]) -> BinaryIO: ...
    @overload
    async def images(self, **params: Unpack[BingImagesTextResponseParams]) -> str: ...
    @overload
    async def images(self, **params: Unpack[BingImagesDefaultParams]) -> BingImagesResponse: ...
    @overload
    async def news(self, **params: Unpack[BingNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def news(self, **params: Unpack[BingNewsTextResponseParams]) -> str: ...
    @overload
    async def news(self, **params: Unpack[BingNewsDefaultParams]) -> BingNewsResponse: ...
    @overload
    async def search(self, **params: Unpack[BingSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[BingSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[BingSearchDefaultParams]) -> BingSearchResponse: ...
    @overload
    async def suggest(self, **params: Unpack[BingSuggestStreamParams]) -> BinaryIO: ...
    @overload
    async def suggest(self, **params: Unpack[BingSuggestTextResponseParams]) -> str: ...
    @overload
    async def suggest(self, **params: Unpack[BingSuggestDefaultParams]) -> BingSuggestResponse: ...
    @overload
    async def videos(self, **params: Unpack[BingVideosStreamParams]) -> BinaryIO: ...
    @overload
    async def videos(self, **params: Unpack[BingVideosTextResponseParams]) -> str: ...
    @overload
    async def videos(self, **params: Unpack[BingVideosDefaultParams]) -> BingVideosResponse: ...

class _AsyncBingGroup:
    @overload
    async def images(self, **params: Unpack[BingImagesStreamParams]) -> BinaryIO: ...
    @overload
    async def images(self, **params: Unpack[BingImagesTextResponseParams]) -> str: ...
    @overload
    async def images(self, **params: Unpack[BingImagesDefaultParams]) -> BingImagesResponse: ...
    @overload
    async def news(self, **params: Unpack[BingNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def news(self, **params: Unpack[BingNewsTextResponseParams]) -> str: ...
    @overload
    async def news(self, **params: Unpack[BingNewsDefaultParams]) -> BingNewsResponse: ...
    @overload
    async def search(self, **params: Unpack[BingSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[BingSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[BingSearchDefaultParams]) -> BingSearchResponse: ...
    @overload
    async def suggest(self, **params: Unpack[BingSuggestStreamParams]) -> BinaryIO: ...
    @overload
    async def suggest(self, **params: Unpack[BingSuggestTextResponseParams]) -> str: ...
    @overload
    async def suggest(self, **params: Unpack[BingSuggestDefaultParams]) -> BingSuggestResponse: ...
    @overload
    async def videos(self, **params: Unpack[BingVideosStreamParams]) -> BinaryIO: ...
    @overload
    async def videos(self, **params: Unpack[BingVideosTextResponseParams]) -> str: ...
    @overload
    async def videos(self, **params: Unpack[BingVideosDefaultParams]) -> BingVideosResponse: ...

BingImagesDefaultParams = TypedDict('BingImagesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
    'page': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

BingImagesTextResponseParams = TypedDict('BingImagesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
    'page': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

BingImagesStreamParams = TypedDict('BingImagesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
    'page': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

BingNewsDefaultParams = TypedDict('BingNewsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
    'page': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

BingNewsTextResponseParams = TypedDict('BingNewsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
    'page': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

BingNewsStreamParams = TypedDict('BingNewsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
    'page': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

BingSearchDefaultParams = TypedDict('BingSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
    'page': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

BingSearchTextResponseParams = TypedDict('BingSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
    'page': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

BingSearchStreamParams = TypedDict('BingSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
    'page': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

BingSuggestDefaultParams = TypedDict('BingSuggestDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'rich': NotRequired[bool],
}, total=False)

BingSuggestTextResponseParams = TypedDict('BingSuggestTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'rich': NotRequired[bool],
}, total=False)

BingSuggestStreamParams = TypedDict('BingSuggestStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
    'rich': NotRequired[bool],
}, total=False)

BingVideosDefaultParams = TypedDict('BingVideosDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
    'page': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

BingVideosTextResponseParams = TypedDict('BingVideosTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
    'page': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)

BingVideosStreamParams = TypedDict('BingVideosStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
    'page': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[str],
    'lang': NotRequired[str],
}, total=False)
