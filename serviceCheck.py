#!/usr/bin/python
from subprocess import Popen, PIPE

print "\033[1;103m"+"\033[1;30m"+"\033[1;5m"+" Services info  "+  "\033[5;m" + "\033[25;m"

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
		numcount = []
		for inn in cList:
				
				#print "\033[1;33m"+" "*2+"service name: "+"\033[1;m",((inn.split(':')[0]).split())[0],"\033[1;33m"+" "*10+"          level 3 "+"\033[1;m",((inn.split(':')[4]).split())[0]+"\033[1;33m"+"          level 5 "+"\033[1;m",((inn.split(':')[6]).split())[0]
				len0 = len(((inn.split(':')[0]).split())[0]); l0 = (((inn.split(':')[0]).split())[0]); #print l0

				len4 = len(((inn.split(':')[4]).split())[0]); 
				x4 = 22 - len(l0);   #print (" "*len(l0) +" "*(x4) + ((inn.split(':')[4]).split())[0]) 
			 	servlev3 = (l0+ (" "*(x4) + ((inn.split(':')[4]).split())[0]))
					
				len6 = len(((inn.split(':')[6]).split())[0]); l6 = (((inn.split(':')[6]).split())[0])
				x6 = 35- len(servlev3);
				servlev5 = ((" "*(x6)+l6))   		
				#x6 = ((" "*(22-int(len6)) + (((inn.split(':')[6]).split())[0])))
				#print (x6)
				#servlev5 = 30-len(servlev3)  
				#print servlev5
				crossout= servlev3 + servlev5; print crossout 
				#print str(" "*25+inn)

	cross(Nou)

#worksrunCMD("chkconfig --list","Services which is on:  "," |")


print "Services: "


def servicesCMD(commandSSH,SectionComments,CommandComments):
        cmd = commandSSH
        p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)
        Nout, err = p.communicate()
        Nou=((Nout.rstrip().splitlines()))
#        print
        print SectionComments
        def cross(cList):
                for inn in cList:
                                print "       "+CommandComments+inn
        cross(Nou)


servicesCMD("chkconfig --list","","| ")

