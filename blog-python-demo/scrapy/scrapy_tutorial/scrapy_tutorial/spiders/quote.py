# -*- coding: utf-8 -*-
"""
爬取http://quotes.toscrape.com/

@author: hch
@date  : 2021/1/5
"""
import scrapy
from scrapy.http import HtmlResponse

from scrapy_tutorial.items import Quote


class QuoteSpider(scrapy.Spider):
    name = "quote"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mongo_collection = "quote"
        self.start_urls = [kwargs.get("start_url", "http://quotes.toscrape.com/")]
        self.allowed_domains = [kwargs.get("allowed_domain", "quotes.toscrape.com")]

    def parse(self, response: HtmlResponse, **kwargs):
        for r in response.css("div.quote"):
            quote = Quote(text=r.css("span.text::text").get(),
                          author=r.css("small.author::text").get(),
                          tags=r.css("div.tags a.tag::text").getall())
            yield quote
        next_page = response.css("li.next>a")
        if next_page:
            yield response.follow(next_page.attrib['href'])
