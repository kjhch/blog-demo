# -*- coding: utf-8 -*-
"""
lxml库的测试

@author: hch
@date  : 2020/10/13
"""

from lxml import etree
import requests


class LxmlTest:
    @staticmethod
    def xpath_test():
        # url = 'http://news.4399.com/xinwen/slcb/m/919733.html'
        # url = 'https://www.9game.cn/wodeshijie1/4707686.html'
        url = 'https://juejin.im/post/6875109882006077448'
        resp = requests.get(url)
        html = etree.fromstring(resp.text, etree.HTMLParser())
        print(html.xpath('/html/head/meta/@content'))
        print(html.xpath('//meta/@charset'))
        # print(etree.tostring(html))


if __name__ == '__main__':
    LxmlTest.xpath_test()
