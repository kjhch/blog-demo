# -*- coding: utf-8 -*-
"""
测试sys模块的一些属性以及一些预置属性，例如python库路径等
https://docs.python.org/3.8/reference/import.html#import-related-module-attributes
https://docs.python.org/3.8/library/sys.html#module-sys

@author: hch
@date  : 2020/10/5
"""

import sys

# 导入模块时会打印下述属性
module_attrs = {
    '__name__': __name__,
    '__loader__': __loader__,
    '__package__': __package__,
    '__spec__': __spec__,
    # '__path__': __path__,
    '__file__': __file__,
    '__cached__': __cached__,
}
w = max(map(len, module_attrs.keys()))

print('#' * 30, 'module attrs of ' + __name__, '#' * 30)
for k, v in module_attrs.items():
    # print(k, v)
    # print('{0:^20s}:{1:s}'.format(k, str(v)))  # 填充与格式化：:[填充字符][对齐方式 < ^ >][宽度][进制/精度/类型]
    print(k.ljust(w), ':', v)
print('#' * 30, 'module attrs of ' + __name__, '#' * 30, '\n')

if __name__ == '__main__':
    print('python home: ', sys.prefix)
    print('解释器路径：', sys.executable)
    print('模块搜索路径：', sys.path)
    print('OS平台：', sys.platform)
    print('命令行参数：', sys.argv)
    print('版本信息：', sys.version)
