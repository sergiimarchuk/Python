#!/usr/bin/python
from subprocess import Popen, PIPE

def crossList(cList):
                for i in cList:
                        print i

def runCMD(commandSSH,Comments):
        cmd = commandSSH
        p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)
        Nout, err = p.communicate()
        Nou=((Nout.rstrip().splitlines()))

        print
        print " -- -- -- -- -- -- -- -- -- -- -- -- " + Comments
        crossList(Nou)
        print


runCMD("hostname -I","IP address which exist on server")
runCMD("uname -a","Systen info")
runCMD("dmesg | grep DMI","DMI")
runCMD("df -T /boot | awk '{ print $7, $2, $1 } '","type fs")
