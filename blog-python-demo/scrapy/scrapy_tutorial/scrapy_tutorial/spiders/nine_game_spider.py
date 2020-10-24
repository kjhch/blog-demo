# -*- coding: utf-8 -*-
"""
爬取九游文章数据

@author: hch
@date  : 2020/10/13
"""

import scrapy
from scrapy.http.response.html import HtmlResponse
from urllib.parse import urlparse


class NineGameSpider(scrapy.Spider):
    domain_xpath = {
        'www.9game.cn': '//div[contains(@class,"article-page-con")]/div[@class="text-con"]',
        'news.4399.com': '//div[@class="content"]'

    }
    title_xpath = '/html/head/title/text()'

    name = 'nine_game_spider'
    allowed_domains = ['www.9game.cn', 'news.4399.com/meiti']
    start_urls = [
        # 'https://www.9game.cn/wodeshijie1/4707686.html',
        'http://news.4399.com/meiti/zixun/xinwen/m/925510.html',
        'http://news.4399.com/yssy/zixun/m/925648.html',
    ]

    def parse(self, response: HtmlResponse, **kwargs):
        domain = urlparse(response.url).netloc
        print(response.url, response.ip_address)

        title_selector = response.xpath(self.title_xpath)
        print(type(title_selector), title_selector, title_selector.get())

        article_selector = response.xpath(self.domain_xpath.get(domain))
        for desc in article_selector.xpath('./descendant::*/text()'):
            paragraph = desc.get().strip()
            if paragraph:
                print(type(desc), paragraph)

        # for p in response.xpath('//div[contains(@class,"article-page-con")]/div[@class="text-title"]/child::*/text()'):
        #     print("===")
        #     print(p.extract().strip())
