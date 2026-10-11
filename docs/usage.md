# Bing client usage

The `@crawlora-org/bing` and `crawlora-bing` packages call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape Bing locally; Crawlora is independent from and not endorsed by Bing or its owners.

The package tracks the public API contract revision `sha256:73cc910f0df40739a5161642e71d8dfcb316ce168baa08a43e8513a5349bd40c` bundled with release `0.1.1`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

Both packages expose all 5 operations in the bundled API contract. JavaScript uses camelCase methods and Python uses snake_case methods. Methods also remain available through the `bing` group and the generated `Client` alias.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| Method | Endpoint | Parameters | Description |
| --- | --- | --- | --- |
| `images` / `images` | `GET /bing/images` | `q` (query, required), `page` (query, optional), `count` (query, optional), `country` (query, optional), `lang` (query, optional) | Search Bing image results |
| `news` / `news` | `GET /bing/news` | `q` (query, required), `page` (query, optional), `count` (query, optional), `country` (query, optional), `lang` (query, optional) | Search Bing news results |
| `search` / `search` | `GET /bing/search` | `q` (query, required), `page` (query, optional), `count` (query, optional), `country` (query, optional), `lang` (query, optional) | Search Bing web results |
| `suggest` / `suggest` | `GET /bing/suggest` | `q` (query, required), `count` (query, optional), `country` (query, optional), `lang` (query, optional), `rich` (query, optional) | Suggest Bing search queries |
| `videos` / `videos` | `GET /bing/videos` | `q` (query, required), `page` (query, optional), `count` (query, optional), `country` (query, optional), `lang` (query, optional) | Search Bing video results |

## Client forms

- JavaScript: import `BingClient` (also exported as `Client`) from `@crawlora-org/bing`; use `new BingClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `BingClient` (also exported as `Client`) from `crawlora_bing`; use `with BingClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncBingClient`, used with `async with` and `await`.

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
