# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Movie(scrapy.Item):
    title = scrapy.Field()
    director = scrapy.Field()
    writer = scrapy.Field()
    starring = scrapy.Field()
    genre = scrapy.Field()
    area = scrapy.Field()
    language = scrapy.Field()
    release_date = scrapy.Field()
    runtime = scrapy.Field()
    alias = scrapy.Field()
    rating = scrapy.Field()
    comments_num = scrapy.Field()
    summary = scrapy.Field()

