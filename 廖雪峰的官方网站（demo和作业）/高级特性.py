#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''切片,有了切片操作，很多地方循环就不再需要了。
Python的切片非常灵活，一行代码就可以实现很多行循环才能完成的操作。
切片操作十分有用。我们先创建一个0-99的数列：'''
L = list(range(100))
#1 取前十位数
print (L[:10])
#2 取后十位数
print (L[-10:])
#3 前11-20个数：
print (L[10:20])
#4 前10个数，每两个取一个：
print (L[:10:2])
#5 所有数，每5个取一个：
print (L[::5])
#6 所有数
# print (L[:])
'''tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：'''
print ((0, 1, 2, 3, 4, 5)[:3])
'''字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：'''
print ( 'ABCDEFG'[:3])
'''其实感觉字符串的切片反而会常用到。'''

'''迭代
如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。
感觉类似于JavaScript中for in 循环
'''
for ch in 'ABCDEFG':
	print(ch)
'''判断是否是可迭代对象的方法。方法是通过collections模块的Iterable类型判断：'''
from collections import Iterable
isIterable =isinstance('abc',Iterable)
print(isIterable)
isIterable =isinstance(123,Iterable)
print(isIterable)
'''同理，如果在Python里面想要获取键值对的话，在for in 循环中传两个参数。
例如'''
for i, value in enumerate(['A', 'B', 'C']):
	print(i,value)
#相同的，也可以去使用两个变量
for x, y in [(1, 1), (2, 4), (3, 9)]:
	print(x, y)
'''……………………………………………………………………………………………………………………………………………………………………………………………………
列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
如：'''
list(range(1,11))  #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[x * x for x in range(1, 11)]  #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
[x * x for x in range(1, 11) if x % 2 == 0]  #[4, 16, 36, 64, 100]
#还可以使用两层循环，可以生成全排列：
[m + n for m in 'ABC' for n in 'XYZ'] #['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
'''运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
>>> import os # 导入os模块，模块的概念后面讲到
>>> [d for d in os.listdir('.')] # os.listdir可以列出文件和目录
['.emacs.d', '.ssh', '.Trash', 'Adlm', 'Applications', 'Desktop', 'Documents', 'Downloads', 'Library', 'Movies', 'Music', 'Pictures', 'Public', 'VirtualBox VMs', 'Workspace', 'XCode']
for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
>>> d = {'x': 'A', 'y': 'B', 'z': 'C' }
>>> for k, v in d.items():
...     print(k, '=', v)
...
y = B
x = A
z = C
因此，列表生成式也可以使用两个变量来生成list：
>>> d = {'x': 'A', 'y': 'B', 'z': 'C' }
>>> [k + '=' + v for k, v in d.items()]
['y=B', 'x=A', 'z=C']
…………………………………………………………………………………………………………………………………………………………………………………………
练习
如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
'''
L = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L if isinstance(s, str) == True]
print(L2)

'''生成器
通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间
，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
Python中，这种一边循环一边计算的机制，称为生成器：generator。
要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：\
'''
g = (x * x for x in range(10))
for n in g:
	print(n)
'''所以，我们创建了一个generator后，基本上永远不会调用next()，而是通过for循环来迭代它，并且不需要关心StopIteration的错误。

generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。

比如，著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：

斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易：
'''
def fib(max):
	n ,a ,b =0,0,1
	while n<max:
		yield b
		a,b = b, a+b
		n=n+1
	return 'done'
f = fib(6)
for i in f:
	print (i)
'''generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
意思是只有next()调用的时候，才能跳过yield，这样理解应该也行吧
除此之外要注意的一点就是：
但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
这个后面在研究下，先跳过
练习

杨辉三角定义如下：
   		  1
        1   1
      1   2   1
    1   3   3   1
  1   4   6   4   1
1   5   10  10  5   1
把每一行看做一个list，试写一个generator，不断输出下一行的list：'''
def triangles():
    L = [1]              #定义L为一个只包含一个元素的列表
    while True:
        yield L          #定义为生成器函数
        L =[1] + [L[n] + L[n-1] for n in range(1,len(L))] + [1]
f = triangles()
n = 0
for t in f:
    print(t)
    n = n + 1
    if n == 10:
        break
'''迭代器
我们已经知道，可以直接作用于for循环的数据类型有以下几种：

一类是集合数据类型，如list、tuple、dict、set、str等；
一类是generator，包括生成器和带yield的generator function。
这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。
可以使用isinstance()判断一个对象是否是Iterable对象：

凡是可作用于for循环的对象都是Iterable类型；

凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
Python的for循环本质上就是通过不断调用next()函数实现的，例如：
for x in [1, 2, 3, 4, 5]:
    pass
实际上完全等价于：
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
也就是说使用for循环的时候，不好写错误机制吧。
