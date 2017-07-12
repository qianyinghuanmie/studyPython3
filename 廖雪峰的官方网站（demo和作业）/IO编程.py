#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
IO在计算机中指Input/Output，也就是输入和输出。

比如你打开浏览器，访问新浪首页，浏览器这个程序就需要通过网络IO获取新浪的网页。

浏览器首先会发送数据给新浪服务器，告诉它我想要首页的HTML，这个动作是往外发数据，叫Output，

随后新浪服务器把网页发过来，这个动作是从外面接收数据，叫Input。

所以，通常，程序完成IO操作会有Input和Output两个数据流。

当然也有只用一个的情况，比如，从磁盘读取文件到内存，就只有Input操作

反过来，把数据写到磁盘文件里，就只是一个Output操作。

异步IO来编写程序性能会远远高于同步IO

异步IO的缺点是编程模型复杂。


得知道什么时候通知你“汉堡做好了”，而通知你的方法也各不相同。如果是服务员跑过来找到你，这是回调模式，

如果服务员发短信通知你，你就得不停地检查手机，这是轮询模式。总之，异步IO的复杂度远远高于同步IO。


注意，本章的IO编程都是同步模式，异步IO由于复杂度太高，后续涉及到服务器端程序开发时我们再讨论。

'''
'''
………………………………………………………………………………………………………………………………………………………………………………………………………………

文件读写

读写文件是最常见的IO操作。Python内置了读写文件的函数，用法和C是兼容的。

读写文件就是请求操作系统打开一个文件对象

然后，通过操作系统提供的接口从这个文件对象中读取数据

或者把数据写入这个文件对象
…………………………………………………………………………………………

读文件

要以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标示符：

>>> f = open('/Users/michael/test.txt', 'r')

标示符'r'表示读，这样，我们就成功地打开了一个文件。

如果文件不存在，open()函数就会抛出一个IOError的错误，并且给出错误码和详细的信息告诉你文件不存在：

>>> f=open('/Users/michael/notfound.txt', 'r')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: '/Users/michael/notfound.txt'

如果文件打开成功，接下来，调用read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示：


>>> f.read()
'Hello, world!'

'''
f = open('test.txt', 'r')
print(f.read())
f.close() # 文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源 并且操作系统同一时间能打开的文件数量也是有限的：
# Python引入了with语句来自动帮我们调用close()方法：
with open('test.txt', 'r') as f:
    print(f.read())
'''
%……………………………………………………………………………………………………………………………………………………………………………………………………………………
file-like Object

像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Objec
………………………………
二进制文件
用'rb'模式打开文件即可：

>>> f = open('/Users/michael/test.jpg', 'rb')
>>> f.read()
b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00...' # 十六进制表示的字节

………………………………
字符编码

要给open()函数传入encoding参数，例如，读取GBK编码的文件
>>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
>>> f.read()
'测试'

你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：

>>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')

…………………………………………………………………………
写文件

写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件

>>> f = open('/Users/michael/test.txt', 'w')
>>> f.write('Hello, world!')
>>> f.close(

你可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件
同理，也是有方便的witch方法

with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!')
要写入特定编码的文本文件，请给open()函数传入encoding参数，将字符串自动转换成指定编码。

……………………………………
小结

在Python中，文件读写是通过open()函数打开的文件对象完成的。使用with语句操作文件IO是个好习惯。

'''
'''
…………………………………………………………………………………………………………………………………………………………………………………………………………………………

StringIO和BytesIO

StringIO：


StringIO顾名思义就是在内存中读写str。

要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：

'''

from io import StringIO
f = StringIO()
f.write('hello')
print(f.getvalue()) # getvalue()方法用于获得写入后的str。

'''
要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：
……………………………………………………………………
>>> from io import StringIO
>>> f = StringIO('Hello!\nHi!\nGoodbye!')
>>> while True:
...     s = f.readline()
...     if s == '':
...         break
...     print(s.strip())
...
Hello!
Hi!
Goodbye!
……………………………………………………………………………………

………………………………………………………………………………………………………………………………………………………………………………………………………………………………

BytesIO

StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。

BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes：
'''

from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
'''

请注意，写入的不是str，而是经过UTF-8编码的bytes。
和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取：

>>> from io import BytesIO
>>> f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
>>> f.read()
b'\xe4\xb8\xad\xe6\x96\x87'
……………………………………………………………………………………………………………………………………
小结

StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。

'''

'''
……………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………

操作文件和目录


如果我们要操作文件、目录，可以在命令行下面输入操作系统提供的各种命令来完成。比如dir、cp等命令。

'''

import os
print(os.name)
'''
如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。

要获取详细的系统信息，可以调用uname()函数：
………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………

环境变量

………………………………………………………………………………………………………………

操作文件和目录

操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：


# 查看当前目录的绝对路径:
>>> os.path.abspath('.')
'/Users/michael'
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
>>> os.path.join('/Users/michael', 'testdir')
'/Users/michael/testdir'
# 然后创建一个目录:
>>> os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
>>> os.rmdir('/Users/michael/testdir')

把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。

在Linux/Unix/Mac下，os.path.join()返回这样的字符串：part-1\part-2


同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：

>>> os.path.split('/Users/michael/testdir/file.txt')
('/Users/michael/testdir', 'file.txt')

os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便

>>> os.path.splitext('/path/to/file.txt')
('/path/to/file', '.txt')

最后看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码：

>>> [x for x in os.listdir('.') if os.path.isdir(x)]
['.lein', '.local', '.m2', '.npm', '.ssh', '.Trash', '.vim', 'Applications', 'Desktop', ...]
'''

# >>> [x for x in os.listdir('.') if os.path.isdir(x)]

#要列出所有的.py文件，也只需一行代码：

# >>> [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']

'''
练习


1.利用os模块编写一个能实现dir -l输出的程序。

2.编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
'''

import os
def search(dir, text):
    for x in os.listdir(dir):
        if os.path.isfile(os.path.join(dir,x)):
            if text in os.path.splitext(x)[0]:
                print('%s, %s'% (dir, x))
        if os.path.isdir(os.path.join(dir,x)):
            search(os.path.join(dir, x),text)


search(r'C:\Users\fdd\Desktop\个人项目\pythonDemo\hello-python3','test')


'''
……………………………………………………………………………………………………………………………………………………………………………………………………

序列化


程序运行的过程中，所有的变量都是在内存中，

定义一个dict：
d = dict(name='Bob', age=20, score=88)

可以随时修改变量，比如把name改成'Bill'，

但是一旦程序结束，变量所占用的内存就被操作系统全部回收

如果没有把修改后的'Bill'存储到磁盘上，下次重新运行程序，变量又被初始化为'Bob'。

我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，

在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。

Python提供了pickle模块来实现序列化。

举例说明：

'''

import pickle

d = dict(name='Bob', age=20, score=88)

print(pickle.dumps(d))

'''
pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。

>>> f = open('dump.txt', 'wb')
>>> pickle.dump(d, f)
>>> f.close()

看看写入的dump.txt文件，一堆乱七八糟的内容，这些都是Python保存的对象内部信息。

当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象


>>> f = open('dump.txt', 'rb')
>>> d = pickle.load(f)
>>> f.close()
>>> d
{'age': 20, 'score': 88, 'name': 'Bob'}

变量的内容又回来了！
………………………………………………………………………………………………………………………………………………………………………………

JSON


如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式

JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。

JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：

JSON类型	Python类型
{}				dict
[]				list
"string"		str
1234.56			int或float
true/false		True/False
null			None
'''

#Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。

import json
d = dict(name='Bob', age=20, score=88)
print(json.dumps(d))
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))
'''
dumps()方法返回一个str，内容就是标准的JSON。
似的，dump()方法可以直接把JSON写入一个file-like Object。

要把JSON反序列化为Python对象

用loads()或者对应的load()方法，前者把JSON的字符串反序列化，

后者从file-like Object中读取字符串并反序列化：

小结

Python语言特定的序列化模块是pickle，但如果要把序列化搞得更通用、更符合Web标准，就可以使用json模块。

json模块的dumps()和loads()函数是定义得非常好的接口的典范。当我们使用时，只需要传入一个必须的参数。但是，当默认的序列化或反序列机制不满足我们的要求时，我们又可以传入更多的参数来定制序列化或反序列化的规则，
既做到了接口简单易用，又做到了充分的扩展性和灵活性。
'''