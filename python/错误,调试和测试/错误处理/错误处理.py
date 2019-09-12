# 在程序运行的过程中，如果发生了错误，可以事先约定返回一个错误代码，这样，就可以知道是否有错，以及出错的原因。在操作系统提供的调用中，返回错误码非常常见。比如打开文件的函数open()，成功时返回文件描述符（就是一个整数），出错时返回-1。
#
# 用错误码来表示是否出错十分不便，因为函数本身应该返回的正常结果和错误码混在一起，造成调用者必须用大量的代码来判断是否出错
import logging


def foo(num):
    if num <= 5:
        return -1
    return num


def bar():
    r = foo(4)
    if r == -1:
        print("Error")
    else:
        pass


bar()
# 一旦出错，还要一级一级上报，直到某个函数可以处理该错误（比如，给用户输出一个错误信息）。
#
# 所以高级语言通常都内置了一套try...except...finally...的错误处理机制，Python也不例外。
try:
    print("Try")
    r = 10 / 0
    print("Result")
except ZeroDivisionError as e:
    print(e)
finally:
    print("Finally")
# 当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。
#
# 上面的代码在计算10 / 0时会产生一个除法运算错误 division by zero
# 从输出可以看到，当错误发生时，后续语句print('result:', r)不会被执行，except由于捕获到ZeroDivisionError，因此被执行。最后，finally语句被执行
# Finally 无论如何一定会被执行
# 你还可以猜测，错误应该有很多种类，如果发生了不同类型的错误，应该由不同的except语句块处理。没错，可以有多个except来捕获不同类型的错误
try:
    print("Try")
    r = 10 / int('a')
    print("Result", r)
except ValueError as v:
    print(v)
except ZeroDivisionError as z:
    print(z)
finally:
    print("Finally")
# Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”
# 第二个except永远也捕获不到UnicodeError，因为UnicodeError是ValueError的子类，如果有，也被第一个except给捕获了。
try:
    foo(4)
except ValueError as v:
    print(v)
except UnicodeError as u:
    print(u)

# 使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，比如函数main()调用foo()，foo()调用bar()，结果bar()出错了，这时，只要main()捕获到了，就可以处理
# 也就是说，不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以了。这样一来，就大大减少了写try...except...finally的麻烦。


def foos(num):
    return 10 / int(num)


def bar(num):
    return foos(num) * 2


def main():
    try:
        print(bar('0'))
    except Exception as es:
        print("new : ", es)
    finally:
        print("Finally")


main()
# 调用栈
# 如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出


# def foo(s):
#     return 10 / int(s)
#
#
# def bar(s):
#     return foo(s) * 2
#
#
# def main():
#     bar(1)


# main()
# 执行结果
# $ python3 err.py
# Traceback (most recent call last):
#   File "err.py", line 11, in <module>
#     main()
#   File "err.py", line 9, in main
#     bar('0')
#   File "err.py", line 6, in bar
#     return foo(s) * 2
#   File "err.py", line 3, in foo
#     return 10 / int(s)
# ZeroDivisionError: division by zero
# 出错的时候，一定要分析错误的调用栈信息，才能定位错误的位置。


# 记录错误
# 如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。
#
# Python内置的logging模块可以非常容易地记录错误信息
# 首先第一行导入Import logging


def err(num):
    return 10 / int(num)


def exe(num):
    return err(num) * 2


def falut():
    try:
        print(exe(1))
    except ZeroDivisionError as ze:
        logging.exception(ze)


falut()


# 抛出错误
# 因为错误是class，捕获一个错误就是捕获到该class的一个实例。因此，错误并不是凭空产生的，而是有意创建并抛出的。Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误
# 如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例


class FooError(ValueError):
    pass


def fooErr(s):
    n = int(s)
    if n == 0:
        raise FooError("invalid value: %s" % s)
    return 10 / n


print(fooErr('1'))


