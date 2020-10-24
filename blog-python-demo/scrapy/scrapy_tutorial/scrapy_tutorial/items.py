# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyTutorialItem(scrapy.Item):
    """ Item 定义结构化数据字段，用来保存爬取到的数据，有点像 Python 中的 dict，但是提供了一些额外的保护减少错误。类似于ORM """
    # define the fields for your item here like:
    name = scrapy.Field()
    title = scrapy.Field()
    info = scrapy.Field()
