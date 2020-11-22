# -*- coding: utf-8 -*-
"""
测试可迭代（iterable），迭代器（iterator）和生成器（generator）

@author: hch
@date: 2020/10/4
"""
from typing import Iterable, Iterator


class T:
    def __init__(self, n=5):
        self.n = n

    def generate(self):
        count = 0
        while count < self.n:
            yield count  # 每next一次，在这边产生中断
            count += 1


class MyRange:
    def __init__(self, num):
        self.num = num

    def __iter__(self):
        """实现该方法，该对象就是一个iterable"""
        return self.MyItr(self.num)

    class MyItr:
        """内部类实现迭代器"""

        def __init__(self, mx):
            self.current = 0
            self.mx = mx

        def __next__(self):
            """实现该方法，该对象就是一个iterator"""
            if self.current >= self.mx:
                raise StopIteration
            r = self.current
            self.current += 1
            return r


def generate():
    n = 0
    while n < 5:
        yield n
        n += 1


def yield_once():
    yield 'only yield once'
    return 'yield return...'


def list1():
    result = []
    for e in range(5):
        result.append(e)
    return result


def test_iterable():
    """测试可迭代对象"""

    """迭代iterable对象——list，for自动使用iter函数创建iterator"""
    for j in list1():
        print(j, end=' ')
    print()

    """next只能应用于iterator"""
    # next(range(3))  # TypeError: 'range' object is not an iterator
    # next([1, 2, 3])  # TypeError: 'list' object is not an iterator
    itr = iter(range(3))
    print(itr, type(itr), itr.__next__(), next(itr))

    mr = MyRange(3)
    print(next(iter(mr)))
    for j in mr:
        print(j, end=' ')
    print(', mr is Iterable:', isinstance(mr, Iterable), ', mr is Iterator:', isinstance(mr, Iterator))


def test_generator():
    t = T()
    g_m = t.generate()  # 通过对象方法获得生成器
    print(g_m, type(g_m), "g.next():", g_m.__next__())  # 通过迭代器的next魔术方法迭代生成器元素
    # t.n = 0
    # next(g)  # StopIteration

    g_f = generate()  # 通过普通函数获取生成器
    print(g_f, type(g_f), "g1.next():", next(g_f))  # 通过内建的next函数迭代生成器元素

    for i in generate():  # 迭代generator对象——由生成器函数生成
        print(i, end=' ')
    print()

    y = yield_once()
    y.__next__()
    # next(y)  # StopIteration: yield return...


if __name__ == '__main__':
    test_iterable()
    test_generator()
