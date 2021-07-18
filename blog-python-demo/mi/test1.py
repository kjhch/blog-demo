# -*- coding: utf-8 -*-
"""
TODO description

@author: hch
@date  : 2021/3/27
"""

import miio

if __name__ == '__main__':
    plug = miio.device.Device(ip="192.168.3.23", token="c6ec82f352204d5b271edbc58b728192")
    lamp = miio.device.Device(ip="192.168.3.12", token="bded6801ce54818b59080c72be27cd2b")
    ai = miio.device.Device(ip="192.168.3.7", token="74344b527276467145584c6f36657173")
    # miiocli device --ip 192.168.3.23 --token c6ec82f352204d5b271edbc58b728192 info
    # miiocli yeelight --ip 192.168.3.12 --token bded6801ce54818b59080c72be27cd2b status
    miio.yeelight.Yeelight(ip="192.168.3.12", token="bded6801ce54818b59080c72be27cd2b").on()
    miio.yeelight.Yeelight(ip="192.168.3.12", token="bded6801ce54818b59080c72be27cd2b").off()

    print(plug.info())
    print(lamp.info())
    print(ai.info())
