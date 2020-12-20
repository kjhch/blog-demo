# -*- coding: utf-8 -*-
"""
异步io测试

@author: hch
@date  : 2020/10/28
"""
import asyncio
from time import sleep, strftime


@asyncio.coroutine
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(1)
    print("Hello again!")


async def test():
    task1 = asyncio.create_task(asyncio.sleep(1))
    task2 = asyncio.create_task(asyncio.sleep(2))
    print(f"begin {strftime('%X')}")
    await task1
    await task2
    print(f'over {strftime("%X")}')


async def pause(delay):
    await asyncio.sleep(delay)


if __name__ == '__main__':
    asyncio.run(test())
