require_relative "lib/crawlora/bing/version"

Gem::Specification.new do |spec|
  spec.name = "crawlora-bing"
  spec.version = Crawlora::Bing::VERSION
  spec.summary = "Bing API client for Crawlora (5 endpoints)"
  spec.description = "Ruby client for Crawlora's hosted Bing API. Covers web, news, image, and video search plus query suggestions across 5 endpoints."
  spec.authors = ["Crawlora"]
  spec.license = "MIT"
  spec.required_ruby_version = ">= 2.6"
  spec.files = Dir["lib/**/*.rb", "README.md", "CHANGELOG.md", "LICENSE"]
  spec.require_paths = ["lib"]
  spec.homepage = "https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=bing-ruby-homepage"
  spec.metadata = { "source_code_uri" => "https://github.com/Crawlora-org/crawlora-bing", "documentation_uri" => "https://github.com/Crawlora-org/crawlora-bing/blob/main/ruby/README.md", "rubygems_mfa_required" => "true" }

end
