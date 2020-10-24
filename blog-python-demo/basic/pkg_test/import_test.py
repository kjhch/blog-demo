# -*- coding: utf-8 -*-
"""
cd到项目目录下，执行python3 basic/pkg_test/import_test.py
从结果可以推断，python执行时会将入口文件所在路径加入到PYTHONPATH中

@author: hch
@date  : 2020/10/15
"""
import sys

print('from b import *')
from b import *

print('from b.c import *')
from b.c import *

print(sys.path)

print('#' * 20, 'exception occurred', '#' * 20)
print('from pkg_test import *')
from pkg_test import *

