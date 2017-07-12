#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''函数是Python内建支持的一种封装，我们通过把大段代码拆成函数，通过一层一层的函数调用，就可以把复杂任务分解成简单的任务，这种分解可以称之为面向过程的程序设计。函数就是面向过程的程序设计的基本单元。

而函数式编程（请注意多了一个“式”字）——Functional Programming，虽然也可以归结到面向过程的程序设计，但其思想更接近数学计算。

我们首先要搞明白计算机（Computer）和计算（Compute）的概念。

在计算机的层次上，CPU执行的是加减乘除的指令代码，以及各种条件判断和跳转指令，所以，汇编语言是最贴近计算机的语言。

而计算则指数学意义上的计算，越是抽象的计算，离计算机硬件越远。

对应到编程语言，就是越低级的语言，越贴近计算机，抽象程度低，执行效率高，比如C语言；越高级的语言，越贴近计算，抽象程度高，执行效率低，比如Lisp语言。

函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量，因此，任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数我们称之为没有副作用。而允许使用变量的程序设计语言，由于函数内部的变量状态不确定，同样的输入，可能得到不同的输出，因此，这种函数是有副作用的。

函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！

Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。'''

'''高阶函数
函数本身也可以赋值给变量，即：变量可以指向函数。
这样的一个例子
f=abs
f(-10) 这里f是一函数
f = abs（-10） 这里f是一个变量

……………………这样的话也就可以把函数当做参数传入
例如：
def add(x, y, f):
    return f(x) + f(y)
ps：挺好理解的，JavaScript是叫做回调函数

……………………………………………………map/reduce…………………………………………………………………………………………………………
Python内建了map()和reduce()函数。

我们先看map。map()函数接收两个参数，一个是函数，一个是Iterable，
map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
在这里，str是一个函数，[1, 2, 3, 4, 5, 6, 7, 8, 9]是一个Iterable
'''
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

'''再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
>>> from functools import reduce
>>> def add(x, y):
...     return x + y
...
>>> reduce(add, [1, 3, 5, 7, 9])
25

这个例子本身没多大用处，但是，如果考虑到字符串str也是一个序列，
对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数：
>>> from functools import reduce
>>> def fn(x, y):
...     return x * 10 + y
...
>>> def char2num(s):
...     return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
...
>>> reduce(fn, map(char2num, '13579'))
13579

整理成一个str2int的函数就是：'''
from functools import reduce


def char2num(s):  # 将字符串和数字对应起来
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
# 这就是一个把字符串转化为整数的函数，而且只需要几行代码！！！！！
print(str2int('32310481290'))

'''练习

1利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，
其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：'''


def normalize(name):
    return name.capitalize()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

'''2 Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
# 测试:'''


def fn(x, y):
    return x * y


def prod(L):
    return reduce(fn, L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
'''3.利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：'''

from functools import reduce


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

'''思路:
先判断是否是浮点数
如果是浮点数的话，通过.截取分为两部分分别为S[0],S[1]
整数部分还是一样，
浮点数部分通过切片的方式[::-1]，，然后加起来即可得到数字
'''
# def str2float(s):
#     s = s.split('.')
#     if '.' in s:
#         return reduce(lambda x, y: x * 10 + y, map(char2num, s[0])) + reduce(lambda x, y: x / 10 + y, map(char2num, s[1][::-1])) / 10
#     else:
#     	return reduce(lambda x, y: x * 10 + y, map(char2num, s))
# print(str2float('123.456'))
'''filter也接收一个函数和一个序列，其实就是一个筛选函数
例如，在一个list中，删掉偶数，只保留奇数，可以这么写：'''


def is_odd(n):
    return n % 2 == 1
print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))
'''把一个序列中的空字符串删掉，可以这么写：'''


def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))
'''练习
回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数：'''


def is_palindrome(n):
    return str(n) == str(n)[::-1]
output = filter(is_palindrome, range(1, 1000))
print(list(output))
'''sorted
排序算法
排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。
如果是数字，我们可以直接比较，但如果是字符串或者两个dict呢？直接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数抽象出来。
Python内置的sorted()函数就可以对list进行排序：
无参数，对数字的处理会从小到大进行排序
例如：
'''
print(sorted([36, 5, -12, 9, -21]))
'''此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
'''
print(sorted([36, 5, -12, 9, -21], key=abs))
'''练习
假设我们用一组tuple表示学生名字和成绩：
'''
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):  # 参数t代表着一个tuple
    return t[0].lower()


def by_score(t):
    return t[1]
    pass
L2 = sorted(L, key=by_score)
print(L2)

'''………………………………………………………………………………………………………………………………………………………………………………………………………………
返回函数：
函数作为返回值，举个例子，实现一个可变参数的求和
'''


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1, 3, 5, 7, 9)
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f2)
print(f())
'''
在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。

请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：

f1()和f2()的调用结果互不影响
'''

'''匿名函数
当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便
在Python中，对匿名函数提供了有限支持。还是以map()函数为例，计算f(x)=x2时，除了定义一个f(x)的函数外，还可以直接传入匿名函数：
举个例子：
list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
在这行代码中匿名函数lambda x: x * x实际上就是：
def f(x):
    return x * x
关键字lambda表示匿名函数，冒号前面的x表示函数参数。
'''
'''
…………………………………………………………………………………………………………………………………………………………………………………………………………………………………………
装饰器
由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
def now():
	print('2015-3-25')
f = now
f()
f.__name__ = ’now‘
函数对象有一个__name__属性，可以拿到函数的名字：now
现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：
'''


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2015-3-25')
print(now())
'''
由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。'''


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
# 这个是一个三层嵌套的decorator


@log('execute')
def now():
    print('2015-3-25')
now()
'''我们来分析上面的代码，首先是执行log('execute')，返回的是decorator函数，再调用返回的函数，
参数是now函数，返回值最终是wrapper函数。
小结
在面向对象（OOP）的设计模式中，decorator被称为装饰模式。OOP的装饰模式需要通过继承和组合来实现
而Python除了能支持OOP的decorator外,直接从语法层次支持decorator。
Python的decorator可以用函数实现，也可以用类实现。
decorator可以增强函数的功能，定义起来虽然有点复杂，但使用起来非常灵活和方便。


请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。

再思考一下能否写出一个@log的decorator，使它既支持：

# args, **kw 应该是支持任意参数的意思
'''

import functools


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            	print('begin call %s()' % func.__name__)
            	func(*args, **kw)
            	print('end  call %s()' % func.__name__)                               
        return wrapper
    return decorator

@log('111111')
def f():
    print('hah')
print(f())
'''偏函数
Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）。
要注意，这里的偏函数和数学意义上的偏函数不一样。
举个例子说明：
int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换：
但其实也是可是二进制，八进制，16进制转换
如果传入base参数，就可以做N进制的转换：
假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去：
def int2(x, base=2):
    return int(x, base)
这样的方法是设置一个int2的函数

functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2

import functools
int2 = functools.partial(int, base=2)

所以，简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。


当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
'''