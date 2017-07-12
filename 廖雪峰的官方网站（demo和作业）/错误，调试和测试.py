#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
在程序运行过程中，总会遇到各种各样的错误。

有的错误是程序编写有问题造成的，比如本来应该输出整数结果输出了字符串，这种错误我们通常称之为bug，bug是必须修复的。

有的错误是用户输入造成的，比如让用户输入email地址，结果得到一个空字符串，这种错误可以通过检查用户输入来做相应的处理。

还有一类错误是完全无法在程序运行过程中预测的，比如写入文件的时候，磁盘满了，写不进去了，或者从网络抓取数据，网络突然断掉了。这类错误也称为异常，在程序中通常是必须处理的，否则，程序会因为各种问题终止并退出。

Python内置了一套异常处理机制，来帮助我们进行错误处理。

此外，我们也需要跟踪程序的执行，查看变量的值是否正确，这个过程称为调试。Python的pdb可以让我们以单步方式执行代码。

最后，编写测试也很重要。有了良好的测试，就可以在程序修改后反复运行，确保程序输出符合我们编写的测试

………………………………………………………………………………………………………………………………………………………………………………………………

错误处理

高级语言通常都内置了一套try...except...finally...的错误处理机制，Python也不例外。
………………………………………………………………

try
让我们用一个例子来看看try的机制：

try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')
我们认为某些代码可能会出错时，就可以用try来运行这段代码，
如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，
即except语句块，执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。

上面的代码在计算10 / 0时会产生一个除法运算错误：
这是执行代码的输出：
………………
try...
except: division by zero
finally...
END
…………………
从输出可以看到，当错误发生时，后续语句print('result:', r)不会被执行，

except由于捕获到ZeroDivisionError，因此被执行。

最后，finally语句被执行。然后，程序继续按照流程往下走

如果把除数0改成2，则执行结果如下：

……………………
try...
result: 5
finally...
END
……………………

由于没有错误发生，所以except语句块不会被执行

但是finally如果有，则一定会被执行（可以没有finally语句）。

需要注意的是：：：：
可以有多个except来捕获不同类型的错误：

下面是多个except的例子

try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

以上新增了一个valueError，值的检验
一个except捕获ValueError，用另一个except捕获ZeroDivisionError。

可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句

Python的错误其实也是class，所有的错误类型都继承自BaseException，

所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。比如：

try:
    foo()
except ValueError as e:
    print('ValueError')
except UnicodeError as e:
    print('UnicodeError')
第二个except永远也捕获不到UnicodeError

因为UnicodeError是ValueError的子类，如果有，也被第一个except给捕获了。

Python所有的错误都是从BaseException类派生的，常见的错误类型和继承关系看这里：

https://docs.python.org/3/library/exceptions.html#exception-hierarchy

使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，

比如函数main()调用foo()，foo()调用bar()，结果bar()出错了，这时，只要main()捕获到了，就可以处理：

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')

也就是说，不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以了。这样一来，就大大减少了写try...except...finally的麻烦。

…………………………………………………………………………………………………………………………………………………………………………………………………………………………

调用堆栈


如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出。来看看err.py：



# err.py:
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    bar('0')

main()

执行，结果如下：

$ python3 err.py
Traceback (most recent call last):
  File "err.py", line 11, in <module>
    main()
  File "err.py", line 9, in main
    bar('0')
  File "err.py", line 6, in bar
    return foo(s) * 2
  File "err.py", line 3, in foo
    return 10 / int(s)
ZeroDivisionError: division by zero

错误信息第1行：
 
Traceback (most recent call last):  告诉我们这是错误的跟踪信息。


第2~3行： File "err.py", line 11, in <module>
    main()

    调用main()出错了，在代码文件err.py的第11行代码，但原因是第9行：

    File "err.py", line 9, in main
    bar('0')

    原因是return foo(s) * 2这个语句出错了，但这还不是最终原因，继续往下看：

      File "err.py", line 3, in foo
    return 10 / int(s)

    原因是return 10 / int(s)这个语句出错了，这是错误产生的源头，因为下面打印了：

    ZeroDivisionError: integer division or modulo by zero

    根据错误类型ZeroDivisionError，我们判断，int(s)本身并没有出错，但是int(s)返回0，在计算10 / 0时出错，至此，找到错误源头。
………………………………………………………………………………………………………………………………………………………………………………………………

记录错误

如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。

既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。

Python内置的logging模块可以非常容易地记录错误信息：
…………………………………………
# err_logging.py
……………………
import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')

…………………………………………………………

同样是出错，但程序打印完错误信息后会继续执行，并正常退出：
…………………………………………………………
$ python3 err_logging.py
ERROR:root:division by zero
Traceback (most recent call last):
  File "err_logging.py", line 13, in main
    bar('0')
  File "err_logging.py", line 9, in bar
    return foo(s) * 2
  File "err_logging.py", line 6, in foo
    return 10 / int(s)
ZeroDivisionError: division by zero
END
……………………………………………………………………
通过配置，logging还可以把错误记录到日志文件里，方便事后排查。

……………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………

抛出错误



因为错误是class，捕获一个错误就是捕获到该class的一个实例。
因此，错误并不是凭空产生的，而是有意创建并抛出的。

Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。

如果要抛出错误，首先根据需要，可以定义一个错误的class，

选择好继承关系，然后，用raise语句抛出一个错误的实例：


…………………………………………………………
# err_raise.py
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')
……………………………………………………………………………………

执行，可以最后跟踪到我们自己定义的错误：

…………………………………………………………………………
$ python3 err_raise.py 
Traceback (most recent call last):
  File "err_throw.py", line 11, in <module>
    foo('0')
  File "err_throw.py", line 8, in foo
    raise FooError('invalid value: %s' % s)
__main__.FooError: invalid value: 0
…………………………………………………………………………………………

只有在必要的时候才定义我们自己的错误类型。

如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），尽量使用Python内置的错误类型。

最后，我们来看另一种错误处理的方式：

………………………………………………………………
# err_reraise.py

def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()
……………………………………………………………………

在bar()函数中，我们明明已经捕获了错误，但是，打印一个ValueError!后，


又把错误通过raise语句抛出去了，这不有病么？

其实这种错误处理方式不但没病，而且相当常见

捕获错误目的只是记录一下，便于后续追踪。

但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。好比一个员工处理不了一个问题时，就把问题抛给他的老板，如果他的老板也处理不了

……………………………………………………
小结

Python内置的try...except...finally用来处理错误十分方便。出错时，会分析错误信息并定位错误发生的代码位置才是最关键的。

程序也可以主动抛出错误，让调用者来处理相应的错误。但是，应该在文档中写清楚可能会抛出哪些错误，以及错误产生的原因

'''

'''………………………………………………………………………………………………………………………………………………………………………………………………………………………
调试

方法1 ：：

断言（ps：有点像打断点）

举个例子：
……………………
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')
……………………
assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
如果断言失败，assert语句本身就会抛出AssertionError：
输出如下：
………………………………
$ python3 err.py
Traceback (most recent call last):
  ...
AssertionError: n is zero!
……………………………………

注： 启动Python解释器时可以用-O参数来关闭assert：
如 python3 -O err.py
………………………………………………………………………………………………………………………………………………………………

logging

和assert比，logging不会抛出错误，而且可以输出到文件：
'''
import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

'''
这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，
当我们指定level=INFO时，logging.debug就不起作用了。

。同理，指定level=WARNING后，debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。

logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。

…………………………………………………………………………………………………………………………………………………………………………………………………………………………………………

pdb


第4种方式是启动Python的调试器pdb

让程序以单步方式运行，可以随时查看运行状态。

我们先准备好一个程序：
………………………………
# err.py
s = '0'
n = int(s)
print(10 / n)
……………………………………
然后启动：


$ python3 -m pdb err.py
> /Users/michael/Github/learn-python3/samples/debug/err.py(2)<module>()
-> s = '0'


以参数-m pdb启动后，pdb定位到下一步要执行的代码-> s = '0'。输入命令l来查看代码：

(Pdb) l
  1     # err.py
  2  -> s = '0'
  3     n = int(s)
  4     print(10 / n)

输入命令n可以单步执行代码：

(Pdb) n
> /Users/michael/Github/learn-python3/samples/debug/err.py(3)<module>()
-> n = int(s)
(Pdb) n
> /Users/michael/Github/learn-python3/samples/debug/err.py(4)<module>()
-> print(10 / n)

任何时候都可以输入命令p 变量名来查看变量：

(Pdb) p s
'0'
(Pdb) p n
0

输入命令q结束调试，退出程序：
(Pdb) q

这种通过pdb在命令行调试的方法理论上是万能的，但实在是太麻烦了，

…………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………

pdb.set_trace()

这个方法也是用pdb，但是不需要单步执行，

我们只需要import pdb，然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点：

# err.py
import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)

运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境，可以用命令p查看变量，或者用命令c继续运行：

$ python3 err.py 
> /Users/michael/Github/learn-python3/samples/debug/err.py(7)<module>()
-> print(10 / n)
(Pdb) p n
0
(Pdb) c
Traceback (most recent call last):
  File "err.py", line 7, in <module>
    print(10 / n)
ZeroDivisionError: division by zero

这个方式比直接启动pdb单步调试效率要高很多，但也高不到哪去。

…………………………………………………………………………………………………………………………………………
IDE
打断点：哈哈哈哈哈

结论：

logging才是终极武器。

IDE调试起来比较方便，

'''

'''
………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………


单元测试

如果你听说过“测试驱动开发”（TDD：Test-Driven Development），单元测试就不陌生。


单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。

比如对函数abs()，我们可以编写出以下几个测试用例：


1.输入正数，比如1、1.2、0.99，期待返回值与输入相同；

2.输入负数，比如-1、-1.2、-0.99，期待返回值与输入相反；

3.输入0，期待返回0；

4.输入非数值类型，比如None、[]、{}，期待抛出TypeError。

把上面的测试用例放到一个测试模块里，就是一个完整的单元测试

如果单元测试通过，说明我们测试的这个函数能够正常工作。

单元测试通过后有什么意义呢？如果我们对abs()函数代码做了修改，只需要再跑一遍单元测试，如果通过，说明我们的修改不会对abs()函数原有的行为造成影响，如果测试不通过，
说明我们的修改与原有行为不一致，要么修改代码，要么修改测试。

我们来编写一个Dict类，这个类的行为和dict一致，但是可以通过属性来访问，用起来就像下面这样：


>>> d = Dict(a=1, b=2)
>>> d['a']
1
>>> d.a
1


mydict.py代码如下：

class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

为了编写单元测试，我们需要引入Python自带的unittest模块，编写mydict_test.py如下：

import unittest

from mydict import Dict

class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。

以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。



对每一类测试都需要编写一个test_xxx()方法。

由于unittest.TestCase提供了很多内置的条件判断，我们只需要调用这些方法就可以断言输出是否是我们所期望的

最常用的断言就是assertEqual()：

self.assertEqual(abs(-1), 1) # 断言函数返回的结果与1相等

另一种重要的断言就是期待抛出指定类型的Error

比如通过d['empty']访问不存在的key时，断言会抛出KeyError：

with self.assertRaises(KeyError):
    value = d['empty']
而通过d.empty访问不存在的key时，我们期待抛出AttributeError：

with self.assertRaises(AttributeError):
    value = d.empty 
……………………………………………………………………………………………………………………………………………………………………………………………………………………………………

运行单元测试

一旦编写好单元测试，我们就可以运行单元测试。
最简单的运行方式是在mydict_test.py的最后加上两行代码：

if __name__ == '__main__':
    unittest.main()
这样就可以把mydict_test.py当做正常的python脚本运行：
1  $ python3 mydict_test.py
2  还有一种方法：
$ python3 -m unittest mydict_test
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
推荐第二种方法。

…………………………………………………………………………………………………………………………………………
setUp与tearDown

可以在单元测试中编写两个特殊的setUp()和tearDown()方法。

setUp()和tearDown()方法有什么用呢？

设想你的测试需要启动一个数据库，这时，就可以在setUp()方法中连接数据库，在tearDown()方法中关闭数据库，


小结

单元测试可以有效地测试某个程序模块的行为，是未来重构代码的信心保证。

单元测试的测试用例要覆盖常用的输入组合、边界条件和异常。

单元测试代码要非常简单，如果测试代码太复杂，那么测试代码本身就可能有bug。

单元测试通过了并不意味着程序就没有bug了，但是不通过程序肯定有bug。

'''

'''
…………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………

文档测试

'''

# mydict2.py
class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__=='__main__':
    import doctest
    doctest.testmod()
# 什么输出也没有。这说明我们编写的doctest运行都是正确的。

#如果程序有问题，比如把__getattr__()方法注释掉，再运行就会报错：

'''
小结

doctest非常有用，不但可以用来测试，还可以直接作为示例代码。通过某些文档生成工具，
就可以自动把包含doctest的注释提取出来。用户看文档的时候，同时也看到了doctest。
'''