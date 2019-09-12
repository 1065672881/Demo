# Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等
# 什么是摘要算法呢？摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）
# 摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过
# 我们以常见的摘要算法MD5为例，计算出一个字符串的MD5值
import hashlib

md5_str = hashlib.md5()
md5_str.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5_str.hexdigest())

# 运行结果 d26a53750bc40b38b65a520292f69306
# 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的
# 试试改动一个字母，看看计算的结果是否完全不同
# MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。


# 另一种常见的摘要算法是SHA1，调用SHA1和调用MD5完全类似
sha1 = hashlib.sha1()
sha1.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())
# 运行结果 b752d34ce353e2916e943dc92501021c8f6bca8c
# HA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。


# 比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长
sha256 = hashlib.sha3_256()
sha256.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(sha256.hexdigest())
# 运行结果 af54dc6956d3c7b7a3a9e17cda140e14a9f239c0ebf285ffb7fff61269e32cf7
# 三个同样的字符，三种不同算法，结果不同



# 摘要算法能应用到什么地方？举个常用例子：
#
# 任何允许用户登录的网站都会存储用户登录的用户名和口令。如何存储用户名和口令呢？方法是存到数据库表中
# 如果以明文保存用户口令，如果数据库泄露，所有用户的口令就落入黑客的手里。此外，网站运维人员是可以访问数据库的，也就是能获取到所有用户的口令。
#
# 正确的保存口令的方式是不存储用户的明文口令，而是存储用户口令的摘要，比如MD5
