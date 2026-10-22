# Bing clients for Crawlora

Official Crawlora client packages for the hosted Bing API. Access 5 API endpoints covering web, news, image, and video search plus query suggestions from JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust. These clients call Crawlora's hosted API; they do not scrape Bing locally. Requests use your Crawlora account and `CRAWLORA_API_KEY`; service usage follows your account billing plan. Crawlora is independent from and not affiliated with or endorsed by Bing or its owners.

## Language packages

- JavaScript / TypeScript: [`@crawlora-org/bing`](javascript/README.md)
- Python: [`crawlora-bing`](python/README.md)
- Go: [`github.com/Crawlora-org/crawlora-bing`](go.mod)
- Ruby: [`crawlora-bing`](ruby/README.md)
- Java: [`net.crawlora:crawlora-bing:0.2.0`](java/README.md)
- PHP: [`crawlora/bing`](php/README.md)
- Rust: [`crawlora-bing`](rust/README.md)

For installation and runnable examples, use the README for your language. See the [API endpoint and parameter reference](docs/usage.md) for shared operation details.

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=bing-repository-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=bing-repository-console) to get an API key, or read the [API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=bing-repository-api-docs). Keep `CRAWLORA_API_KEY` out of source control.

## API coverage and supported endpoints

The seven language clients provide access to all 5 selected public Bing API operations. Search or browse by endpoint path and operation ID below; the [complete API reference](docs/usage.md) adds parameters, enums, and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/bing/images` | `bing-images` | Search Bing image results |
| `GET` | `/bing/news` | `bing-news` | Search Bing news results |
| `GET` | `/bing/search` | `bing-search` | Search Bing web results |
| `GET` | `/bing/suggest` | `bing-suggest` | Suggest Bing search queries |
| `GET` | `/bing/videos` | `bing-videos` | Search Bing video results |

## License

MIT. See [LICENSE](LICENSE).
