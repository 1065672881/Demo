# filter 过滤器
# 和map 不同的是 filter根据返回的值是True还是False决定是否删除该元素
# 运行结果 2,4,6,10


def is_odd(x):
    return x % 2 == 0


print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

# 删除空元素
# 运行结果 ['A', 'B', 'C']


def not_emp(x):
    return x and x.strip()


print(list(filter(not_emp, ['A', '', 'B', None, 'C', '  '])))
