# -*- coding: utf-8 -*-
"""
python自带库urllib的一些测试

@author: hch
@date  : 2020/10/12
"""

from urllib.request import *
from urllib.parse import *
from urllib.robotparser import *


class UrllibTest:
    @staticmethod
    def encode_test():
        encode = urlencode([('a', ['w', 'q', 'e']), ('s', 'query')])
        print(encode)
        print(unquote(encode))

    @staticmethod
    def robot_test():
        rp = RobotFileParser('http://www.jianshu.com/robots.txt')
        rp.read()
        print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
        print(rp.can_fetch('*', "http://www.jianshu.com/search?q=python&page=1&type=collections"))
        print(rp.can_fetch('*', "http://www.jianshu.com/test"))


if __name__ == '__main__':
    UrllibTest.encode_test()
    UrllibTest.robot_test()
    # print(urlopen('http://www.baidu.com').read())
