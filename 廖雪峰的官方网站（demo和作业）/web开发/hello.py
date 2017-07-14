#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
……………………………………………………………………………………………………………………………………………………………………………………………………
WSGI接口

了解了HTTP协议和HTML文档，我们其实就明白了一个Web应用的本质就是：


1、浏览器发送一个HTTP请求；

2、服务器收到请求，生成一个HTML文档；

3、服务器把HTML文档作为HTTP响应的Body发送给浏览器；

4、浏览器收到HTTP响应，从HTTP Body取出HTML文档并显示。

最简单的Web应用就是先把HTML用文件保存好，用一个现成的HTTP服务器软件，接收用户请求，从文件中读取HTML，返回。

Apache、Nginx、Lighttpd等这些常见的静态服务器就是干这件事情的。

我们用Python专注于生成HTML文档。因为我们不希望接触到TCP连接、HTTP原始请求和响应格式，

所以，需要一个统一的接口，让我们专心用Python编写Web业务。

这个接口就是WSGI：Web Server Gateway Interface。

WSGI接口定义非常简单，它只要求Web开发者实现一个函数，就可以响应HTTP请求。我们来看一个最简单的Web版本的“Hello, web!”：


'''


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]

'''
通常情况下，都应该把Content-Type头发送给浏览器。其他很多常用的HTTP Header也应该发送。

所以application()函数必须由WSGI服务器来调用。
好消息是Python内置了一个WSGI服务器，这个模块叫wsgiref，它是用纯Python编写的WSGI服务器的参考实现。所谓“参考实现”是指该实现完全符合WSGI标准，但是不考虑任何运行效率，仅供开发和测试使用

小结

无论多么复杂的Web应用程序，入口都是一个WSGI处理函数。HTTP请求的所有输入信息都可以通过environ获得，HTTP响应的输出都可以通过start_response()加上函数返回值作为Body。

复杂的Web应用程序，光靠一个WSGI函数来处理还是太底层了，我们需要在WSGI之上再抽象出Web框架，进一步简化Web开发。
'''