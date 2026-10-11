# Crawlora Bing API client for Ruby (`crawlora-bing`)

This Ruby gem calls Crawlora's hosted Bing API at `https://api.crawlora.net/api/v1`. It exposes 5 endpoints covering web, news, image, and video search plus query suggestions; it does not call or scrape Bing directly. Requests require your Crawlora API key and use your account's service plan.

## Install

```ruby
gem "crawlora-bing"
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=bing-ruby-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=bing-ruby-console) to get an API key, and set `CRAWLORA_API_KEY` before running the client:

```ruby
require "json"
require "crawlora/bing"

client = Crawlora::Bing::Client.new
result = client.request("bing-search", JSON.parse("{\"q\": \"sample\"}"))
puts result
client.close
```

Use an operation-specific method for normal calls. `request(operation_id, params = {}, response_type: :auto)` is available for every operation. `response_type: :text` returns raw response text. This gem includes 5 API operations.

```ruby
client = Crawlora::Bing::Client.new(api_key: ENV.fetch("CRAWLORA_API_KEY"), timeout: 30)
# client.<operation_method>(<endpoint parameters>)
client.close
```

Client options include `api_key`, `base_url`, and `timeout`. Ruby stdlib provides the HTTP and JSON support.

## Supported Bing API endpoints

Browse every route included in this gem. The [endpoint reference](https://github.com/Crawlora-org/crawlora-bing/blob/main/docs/usage.md) includes parameter and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/bing/images` | `bing-images` | Search Bing image results |
| `GET` | `/bing/news` | `bing-news` | Search Bing news results |
| `GET` | `/bing/search` | `bing-search` | Search Bing web results |
| `GET` | `/bing/suggest` | `bing-suggest` | Suggest Bing search queries |
| `GET` | `/bing/videos` | `bing-videos` | Search Bing video results |

See [Crawlora](https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=bing-ruby-homepage), the [API documentation](https://crawlora.net/docs?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=bing-ruby-api-docs), and [the package repository](https://github.com/Crawlora-org/crawlora-bing) for account setup, the API operation reference, and release history.
