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
