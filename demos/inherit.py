#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#继承和多态
class Animal(object):
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Cat is running...')

class Cat(Animal):
     def run(self):
        print('Cat is running...')
dog = Dog()
dog.run()

a = list()
b = Animal()
c = Dog()
print (isinstance(a, list))
print (isinstance(b, Animal))
print (isinstance(c, Dog))

print (isinstance(c, Animal))
def run_twice(animal):
	animal.run()
	animal.run()
runDemo = run_twice(Cat())

#继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。
#动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。