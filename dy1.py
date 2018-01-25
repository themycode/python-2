conf=input('Please enter an IP number more than how many connections will be blocked:')
data = ''
with open('/usr/local/ddos/ddos.conf', 'r+') as f:
    for line in f.readlines():
        if (line.find('NO_OF_CONNECTIONS') == 0):
            line = 'NO_OF_CONNECTIONS={}'.format(conf) + '\n'
        data += line

with open('/usr/local/ddos/ddos.conf', 'r+') as f:
    f.writelines(data)