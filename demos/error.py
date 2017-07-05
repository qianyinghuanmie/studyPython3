# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# def foo():
# 	r = some_funtion()
# 	if r===(-1):
# 		return (-1)
# 	return r
# def bar():
# 	r = foo()
# 	if r==(-1):
# 		print('Error')
# 	else:
# 		pass
# 一般来说，每个功能的实现都需要错误调试机制，在Python中，同样有try的方法
# try:
#     print('try...')
#     r = 10 / 0
#     print('result:', r)
# except ZeroDivisionError as e:
#     print('except:', e)
# finally:
#     print('finally...')
# print('END')

# try:
#     print('try...')
#     r = 10 / int('2')
#     print('result:', r)
# except ValueError as e:
#     print('ValueError:', e)
# except ZeroDivisionError as e:
#     print('ZeroDivisionError:', e)
# else:
#     print('no error!')
# finally:
#     print('finally...')
# print('END')
# 根据层级关系，捕捉错误只要在合适的地方捕捉就行

# 记录错误
# import logging

# def foo(s):
#     return 10 / int(s)

# def bar(s):
#     return foo(s) * 2

# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)

# main()
# print('END')

# 抛出错误
# 自己定义一个可以抛出的错误。
# class FooError(ValueError):
# 	pass
# def foo(s):
#     n = int(s)
#     if n==0:
# 	     raise FooError('invalid value: %s' % s)
#     return 10 / n
# foo(1)

# 调试 pdb
# pdb是一个调试器，可以单步运行，可以随时查看运行状态
# s = '0'
# n = int(s)
# print(10/n)
# 单元测试
import unittest
from error import Dict


class TestDict(unittest.TestCase):
    """docstring for TestDict"""

    def test_init(self):
        d = Dict(a=1, n='test')

    self.assertEqual(d.a, 1)
