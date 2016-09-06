<pre>
#!/usr/bin/python
import os, sys, datetime, time,socket
import smtplib
from datetime import datetime
from subprocess import Popen, PIPE

hfqdn = socket.getfqdn()
imess = "\"Please check \""
bmess = " \" Issue in system log: kernel: o2net: No connection established with node 1 after 60.0 seconds, check network and cluster configuration. \""
sendapp = "mail -s"
emails = "'user1@domain.com', 'user2@domain.com'"
listMon = {'Jan': '1', 'Feb': '2', 'Mar': '3',  'Apr': '4',  'May': '5', 'Jun': '6', 'Jul': '7', 'Aug': '8', 'Sep': '9', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
localtime = time.localtime(time.time())
timestamp = int(time.time());
#print "current time in second1",timestamp
intts = (timestamp)
nmin = 8900
now = datetime.now();mm = str(now.month);dd = str(now.day);yyyy = str(now.year);hour = str(now.hour);mi = str(now.minute);sec=str(now.second);

def status(commandSSH,cmdARG1,cmdARG2,cmdARG3,cmdARG4):
    cmd = commandSSH + cmdARG1 + " | "+ cmdARG2 + cmdARG3 + cmdARG4
    print cmd
    p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)
    Nout, err = p.communicate()

def checkSysLog():
    with open("/var/log/messages-20160124", "rb") as fp:
        tmlist = [];
        for lin in fp:
            k = lin
            if "ERRRRRRRRROOOOOOOOOORRRR" in k:
                tpoint = lin.split();
                #ups=tpoint; print tpoint
                ups0 = tpoint[0]; ''' MONTH '''; ups00 = listMon.get(ups0);
                ups1 = tpoint[1]; ''' DAY       '''
                ups2 = tpoint[2]; ''' TIME format h: m: s '''
                uhour = tpoint[2].split(':')[0];        ''' hour '''
                uminut = tpoint[2].split(':')[1];       ''' minut '''
                usec = tpoint[2].split(':')[2];         ''' second '''
                conDateInSecLogRec = datetime(int(yyyy), int(ups00), int(ups1), int(uhour), int(uminut), int(usec)); ''' convert date form log record into seconds '''
                #print "conv record log date ",int(conDateInSecLogRec.strftime('%s'))
                #print type(conDateInSecLogRec)
                upas = int(conDateInSecLogRec.strftime('%s')) #- int(nmin)
                #print upas
                #print int(upas)
                tmago = intts-nmin
                if  tmago < upas:
                    tmlist.append(lin)
                    #status("echo ",imess+hfqdn,sendapp+"\""+lin+"\""," user1@domain.com","")
                    #print "lin",(lin),
        #return tmlist
        print len(tmlist)
        if len(tmlist)>0:
            #status("echo ","\""+(" ".join(str(x) for x in tmlist))+"\"",sendapp+" "+imess+" "+hfqdn,emails,"")
            #status("echo ",imess+hfqdn,sendapp+"\""+(" ".join(str(x) for x in tmlist))+"\""," user1@domain.com","")
            #status("echo ",imess+hfqdn,sendapp+bmess," user1@domain.com","")
            #print (" ".join(str(x) for x in tmlist))
            print len(tmlist)
            html=''
            html=html + '<html><body>'
            html=html + '<h1>Test</h1>'
            html=html + '<font color="red"><h2>Test2</h1></font>'
            html=html + '<br>'
            html=html + '<br>'
            html=html + 'dawefasdfasdfasdfasdfasdfasdfa<br>'
            html=html + '111111111111111111111111111<br>'
            html=html + '<pre> (" ".join(str(x) for x in tmlist) </pre>'
            html=html + '<table border="1" width=100%">'
            html=html + '<tr>'
            html=html + '<td><% x  %>></td>'
            html=html + '</tr>'
            html=html + '</table>'
            html=html + '</body></html>'

            #import smtplib

            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText

            me = "test@gmail.com"
            you = ['user1@domain.com']

            msg = MIMEMultipart('alternative')
            msg['Subject'] = "My test email"
            msg['From'] = me
            msg['To'] = ','.join(you)

            part2 = MIMEText(html, 'html')

            msg.attach(part2)

            s = smtplib.SMTP('127.0.0.1')
            s.sendmail(me, you, msg.as_string())
            s.quit()

checkSysLog()
#print (imess+hfqdn)
'''#echo "Please check "host99006 | mail -s"Jan 17 04:02:37 host99006 check configuration.'''


</pre>
