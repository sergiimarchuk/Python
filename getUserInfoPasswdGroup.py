<pre>
# cat pypass.py
#!/usr/bin/python
def passwdf():
        with open("/etc/passwd", "rb") as fp:
                for lin in fp:
                        k = lin
                        if "nidlar" in k:
                                #print k.split(":")#print "Username",k.split(":")[0]#print "Password",k.split(":")[1]#print "UID",k.split(":")[2]#print "GroupID",k.split(":")[3]#print "UserID",k.split(":")[4]#print "HomeDirectory",k.split(":")[5]#print "CommandShell",k.split(":")[6]
                                username = k.split(":")[0]
                                comment = k.split(":")[4]
                                home = k.split(":")[5]
                                r="- user: name="+ "'"+username + "'" + " comment=" + "'" + comment + "'"+" home='" + home + "'"
                                return(r)
def shadowf():
        with open("/etc/shadow", "rb") as sp:
                for lins in sp:
                        ks = lins
                        if "nidlar" in ks:
                                #print ks.split(":")#print "User name",ks.split(":")[0]#print "Password",ks.split(":")[1]#print "LastPasswordChange",ks.split(":")[2]#print "Minimum",ks.split(":")[3]#print "Maximum",ks.split(":")[4]#print "Warn",ks.split(":")[5]#print "Inactive",ks.split(":")[6]#print "Expire",ks.split(":")[7]
                                s = " password='"+ks.split(":")[1]+"'"
                                return(s)
def gpasswdf():
        with open("/etc/passwd", "rb") as sgp:
                for nsgp in sgp:
                        ksgp = nsgp
                        if "nidlar" in ksgp:
                                gpasswd = ksgp.split(":")[3]
                                gr=" group='"+gpasswd + "'"
                                return(gr)

def groupf():
        with open("/etc/group", "rb") as sgf:
                lines = []
                for line in sgf:
                        #print len(line)
                        if "nidlar" in sgf:
                                lines.append(line[:-1]) if line[-1] == "\n" else lines.append(line)
                                oo=lines
                                #print lines
                                return(type(oo))

def allfroupf():
        with open("/etc/group", "rb") as gro:
                lines = []
                for line in gro:
                #print len(line)
                        if "nidlar" in line:
                                if (line not in lines):
                                        lines.append(line[:-1]) if line[-1] == "\n" else lines.append(line)
                                        oo=lines
                for ij in oo:
                        #print ij.split(":")[0]
                        return(ij.split(":")[0])



res =  passwdf() + shadowf() +  gpasswdf()# + allfroupf()
print res

#print groupf()


with open("/etc/group", "rb") as gro:
        lines = []
        for line in gro:
        #print len(line)
                if "nidlar" in line:
                        if (line not in lines):
                                lines.append(line[:-1]) if line[-1] == "\n" else lines.append(line)
                                oo=lines
        ok = []
        for ij in oo:
                print ij.split(":")[0]
                print (ok.append(ij.split(":")[0]))
</pre>
