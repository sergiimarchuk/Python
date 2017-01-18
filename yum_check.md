````bash

#!/usr/bin/python

import subprocess

def ssh_command(hostname,mycommand):
    ssh = subprocess.Popen(["ssh", hostname, mycommand ], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = ssh.stdout.readlines()
    return(result)

server_yum_hist = ssh_command("localhost","yum history")
c = 0; s = 0
for i in server_yum_hist:
        li = [];
        if '|' in i:
                line = i.split("|")[3]
                if "U" in line:
                        while c < 1:
                                print i,
                                c = c + 1; s = 1; u = 1
                if ("U" not in line) and  s is 0:
                        s = 0
if s == 0:
        print "Please check this info manuanlly on server"
````
