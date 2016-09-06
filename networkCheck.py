#!/usr/bin/python
from subprocess import Popen, PIPE

print "\033[1;103m"+"\033[1;30m"+"\033[1;5m"+" Network info  "+  "\033[5;m" + "\033[25;m"

def crossList(cList):
                for i in cList:
                        print i

def runCMD(commandSSH,SectionComments,CommandComments):
        cmd = commandSSH
        p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)
        Nout, err = p.communicate()
        Nou=((Nout.rstrip().splitlines()))
        print
        print "\033[1;34m" +SectionComments+ "\033[1;m" 
        def cross(cList):
                for inn in cList:
                                print "       "+CommandComments+inn
        cross(Nou)

runCMD("hostname", "Hostname:  ","| ")
runCMD("hostname -I","IP:  ","| ")
runCMD("ip a","","| ")
runCMD("ifconfig -a","Network:  ","| ")
runCMD("netstat -r", "Route:  ","| ")


