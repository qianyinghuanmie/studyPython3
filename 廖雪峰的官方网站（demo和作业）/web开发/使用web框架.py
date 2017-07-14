#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
了解了WSGI框架，我们发现：其实一个Web App

，就是写一个WSGI的处理函数，针对每个HTTP请求进行响应。

但是如何处理HTTP请求不是问题，问题是如何处理100个不同的URL

每一个URL可以对应GET和POST请求，当然还有PUT、DELETE等请求，但是我们通常只考虑最常见的GET和POST请求。

最简单的想法是从environ变量里取出HTTP请求的信息，然后逐个判断：

但太多的url判断就会相当麻烦

在这里引用一个Flask的web框架

写一个app.py，处理3个URL，分别是：

GET /：首页，返回Home；

GET /signin：登录页，显示登录表单；

POST /signin：处理登录表单，显示登录结果

注意噢，同一个URL/signin分别有GET和POST两种请求，映射到两个处理函数中。

'''


# from flask import Flask
# from flask import request

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def home():
#     return '<h1>Home</h1>'

# @app.route('/signin', methods=['GET'])
# def signin_form():
#     return '''<form action="/signin" method="post">
#               <p><input name="username"></p>
#               <p><input name="password" type="password"></p>
#               <p><button type="submit">Sign In</button></p>
#               </form>'''

# @app.route('/signin', methods=['POST'])
# def signin():
#     # 需要从request对象读取表单内容：
#     if request.form['username']=='admin' and request.form['password']=='password':
#         return '<h3>Hello, admin!</h3>'
#     return '<h3>Bad username or password.</h3>'

# if __name__ == '__main__':
#     app.run()

'''
实际的Web App应该拿到用户名和口令后，去数据库查询再比对，来判断用户是否能登录成功。

在这里是进行了用户名和密码的模拟。

除了Flask，常见的Python Web框架还有：

Django：全能型Web框架；

web.py：一个小巧的Web框架；

Bottle：和Flask类似的Web框架；

Tornado：Facebook的开源异步Web框架。

当然了，因为开发Python的Web框架也不是什么难事，我们后面也会讲到开发Web框架的内容。

'''