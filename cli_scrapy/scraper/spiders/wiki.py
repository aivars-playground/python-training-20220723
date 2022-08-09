import scrapy
from scraper.items import Contribution


class DatasetSpider(scrapy.Spider):
    name = "wiki"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/w/index.php?title=Scrapy&action=history"]

    custom_settings = {
        "FEED_FORMAT": "json",
        "FEED_URI": ".ignoreme/wiki_out.json",
    }

    def __init__(self):
        self.page = 0

    def parse(self, response):
        for contribution in response.css(".mw-contributions-list"):
            yield Contribution(
                author=contribution.css(".history-user > a::attr(title)").get(),
                dates=contribution.css(".mw-changeslist-date::text").extract(),
                page=self.page,
            )

        for nextlink in response.css("a.mw-nextlink"):
            self.page += 1
            yield response.follow(nextlink, callback=self.parse)
