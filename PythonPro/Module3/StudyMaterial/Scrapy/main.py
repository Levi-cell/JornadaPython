from scrapy import Spider

class exemploScrapy(Spider):
    name = "curso python pro"
    startUrls = ["http://quotes.toscrape.com/page/1",
                 "http://quotes.toscrape.com/page/2"]

    def parse(self, response, **kwargs):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").extract(),
                "author": quote.css("small.author::text").extract(),
                "tags": quote.css("div.tags a.tag::text").extract()
            }