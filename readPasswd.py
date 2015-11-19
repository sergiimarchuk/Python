#!/usr/bin/python

with open("/etc/passwd", "rb") as gro:
        lines = []
        for line in gro:
                #print "line is = ",(line)
                arr = line.split(":")[0] + ' ' + line.split(":")[1] + ' ' + line.split(":")[2] + ' ' + line.split(":")[3] + ' ' + line.split(":")[4] + ' ' + line.split(":")[5] + ' ' + line.split(":")[6]
                mass3=line.split(":")[0]+'    '+line.split(":")[2]
                print arr
                print type(arr)


"""
Username
Password
UID
GID
GECOS
Home directory
Shell
"""
