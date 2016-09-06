#!/usr/bin/python
import os
import os.path
from subprocess import Popen, PIPE

print "\033[1;103m"+"\033[1;30m"+"\033[1;5m"+"  NTP Status  "+  "\033[5;m" + "\033[25;m"

def readFile(pathFile):
	with open(pathFile, "rb") as fp:
	#f=os.popen(pathFile)
		for i in fp.readlines():
     			print "myresult:",(i),
#readFile("/etc/ntp.conf")	


def checkExistsFile(pathFile):
	if os.path.isfile(pathFile) and os.access(pathFile, os.R_OK):
		print "File /etc/ntp.conf exists and is readable"
		#readFile()
	else:
		print "Either file is missing or is not readable"

checkExistsFile("/etc/ntp.conf")


def runCMD(commandSSH,SectionComments,CommandComments):
        cmd = commandSSH
        p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)
        Nout, err = p.communicate()
        Nou=((Nout.rstrip().splitlines()))
        print
	if len(Nou) <> 0:
        	print "\033[1;34m"+SectionComments+"\033[1;m"
        	def cross(cList):
                	for inn in cList:
                        	        print "       "+CommandComments+inn
		cross(Nou)
	else:
		print SectionComments + "not installed on server"

runCMD("rpm -qa | grep ntp","RPM package NTP :  ","| ")
runCMD("cat /etc/ntp.conf | grep -v ^# | grep -v ^$ | grep -v grep","Config NTP : ","|  " )


def getIDusers(commandSSH,SectionComments,CommandComments):
	cmd = commandSSH
	p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)
	Nout, err = p.communicate()
	Nou=((Nout.rstrip().splitlines()))
	print
	print "\033[1;34m" +SectionComments+"\033[1;m"
	def cross(cList):
		for inn in cList:
			pr = inn,
			#print "       " +CommandComments+inn,
			return pr
	print "       "+CommandComments+" "+(str(cross(Nou))).split()[11] + "  Process ID : " + (str(cross(Nou))).split()[1]

#getIDusers("ps -ef | grep ntp | grep -v grep | grep -v ntpCheck.py","NTP process :  ","ntp service : ")

