#!/usr/bin/python
from subprocess import Popen, PIPE
with open("listsrv.txt", "rb") as lsrf:
        n = 0
        for l in lsrf:
                a = l,
                #print (((str(a).split("'"))[1]).split("\\"))[0]
                servname = ((((str(a).split("'"))[1]).split("\\"))[0])
                cmd = "command arguments "+servname
                p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)
                Nout, err = p.communicate()
                Nou=((Nout.rstrip().splitlines()))
                print n
                n = n + 1
                m = 0
                while m < (len(Nou)):
                        print (Nou)[m]
                        m = m + 1
                #if n <= (len(Nou)):
                #       print ((Nou)[n]),
                #       n = n + 1
                #print (Nou)[0]," ",(' '.join((((Nou)[12].split())))),(' '.join((((Nou)[13].split())))),(' '.join((((Nou)[8].split()))))


