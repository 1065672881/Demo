# 排序算法
# 函数sorted()排序
print(sorted([1, 2, 5, -10, 12, -5]))

# sorted 也可以接收一个key来自定义排序
# 使用abs绝对值排序
print(sorted([1, 2, 5, -10, 12, -5], key=abs))

# 对于字符串进行排序
# 对于字符串，以ASCII表为基础进行排序
print(sorted(["A", "a", "B", "c", "b", "d"]))

# sorted默认是正序排序(从小到大)，如果需要想要逆序排序(从大到小)需加入另一个参数
print(sorted([1, 2, 5, -10, 12, -5], reverse=True))


