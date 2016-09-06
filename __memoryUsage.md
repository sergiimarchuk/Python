<pre>
#!/usr/bin/python
import psutil
import time
percentUsed = psutil.virtual_memory().percent

def memory_Usage():
        virt = psutil.virtual_memory()

        total_threshold1= int(virt.total / 1024 / 1024)

        print
        print " .1. Memory usage:           ..."
        print "................................................................"
        print " Total Memory:                | " + str(int(virt.total / 1024 / 1024)) + " M"
        print " Used  Memory:                | " + str(int(virt.used / 1024 / 1024)) + " M" +" "+ " Percent value "  +str(percentUsed) + "%"
        print " Free  Memory:                | " + str(int(virt.free / 1024 / 1024)) + " M"
        print " Virt  Memory:                | " + str(int(getattr(virt, 'shared', 0) / 1024)) + " K"
        print " Buffers Memory:              | " + str(int(getattr(virt, 'buffers', 0) / 1024)) + " K"
        print " Cached  Memory:              | " + str(int(getattr(virt, 'cached', 0) / 1024)) + " K"
        print("................................................................")
        if percentUsed > 80 and percentUsed < 90:
                print "Warning. Utilization memory is between 80% and 90% Current value is "+ str(percentUsed) + "%"
        if percentUsed >= 90:
                print ".......Critical. Current uses memory: " +str(percentUsed)+"%"+ "............\n";
        if percentUsed < 80:
                print " Utilization memory status is OK.",str(percentUsed)+"%"
        print("................................................................\n\n")

def util_Swap():
        print " .2. Utilization Swap:       ..."
        swap = psutil.swap_memory()
        """ Percent uses swap: (int(swap.used / 1024)*100%) / (int(swap.total / 1024) """
        perUsSw = ((int(swap.used / 1024)*100) / (int(swap.total / 1024)));
        print "................................................................"
        print " SWAP Total:                   | " + str(int(swap.total / 1024 / 1024)) + " M"
        print " SWAP Used:                    | " + str(int(swap.used / 1024 /1024)) + " M" + "    Percent value " + str(perUsSw) + "%"
        print " SWAP Free:                    | " + str(int(swap.free / 1024)) + " K"
        if perUsSw  >= 30 and perUsSw < 50:
                print "..Warning Utilization SWAP is between 10% and 50% Current value is "+ str(perUsSw) + ".."
        if perUsSw >= 50:
                print "..........Critical Utilization SWAP is more then 50%.........."
                print ".................. Current uses SWAP: " +str(perUsSw)+"%"+ ".....................\n\n"
                print ".................. Critical, please take care. .................";
        if perUsSw >=0 and perUsSw < 10:
                print ".................. Current uses SWAP: " +str(perUsSw)+"%"+ "..................."
                print " Utilization SWAP status is OK.";
        print "................................................................\n\n"
def util_CPU():
        print " .3. Utilization CPU:         ..."
        print "................................................................"
        print " Number of CPUs:               | " +str(psutil.cpu_count())
        print " Number of Physical CPUs:      | " +str(psutil.cpu_count(logical=False))
        print "................................................................\n\n"
        #print "Total space swap :      | " + str(int(swap.free / 1024))

def util_Dsik():
        print " .4. Utilization disk space:   ..."
        print "................................................................"
        io = psutil.disk_partitions()
        for i in str(io).split(", "):
                if "mountpoint" in i:
                        y = ((str((str(i).split("='"))[1]).split("'"))[0]); #print y
                        #print (str((str(i).split("='"))[1]).split("'"))[0]
                        #print (psutil.disk_usage((str((str(i).split("='"))[1]).split("'"))[0]))
                        #print "disk_used: ",round((disk.used / 1024 / 1024 / float(1024)),2) # get info about used space od disk
                        #print psutil.disk_usage((str((str(i).split("='"))[1]).split("'"))[0])
                        for li in [y]:
                                #print (li)
                                disk = psutil.disk_usage(li);
                                print "Total partition size (GB):  "+li+"     | ",round((disk.total / 1024 / 1024 / float(1024)),2),"GB"
                                useSizePer =  round(((round((disk.used / 1024 / 1024 / float(1024)),2))*100 / round((disk.total / 1024 / 1024 / float(1024)),2)),2)
                                #print "disk----",disk #get general info, out type is class
                                print "Used  partition size (GB):  "+li+"     | ",round((disk.used / 1024 / 1024 / float(1024)),2),"GB" # get info about used space od disk
                                if useSizePer > 80 and useSizePer < 90:
                                        print "Warning. Utilization memory is between 80% and 90% Current value is "+ str(useSizePer) + "%"
                                if useSizePer >= 90:
                                     print ".......Critical. Current uses memory: " +str(useSizePer)+"%"+ "............\n";
                                if useSizePer < 80:
                                     print " Utilization memory status is OK.",str(useSizePer)+"%"
                                print("................................................................\n\n")

        #print "................................................................\n\n"
"""
print "\n\nsep. check.\n"

disk = psutil.disk_usage('/'); print "disk----",disk #get general info, out type is class
print "disk_used: ",round((disk.used / 1024 / 1024 / float(1024)),2) # get info about used space od disk
print "disk_free: ",round((disk.free / 1024 / 1024 / float(1024)),2) # get info about free space of disk
disk_percent_used = disk.percent; print "disk_percent_used:",str(disk_percent_used)+"%" # get info % free sace of disk
"""


"""
- psutil.disk_partitions()
- psutil.net_connections()
- psutil.users()
- psutil.Process.open_files() (it turned out this is not reliable on
Windows and FreeBSD)
- psutil.Process.connections()
- psutil.Process.memory_percent() ('cause it's a very simple utility method)
"""
</pre>
