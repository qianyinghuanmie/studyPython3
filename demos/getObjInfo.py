#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#获取对象的信息
# a = type(123)
# print (a)
# b = type('123')
# print (b)
# c = type(None)
# print (c)
# d = type(abs)
# print (d)
#判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
# type(fn)==types.FunctionType
# type(abs)==types.BuiltinFunctionType
# type(lambda x: x)==types.LambdaType
# type((x for x in range(10)))==types.GeneratorType
#isinstance()就可以告诉我们，一个对象是否是某种类型。先创建3种类型的对象
#使用dir()
#如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回
#个包含字符串的list，比如，获得一个str对象的所有属性和方法：
# print(dir('abc'))
# print('abc'.__len__())
# class MyObject(object):
#     def __init__(self):
# 	     self.x=9
#     def power(self):
#     	return self.x * self.x
# obj = MyObject()
# print (getattr(obj, 'x', 404))
# 获取属性的值，如果获取不到的话，返回404
#########################################
#实例属性和类属性
class Student(object):
	"""docstring for Student"""
	name = 'Student'
s = Student()
print (s.name)