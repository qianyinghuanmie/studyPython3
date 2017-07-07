#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''和list比较，dict有以下几个特点：

查找和插入的速度极快，不会随着key的增加而变慢；
需要占用大量的内存，内存浪费多。
而list相反：

查找和插入的时间随着元素的增加而增加；
占用空间小，浪费内存很少。'''
tuple=(1,2,3)
dict={'mike':999,tuple:1}
print (dict)
print (dict[tuple])

# 下面的代码会报错
tuple=(1,[2,3])
dict={'mike':999,tuple:1}
print (dict)
print (dict[tuple])

#带list的tuple不能作为dict的key，同理也不能作为set的key。因为key是不可变的