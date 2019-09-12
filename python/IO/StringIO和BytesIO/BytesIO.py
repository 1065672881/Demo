# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
#
# BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes：
from io import BytesIO

f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
# 和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取：
f1 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
str = f1.read()
print(str.strip())
