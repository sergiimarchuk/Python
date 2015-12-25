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
        print "\033[1;34m" +SectionComments+ "\033[1;m"
        def cross(cList):
                for inn in cList:
                                print "       " +CommandComments+inn,
        #cross(Nou)
        extfs = (Nou[1].split())[1]
        if extfs == "ext4" or extfs == "ext4":
                print "\033[1;33m" + CommandComments+ "\033[1;m"+"\033[1;48m" + extfs + "\033[1;m"+"\033[1;32m Looks good\033[1;m"
        else:
                print CommandComments+"Please take a look on /boot and fs type"


statusBootFS("df -T /boot | awk '{ print $7, $2, $1 } '","Type FS :  ","Type fs /boot: ")


def getIDusers(commandSSH,SectionComments,CommandComments):
        userlist = ['aouser','aoapp']
        for ul in userlist:
                cmd = commandSSH+" "+ul
                p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)
                Nout, err = p.communicate()
                Nou=((Nout.rstrip().splitlines()))
                print
                print "\033[1;34m" +SectionComments+ ul +"\033[1;m"

                def cross(cList):
                        for inn in cList:
                                        print "       " +CommandComments+inn,

                cross(Nou)

getIDusers("id","User ID Info :  ","id: ")

def getPERfolder(commandSSH,commandARG1,SectionComments,CommandComments):
        userlist = ['aouser','aoapp','nnnn']
        for ul in userlist:
                cmd = commandSSH+" "+ul+" "+commandARG1
                p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)
                Nout, err = p.communicate()
                Nou=((Nout.rstrip().splitlines()))
                print
                #print "\033[1;34m" +SectionComments+ ul +" "+ err+"\033[1;m"

                def cross(cList):
                        for inn in cList:
                                        #print "       " +CommandComments+inn,
                                        print "Permissions Home directory: " +ul+" ",(inn).split(':')[5],
                                        cmd = "ls -ld"+" "+(inn).split(':')[5]
                                        p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)
                                        out, err = p.communicate()
                                        print out
                                        #print cmd

                cross(Nou)
getPERfolder("grep","/etc/passwd","User ID Info :  ","id: ")

