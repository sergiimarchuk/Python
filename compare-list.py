#!/usr/bin/python

listA1 = ['A','B','C','D','E','G','H','L']

listB1 = ['X','Y','C','M','N','Z','W','J','J','L','H']

lenA1 = len(listA1)
lenB1 = len(listB1)

print "len listA ",lenA1
print "len listB ",lenB1

print "----------------------------------------------------------------------------------------------------------"
print listA1; print listB1
print "----------------------------------------------------------------------------------------------------------"
print


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


compareList(listA1,listB1)
