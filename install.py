import os
def main():
  try:
    g=os.system('git clone https://github.com/snail007/ddos-defalte.git')
    print g
  except:
      print'[-]You didn t install git'
  try:
    s=os.system('tar zxfv ddos-defalte.tar.gz')
    print s
  except:
      print '[-]Youd didan t install tar'
  v=os.system('cd ddos-defalte')
  print v
  dsd=os.system('./install.sh')
  print dsd
if __name__ == '__main__':
    main()