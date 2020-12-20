# -*- coding: utf-8 -*-
"""
TODO description

@author: hch
@date  : 2020/12/20
"""
import asyncio
import time


async def coroutine_A():
    print("协程A开始执行")
    print("协程A出让执行权")
    await asyncio.sleep(2)
    print("协程A重新获得执行权,并执行结束")


async def coroutine_B():
    print("协程B开始执行")
    print("协程B出让执行权")
    await asyncio.sleep(2)
    print("协程B重新获得执行权,并执行结束")


# 协程C始终不出让执行权
async def coroutine_C():
    while (1):
        time.sleep(0.4)
        print("协程C不使用await关键字，故不选择出让执行权，所以继续执行C")


if __name__ == "__main__":
    start_time = time.time()
    loop = asyncio.get_event_loop()
    group1 = [coroutine_A(), coroutine_B(),  ]
    # group1 = asyncio.gather(*group1)
    loop.run_until_complete(asyncio.gather(*group1, return_exceptions=True))
    print("程序运行时间: {}".format(time.time() - start_time))
