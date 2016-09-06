<pre>
while m < n:
        o = m
        ip_ = '192.168.10.'+str(o)
        m = m + 1
        print m ,ip_
        subprocess.call(["ping", ip_, "-c 3"])
"""
"""
hostname = "yahoo.com"
hnl = ["yahoo.com", "google.com", "bigmir.net", "ukr.net", "i.ua", "uu.ut"]
for hn in hnl:
        print hn
        out = subprocess.call(["ping", hn, "-c 3"])
        print "OUT",(out)
#subprocess.call(["ping", hostname, "-c 3"])
#ping localhost -c 3
"""




import subprocess
host = ["google.com", "y1ahoo.com1"]
n = 0
print
print host
print " - - - - - - - - -"
for h in host:
        ping = subprocess.Popen(
                ["ping", "-c", "3", host[n]],
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE

        )
        out, error = ping.communicate()
        #print host[n],type(out),

        if ("PING " +host[n]) in out:
                #print [out]
                print
                print " :: " + host[n] + " :: " + "host is UP"
                if " transmitted," in out:
                        print " "+ str(out.split("transmitted"))
                        print
        else:
                        print " :: " + host[n] + " :: " +"host is down. Please check."
                        print
        n = n + 1
print


</pre>
