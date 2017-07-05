#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '#一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；

__author__ = 'Michael Liao'   # __author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；

import sys  #导入sys模块后,可以使用这个变量

def test():
    args = sys.argv #sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称
    if len(args)==1: #args
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')
if __name__=='__main__':
  test()

#作用域

#在一个模块中，我们可能会定义很多函数和变量，
#但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。在Python中，是通过_前缀来实现的。
#
def _private_1(name):
    return 'Hello, %s' % name  # 定义一个私有方法1
def _private_2(name):
    return 'Hi, %s' % name   # 定义一个私有方法2
def greeting(name):          # 暴露方扥greeting
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

