# Crawlora Bing API client for PHP (`crawlora/bing`)

This PHP package calls Crawlora's hosted Bing API at `https://api.crawlora.net/api/v1`. It exposes 5 endpoints covering web, news, image, and video search plus query suggestions. It does not call or scrape Bing directly. Requests require a Crawlora API key and use your Crawlora account's service plan.

## Install

```sh
composer require crawlora/bing
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=bing-php-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=bing-php-console) to get an API key, then set `CRAWLORA_API_KEY` in your environment.

```php
<?php
require __DIR__ . '/vendor/autoload.php';

$client = new Crawlora\Bing\Client(apiKey: getenv('CRAWLORA_API_KEY'));
$result = $client->request("bing-search", ['q' => 'sample']);
print_r($result);
$client->close();
```

The client uses PHP cURL and JSON. Constructor options are `apiKey`, `baseUrl`, and `timeout`. Call the operation-specific method for direct access to each supported operation, or `request($operationId, $params, $responseType)` to dispatch by operation ID. Set `$responseType` to `text` for raw text output such as transcript formats. The package includes 5 API operations.

## Supported Bing API endpoints

Browse every route included in this Composer package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-bing/blob/main/docs/usage.md) includes parameter and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/bing/images` | `bing-images` | Search Bing image results |
| `GET` | `/bing/news` | `bing-news` | Search Bing news results |
| `GET` | `/bing/search` | `bing-search` | Search Bing web results |
| `GET` | `/bing/suggest` | `bing-suggest` | Suggest Bing search queries |
| `GET` | `/bing/videos` | `bing-videos` | Search Bing video results |

See [Crawlora](https://crawlora.net/?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=bing-php-homepage), the [API documentation](https://crawlora.net/docs?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=bing-php-api-docs), and the [PHP client source](https://github.com/Crawlora-org/crawlora-bing). The complete operation and parameter reference is in the [platform repository](https://github.com/Crawlora-org/crawlora-bing/blob/main/docs/usage.md).
