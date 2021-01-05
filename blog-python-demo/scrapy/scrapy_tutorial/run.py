# -*- coding: utf-8 -*-
"""
爬虫的入口脚本

@author: hch
@date  : 2020/10/13
"""
import sys
from scrapy import cmdline


def main(argc: int, argv: list):
    if argc > 3 and argv[1] == 'scrapy':
        cmdline.execute(argv[1:])
    else:
        cmdline.execute('scrapy crawl quote'.split(' '))


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
