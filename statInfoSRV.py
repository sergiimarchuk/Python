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
runCMD("df -T /boot | awk '{ print $7, $2, $1 } '","Partiotion:  ","type fs /boot: ")
runCMD("uptime","Uptime:  ","uptime: ")
runCMD("lsb_release -a | grep Description | awk '{ print $2, $3, $4  }'","Linux Release:  ","linux release: ")

def statusBootFS(commandSSH,SectionComments,CommandComments):
        cmd = commandSSH
        p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)
        Nout, err = p.communicate()
        Nou=((Nout.rstrip().splitlines()))
        print
        print SectionComments
        def cross(cList):
                for inn in cList:
                                print "       "+CommandComments+inn,
        #cross(Nou)
        extfs = (Nou[1].split())[1]
        if extfs == "ext4" or extfs == "ext4":
                mess = '\033[1;32mGreen like Grass\033[1;m'
                print '\033[1;32m%CommandComments%\033[1;m'+extfs+'\033[1;32m Looks good\033[1;m'
        else:
                print CommandComments+"Please take a look on /boot and fs type"


statusBootFS("df -T /boot | awk '{ print $7, $2, $1 } '","Type FS :  ","Type fs /boot: ")
