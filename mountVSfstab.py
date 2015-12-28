#!/usr/bin/python
from subprocess import Popen, PIPE

def mountRun():
        cmd = "mount | awk  '{print $3}'"
        p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)
        out, err = p.communicate()

        ou=((out.rstrip().splitlines()));
        mlist = []; i= 0; maxl = len(ou)
        for n in ou:
                if i <= maxl:
                        mlist.append(ou[i])
                        i = i +1;
        return  mlist

def catFstab():
        cmd = "cat /etc/fstab | grep -v ^# | grep -v ^$ | awk  '{print $2}'"
        p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)
        out, err = p.communicate()

        tou=((out.rstrip().splitlines()));
        tmlist = []; ti= 0; tmaxl = len(tou)
        for tn in tou:
                if ti <= tmaxl:
                        tmlist.append(tou[ti])
                        ti = ti +1;
        return tmlist

slistA1 = set(mountRun()); #print slistA1; print "vs"
slistB1 = set(catFstab()); #print slistB1

def crossList(cList):
                for el in cList:
                        print el


def compSet(listA1,listB1):
        slistA1 = set(listA1);
        slistB1 = set(listB1);

        Y = slistA1.symmetric_difference(slistB1)

        #print '\033[1;31m\"Attantion! Please take a look and compare "cat /etc/fstab" and "mount" "\033[1;m' #,list(Y)
        #print
        if slistA1 <> slistB1:
                print '\033[1;31m\"Attantion! Please take a look and compare "cat /etc/fstab" and "mount" "\033[1;m'
                UA = slistA1.difference(slistB1);
                UB = slistB1.difference(slistA1);
                def crossList(cList):
                        for el in cList:
                                print el
                crossList(UA);
                crossList(UB);
        else:
                print "\033[1;31m" + "mount VS fstab is Equal." + "\033[1;m"
                #UA = slistA1.difference(slistB1);
                #UB = slistB1.difference(slistA1);

print
compSet(slistA1,slistB1)
