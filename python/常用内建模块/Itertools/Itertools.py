# Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数
# 首先，我们看看itertools提供的几个“无限”迭代器

import itertools
natuals = itertools.count(1)
print(natuals)
# for n in natuals:
#     print(n)


# 因为count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来
# cycle()会把传入的一个序列无限重复下去
cs = itertools.cycle('ABC')
# for c in cs:
#     print(c)


# 无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，它不会事先把无限个元素生成出来，事实上也不可能在内存中创建无限多个元素。
#
# 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))


# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器
for c in itertools.chain('ABC', 'XZY'):
    print(c)


# groupby()
# groupby()把迭代器中相邻的重复元素挑出来放在一起：
for key, group in itertools.groupby('AAAABBBBCCCD'):
    print(key, list(group))
