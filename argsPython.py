#!/usr/bin/python
import sys
from subprocess import Popen, PIPE
dicarg =  {'shell':'-m -s /bin/bash','homedir':'-d /tmp/test'}

def CreateUser(commandSSH,commandARG1,SectionComments,CommandComments):
                cmd = commandSSH+" "+ sys.argv[1]+" "+dicarg.get(sys.argv[2])+" "+dicarg.get(sys.argv[3])
                p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)
                Nout, err = p.communicate()
                Nou=((Nout.rstrip().splitlines()))

CreateUser("/usr/sbin/useradd",sys.argv[1],sys.argv[2],sys.argv[3])


'''
Example.
[@appsrv spython]# ./createUserDef.py testuser1 shell homedir
'''
