# 面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板，比如Student类，而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同
# 首先定义一个学生类 类的定义通过class 关键字


class Student(object):
    pass


# class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，继承的概念我们后面再讲，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
# 创建出类后，可以创建出类的实例，通过类名()的方式
# 类也可以赋值给一个变量


bart = Student()
# 输出值 <__main__.Student object at 0x00000174D9A5ED88> 0x00000174D9A5ED88是内存地址
print(bart)
# <class '__main__.Student'>
print(Student)


# 类是抽象的概念，类内部可以存在某个对象的一些特性，比如，姓名，性别
class Person(object):

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


# 类的内部有了初始化函数后，就必须传入需要的参数
human = Person("Max", "男")
print(human.name)


# 数据封装
# 面向对象编程的一个重要特点就是数据封装
# 无需在外部访问类内部的成员，可以在类的内部定义一个访问函数
class Teacher(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def access(self):
        print("姓名 : %s ,年龄 : %d" % (self.name, self.age))


Teacher("MAC", 30).access()

# 可以在类内部封装属于该类的方法,外部调用无需明白内部细节
