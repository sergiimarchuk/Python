<pre>
#!/usr/bin/python
import os, sys, datetime, time

listMon = {'Jan': '1', 'Feb': '2', 'Mar': '3',  'Apr': '4',  'May': '5', 'Jun': '6', 'Jul': '7', 'Aug': '8', 'Sep': '9', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
localtime = time.localtime(time.time())
weeks4inSec = 2419200
timestamp = int(time.time());

''' print timestamp #let show current time in second from 1970 to now
from python shell >>> datetime.fromtimestamp(1454424325)
out put what we got in this case datetime.datetime(2016, 2, 2, 16, 45, 25)
'''

datetime = str(localtime[0]) + """-""" + str(localtime[1]) + """-"""  + str(localtime[2]) + 'H'  + str(localtime[3]) + 'm' + str(localtime[4])
listfile = {'/etc/passwd':'ep', '/var/log/messages':'vlm'}

f=os.popen("tail -n 200 /var/log/messages | grep -i ERROR1")
for i in f.readlines():
    print "  | ",i,
    #print i.split(),
    print i.split()[0], i.split()[1], (i.split()[2]).split(':')[0],(i.split()[2]).split(':')[1],(i.split()[2]).split(':')[2]

    fnout = '/var/log/logbook/logtest-%s.txt'%datetime
    #print fnout
    f = open(fnout,'a')
    f.write(' ' + datetime +', ' + i)
    #f.write(datetime +', ' + i +'\n')
    f.close()
</pre>

<pre>
#!/usr/bin/python
import os, sys, datetime, time
from datetime import datetime

listMon = {'Jan': '1', 'Feb': '2', 'Mar': '3',  'Apr': '4',  'May': '5', 'Jun': '6', 'Jul': '7', 'Aug': '8', 'Sep': '9', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
localtime = time.localtime(time.time())
timestamp = int(time.time());
print "current time in second1",timestamp
#rint localtime

now = datetime.now();mm = str(now.month);dd = str(now.day);yyyy = str(now.year);hour = str(now.hour);mi = str(now.minute);sec=str(now.second);  #print yyyy+mm+dd+hour+mm

def passwdf():
        with open("/var/log/messages", "rb") as fp:
                for lin in fp:
                        k = lin
                        if "ERROR1" in k:
                                tpoint = lin.split()
                                tmon = (lin.split()[0]),
                                tday = lin.split()[1],
                                ttime = lin.split()[2],
                                #print type(ttime)
                                #print lin,
                                tstring = list(tmon+tday+ttime); print tstring
                                #return(r)

#passwdf()

#str(int((listMon.get(monthLic))))


#month = listMon.get('Feb')
#print month
t2=datetime(int(yyyy), int(mm), int(dd), int(hour), int(mi), int(sec))
#print "gettterconverter time ",t2
print "current time in second2",int(t2.strftime('%s'))

#t1=datetime(2016, 3, 22, 13, 06, 25)
#print t1

#print int(t1.strftime('%s'))

''' print timestamp #let show current time in second from 1970 to now
from python shell >>> datetime.fromtimestamp(1454424325)
out put what we got in this case datetime.datetime(2016, 2, 2, 16, 45, 25)
'''


</pre>

<pre>
#!/usr/bin/python
import os, sys, datetime, time
from datetime import datetime

listMon = {'Jan': '1', 'Feb': '2', 'Mar': '3',  'Apr': '4',  'May': '5', 'Jun': '6', 'Jul': '7', 'Aug': '8', 'Sep': '9', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
localtime = time.localtime(time.time())
timestamp = int(time.time());
print "current time in second1",timestamp
nmin = 540
now = datetime.now();mm = str(now.month);dd = str(now.day);yyyy = str(now.year);hour = str(now.hour);mi = str(now.minute);sec=str(now.second);
def passwdf():
        with open("/var/log/messages", "rb") as fp:
                for lin in fp:
                        k = lin
                        if "ERROR1" in k:
                                tpoint = lin.split();
                                #ups=tpoint; print tpoint
                                ups0 = tpoint[0]; ''' MONTH '''; ups00 = listMon.get(ups0);
                                ups1 = tpoint[1]; ''' DAY       '''
                                ups2 = tpoint[2]; ''' TIME format h: m: s '''
                                uhour = tpoint[2].split(':')[0];        ''' hour '''
                                uminut = tpoint[2].split(':')[1];       ''' minut '''
                                usec = tpoint[2].split(':')[2];         ''' second '''
                                conDateInSecLogRec = datetime(int(yyyy), int(ups00), int(ups1), int(uhour), int(uminut), int(usec)); ''' convert date form log record into seconds '''
                                print "conv record log date ",int(conDateInSecLogRec.strftime('%s'))
                                #u= 3-1; print u
                                print type(conDateInSecLogRec)
                                upas = int(conDateInSecLogRec.strftime('%s')) - int(nmin)
                                print upas
                                        #if
                                print lin,
                                #return(r)

passwdf()

</pre>

<pre>
#!/usr/bin/python
import os, sys, datetime, time
from datetime import datetime

listMon = {'Jan': '1', 'Feb': '2', 'Mar': '3',  'Apr': '4',  'May': '5', 'Jun': '6', 'Jul': '7', 'Aug': '8', 'Sep': '9', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
localtime = time.localtime(time.time())
timestamp = int(time.time());
#print "current time in second1",timestamp
intts = (timestamp)
nmin = 540
now = datetime.now();mm = str(now.month);dd = str(now.day);yyyy = str(now.year);hour = str(now.hour);mi = str(now.minute);sec=str(now.second);
def checkSysLog():
    with open("/var/log/messages", "rb") as fp:
        for lin in fp:
            k = lin
            if "ERROR1" in k:
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
                    print lin,
                #return(r)

checkSysLog()
</pre>

<pre>
#!/usr/bin/python
import os, sys, datetime, time,socket
from datetime import datetime
from subprocess import Popen, PIPE

hfqdn = socket.getfqdn()
imess = "\"Please check \""
bmess = " \" Issue in system log: kernel: o2net: No connection established with node 1 after 60.0 seconds, check network and cluster configuration. \""
sendapp = "mail -s"
emails = " sergii.marchuk@.com"
listMon = {'Jan': '1', 'Feb': '2', 'Mar': '3',  'Apr': '4',  'May': '5', 'Jun': '6', 'Jul': '7', 'Aug': '8', 'Sep': '9', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
localtime = time.localtime(time.time())
timestamp = int(time.time());
#print "current time in second1",timestamp
intts = (timestamp)
nmin = 540
now = datetime.now();mm = str(now.month);dd = str(now.day);yyyy = str(now.year);hour = str(now.hour);mi = str(now.minute);sec=str(now.second);

def status(commandSSH,cmdARG1,cmdARG2,cmdARG3,cmdARG4):
                cmd = commandSSH + cmdARG1 + " | "+ cmdARG2 + cmdARG3 + cmdARG4
                print cmd
                p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)
                Nout, err = p.communicate()

def checkSysLog():
    with open("/var/log/messages", "rb") as fp:
        tmlist = [];
        for lin in fp:
            k = lin
            if "kernel: o2net: No connection established" in k:
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
                    #status("echo ",imess+hfqdn,sendapp+"\""+lin+"\""," sergii.marchuk@.com","")
                    #print "lin",(lin),
        #return tmlist
        print tmlist
        if len(tmlist)>0:
                status("echo ","\""+(" ".join(str(x) for x in tmlist))+"\"",sendapp+" "+imess+hfqdn,emails,"")
                #status("echo ",imess+hfqdn,sendapp+"\""+(" ".join(str(x) for x in tmlist))+"\""," sergii.marchuk@.com","")
                ###status("echo ",imess+hfqdn,sendapp+bmess," sergii.marchuk@.com","")
                #status("echo ",imess+hfqdn,sendapp+bmess," sergii.marchuk@.com","")
                print (" ".join(str(x) for x in tmlist))

checkSysLog()
print (imess+hfqdn)
#echo "checking send message" | mail -s "this is a test email" sergii.marchuk@.com
#echo "checking send message" | mail -s "this is a test email" sergii.marchuk@.com

''' def status(commandSSH,cmdARG1,cmdARG2,cmdARG3,cmdARG4):
                cmd = commandSSH + cmdARG1 + " | "+ cmdARG2 + cmdARG3 + cmdARG4
                print cmd
                p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)
                Nout, err = p.communicate()
'''

#status("echo ", "\"Please check oracle\" | ","mail -s \"This is a Test email\""," sergii.marchuk@.com","")
#status("echo ",imess+hfqdn,"mail -s \"This is a Test email\""," sergii.marchuk@.com","")
###status("echo ",imess+hfqdn+bmess,sendapp+bmess," sergii.marchuk@.com","")
#status("echo ",imess+hfqdn,sendapp+checkSysLog()," sergii.marchuk@.com","")

</pre>
