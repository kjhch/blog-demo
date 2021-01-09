# -*- coding: utf-8 -*-
"""
豆瓣电影爬虫

@author: hch
@date  : 2021/1/5
"""
import scrapy
from scrapy import Request
from scrapy.http import HtmlResponse

from douban.items import Movie
from douban.utils import get_proxy


class MovieSpider(scrapy.Spider):
    name = "movie"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [kwargs.get("start_url", "https://movie.douban.com/top250")]
        self.allowed_domains = kwargs.get("allowed_domains", ["movie.douban.com"])
        self.mongo_collection = 'douban_movie'

    def start_requests(self):
        yield Request(self.start_urls[0], meta={'proxy': get_proxy()})

    def parse(self, response: HtmlResponse, **kwargs):
        # 电影详情页
        if "subject" in response.url:
            movie = Movie()
            info = response.css("div#info")
            rating = response.css("div#interest_sectl")
            movie['title'] = response.css("h1>span[property='v:itemreviewed']::text").get()
            movie['director'] = info.css("a[rel='v:directedBy']::text").getall()
            movie['writer'] = info.css("span.pl:contains('编剧')+span>a::text").getall()
            movie['starring'] = info.css("a[rel='v:starring']::text").getall()
            movie['genre'] = info.css("span[property='v:genre']::text").getall()
            movie['area'] = info.re('<span class="pl">制片国家/地区:</span>(.*?)<br>')[0].split("/")
            movie['language'] = info.re('<span class="pl">语言:</span>(.*?)<br>')[0].split("/")
            movie['release_date'] = info.css("span[property='v:initialReleaseDate']::text").getall()
            movie['runtime'] = info.css("span[property='v:runtime']::text").getall()
            movie['alias'] = info.re('<span class="pl">又名:</span>(.*?)<br>')[0].split("/")
            movie['rating'] = rating.css("strong[property='v:average']::text").get()
            movie['comments_num'] = rating.css("span[property='v:votes']::text").get()
            movie['summary'] = response.css("div#link-report > span[property='v:summary']::text").getall()
            yield movie
        else:
            # 生成电影详情页请求
            yield from response.follow_all(response.css("div.hd > a::attr(href)"), meta={'proxy': get_proxy()})

            # 生成下一页请求
            next_page = response.css("span.next > a::attr(href)")
            if next_page:
                yield response.follow(next_page[0], meta={'proxy': get_proxy()})
