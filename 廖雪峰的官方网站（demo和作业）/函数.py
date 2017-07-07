#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python内置了很多有用的函数，我们可以直接调用。

n1 = 255
n2 = 1000
print(hex(1))

# 定义函数
'''定义函数时，需要确定函数名和参数个数；

如果有必要，可以先对参数的数据类型做检查；

函数体内部可以用return随时返回函数结果；
………………………………………………………………………………………………………………………………………………
练习

请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：

ax2 + bx + c = 0

的两个解。'''
import math


def quadratic(a, b, c):
    f = b**2 - 4 * a * c
    if f < 0:
        return ('方程无解')
    elif f == 0:
        return (-b / (2 * a))
    else:
        x1 = (-b - math.sqrt(f)) / (2 * a)
        x2 = (-b + math.sqrt(f)) / (2 * a)
        return (x1, x2)
print(quadratic(2, 3, 1))

# 函数参数
'''1 位置参数
: 通过参数的位置，传入函数
2 默认参数
：一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
二是如何设置默认参数。
当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
（既然是默认参数的话，一般是不怎么变化的才对）
3 可变参数
顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个
要定义出这个函数，我们必须确定输入的参数。由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来，这样，函数可以定义如下：
4 关键字参数
而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。请看示例：
def person(name, age, **kw):
5 命名关键字参数
6 参数组合'''
# 定义一个可变函数


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(2, 3))
# 本质上应该就是传个list或者tuple

# 定义一个关键字参数


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
print(person('Michael', 30))
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)
# kw作为一dict传入进去

# 命名关键字参数
# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。


def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。


def person(name, age, *, city, job):
    print(name, age, city, job)
# 注意了，调用的时候应该传入关键字参数，例如上面定义的函数，应该传入city='beijing',job='engineer'
# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：


def person(name, age, *args, city, job):
    print(name, age, args, city, job)

# 参数组合
'''在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：
必选参数、默认参数、可变参数、命名关键字参数和关键字参数'''


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

# 递归函数


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)
print(fact(100))
'''关于递归就不得不提他尾递归，这个好像在哪个语言都有，在JavaScript也是这样'''
# 尾递归优化后的


def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
print(fact(6))
'''使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。

针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。

Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。'''
'''在JavaScript的严格模式好像是有尾递归的优化。

#递归的练习作业
汉诺塔的移动可以用递归函数非常简单地实现。

请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法，例如：'''
# 汉诺塔
B=[]
def move(n,a,b,c):
    if n==1:
        buzhou=a+str(n)+'-->'+c+str(n) #一个圆盘需要从A到C操作步骤
        B.append(buzhou)
    else:
        move(n-1,a,c,b) #将前n-1个盘子从A移动到B上
        buzhou=a+str(n)+'-->'+c+str(n) #将A柱的第n个盘移到C柱操作步骤
        B.append(buzhou) #向列表中添加操作步骤
        move(n-1,b,a,c) #将B上的n-1个盘子移动到C上
move(5,'A','B','C')
print('总共需要操作'+str(len(B))+'次,\n'+'操作过程为:',B)