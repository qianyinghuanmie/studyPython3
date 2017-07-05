#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# class Student(object):
# 	def __init__(self, name, score):
# 		# super(Student, self).__init__()
# 		self.name = name
# 		self.score = score

# 	def print_score(self):
# 		print ('%r: %s' % (self.name, self.score))

# bart = Student('Bart SimPoson ', '59')
# bart.print_score()
# bart.name = 'hah'
# print (bart.name)
# 在设置对象的时候，可以给属性加上双划线，让其变成私有属性。=
#在不加下划线的时候是公有变量
class Student(object):
    def __init__(self, name, score):
	    self.__score = score
	    self.__name = name

    def get_name(self):
         return self.__name

    def get_score(self):
         return self.__name
bart = Student('abc', '90')
print (bart.get_name())