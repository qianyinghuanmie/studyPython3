#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''elif是else if的缩写，完全可以有多个elif，所以if语句的完整形式就是：'''
'''if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>'''
'''
练习

小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
用if-elif判断并打印结果：
'''
height = 1.77
weight = 75.5
BMI = (weight/height**2)
if BMI<18.5:
    print('体重过轻')
elif BMI<25:
    print('体重正常')
elif BMI<28:
    print('体重过重')
elif BMI<32:
    print('肥胖')
else:
    print('严重肥胖')