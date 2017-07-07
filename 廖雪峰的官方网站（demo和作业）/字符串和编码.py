#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#作业
s1 = 72
s2 = 85
r = (s2-s1)/s1*100
print('小明成绩提升了：%.1f%%' %r)

'''最后一行的这一部分%.1f%%' %r就是占位符的应用，它实际分三部分：
1, %.1f
2, %%
3, %r

%.1f就是一个占位符号，f表示它是给一个浮点数占的位，f前面的.1表示取一位小数；
%%就是显示一个百分号，因为%被当占位符用了，当结果中要显示百分号时，需要用%%来实现；
%r,这个r才是真正的主角，在最后显示的结果中，前面的占位符%.f将被r的数值取代。

所以最后显示的结果是： 小明的成绩提升了：18.1%'''