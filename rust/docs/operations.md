# Crawlora Bing Rust SDK Operations

Generated from `openapi/public.json`. Deprecated, admin, and internal operations are excluded from this SDK contract.

Total operations: `5`

| Group | SDK method | Operation ID | HTTP | Params | Auth | Response | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| bing | `bing.images` | `bing-images` | `GET /bing/images` | `q` (query String required)<br>`page` (query i64)<br>`count` (query i64)<br>`country` (query String)<br>`lang` (query String) | `ApiKeyAuth` | `BingImagesResponse` |  |
| bing | `bing.news` | `bing-news` | `GET /bing/news` | `q` (query String required)<br>`page` (query i64)<br>`count` (query i64)<br>`country` (query String)<br>`lang` (query String) | `ApiKeyAuth` | `BingNewsResponse` |  |
| bing | `bing.search` | `bing-search` | `GET /bing/search` | `q` (query String required)<br>`page` (query i64)<br>`count` (query i64)<br>`country` (query String)<br>`lang` (query String) | `ApiKeyAuth` | `BingSearchResponse` |  |
| bing | `bing.suggest` | `bing-suggest` | `GET /bing/suggest` | `q` (query String required)<br>`count` (query i64)<br>`country` (query String)<br>`lang` (query String)<br>`rich` (query bool) | `ApiKeyAuth` | `BingSuggestResponse` |  |
| bing | `bing.videos` | `bing-videos` | `GET /bing/videos` | `q` (query String required)<br>`page` (query i64)<br>`count` (query i64)<br>`country` (query String)<br>`lang` (query String) | `ApiKeyAuth` | `BingVideosResponse` |  |
