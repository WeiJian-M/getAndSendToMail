#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.qiushibaike.com/text/page/1/')
soup = BeautifulSoup(r.content,'lxml')

contentUrl = soup.find('div',class_='col1 old-style-col1').find('div',class_="article block untagged mb15 typs_long").find('a',class_="contentHerf").get('href')

textUrl = 'https://www.qiushibaike.com' + contentUrl

textR = requests.get(textUrl)
textSoup = BeautifulSoup(textR.content, 'lxml')
text = textSoup.find('div',class_="content").text

my_sender='714540398@qq.com'  # 发件人邮箱账号
my_pass = 'xlfprgqmxaadbeah'   # 发件人邮箱密码(注意这个密码不是QQ邮箱的密码，是在QQ邮箱的SMTP中生成的授权码)
my_user='m714540398@163.com'   # 收件人邮箱账号，我这边发送给自己
def mail():
  ret=True
  try:
    msg=MIMEText(text,'plain','utf-8') #填写邮件内容
    msg['From']=formataddr(["猪小集",my_sender]) # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg['To']=formataddr(["马小马",my_user])       # 括号里的对应收件人邮箱昵称、收件人邮箱账号
    msg['Subject']="每日笑话"        # 邮件的主题，也可以说是标题
 
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