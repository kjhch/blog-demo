# -*- coding: utf-8 -*-
"""
测试字符串的一些操作

@author: hch
@date  : 2020/10/17
"""

if __name__ == '__main__':
    name = 'hch'
    age = 18
    print(f'My name is {name}, {age} years old.')
    print(r'\n')
    print(b'abc'.decode('utf-8'))
    # print(b'中')  # SyntaxError: bytes can only contain ASCII literal characters.
    print(u'中')

    print('%s is %d in digital, %x in hex, %o in octal' % ('eleven', 11, 11, 11))
