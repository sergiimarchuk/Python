<pre>
#!/usr/bin/python
import csv
from subprocess import Popen, PIPE
with open("listsrv.txt", "rb") as lsrf:
        n = 0
        Fn  = ("uttxt.csv")
        for l in lsrf:
                a = l,
                #print (((str(a).split("'"))[1]).split("\\"))[0]
                servname = ((((str(a).split("'"))[1]).split("\\"))[0])
                cmd = "sysdb name eq -t burk "+servname
                p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)
                Nout, err = p.communicate()
                Nou=((Nout.rstrip().splitlines()))
                print n,"Server Name -",servname
                n = n + 1
                m = 0
                ll = []
                while m < (len(Nou)):
                        #print (Nou)[m]
                        print m,((' '.join((((Nou)[m].split())))))
                        ll.append(((' '.join((((Nou)[m].split()))))))
                        m = m + 1
                #print (ll)
                print
                #w = csv.writer(open(Fn,'a'),dialect='excel')
                #w.writerows(tuple([str(ll).split(",")]))


                #if n <= (len(Nou)):
                #       print ((Nou)[n]),
                #       n = n + 1
                #print (Nou)[0]," ",(' '.join((((Nou)[12].split())))),(' '.join((((Nou)[13].split())))),(' '.join((((Nou)[8].split()))))


</pre>
