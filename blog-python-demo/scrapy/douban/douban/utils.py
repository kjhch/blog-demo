# -*- coding: utf-8 -*-
"""
utils

@author: hch
@date  : 2021/1/9
"""
import requests

SERVER = "localhost:5000"
USE_PROXY = False


def get_proxy():
    r = None
    if USE_PROXY:
        try:
            resp = requests.get(f'http://{SERVER}/proxy')
            r = resp.text
        except Exception as e:
            print(e)
    return r


def del_proxy(p):
    try:
        requests.delete(f'http://{SERVER}/proxy?key={p}')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    get_proxy()
    # del_proxy(183)
