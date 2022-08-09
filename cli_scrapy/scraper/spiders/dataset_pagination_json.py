import scrapy
from scraper.items import Dataset


class DatasetSpider(scrapy.Spider):
    name = "dataset_pagination_json"
    allowed_domains = ["catalog.data.gov"]
    start_urls = ["https://catalog.data.gov/dataset"]

    max_pages = 5

    custom_settings = {"FEED_FORMAT": "json", "FEED_URI": "file:///tmp/out.json"}

    def parse(self, response):
        host = response.url.split("/dataset")[0]

        for dataset in response.css(".dataset-content"):
            yield Dataset(
                name=dataset.css("h3.dataset-heading > a::text").get(),
                link=host + dataset.css("h3.dataset-heading > a::attr(href)").get(),
                organization=dataset.css(".dataset-organization::text")
                .get()
                .strip(" —"),
            )

        # might not work.. gov page now looks different
        # idea - read page, and then call self on next page
        for link in response.css(".pagination > ul > li:last-child:not(.active) > a"):
            page_number = int(link.attrib["href"].split("=")[1])
            print("--------------page_number:", page_number)
            if page_number > self.__class__.max_pages:
                break
            yield response.follow(link, callback=self.parse)
