#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#关于多重继承
# class Runnable(object):
#      def run(self):
#      	print('Running……')
# class Flyable(object):
#      def run(self):
#      	print('Running……')		
# 多重继承中的MixIn
# 在设计类的继承关系时，通常，主线都是单一继承的。
# class Student(object):
# 	"""docstring for Student"""
# 	def __init__(self, name):
# 		self.name = name
# 	def __str__(self):
# 		 return 'Student object (name: %s)' % self.name
#     __repr__ = __str__
# # print(Student('Michael'))
# s = Student('xuwei')
# print (s)
# 斐波那契数列为例
# class Fib(object):
# 	"""docstring for Fib"""
# 	def __init__(self):
# 		self.a ,self.b=0,1 #初始化两个计数器a，b
# 	def __iter__(self):
# 		return self #实例本身就是迭代对象，故返回的自己
# 	def __next__(self):
# 		self.a, self.b =self.b, self.a+self.b #计算下一个值
# 		if self.a>100: #退出循环的条件
# 			raise StopIteration()
# 		return self.a
# 	# def __getitem__(self,n): #要想让这个类能够让其像list一样访问。
# 	# 	a,b=1,1
# 	# 	for x in range(n):
# 	# 		a,b=b,a+b
# 	# 	return a
# 	def __getitem__(self,n): #要想让这个类能够让其像list一样访问。
# 	    if isinstance(n,int):#n是索引
# 	    	a,b =1,1
# 	    	for x in range(n):
# 	    		a,b = b,a+b
# 	    	return a
# 	    if isinstance(n,slice): #n是切片
# 	        start = n.start
# 	        stop = n.stop
# 	        if start is None:
# 	        	start = 0
# 	        a,b=1,1
# 	        L = []
# 	        for x in range(stop):
# 	        	if x>= start:
# 	        		L.append(a)
# 	        	a,b = b,a+b
# 	        return L
# for n in Fib():
# 	print (n)
# f = Fib()
# print (f[10])
# 切片：
# f = Fib()
# print (f[:10:2])
# 关于动态去添加这些属性
# class Chain(object):

#     def __init__(self, path=''):
#         self._path = path

#     def __getattr__(self, path):
#         return Chain('%s/%s' % (self._path, path))

#     def __str__(self):
#         return self._path

#     __repr__ = __str__
# print(Chain().status.user.timeline.list)

#一个对象实例可以有自己的属性和方法，也可以直接

#使用枚举类
# from enum import Enum
# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# for name,member in Month.__members__.items():
# 	  print(name, '=>', member, ',', member.value)
#如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
# from enum import Enum, unique
# @unique
# class Weekday(Enum):
#     Sun = 0 #Sun的value 被设定为0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4m
#     Fri = 5
#     Sat = 6
# # @unique装饰器可以帮助我们检查保证没有重复值
# day1 = Weekday.Mon
# print(day1.value)
#使用元类
#type()
#type()函数可以查看一个类型或变量的类型，Hello是个class

