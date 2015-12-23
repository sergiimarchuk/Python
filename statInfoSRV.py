#!/usr/bin/python
from subprocess import Popen, PIPE

def crossList(cList):
                for i in cList:
                        print i

def runCMD(commandSSH,SectionComments,CommandComments):
        cmd = commandSSH
        p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)
        Nout, err = p.communicate()
        Nou=((Nout.rstrip().splitlines()))
        print
        print SectionComments
        def cross(cList):
                for inn in cList:
                                print "       "+CommandComments+inn
        cross(Nou)

runCMD("hostname -I","Network:  ","IP address which exist on server: ")
runCMD("uname -a","System:  ","Systen info: ")
runCMD("dmesg | grep DMI ","DMI:  ","DMI: ")
runCMD("df -T /boot | awk '{ print $7, $2, $1 } '","Partiotion:  ","Type fs /boot: ")
runCMD("uptime","Uptime:  ","uptime: ")
runCMD("lsb_release -a | grep Description | awk '{ print $2, $3, $4  }'","Linux Release:  ","linux release: ")
