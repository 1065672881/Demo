# 匿名函数
# lambda表示匿名函数,冒号前面的x表示函数参数,
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6])))

# 匿名函数可作为返回值


def func(x):
    return lambda i: i * i


print(func(5))
