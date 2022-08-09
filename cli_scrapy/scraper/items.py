# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from dataclasses import dataclass


class Dataset(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    link = scrapy.Field()
    organization = scrapy.Field()


@dataclass
class Contribution:
    author: scrapy.Field()
    dates: scrapy.Field()
    page: scrapy.Field()
