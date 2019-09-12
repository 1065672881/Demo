# 看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。
#
# __slots__我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数。
#
# 除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类

# 先定义一个学生类


class Studuent(object):

    def __init__(self, name):
        self.name = name


# 打印出一堆<__main__.Student object at 0x109afb190>，不好看。
#
# 怎么才能打印得好看呢？只需要定义好__str__()方法，返回一个好看的字符串就可以了

# __str__()

class Studuent(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Studnet : " + self.name


print(Studuent("MAX"))
# 还可以使用变量

s = Studuent("MAC")
print(s)


# 这是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的
# 再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的写法


class Studuent(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Studnet : " + self.name

    __repr__ = __str__


s1 = Studuent("AX")
print(s1)


# ---------------------------没明白------------------------------


# __iter__
# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环
# 创建Fib类


class Fib(object):

    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 20:
            raise StopIteration
        return self.a


for n in Fib():
    print(n)


# __getitem__
# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：
# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：


class Fib(object):

    def __getitem__(self, item):
        a, b = 1, 1
        for x in range(item):
            a, b = b, a + b
        return a


print(Fib()[3])


# 但是list有个神奇的切片方法
# Fib却错误
# 原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：


class Fib(object):

    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 1, 1
            for x in range(item):  # 是数值
                a, b = b, a + b
            return a
        if isinstance(item, slice):  # 是切片
            start = item.start
            end = item.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for i in range(end):
                if i >= start:
                    L.append(a)
                a, b = b, a+b
            return L


print(Fib()[:3])
# 但是没有对step参数作处理
# 也没有对负数作处理，所以，要正确实现一个__getitem__()还是有很多工作要做的
# 此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。
#
# 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。
#
# 总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。


# __getattr__
# 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错
# 要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性


class Stu(object):
    def __init__(self, name):
        self.name = name

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        raise AttributeError("错误信息")
# 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，这样，我们就有机会返回score的值


s2 = Stu("MAX")
print(s2.name)
print(s2.score)
# 此外，注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误：

# 这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。
#
# 这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况作调用。
#
# 举个例子：
#
# 现在很多网站都搞REST API，比如新浪微博、豆瓣啥的，调用API的URL类似：
#
# http://api.server/user/friends
# http://api.server/user/timeline/list
# 如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。
#
# 利用完全动态的__getattr__，我们可以写出一个链式调用：


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path


print(Chain().status.user.timeline.list)

# __call__
# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用
class Stud(object):

    def __init__(self, name):
        self._name = name

    def __call__(self):
        print("Name : "+self._name)


s4 = Stud("M")
s4()

# __call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。
#
# 如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的，这么一来，我们就模糊了对象和函数的界限。
#
# 那么，怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象
# 结果是True
# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
print(callable(Stud("SL")))

