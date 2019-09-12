import smtplib
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

msg = MIMEMultipart()
mail_host = 'smtp.qq.com'
mail_user = 'wwwsuileicom@qq.com'
mail_pass = 'aarioefidnqtbchd'
sender = 'wwwsuileicom@qq.com'
receivers = ['2593515964@qq.com']
msg['From'] = Header('油条测试', 'utf-8')
msg['to'] = Header('测试', 'utf-8')
msg['Subject'] = Header('Python SMTP 邮件测试', 'utf-8')
msg.attach(MIMEText('<html><body><h1>Hello</h1>' + '<p><img src="cid:0"></p>' + '</body></html>', 'html', 'utf-8'))
with open('timg.jpg', 'rb') as f:
    mime = MIMEBase('image', 'jpg', filename='timg.jpg')
    # 加上头部信息
    mime.add_header('Content-Disposition', 'attachment', filename='timg.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)
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
