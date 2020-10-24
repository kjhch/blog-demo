# -*- coding: utf-8 -*-
"""
测试对象属性以及一些相关的魔法方法

@author: hch
@date  : 2020/10/4
"""
import basic.sys_test
import basic.sys_test


class T:
    """默认继承object类"""
    attr1 = 'attr1'

    def __init__(self):
        self.attr2 = 'attr2'
        # self._prot = 'prot'
        # self.__pri = 'pri'
        print(self, 'init', '\n')

    def __getitem__(self, key):
        """通过dict方式访问属性时会调用该方法"""
        print('__getitem__ called:', key)
        # print(self, super())
        # return getattr(self, key)
        return super().__getattribute__(key)

    def __getattr__(self, name):
        """当属性不存在时调用"""
        print('__getattr__ called:', name)
        return '%s not existed' % name

    def __setattr__(self, key, value):
        print('__setattr__ called:', key, value)
        return super().__setattr__(key, value)

    def __delattr__(self, item):
        print('__delattr__ called:', item)
        return super().__delattr__(item)

    def __getattribute__(self, name):
        """获取属性或调用方法时执行"""
        print('__getattribute__ called:', name)
        # return super(T, self).__getattribute__(name)  # python2写法
        return super().__getattribute__(name)

    def m(self):
        pass


class TC(T):
    """T的子类，继承T中的方法和属性"""
    attr3: str = 'attr3'

    def __init__(self):
        super().__init__()
        self.attr4 = 'attr4'
        self._attr5 = 'attr5'
        self.__attr6 = 'attr6'
        # print(self._prot, self.__pri)
        print(self, 'init', '\n')


if __name__ == '__main__':
    print('=' * 20, 'T', '=' * 20)
    t = T()
    print('t.__dir__():', t.__dir__(), '\n')  # 返回一个list，包含当前类和父类的属性和方法
    print('t.__dict__:', t.__dict__, '\n')  # 仅包含当前类的属性
    print('getattr(t, attr1):', getattr(t, 'attr1'), '\n')
    print('T.attr1:', T.attr1, '\n')  # 通过类访问属性不会调用__getattribute__
    print('getattr(t, attr2):', getattr(t, 'attr2'), '\n')
    print('t.attr2:', t.attr2, '\n')
    print('t[attr2]:', t['attr2'], '\n')  # 使用dict的形式访问属性，会调用__getitem__
    print('t.buz:', t.buz, '\n')  # 属性不存在，会调用__getattr__
    print('t.m():', t.m(), '\n')
    print(delattr(t, 'attr2'))

    print('=' * 20, 'TC', '=' * 20)
    tc = TC()
    print('tc.attr1:', tc.attr1, '\n')
    print('tc[attr1]:', tc['attr1'], '\n')
    print('tc[attr2]:', tc['attr2'], '\n')
    print('tc[attr3]:', tc['attr3'], '\n')
    print('tc[attr4]:', tc['attr4'], '\n')
    print(tc._attr5, '\n')  # 最好不要访问保护变量
    print(tc.__attr6, '\n')  # python会对双下划线属性进行名称修饰，只能通过_TC__attr6强行访问
    print(tc._TC__attr6)
