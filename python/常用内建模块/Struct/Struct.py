# 准确地讲，Python没有专门处理字节的数据类型。但由于b'str'可以表示字节，所以，字节数组＝二进制str。而在C语言中，我们可以很方便地用struct、union来处理字节，以及字节和int，float的转换。
# 在Python中，比方说要把一个32位无符号整数变成字节，也就是4个长度的bytes，你得配合位运算符这么写
import struct

n = 10240099
b1 = (n & 0xff000000) >> 24
b2 = (n & 0xff0000) >> 16
b3 = (n & 0xff00) >> 8
b4 = n & 0xff
bs = bytes([b1, b2, b3, b4])
print(bs)
# 非常麻烦。如果换成浮点数就无能为力了

# Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换
# '>I'的意思是：
# >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
# 后面的参数个数要和处理指令一致。
print(struct.pack('>I', 10240099))
print(struct.unpack('>I', b'\x00\x9c@c'))

# Windows的位图文件（.bmp）是一种非常简单的文件格式，我们来用struct分析一下
s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
print(struct.unpack('<ccIIIIIIHH', s))
