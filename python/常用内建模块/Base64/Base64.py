# Base64是一种用64个字符来表示任意二进制数据的方法。
# 用记事本打开exe、jpg、pdf这些文件时，我们都会看到一大堆乱码，因为二进制文件包含很多无法显示和打印的字符，所以，如果要让记事本这样的文本处理软件能处理二进制数据，就需要一个二进制到字符串的转换方法。Base64是一种最常见的二进制编码方法
import base64
# Base64的原理很简单，首先，准备一个包含64个字符的数组
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 's', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
         'S', 'T', 'U', 'V', 'W', 'S', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']

# Python内置的base64可以直接进行base64的编解码：
print(base64.b64encode(b'binary/x00string'))
print(base64.b64decode(b'YmluYXJ5L3gwMHN0cmluZw=='))

# 于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_
print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64decode(b'abcd--__'))

# 还可以自己定义64个字符的排列顺序，这样就可以自定义Base64编码，不过，通常情况下完全没有必要。
#
# Base64是一种通过查表的编码方法，不能用于加密，即使使用自定义的编码表也不行。
#
# Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容等。
#
# 由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉
