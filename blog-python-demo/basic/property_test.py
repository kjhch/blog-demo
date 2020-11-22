# -*- coding: utf-8 -*-
"""
测试@property装饰器

@author: hch
@date  : 2020/11/16
"""


class PropertyTest:
    def __init__(self):
        self._name = 'init1'
        self.name = 'init2'

    @property
    def name(self):
        print('name getter')
        return self._name

    @name.setter
    def name(self, value):
        print('name setter: ' + value)
        self._name = value


if __name__ == '__main__':
    p = PropertyTest()
    p.name = 'test'
    print(p.name)
