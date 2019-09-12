# 偏函数把某个函数的参数固定，使得调用此函数更为简单
# 需首先导入模块 import functools
import functools
# 做个字符转整数的二进制转换
int2 = functools.partial(int, base=2)
print(int2('1000000'))


