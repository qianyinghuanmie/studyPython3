#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
面向对象编程——Object Oriented Programming，简称OOP，
是一种程序设计思想。OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。

面向过程的程序设计把计算机程序视为一系列的命令集合，即一组函数的顺序执行。为了简化程序设计，面向过程把函数继续切分为子函数，即把大块函数通过切割成小块函数来降低系统的复杂度。

假设我们要处理学生的成绩表，为了表示一个学生的成绩，面向过程的程序可以用一个dict表示：

一个对象的例子：
'''
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

#当建立起对象以后
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()

'''
数据封装、继承和多态是面向对象的三大特点，我们后面会详细讲解。
…………………………………………………………………………………………………………………………………………………………………………………………………………………………………………
类和实例

面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板，比如Student类，而实例是根据类创建出来的一个个具体的“对象”，
每个对象都拥有相同的方法，但各自的数据可能不同。
'''

class Student(object):
    pass

'''class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，继承的概念我们后面再讲，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
定义好了Student类，就可以根据Student类创建出Student的实例，创建实例是通过类名+()实现的：
'''
bart=Student()
print(bart)  #<__main__.Student object at 0x0101DC30>

'''可以看到，变量bart指向的就是一个Student的实例，后面的0x10a67a590是内存地址，每个object的地址都不一样，而Student本身则是一个类。
可以自由地给一个实例变量绑定属性，比如，给实例bart绑定一个name属性：

由于类可以起到模板的作用，因此，可以在创建实例的时候，
把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score
就是初始化属性

注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。

有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去：

除了self以外，定义几个变量就要传几个变量。

……………………………………………………………………………………………………………………………………………………………………………………………………………………
数据封装
面向对象编程的一个重要特点就是数据封装。在上面的Student类中，每个实例就拥有各自的name和score这些数据。我们可以通过函数来访问这些数据，比如打印一个学生的成绩：


但是，既然Student实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问，可以直接在Student类的内部定义访问数据的函数，这样，就把“数据”给封装起来了。这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法：


类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；

方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；

通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。

和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：

……………………………………………………………………………………………………………………………………………………………………………………………………………………………………
访问限制
在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑。

但是，从前面Student类的定义来看，外部代码还是可以自由地修改一个实例的name、score属性：

如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__

在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private）

只有内部可以访问，外部不能访问，所以，我们把Student类改一改：

如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__

在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），

只有内部可以访问，外部不能访问，所以，我们把Student类改一改：


'''


class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score
    #如果又要允许外部代码修改score怎么办？可以再给Student类增加set_score方法：
    def set_score(self, score):
        self.__score = score

'''改完后，对于外部代码来说，没什么变动，但是已经无法从外部访问实例变量.__name和实例变量.__score了：
这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮

但是如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法：

最后，外部想要自定义属性的时候，最好不要起和函数内部名一样带下划线的，其实自定义不要起下划线的应该就没有什么问题。
…………………………………………………………………………………………………………………………………………………………………………………………………………………………………………
继承和多态
在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），
而被继承的class称为基类、父类或超类（Base class、Super class）。
先创建出一个animal类

class Animal(object):
    def run(self):
        print('Animal is running...')
当我们需要编写Dog和Cat类时，就可以直接从Animal类继承：

class Dog(Animal):
    pass

class Cat(Animal):
    pass        
这样的话。Dog和Cat都是继承了animal  。
继承的好处：
最大的好处是子类获得了父类的全部功能。他们也自然而然的获取到了run的方法。
多态：
子类新的方法会将父类的方法覆盖  
……………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………
获取对象信息的方法
1：type()：
基本类型都可以用type()判断：
>>> type(123)
<class 'int'>
>>> type('str')
<class 'str'>
>>> type(None)
<type(None) 'NoneType'>
如果一个变量指向函数或者类，也可以用type()判断：
>>> type(abs)
<class 'builtin_function_or_method'>
>>> type(a)
<class '__main__.Animal'>
type函数的类型：
………………………………………………………………………………………………
使用isinstance()
有继承关系的话，使用Type就很纠结了
isinstance()就可以告诉我们，一个对象是否是某种类型
以下还可以判断基本类型
>>> isinstance('a', str)
True
>>> isinstance(123, int)
True
>>> isinstance(b'a', bytes)
True
……………………………………………………………………………………………………………………
使用dir()

如果要获得一个对象的所有属性和方法，可以使用dir()函数，
它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，
实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：
>>> len('ABC')
3
>>> 'ABC'.__len__()
3
…………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………………
实例属性和类属性
由于Python是动态语言，根据类创建的实例可以任意绑定属性
'''
class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90
# 但是，如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有：


'''在编写程序的时候，千万不要把实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。'''
