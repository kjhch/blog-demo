# -*- coding: utf-8 -*-
"""
生成器测试，生产者消费者为例

@author: hch
@date  : 2020/10/28
"""
from types import GeneratorType


def consumer():
    r = ''
    while True:
        n = yield r
        print(f'consumer consumes {n}...')
        r = f'{n} ok'


def producer(c: GeneratorType):
    c.send(None)  # 必须send None来初始化
    n = 0
    while n < 5:
        n += 1
        print(f'producer produces {n}')
        r = c.send(n)
        print(f'producer get msg from consumer: {r}')
    c.close()


def gen1():
    total = 0
    while True:
        n = yield total
        print(f'get n: {n}')
        if n:
            total += n
        else:
            break
    return total


def gen2(itr):
    r = yield from itr
    print(f'return {r}')
    # for t in itr:
    #     yield t


if __name__ == '__main__':
    producer(consumer())

    g = gen2(gen1())
    g.send(None)
    print(g.send(1))
    print(g.send(2))
    print(g.send(3))
    print(g.send(4))
    print(g.send(None))

    g = gen2(['a', 'b', 'c'])
    print(g.send(None))
    print(g.send(None))
    # print(g.send(1)) # AttributeError: 'list_iterator' object has no attribute 'send'

