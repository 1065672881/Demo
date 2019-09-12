# 很多时候，数据读写不一定是文件，也可以在内存中读写。
#
# StringIO顾名思义就是在内存中读写str。
#
# 要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可
from io import StringIO

f = StringIO()
print(f.write('hello'))
# getvalue()方法用于获得写入后的字符
print(f.getvalue())

# 要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取
f1 = StringIO('Hello!\nhi!\nGoodBye!')
while True:
    s = f1.readline()
    if s == '':
        break
    print(s.strip())
