# 当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？
# 首先使用Type()来判断对象类型
# 输出结果<class 'int'>
print(type(123))

# 如果一个变量指向函数或者类，也可以用type()判断：
# 还记得abs是什么吗？
# 输出结果 <class 'builtin_function_or_method'>
print(type(abs))

# Type()函数返回class类型
# 但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
# 首先导入模块
import types


def fun():
    def run():
        print("run")


# 输出结果:True
print(type(fun) == types.FunctionType)


# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。


class Animal(object):
    pass


class Dog(Animal):
    pass


dog = Dog()
# 输出结果True,True
print(isinstance(dog, Animal))
print(isinstance(dog, Dog))
# 基本类型也可以用isinstance来判断
# 并且还可以判断一个变量是否是某些类型中的一种
print(isinstance([1, 2, 3], (list, tuple)))
# 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”


# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
# 比如，获得一个str对象的所有属性和方法
print(dir('ABC'))


# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()
# 紧接着，可以测试该对象的属性
print(hasattr(obj, 'x'))  # obj有没有属性x
print(setattr(obj, 'y', 20))  # 设置一个属性y

print(obj.y)  # 获取属性Y
# 如果试图获取不存在的属性，会抛出AttributeError的错误：
# getattr(obj, 'z') # 获取属性'z'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'MyObject' object has no attribute 'z'

# 可以传入一个default参数，如果属性不存在，就返回默认值
print(getattr(obj, 'z', 25))
# 也可以获得对象的方法：
print(hasattr(obj, 'power'))
fun = getattr(obj, 'power')
# 调用fun()等于调用obj.power()
print(fun())
# 通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息
