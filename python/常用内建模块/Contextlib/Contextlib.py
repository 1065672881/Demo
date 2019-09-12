# 在Python中，读写文件这样的资源要特别注意，必须在使用完毕后正确关闭它们。正确关闭文件资源的一个方法是使用try...finally
from contextlib import contextmanager, closing
from urllib.request import urlopen
try:
    f = open('test', 'r')
    print(f.read())
finally:
    f.close()
# 写try...finally非常繁琐。Python的with语句允许我们非常方便地使用资源，而不必担心资源没有关闭，所以上面的代码可以简化为
with open('test', 'r') as f:
    print(f.read())

# 并不是只有open()函数返回的fp对象才能使用with语句。实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句。
# 实现上下文管理是通过__enter__和__exit__这两个方法实现的。例如，下面的class实现了这两个方法


class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('开始')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print("错误")
        else:
            print("结束")

    def query(self):
        print(self.name)


with Query('MAX') as q:
    print(q)


# @contextmanager
# 编写__enter__和__exit__仍然很繁琐，因此Python的标准库contextlib提供了更简单的写法，上面的代码可以改写如下：


class Query(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)


@contextmanager
def create_query(name):
    print("开始")
    q = Query(name)
    yield q
    print("结束")


with create_query("MAX") as s:
    s.query()
# 很多时候，我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现。例如：


@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)


with tag("h1"):
    print("hello")
    print("world")
# 代码的执行顺序是：
# with语句首先执行yield之前的语句，因此打印出<h1>；
# yield调用会执行with语句内部的所有语句，因此打印出hello和world；
# 最后执行yield之后的语句，打印出</h1>。
# 因此，@contextmanager让我们通过编写generator来简化上下文管理


# @closing
# 如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，可以用closing()来把该对象变为上下文对象。例如，用with语句使用urlopen()
with closing(urlopen('https://www.python.org')) as pyt:
    for line in pyt:
        print(line)


@contextmanager
def closing(thing):
    try:
        yield thing
    finally:
        thing.close()
