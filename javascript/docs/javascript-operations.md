# Crawlora Bing JavaScript Client Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `5`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| bing | `bing.images` | `bing-images` | `GET /bing/images` | `q` (query string required)<br>`page` (query number)<br>`count` (query number)<br>`country` (query string)<br>`lang` (query string) | `ApiKeyAuth` | `BingImagesResponse` |  |
| bing | `bing.news` | `bing-news` | `GET /bing/news` | `q` (query string required)<br>`page` (query number)<br>`count` (query number)<br>`country` (query string)<br>`lang` (query string) | `ApiKeyAuth` | `BingNewsResponse` |  |
| bing | `bing.search` | `bing-search` | `GET /bing/search` | `q` (query string required)<br>`page` (query number)<br>`count` (query number)<br>`country` (query string)<br>`lang` (query string) | `ApiKeyAuth` | `BingSearchResponse` |  |
| bing | `bing.suggest` | `bing-suggest` | `GET /bing/suggest` | `q` (query string required)<br>`count` (query number)<br>`country` (query string)<br>`lang` (query string)<br>`rich` (query boolean) | `ApiKeyAuth` | `BingSuggestResponse` |  |
| bing | `bing.videos` | `bing-videos` | `GET /bing/videos` | `q` (query string required)<br>`page` (query number)<br>`count` (query number)<br>`country` (query string)<br>`lang` (query string) | `ApiKeyAuth` | `BingVideosResponse` |  |
