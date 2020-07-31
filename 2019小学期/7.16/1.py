# import poplib
#
# user = '921998348@qq.com'
# pwd = input('输入密码')
# host = 'pop.qq.com'
# M = poplib.POP3(host)
# M.user(user)
# M.pass_(pwd)
# mboxstat = M.stat()
# print("邮件数量", mboxstat[0])
# mylist = M.list()
# for i in range(3):
#     print(mylist[1][i])
# numMessages = len(M.list()[1])
# print("邮件数量", numMessages)
# k = 0
# mailx = M.retr(k)[1]
# i = 0
# for line in mailx:
#     print(line)
#     i = i + 1
#     if i >= 5:
#         break
# M.quit()

import smtplib
import email


def prompt(prompt):
    return input(prompt).strip()


fromaddr = prompt("From:")
toaddrs = prompt("To:")
subject = prompt("Subject:")
print("Enter message, end with continusly enter:")
text = "hh"
while True:
    try:
        line = input()
    except EOFError:
        break
    if len(line) == 0:
        break
    text = text + line + "\r\n"
msg = email.message_from_string(text)
msg['Subject'] = subject
msg['From'] = fromaddr
msg['To'] = toaddrs
msg.set_charset('GB2312')
server = smtplib.SMTP('smtp.qq.com')  # 202.118.224.233
user = fromaddr
pwd = input('请输入邮箱密码')
server.login(user, pwd)
server.send_message(msg, fromaddr, toaddrs)
print("Send successfully")
server.quit()
