# -*- coding: utf-8 -*-
"""
测试可迭代（iterable），迭代器（iterator）和生成器（generator）

@author: hch
@date: 2020/10/4
"""


class T:
    def __init__(self, n=5):
        self.n = n

    def generate(self):
        count = 0
        while count < self.n:
            yield count  # 每next一次，在这边产生中断
            count += 1


def generate():
    n = 0
    while n < 5:
        yield n
        n += 1


def yield_once():
    yield 'only yield once'
    return 'yield return...'


def generate1():
    result = []
    for i in range(5):
        result.append(i)
    return result


if __name__ == '__main__':
    t = T()
    g_m = t.generate()  # 通过对象方法获得生成器
    print(g_m, type(g_m), "g.next():", g_m.__next__())  # 通过迭代器的next魔术方法迭代生成器元素
    # t.n = 0
    # next(g)  # StopIteration

    g_f = generate()  # 通过普通函数获取生成器
    print(g_f, type(g_f), "g1.next():", next(g_f))  # 通过内建的next函数迭代生成器元素

    for i in generate1():  # 迭代iterable对象——list，for自动使用iter函数创建iterator
        print(i, end=' ')
    print()

    for i in generate():  # 迭代generator对象——由生成器函数生成
        print(i, end=' ')
    print()

    # next(range(3))  # TypeError: 'range' object is not an iterator
    # next([1, 2, 3])  # TypeError: 'list' object is not an iterator
    itr = iter(range(3))
    print(itr, type(itr), itr.__next__(), next(itr))

    y = yield_once()
    y.__next__()
    # next(y)  # StopIteration: yield return...
