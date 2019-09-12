# 函数作为返回值
# 正常实现可变参数求和


def calc_sum(*args):
    ac_num = 0
    for n in args:
        ac_num = ac_num + n
    return ac_num


print(calc_sum(1, 2, 3))


# 以函数作为返回值返回
# 此时函数执行结果是<function calc_sum.<locals>.calc_child_sum at 0x00000191D5735798>
# 如果想获取数据 ,需执行f()函数
# 在calc_sum函数中定义calc_chid_sum函数，内部函数可以引用外部函数的变量和参数,当外部函数返回内部函数时，外部函数相关的参数和变量都存在内部函数中
# 称为闭包
def calc_sum(*args):
    def calc_child_sum():
        ac_num = 0
        for n in args:
            ac_num = ac_num + n
        return ac_num
    return calc_child_sum


f = calc_sum(1, 2, 3)
print(f())
# 注意，每次调用calc_sum 都会返回一个新的函数
# 执行结果为False
f1 = calc_sum(1, 2, 3)
f2 = calc_sum(1, 2, 3)
print(f1 == f2)

# 闭包引用循环变量的问题
# 输出值是999 并非1，4，9


def count():
    fs = []
    for i in range(1, 4):
        def fcs():
            return i*i
        fs.append(fcs)
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

# 解决闭包问题


def count():
    def fcs(j):
        def fci():
            return j*j
        return fci
    fs = []
    for i in range(1, 4):
        fs.append(fcs(i))
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())



