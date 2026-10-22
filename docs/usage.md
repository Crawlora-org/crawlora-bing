# Bing API endpoint reference and client usage

This reference lists all 5 public Bing API endpoints exposed by the JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust clients, including the `@crawlora-org/bing`, `crawlora-bing`, and `crawlora-bing` packages. The clients call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape Bing locally; Crawlora is independent from and not endorsed by Bing or its owners.

The package tracks the public API contract revision `sha256:0c1aae283aa17db66ba7f542134d6b983351857e5d153e22cbf40c4fb6506eb0` bundled with release `0.2.0`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

All language packages expose the selected public API operations in the bundled contract. JavaScript uses camelCase methods, Python and Rust use snake_case methods. JavaScript, Python, and Rust methods are grouped under `bing`; Rust uses typed parameter structs and returns the complete HTTP response.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)
- [Rust](../rust/examples/quick_start.rs)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| JavaScript | Python | Rust | Endpoint | Parameters | Description |
| --- | --- | --- | --- | --- | --- |
| `images` | `images` | `bing.images` | `GET /bing/images` | `q` (query, required), `page` (query, optional), `count` (query, optional), `country` (query, optional), `lang` (query, optional) | Search Bing image results |
| `news` | `news` | `bing.news` | `GET /bing/news` | `q` (query, required), `page` (query, optional), `count` (query, optional), `country` (query, optional), `lang` (query, optional) | Search Bing news results |
| `search` | `search` | `bing.search` | `GET /bing/search` | `q` (query, required), `page` (query, optional), `count` (query, optional), `country` (query, optional), `lang` (query, optional) | Search Bing web results |
| `suggest` | `suggest` | `bing.suggest` | `GET /bing/suggest` | `q` (query, required), `count` (query, optional), `country` (query, optional), `lang` (query, optional), `rich` (query, optional) | Suggest Bing search queries |
| `videos` | `videos` | `bing.videos` | `GET /bing/videos` | `q` (query, required), `page` (query, optional), `count` (query, optional), `country` (query, optional), `lang` (query, optional) | Search Bing video results |

## Client forms

- JavaScript: import `BingClient` (also exported as `Client`) from `@crawlora-org/bing`; use `new BingClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `BingClient` (also exported as `Client`) from `crawlora_bing`; use `with BingClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncBingClient`, used with `async with` and `await`.
- Rust: add `crawlora-bing` with Cargo; import `Client` and the generated operation parameter struct, then call `client.bing.<snake_case_method>(params).await`. See the [Rust example](https://github.com/Crawlora-org/crawlora-bing/blob/main/rust/examples/quick_start.rs).

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
