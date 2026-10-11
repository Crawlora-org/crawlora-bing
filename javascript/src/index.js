import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class BingClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-bing-js/0.1.1" });
    this["images"] = (...args) => this.request("bing-images", ...args);
    this["news"] = (...args) => this.request("bing-news", ...args);
    this["search"] = (...args) => this.request("bing-search", ...args);
    this["suggest"] = (...args) => this.request("bing-suggest", ...args);
    this["videos"] = (...args) => this.request("bing-videos", ...args);
  }
}

export { BingClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.1.1";
export default BingClient;
