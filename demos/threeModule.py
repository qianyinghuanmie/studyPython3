#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 获取当前的时间
# from datetime import datetime
#
# now = datetime.now()  # 获取当前datetime
# print(now)
#
# # 获取指定日期和时间
# from datetime import datetime
#
# dt = datetime(2015, 4, 19, 12, 20) #用指定日期时间创建datetime
# dt = dt.timestamp()
# t = datetime.fromtimestamp(dt)
# print(dt)
# print(t)
#转时间戳
# 还有关于str的转换，dateime 的加减，以及utc之间的转换

# collections
# collections是Python内建的一个集合模块，提供了许多有用的集合类。

# collections模块提供了一些有用的集合类，可以根据需要选用。

# import hashlib
#
# md5 = hashlib.md5()
# md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
# print(md5.hexdigest())
# import itertools
# natuals = itertools.count(1)
# for n in natuals:
#     print(n)
# import itertools
#
# natuals = itertools.count(1)
# ns = itertools.takewhile(lambda x: x <= 10, natuals)
# a =  list(ns)
# print(a)

#contextlib
# 只要有正确的上下文管理，就可以用于with语句，在这个类定义了进入和退出的函数。
# class Query(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     def __enter__(self):
#         print('Begin')
#         return self
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         if exc_type:
#             print('Error')
#         else:
#             print('End')
#
#     def query(self):
#         print('Query info about %s...' % self.name)
#
# with Query('Bob') as q:
#     q.query()

# 使用contextlib库，可以有更加简单的方法。
# from contextlib import contextmanager
#
# class Query(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     def query(self):
#         print('Query info about %s...' % self.name)
#
# @contextmanager
# def tag(name):
#     print("<%s>" % name)
#     yield
#     print("</%s>" % name)
#
# with tag("h1"):
#     print("hello")
#     print("world")
# # 如果一个类，没有上下文的话，可以使用closing实现
from urllib import request

with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))

    from urllib import request

    req = request.Request('http://www.douban.com/')
    req.add_header('User-Agent',
                   'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    with request.urlopen(req) as f:
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', f.read().decode('utf-8'))