import chardet

# 当我们拿到一个bytes时，就可以对其检测编码。用chardet检测编码，只需要一行代码：
print(chardet.detect(b'Hello, World'))

# 我们来试试检测GBK编码的中文
language = '中国'.encode('gbk')
print(chardet.detect(language))

# 对日文进行监测
data = '最新の主要ニュース'.encode('euc-jp')
print(chardet.detect(data))
