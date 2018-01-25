live=raw_input('Please enter your mailbox, so that you can tell you the IP that has been sealed:')
data=''
with open('/usr/local/ddos/ddos.conf','r+')as f:
    for line in f.readlines():
        if(line.find('EMAIL_TO')==0):
            line='EMAIL_TO={}'.format(live)
        data+=line

with open('/usr/local/ddos/ddos.conf','r+')as f:
    f.writelines(data)