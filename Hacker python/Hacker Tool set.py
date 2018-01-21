# -*- coding:'utf-8' -*-
#@欢迎加入即刻安全交流群:307283889
import os
import time
print('_!_!_!_!_!_!_!_!_!_!_!_!_!_')
print(    '!_!_!_!_!_!_!_!_!_!_!_!_!_!')
print(    '   ！——！——！——！')
print(        '!！——！——！')
print('1.进行一系列脚本扫描')
print('2.进行DDOS')
print('3.使用nmap 利用已知的漏洞入侵系统')
print('4.使用nmap 探测目标机是否感染了病毒、开启了后门等信息')
print('5.使用nmap 对系统进行安全检查')
print('6.更新nmap脚本数据库')
print('7.使用nmap检测MS-17-010')
print('8.生成metasploit自动攻击模块要用的rc')
print('9.安装nmap高级漏洞扫描模块')
print('10.调用高级漏洞扫描模块')
print('11.自己写的web信息收集器')
print('12.使用metasploit自动攻击模块')
gs=input('请输入你要执行的步骤:')
def nmap():
    try:
      g=input('目标IP:')
      print('[+]一般枚举')
      nmap1=os.system('nmap -vv -Pn -sC -sS -T4 -p {}'.format(g))
      print(nmap1)
      print('====================================================')
      nmap2=os.system('nmap -v -sS -A -T4 {}'.format(g))
      print(nmap2)
      print('====================================================')
      print('[*]Verbose，SYN Stealth，版本信息和针对服务的脚本。')
      nmap3=os.system('nmap -v -p 445 --script=smb-check-vulns --script-args=unsafe=1 {}'.format(g))
      print(nmap3)
      print('====================================================')
      print('[*]进行信息挖掘')
      nmap4=os.system('nmap -sS --script discovery {}'.format(g))
      print(nmap4)
      print('====================================================')
      print('[*]进行利用第三方的数据库或资源进行信息收集或者攻击')
      nmap5=os.system('nmap -sS --script external {}'.format(g))
      print(nmap5)
      print('====================================================')
      print('[*]进行模糊测试，发送异常的包到目标机，探测出潜在漏洞 ')
      nmap6=os.system('nmap -sS --script fuzzer {}'.format(g))
      print(nmap6)
      print('====================================================')
      print('[*]对目标机进行检查是否存在常见的漏洞')
      nmap7=os.system('nmap -sS --script vuln {}'.format(g))
      print(nmap7)
    except:
        print('[-]出现了错误')
        exit()

def ddos():
    try:
      print('[*]进行拒绝服务攻击')
      g1=input('请输入目标IP:')
      nmap8=os.system('nmap --script dos {}'.format(g1))
      print(nmap8)
    except:
        print('[-]出现了错误')
        exit()
def exploit():
    try:
      print('[*]利用已知的漏洞入侵系统')
      g2=input('请输入目标IP:')
      nmap9=os.system('nmap --script exploit {}'.format(g2))
      print(nmap9)
    except:
        print('[-]出现了错误')
        exit()
def malware():
    try:
      print('[*]探测目标机是否感染了病毒、开启了后门等信息')
      g3=input('请输入目标IP:')
      nmap10=os.system('nmap --script malware {}'.format(g3))
      print(nmap10)
    except:
        print('[-]出现了错误')
        exit()
def safe():
    try:
        print('[*]检测系统安全问题')
        g4=input('请输入目标IP:')
        nmap11=os.system('nmap --script safe {}'.format(g4))
        print(nmap11)
    except:
        print('[-]出现了错误')
        exit()
def update():
    try:
      print('[*]更新脚本数据库')
      nmap12=os.system('nmap --script-update')
      print(nmap12)
    except:
        print('[-]出现了错误')
        exit()
def ms17010():
    try:
      print('[*]扫描MS17010的脚本')
      g5=input('请输入目标IP:')
      nmap13=os.system('nmap --script smb-vuln-ms17-010 {}'.format(g5))
      print(nmap13)
    except:
        print('[-]出现了错误')
        exit()
def scanner():
    try:
        lid=input('请输入目标IP:')
        xc=input('请输入线程(最大不能超过10):')
        file=open('zdgj.rc','w')
        file.write('use auxiliary/scanner/portscan/tcp'+"\n")
        file.write('set RHOSTS {}'.format(lid)+"\n")
        file.write('set THREADS {}'.format(xc)+"\n")
        file.write('run'+"\n")
    except:
        print('[-]出现了错误')
        exit()
def gjls():
    try:
      print('[*]nmap安装高级漏洞扫描')
      print('[*]通过其程序Github或官网压缩包下载，解压后把其中的文件释放到以下Nmap文件夹内')
      print('[*]详细教程:http://www.tiaozhanziwo.com/archives/781.html')
      print('[*]详细教程2:http://www.52bug.cn/hacktool/3661.html')
      nmap14=os.system('git clone github：https://github.com/scipag/vulscan')
      print(nmap14)
    except:
        print('[-]出现了错误，请确认你安装了git')
def gjldsm():
    try:
      print('[*]执行高级漏洞扫描模块前请确认你安装了该模块')
      gs6=input('请输入目标IP:')
      nmap15=os.system('nmap -sS -sV --script=vulscan {}'.format(gs6))
      print(nmap15)
    except:
        print('[-]出现了错误')
        exit()
def chax():
    print('[*]调用chaxw.py')
    import chaxw
def msf():
    metasploit = os.system('msfconsole -r /root/zdgj.rc')
    print(metasploit)
if gs=='1':
  nmap()
elif gs=='2':
    ddos()
elif gs=='3':
    exploit()
elif gs=='4':
    malware()
elif gs=='5':
  safe()
elif gs=='6':
  update()
elif gs=='7':
    ms17010()
elif gs=='8':
  scanner()
elif gs=='9':
    gjls()
elif gs=='10':
    gjldsm()
elif gs=='11':
    chax()
elif gs=='12':
    msf()
