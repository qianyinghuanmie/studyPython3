#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# f = open('test.txt', 'r')
# print(f.read())
# f.close()
# with open('test.txt', 'r') as f:
#     print(f.read())
# with open('test.txt', 'w') as f:
#     f.write('Hello, world!')
#
# with open('test.png', 'rb') as f:
#     print(f.read())
#  StringIO和 BytesIO
# StringIO

# from io import StringIO
# f = StringIO('hello\nhi!\ngoodbye')
# while True:
#     s = f.readline()
#     if s == '':
#         break
#     print(s.strip())
# print(f.getvalue())
#  BytesIO
# from io import BytesIO
# f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
# print(f.read())
#
# import os
# print(os.environ)
# print(os.environ.get('PATH'))
# print(os.path.abspath('.'))
# a = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
# print(a)
# 序列化
import pickle
# d = dict(name = 'Bob', age = 20, score =88)
# print(pickle.dumps(d))
# f = open('test.txt', 'wb')
# pickle.dump(d, f)
# f.close()
# f = open('test.txt', 'rb')
# d = pickle.load(f)
# f.close()
# print(d)
#Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，因此
# ，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。
# python对象转为json对象
# import json
# d = dict(name = 'Bob', age = 20, score =818)
# a = json.dumps(d)
# print(a)
# json对象转为python对象
# import json
# json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# print (json.loads(json_str))

import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
# def student2dict(std):
#         return {
#             'name': std.name,
#             'age': std.age,
#             'score': std.score
#         }
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))