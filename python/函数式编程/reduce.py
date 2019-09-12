from functools import reduce
# reduce
# reduce 必须接收两个参数，将结果和序列的下一个元素做累加


def add(x, y):
    return x+y


print(reduce(add, [1, 2, 3, 4]))
# 把序列[1, 3, 5, 7, 9]变换成整数13579


def fn(x, y):
    return x*10+y


print(reduce(fn, [5, 6, 7, 8, 9]))
# 将用户输入的不规则名称转换为首字母大写，其他字母小写的格式
L1 = ['adam', 'LISA', 'barT']


def normalize(na):
    return str(na)[0].upper() + str(na)[1:].lower()


print(list(map(normalize, L1)))
# 接收一个list并求积


def p(l):
    def sl(x, y):
        return x*y
    print(reduce(sl, l))


p([3, 5, 7, 9])
