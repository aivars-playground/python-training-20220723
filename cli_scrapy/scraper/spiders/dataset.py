import scrapy


class DatasetSpider(scrapy.Spider):
    name = 'dataset'
    allowed_domains = ['catalog.data.gov']
    start_urls = ['http://catalog.data.gov/']

    def parse(self, response):
        pass
