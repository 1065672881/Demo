# 装饰器
# 函数对象可赋给变量，通过变量也可调用此函数


def now():
    print("被调用")


new_now = now
new_now()
# 函数对象的_name_属性，可拿到函数的名称
print(now.__name__)

# 在代码运行期间动态只能加功能的方式，叫装饰器


def log(fun):
    def wrapper():
        print("call me: %s()" % fun.__name__)
        return fun()
    return wrapper

# @可以将函数置于其他函数中 : 把@log放到new_now()函数的定义处，相当于执行了语句：new_now = log(new_now)
@log
def new_now():
    print("2019-08-29")


new_now()

# 装饰器也可接收参数


def logs(text):
    def decorator(func):
        def wapper():
            print("%s : %s()" % (text, func.__name__))
            return func()
        return wapper
    return decorator


# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator


@logs("Exec")
def new_new_now():
    print("2019-08-29")


new_new_now()


