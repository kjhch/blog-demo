# -*- coding: utf-8 -*-
"""
TODO description

@author: hch
@date  : 2021/3/27
"""
import codecs
import socket
from miio.protocol import Message

if __name__ == '__main__':
    helobytes = bytes.fromhex('21310020ffffffffffffffffffffffffffffffffffffffffffffffffffffffff')

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.sendto(helobytes, ('192.168.3.23', 54321))  # 插座ip，端口54321

    data, addr = s.recvfrom(1024)
    print(data, addr)

    m=Message.parse(data)

    tok=codecs.encode(m.checksum,'hex')

    print(m)

    print(tok)
