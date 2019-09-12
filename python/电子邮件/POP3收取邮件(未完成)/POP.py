# SMTP用于发送邮件，如果要收取邮件呢？
#
# 收取邮件就是编写一个MUA作为客户端，从MDA把邮件获取到用户的电脑或者手机上。收取邮件最常用的协议是POP协议，目前版本号是3，俗称POP3。
#
# Python内置一个poplib模块，实现了POP3协议，可以直接用来收邮件。
#
# 注意到POP3协议收取的不是一个已经可以阅读的邮件本身，而是邮件的原始文本，这和SMTP协议很像，SMTP发送的也是经过编码后的一大段文本。
#
# 要把POP3收取的文本变成可以阅读的邮件，还需要用email模块提供的各种类来解析原始文本，变成可阅读的邮件对象。
#
# 所以，收取邮件分两步：
#
# 第一步：用poplib把邮件的原始文本下载到本地；
#
# 第二部：用email解析原始文本，还原为邮件对象。
#
# 通过POP3下载邮件
# POP3协议本身很简单，以下面的代码为例，我们来获取最新的一封邮件内容

from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

import poplib


# 输入邮件地址， 口令和pop3服务器地址
email = 'wwwsuileicom@qq.com'
password = 'aarioefidnqtbchd'
pop_server = 'pop.qq.com'
server = poplib.POP3(pop_server)
server.set_debuglevel(1)
# 打印pop3欢迎信息
print(server.getwelcome().decode('utf-8'))

server.user(email)
server.pass_(password)
resp, mails, octets = server.list()
print(server.list())  # 显示邮件列表

# 获取最新一封邮件, 注意索引号从1开始:
index = len(mails)
resp, lines, octets = server.retr(index)
print(server.retr(index))
# lines存储了邮件的原始文本的每一行,
# 可以获得整个邮件的原始文本:
msg_context = b'\r\n'.join(lines).decode('utf-8')
msg = Parser.parsestr(msg_context)
print(msg)
server.quit()
# 解析邮件的过程和上一节构造邮件正好相反，因此，先导入必要的模块：
#
# from email.parser import Parser
# from email.header import decode_header
# from email.utils import parseaddr
#
# import poplib
# 只需要一行代码就可以把邮件内容解析为Message对象：
#
# msg = Parser().parsestr(msg_content)
# 但是这个Message对象本身可能是一个MIMEMultipart对象，即包含嵌套的其他MIMEBase对象，嵌套可能还不止一层。
#
# 所以我们要递归地打印出Message对象的层次结构

