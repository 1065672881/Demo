from collections.abc import Iterable
from functools import reduce
import os

# 输入和输出
# 输出
print("需要输出的数据")
# 输入(input)
# input输出的值是字符串,如需要整数则需int()函数i = int(i)
i = input("请输入:")
print(i)
# =
# =号是赋值，左边给右边赋值


# 数据类型和变量
# 变量
# a就是变量名,变量可以是任意数据类型
# 变量在程序中用变量名表示，必须是大小写英文，数字和_组合，不能以数字开头,例如
a = 1
# 常量(就是不能变得变量,用全部大写字母表示)
FINAL = 1
# 整数
num = 1
# 浮点数(小数)
num = 1.1
# 字符串(用单引号或双引号括起来的任意文本,如:)
var = "1.1"
# 或
var = '1.1'
# 转义符(\n) 换行
print("I\nm ok")
# 转义符(\t) 缩进
print("I\tm ok")
# 转义\ 需\\
print("I\\m ok")
# r默认不转义
print(r"iii'''")
# 布尔值(True或False,例如:)
print(2 > 1)

# 逻辑运算符
# and(判断两边都为True则为True,否则为False,例如:)
print(2 > 1 and 3 > 2)
# or(判断两边一个为True则为True,否则为False,例如:)
print(2 > 1 or 3 < 2)
# or(将True转为False,False转为True,例如:)
print(not True)
# 空值(None)
print(None)

# 字符串和编码(详见ASCII表)
# Python字符串/编码
# ord()函数获取字符串整数表示
print(ord('中'))
# chr()函数将编码转为对应字符
print(chr(20013))
# 如需在网络传输，或者保存磁盘，须将字符串转为字节,Python中用b前缀的单引或双引表示
print(b'ABC')

# 以编码表示
# 运行结果是b'ABC'
print("ABC".encode("ascii"))
# 在网络或磁盘读取字节文件需解码decode，例如:
# 如包含无法解码文件，decode则会报错
print(b'ABC'.decode('ascii'))
# 计算字符串包含多少字符len()
print(len("ABC"))
# 格式化字符串 使用%s占位符
print("Hi,%s" % "World")
# 占位符	替换内容
# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数

# format占位符，效果与%相同
# 所输入数值的位置索引和占位{索引}相同
print("Hello {0}".format('World'))


# Python集合
# list (list是Python内置数据类型(列表),例如，列出班级部分学生姓名)
# 变量classmates就是list
# 使用len()可以获取list元素的个数
classmates = ["Mi", "Ci", "Di"]
print(classmates)
# 使用索引访问list,例如:
# 索引从0开始(及0就是第一个list元素，以此类推)
# 索引超出报错
print(classmates[0])
# 获取最后一个元素(以此类推)
print(classmates[-1])
# 往list结尾加入一条数据,例如:
classmates.append('Admin')
# 把数据插入到指定位置，例如:
classmates.insert(1, "System")
# 删除末尾元素
classmates.pop()
# 删除指定位置
classmates.pop(1)
# 替换某个元素,直接给对应位置赋值
classmates[1] = "SYS"
# list元素中可包含另一个list,例如:
s = [1, 2, 3, [4, 5], 6]
# 拆开写就是
i = [4, 5]
s = [1, 2, 3, i, 6]
# 元组(tuple)和列表(list)相似，只不过tuple一旦初始化，则不可修改,例如:
# 在定义元组时，元素就确定下来
test = (1, 2, 3, 4, 5)
# 定义单个元素的元组,(后面加个逗号消除歧义)
test1 = (1,)
# 可变元组，其实元组本身没有改变
# 改变的是元组内list，list是可改变的
test2 = (1, 2, 3, [4, 5])
test2[3][0] = 6
print(test2)

# 条件判断
# 使用if语句,例如
# 主要不要忘记冒号:
# if else判断的特点就是如果一个条件判断为true，则后面的判断都不执行
# if 后的比较如果是布尔值True则打印true
age = 20
if age <= 50:
    print("true")
# else语句，表示如果后面的比较是false,则进入else语句,例如:
if age > 20:
    print("true")
else:
    print("false")
# elif 就是else后加入if判断，例如:
if age > 20:
    print("true")
elif age < 50:
    print("false")

# 循环
# 将list或tuple依次输出
# n是定义的变量，name是列表名称
name = [1, 2, 3, 4]
for n in name:
    print(n)
# 生成整数序列(range)
# 输出 5个整数
# range从0开始，所以输出结果是0-4
for num in range(5):
    print(num)
# while循环
# 条件满足继续运行，不满足则退出
# while循环需退出条件，否则出现死循环，（循环不停止）
z = 0
while z == 5:
    z += 1
    print(z)
# 死循环状态
# while True:
#     print(1)
# 不要运行这段代码。。。。

# break
# 可提前跳出循环
z = 0
while z >= 50:
    if z == 10:
        break
    z += 1
    print(z)
# continue
# 跳过当前循环，进入下一次循环
while z >= 50:
    if z == 10:
        continue
    print(z)
# dict字典列表和set集合
#    略


# 调用函数
# abs()绝对值函数
print(abs(-10))
# max()函数,接收多个参数，返回最大值
print(max(1, 2, 3, 4))


# 数据类型转换
# int()转换为数值
# str()转换为字符串
# float()转换为浮点数


# 自定义函数
# def来定义函数
# 定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。例如:
# 中间是函数体
def my_test(x):
    if x == 5:
        return x
    else:
        print(x)


# 定义一个空函数,函数体使用pass关键字
def my_pass(x): pass


# 参数检查,not isinstance()
# raise TypeError() 自定义错误信息
def my_instance(x):
    if not isinstance(x, (int, str)):
        raise TypeError("参数部署数值或字符")


# 函数的参数
# def定义的函数，（）内是函数的参数，
# 调用该函数时，所传参数须和该函数的定义的参数一致,例如
def my_instance(x):
    if not isinstance(x, (int, str)):
        raise TypeError("参数部署数值或字符")


my_instance(10)
# 若传入参数数量不一致则出错,例如:
# my_instance(10, 11)
# my_instance() takes 1 positional argument but 2 were given 错误信息



# 集合切片
# 切片取集合前三个元素
# 索引从0开始取到索引为3结束,但不包括索引3
# 如果开始索引为0，可省略
num_abc = [1, 2, 3, 4, 5, 6]
print(num_abc[:3])
# 同样也可以使用切片从后往前取
print(num_abc[-3:])
# 例如每2个数取一个
print(num_abc[:6:2])
# 所有数每2个取一个
print(num_abc[::2])
# 复制原list
print(num_abc[:])


# 列表生成式
print([x * x for x in range(1, 11)])
# 生成式还可加入判断
# 判断是偶数
print([x * x for x in range(1, 11) if x % 2 == 0])
# 使用两层循环生成全排列
# 交叉赋值
print([m + n for m in 'ABC' for n in 'abc'])
# 列出当前目录下所有文件和目录名
# 首先导入模块 import os
# 运行结果就是我当前创建的文件 python.py
# 因格式不符合规范，import黄线，应放置与最顶端
print([d for d in os.listdir('.')])
# 可循环多个变量
d = {'a': 'a', 'b': 'b'}
for key, value in d.items():
    print(key, value)
# 也可对生成式变量进行格式化
d = {'a', 'b', 'c'}
print([k.upper() for k in d])


# 生成器(generator)
g = (x * x for x in [1, 2, 3])
# 可通过next()获得generator的值,不过有些变态
print(next((x * x for x in [1, 2, 3])))
# 也可用循环迭代，generator也是可迭代对象
for n in g:
    print(n)
# 尝试用函数完成斐波那契数列
# 定义函数如下 : fib
# max_num 斐波那契数列自定义最多显示数量
# h 是循环进入条件，每次+1,若大于最多显示数列，则退出循环
# j 用来临时赋值 k
# k 数列当前显示的数据
# j+k 将前一个k的值加上当前k的值

print("数列开始================")


def fib(max_num):
    h, j, k = 0, 0, 1
    while h < max_num:
        print(k)
        j, k = k, j + k
        h = h + 1
    return "结束"


fib(10)


# 如果要把以上fib函数变成generator ，只需将return 换成 yield
# 运行结果 : <generator object fib at 0x00000139D21C7348>
# generator的执行流程不太一样，函数执行按顺序，遇到return返回，然后再按顺序执行，
# generator执行，每次调用next运行，遇到yield返回，再次执行，从上次返回的yield处执行


def fib(max_num):
    h, j, k = 0, 0, 1
    while h < max_num:
        print(k)
        j, k = k, j + k
        h = h + 1
    yield "结束"


print(fib(10))
# 使用循环调用generator,发现拿不到return语句返回的值,需捕获StopIteration，值在StopIteration的value中
f = fib(10)
while True:
    try:
        print(next(g))
    except StopIteration as e:
        print(e.value)
        break


# 集合迭代
# 迭代不只用于集合，也可用于可迭代对象
# 判断一个元素是否为可迭代对象或集合
# 首先引入 from collections.abc import Iterable
print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
# 使用下标循环集合
for key, value in enumerate(["A", "B", "C"]):
    print(key, value)


# 函数式编程
# map/reduce
# map
# map有两个参数，一个是函数，一个是可迭代对象，map将传入的函数依次适用与每个元素
# 例如将每个元素以平方方式输出
# 需转换成list
def square(x):
    return x*x


test_num = [1, 2, 3, 4, 5, 6]
print(list(map(square, test_num)))
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


# filter 过滤器
# 和map 不同的是 filter根据返回的值是True还是False决定是否删除该元素
# 运行结果 2,4,6,10
def is_odd(x):
    return x % 2 == 0


print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

# 删除空元素


def not_emp(x):
    return x and x.strip()


print(list(filter(not_emp, ['A', '', 'B', None, 'C', '  '])))




