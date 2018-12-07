##### Insert records into sqlite.db

</pre>
#!/opt/python27/bin/python
from collections import Counter
import glob
import os
import socket
import time 
import datetime
import sqlite3

conn = sqlite3.connect('/opt/python/db_srv_evry/db_srv.db')
concur = conn.cursor()
import glob
import os

a = glob.glob("*")
_pwd_ = os.getcwd()



# function do parsing log file for Memory.
def pars_log():
    with open("/opt/python/db_srv_evry/responsibility-list.txt", "rb") as log_f:
        for line in log_f:
            print line.split(":")[0] #, "the first responsible person is - ", line.split(":")[1], "second is - - ", line.split(":")[2]
            zzz = line.split(":")[0]
            #print(zzz)
            
            concur.execute('INSERT INTO tab_srv(namesrv) VALUES (?)', (zzz, ))
            
            #concur.execute("INSERT INTO tab_srv(namesrv) VALUES ('" + zzz + "')")
            conn.commit()       
</pre>
