# SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。
#
# Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。
#
# 首先，我们来构造一个最简单的纯文本邮件
from email.mime.text import MIMEText, MIMENonMultipart
from email.header import Header
import smtplib
# msg = MIMEText('Hello, send By Python..', 'plain', 'utf-8')
# # 注意到构造MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。
# # 然后，通过SMTP发出去
# from_addr = input('From:')
# password = input('Password')
# to_addr = input('To:')
# smtp_server = input('SMTP server:')
#
# server = smtplib.SMTP(smtp_server, 25)
# server.set_debuglevel(1)
# server.login(from_addr, password)
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()
# # 我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。SMTP协议就是简单的文本命令和响应。login()方法用来登录SMTP服务器，sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str

mail_host = 'smtp.qq.com'
mail_user = 'wwwsuileicom@qq.com'
mail_pass = 'aarioefidnqtbchd'
sender = 'wwwsuileicom@qq.com'
receivers = ['2593515964@qq.com']
msg = MIMEText('Python,SMTP测试', 'plain', 'utf-8')
msg['From'] = Header('油条测试', 'utf-8')
msg['to'] = Header('测试', 'utf-8')
print(111)
subject = 'Python SMTP 邮件测试'
msg['Subject'] = Header(subject, 'utf-8')
try:
    smtpObj = smtplib.SMTP('smtp.qq.com')
    smtpObj.set_debuglevel(1)
    smtpObj.starttls()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, msg.as_string())
    print('发送成功')
except smtplib.SMTPException as e:
    print(e)
    print('发送失败')


