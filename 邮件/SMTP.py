# smtplib 发送邮件
# email 构造邮件
from email.mime.text import MIMEText
# 构造MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性
msg = MIMEText('hello, send by Python', 'plain', 'utf-8')
# 输入Email地址和口令
from_addr = input('From: ')
password = input('Password: ')
# 输入收件人的地址
to_addr = input('To: ')
# 输入SMIP服务器地址
smtp_server = input('SMTP server: ')

import smtplib
# SMTP协议默认端口是25
server = smtplib.SMTP(smtp_server, 25)
# 打印出和SMTP服务器交互的所有信息
server.set_debuglevel(1)
# 登录SMTP服务器
server.login(from_addr, password)
# 发送邮件，可以同时发给多人
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432005226355aadb8d4b2f3f42f6b1d6f2c5bd8d5263000
