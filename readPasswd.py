#!/usr/bin/python

with open("/etc/passwd", "rb") as gro:
        lines = []
        for line in gro:
                #print "line is = ",type(line)
                #arr = line.split(":")[0] + ':' + line.split(":")[1] + ':' + line.split(":")[2] + ':' + line.split(":")[3] + ':' + line.split(":")[4] + ':' + line.split(":")[5] + ':' + line.split(":")[6]
                #print arr
                lines.append(line);
        print type(lines)
        i = len(lines)
        k=0
        while k < i:
                for inl in lines:
                        print (lines[k])
                        k = k+1
                        #print "k =",k



                #print inl

"""
                      oo=lines
                ok = []
                for ij in oo:
                        #print ij.split(":")[0]
                        #print (ok.append(ij.split(":")[0]))
                        ok.append(ij.split(":")[0])
                ko = " groups='" + ','.join(ok) + "'"
                return(ko)
"""



#print type(arr)


"""
Username
Password
UID
GID
GECOS
Home directory
Shell
"""
