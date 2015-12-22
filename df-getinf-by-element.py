#!/usr/bin/python

def compareList(listA,listB):
        lenA = len(listA)
        lenB = len(listB)
        countA = 0
        for a in listA:
                print "countA =------------------------------------------------------------------ ",countA
                countB = 0
                for b in listB:
                        if listA[countA] == listB[countB]:
                                print; print;
                                #print "EQUAL!!!",
                                print '\033[1;42m\"EQUAL "\033[1;m',listA[countA]," " ,listB[countB],"  ",countA+1,
                                countB = countB +1
                        else:
                                print;print;print '\033[1;45m"Not equal |"\033[1;m',listA[countA]," ", listB[countB],"Not equal",
                                countB = countB +1
                                print "| Below countB =",countB,; print
                countA = countA + 1


from subprocess import Popen, PIPE
cmd = "mount | awk  '{print $3}'"
p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)
out, err = p.communicate()


#this line return code result so it is not import. in this case
#print "Return code: ", p.returncode
# this standart lin for out put current result
#print out.rstrip(), err.rstrip()
"""print "Type output --------- ",type(out.rstrip());
for l in (out.rstrip().splitlines()):
        print l"""
"""for s in ou:
        print s""" #print len(ou) ; #print "type ",type(ou) #print ou[1]


ou=((out.rstrip().splitlines())); print ; print ; print ;
mlist = []; i= 0; maxl = len(ou)
for n in ou:
        if i <= maxl:
                #print ou[i],
                #print i
                mlist.append(ou[i])
                i = i +1; print
print sorted(mlist); print; print; print


cmd = "cat /etc/fstab | grep -v ^# | grep -v ^$ | awk  '{print $2}'"
p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)
out, err = p.communicate()

#print out.rstrip(), err.rstrip()



tou=((out.rstrip().splitlines())); print ; print ; print ;
tmlist = []; ti= 0; tmaxl = len(tou)
for tn in tou:
        if ti <= tmaxl:
                #print tou[ti],
                #print i
                tmlist.append(tou[ti])
                ti = ti +1; print
print sorted(tmlist); print; print; print


compareList(mlist,tmlist)


#print cmp(mlist, mlist)

"""
y = len(mlist); print;  q=0;
for w in mlist:
        if q <= len(mlist):
                print q,((sorted(mlist)[q])),
                q = q + 1; print

z= len(tmlist); print; x=0;
for p in tmlist:
        if x <= len(tmlist):
                print x,((sorted(tmlist)[x])),
                x = x + 1

"""
