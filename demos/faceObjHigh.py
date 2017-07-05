#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# class Student(object):
# 	pass
# s = Student()
# s.name = "xuwei"
# print (s.name)
# def set_age(self, age):
# 	self.age=age
# from types import MethodType
# s.set_age=MethodType(set_age, s) #给实例绑定一个方法
# s.set_age(25) #调用实例方法
# print (s.age)
#注意：给一个实例绑定方法，对另一个实例是没有作用的。
#要想每个实例都有方法，直接在class绑定方法，类似于属性。
# class Student(object):
#       __slots__ = ('name', 'age', 'score') #用tuple定义允许绑定的属性名称
# #在这里slots起到的作用是限制class实例能够添加的属性
# s = Student()
# s.name = "xuwei"
# s.age = 25
# s.score = 99
# print (dir(s))
#使用@property
#在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：
# class Student(object):
# 	"""docstring for Student"""
# 	def get_score(self):
# 		return self.score
# 	def set_score(self, value):
# 		if not isinstance(value, int):
# 			raise ValueError('score must be an integer!')
# 		if value<0 or value>100:
# 			raise ValueError('score must between 0 ~ 100!')
# 		self.score= value
# s = Student()
# s.set_score(101)
# print(s.get_score())
