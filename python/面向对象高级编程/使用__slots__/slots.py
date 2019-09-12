# 正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。先定义class：


class Student(object):
    pass


# 给实例绑定一个属性
s = Student()
s.name = 20
print(s.name)

# 但是给一个实例绑定属性，对另一个实例是不起作用的
# 抛出异常 Student' object has no attribute 'name'
s2 = Student()


# print(s2.name)
# 为了给所有实例都绑定方法，可以给class绑定方法：


class Student(object):
    def __init__(self, name):
        self.name = name

    def set_name(self, name):
        self.name = name


# 给class绑定方法后，所有实例均可调用
s2 = Student(25)
print(s2.name)


# 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
#
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性

# 没效果...
class AYS(object):
    __slots__ = ('name', 'age')


stu = AYS()
s.name = 'MAX'
s.age = 20
s.so = 11
