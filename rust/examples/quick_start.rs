use crawlora_bing::{BingSearchParams, Client, ModelBingSearchResponseDoc};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = std::env::var("CRAWLORA_API_KEY")?;
    let client = Client::new(api_key)?;
    let response = client
        .bing
        .search(BingSearchParams {
            q: Some("open source web crawler".to_owned()),
            ..Default::default()
        })
        .await?;
    let data: ModelBingSearchResponseDoc = response.into_json()?;
    println!("{data:#?}");
    Ok(())
}
