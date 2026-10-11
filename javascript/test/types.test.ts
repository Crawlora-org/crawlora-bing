import { BingClient } from "../src/index.js";

const client = new BingClient({ apiKey: "test-key" });
void client.images({"q": "sample"});
void client.request("bing-images", {"q": "sample"});
const streamResponse: Promise<Response> = client.request("bing-images", {"q": "sample"}, { responseType: "stream" });
const operationStream: Promise<Response> = client.operation("bing-images", {"q": "sample"}, { responseType: "stream" });
const directStream: Promise<Response> = client.images({"q": "sample"}, { responseType: "stream" });
void streamResponse; void operationStream; void directStream;
void client.request("bing-images", {"q": "sample", "page": 1, "count": 1, "country": "sample", "lang": "sample"}, { responseType: "text" });
const rawText: Promise<string> = client.request("bing-images", {"q": "sample"}, { responseType: "text" });
void rawText;



// @ts-expect-error The selected operation requires its documented params.
void client.images();
