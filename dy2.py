lv=raw_input('Use APF or iptables to seal IP. It is recommended to use iptables to change the value of APF_BAN to 0:')
data=''
with open('/usr/local/ddos/ddos.conf','r+') as f:
    for line in f.readlines():
        if(line.find('APF_BAN')==0):
            line='APF_BAN={}'.format(lv)+'\n'
        data+=line

with open('/usr/local/ddos/ddos.conf','r+') as f:
    f.writelines(data)
