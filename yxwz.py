#-*- coding:'utf-8' -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
zhengwen=input('请输入正文:')
fajianr=input('请输入发件人:')
shoujianr=input('请输入收件人:')
zhuti=input('主题:')
messeng=MIMEText(zhengwen,'plain','utf-8')#正文
messeng['From']=Header(fajianr,'utf-8')#发件人
messeng['TO']=Header(shoujianr,'utf-8')#收件人
subject=zhuti#主题
messeng['Subject']=Header(subject,'utf-8')
def yxwz():
  try:
    smtp=smtplib.SMTP()
    smtp.connect('smtp.sohu.com','25')
    smtp.login('你的搜狐邮箱','你搜狐的密码')
  smtp.sendmail('你的搜狐邮箱'['目标邮箱'],messeng.as_string())
    smtp.quit()
    print('[*]邮件发送成功')
  except Exception as e:
      print('[-]发送失败,报错原因:',e)
yxwz()