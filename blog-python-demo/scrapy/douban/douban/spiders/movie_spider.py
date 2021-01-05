# -*- coding: utf-8 -*-
"""
豆瓣电影爬虫

@author: hch
@date  : 2021/1/5
"""
import scrapy


class MovieSpider(scrapy.Spider):
    name = "movie"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [kwargs.get("start_url", "http://movie.douban.com")]
        self.allowed_domains = kwargs.get("allowed_domains", ["movie.douban.com"])

    def parse(self, response, **kwargs):
        print(response)
