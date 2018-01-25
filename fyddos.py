import os
import time
def fyddos():
    IGNORE_IP_LIST = "/usr/local/ddos/ignore.ip.list"
    PGOPDIR="/usr/local/ddos/ddos.conf"
    PROG = "/usr/local/ddos/ddos.sh"
    if os.path.exists(PROG):
     print '[+]The execution file exists to continue the program.'
    else:
        print '[-]The execution file does not exist, the closing procedure.'
        exit()
    if os.path.exists(PGOPDIR):
        print '[+]The configuration file exists to start the execution of the program.'
    else:
        print '[-]There is no exit procedure for the configuration file.'
        exit()
    if os.path.exists(IGNORE_IP_LIST):
        print '[+]The IP white list file exists to continue the program.'
    else:
        print '[-]IP white list file does not exist, end the program.'
        exit()

    time.sleep(1)
    print '[+]Start configuring the IP white list.'
    IPlist=raw_input('Please enter your white list IP, and if not, enter q to enter the next step:')
    if IPlist=='q':
        try:
          import dy1
        except Exception , g:
            print '[-]Catch the error cause:',g
        print '[+]It has been added to it.'
        time.sleep(3)
        try:
          import dy2
        except Exception , r:
            print '[-]Catch the error cause:',r
        time.sleep(3)
        try:
            import dy3
        except Exception , p:
            print '[-]Catch the error cause:',p
        print '[+]Query information,Please input: netstat -ntu | awk ''{print $5}'' | cut -d: -f1 | sort | uniq-c | sort -n command view.'
        isd=os.system('ddos')
        sda=os.system('service iptables status')
        print isd
        print sda

    else:
        list=open('/usr/local/ddos/ignore.ip.list','w')
        list.write(IPlist+"\n")
        print '[+]It has been added to it:',IPlist
        time.sleep(3)
        try:
          import dy1
        except Exception , w:
          print('[-]Catch the error cause:',w)
        time.sleep(3)
        try:
            import dy2
        except Exception , d:
            print '[-]Catch the error cause:',d
        time.sleep(3)
        try:
            import dy3
        except Exception ,z:
            print '[-]Catch the error cause:',z
        print '[+]Query information,Please input: netstat -ntu | awk ''{print $5}'' | cut -d: -f1 | sort | uniq-c | sort -n command view.'
        isds = os.system('ddos')
        sdas= os.system('service iptables status')
        print isds
        print sdas

fyddos()