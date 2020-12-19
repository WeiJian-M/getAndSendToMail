'''
Description: 
Author: Weijian Ma
Date: 2020-10-22 09:57:17
LastEditTime: 2020-10-22 16:25:06
LastEditors: Weijian Ma
'''
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import requests
from bs4 import BeautifulSoup

r = requests.get('https://news.topurl.cn/')
soup = BeautifulSoup(r.content,'lxml')


weather = soup.find('div',class_="line weather").text
news = soup.find('div',class_="news-wrap").find_all('div',class_='line')
text = ''
count = 1
for i in news:
    temp = i.find("a").text
    text = text + str(count) + '. ' + temp + '\n'*2
    count = count + 1

my_sender='714540398@qq.com'  # 发件人邮箱账号
my_pass = 'xlfprgqmxaadbeah'   # 发件人邮箱密码(注意这个密码不是QQ邮箱的密码，是在QQ邮箱的SMTP中生成的授权码)
my_user='m714540398@163.com'   
def mail():
  ret=True
  try:
    msg=MIMEText(text,'plain','utf-8') #填写邮件内容
    msg['From']=formataddr(["猪小集",my_sender]) # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg['To']=formataddr(["马小马",my_user])       # 括号里的对应收件人邮箱昵称、收件人邮箱账号
    msg['Subject']="每日新闻"        # 邮件的主题，也可以说是标题
 
    server=smtplib.SMTP_SSL("smtp.qq.com", 465) # 发件人邮箱中的SMTP服务器，端口是25
    server.login(my_sender, my_pass) # 括号中对应的是发件人邮箱账号、邮箱密码
    server.sendmail(my_sender,[my_user,],msg.as_string()) # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    server.quit() # 关闭连接
  except Exception: # 如果 try 中的语句没有执行，则会执行下面的 ret=False
    ret=False
  return ret
ret=mail()
if ret:
  print("邮件发送成功")
else:
  print("邮件发送失败")
    