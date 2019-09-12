# 在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑。
# 但外部还是可以修改内部细节
# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问


class Student(object):

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def access(self):
        print("姓名 : %s , 年龄 : %s" % (self.__name, self.__age))


stu = Student("MAX", 30)
# 无法从外部访问内部成员
# 报出异常
# print(stu.__name)
# 只能通过公开的access函数输出成员数据
stu.access()

# 如果必须要从外部修改内部成员信息，可以增加setName,获取可以增加getName


class Student(object):

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def access(self):
        print("姓名 : %s , 年龄 : %s" % (self.__name, self.__age))

    def get_Name(self):
        return self.__name

    def get_Age(self):
        return self.__age

    def set_Name(self, name):
        self.__name = name

    def set_Age(self, age):
        self.__age = age


stu = Student("Max", 30)
# 现在想要修改年龄成29并输出
stu.set_Age(29)
print(stu.get_Age())
# 通过增加get，set方法来实现外部修改
# 你现在会想，原来的stu.name = 29也可以，为什么要大费周章
# 因为定义函数可以实现参数检查，避免无效参数,比如年龄输入9999


class Student(object):

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def access(self):
        print("姓名 : %s , 年龄 : %s" % (self.__name, self.__age))

    def get_Name(self):
        return self.__name

    def get_Age(self):
        return self.__age

    def set_Name(self, name):
        self.__name = name

    def set_Age(self, age):
        if 0 <= age <= 150:
            self.__age = age
        else:
            raise TypeError("参数异常")


# 给出160年龄 就会显示错误信息，参数异常
stu = Student("Max", 30)
# stu.set_Age(160)
# print(stu.get_Age())

# 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量：
# 但是强烈不建议
# 仍然可以访问，就是说Python 内部机制没有任务办法阻止你干一些勾当，请自觉
print(stu._Student__name)


