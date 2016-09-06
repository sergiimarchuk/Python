<pre>
#!/opt/python27/bin/python
import psutil
import time
import datetime
import json
import logging

#Comm: Date stamp
stamp_now = datetime.datetime.now()

# -- Section memory
percentUsed = psutil.virtual_memory().percent
def memory_usage_retturn():
        """ Check Usage memory """
        virt = psutil.virtual_memory()

        total_threshold1= int(virt.total / 1024 / 1024)

        if percentUsed > 80 and percentUsed < 90:
                return "Status Warning. Memory usage beetween 80% and 90%. Total memory " + str(total_threshold1) + " Mb. " + "Current Usage Memory is "  + str(percentUsed) + "%"
        if percentUsed >= 90:
                return "Status Crtitacal. Memory usage more then 90%. Total memory " + str(total_threshold1) + " Mb. " + "Current Usage Memory is "  + str(percentUsed) + "%"
        if percentUsed < 80:
                return "Status Ok. Memory usage on server looks good. Less 80%. Total memory " + str(total_threshold1) + " Mb. " + "Current Usage Memory is "  + str(percentUsed) + "%"

#Comm: String for logging into file
mem_u = str(stamp_now) + " .:SECTION MEMORY:. " +memory_usage_retturn()
with open ('localhost-5656', 'a') as f: f.write (mem_u + '\n')

# -- Section SWAP
def util_swap():
        """ Percent uses swap: (int(swap.used / 1024)*100%) / (int(swap.total / 1024) """
        swap = psutil.swap_memory()
        perUsSw = ((int(swap.used / 1024)*100) / (int(swap.total / 1024)));
        SWAP_Total = "Swap Total " + str(int(swap.total / 1024 / 1024)) + " Mb."
        SWAP_Used = " SWAP Used " + str(int(swap.used / 1024 /1024)) + " Mb." + " Percent value " + str(perUsSw) + "%"

        #Comm: Common variable SWAP include genaral info about this.
        #print " SWAP Free:                    | " + str(int(swap.free / 1024)) + " K"
        if perUsSw  >= 30 and perUsSw < 50:
                return "Status Warning. Utilization SWAP is between 10% and 50%. " + "Current value is "+ str(perUsSw) + "%"
        if perUsSw >= 50:
                return "Status Critical. Utilization SWAP is more then 50% " + "Current uses SWAP: " +str(perUsSw)+"%"
                #print ".................. Current uses SWAP: " +str(perUsSw)+"%"+ ".....................\n\n"
                #print ".................. Critical, please take care. .................";
        if perUsSw >=0 and perUsSw < 10:
                #print ".................. Current uses SWAP: " +str(perUsSw)+"%"+ "..................."
                return "Status Ok. Utilization SWAP status is OK. " + SWAP_Total + " Current uses SWAP: " +str(perUsSw)+"%"
                
util_swap_u = str(stamp_now) + " .:SECTION SWAP:. " + util_swap()
with open ('localhost-5656', 'a') as f: f.write (util_swap_u + '\n')

# -- Section CPU
def util_cpu():
        """ Utilization CPU. But weird i got bugs during counting cpu phisical / logical. """
        Number_of_CPUs = str(psutil.cpu_count())
        Number_of_Physical_CPUs = str(psutil.cpu_count(logical=False))
        iu = psutil.cpu_percent(interval=1, percpu=True)
        lenght = len(iu)
        c = 0; m = []
        while c <= lenght:
                for cn in iu:
                        if cn >= 90:
                                #return "Status Critical. Uusage CPU count" + str(c) + str(cn) + "%"
                                status  = "Status Critical. Core " + str(c) + " Util CPU " + str(cn) + "%"
                                m.append(status)
                        if cn >= 75 and cn <90:
                                #return "Status Warning. Usage CPU count" + str(c) + str(cn) + "%"
                                status  = "Status Warning. Core " + str(c) + " Util CPU " + str(cn) + "%"
                                m.append(status)
                        if cn < 75:
                                #return "Status OK. Utilization is OK","Kernel count :" + str(c)
                                status  = "Status OK. Core " + str(c) + " Util CPU " + str(cn) + "%"
                                m.append(status)
                        c = c + 1
                rs = (str(m).replace("[","")).replace("]","").replace("'","")
                #print (rs)
                return (rs)

util_cpu_u = str(stamp_now) + " .:SECTION CPU:. " + str(util_cpu())
with open ('localhost-5656', 'a') as f: f.write (util_cpu_u + '\n')

# -- Section Utilization disk space
def util_disk():
        """  Utilization disk space """
        io = psutil.disk_partitions()
        c_mountp = 0
        counter = 0
        sta = []
        for i in str(io).split(", "):
                if "mountpoint" in i:
                        y = ((str((str(i).split("='"))[1]).split("'"))[0]);
                        #print "MOUNTPOINT)",y
                        c_mountp = c_mountp + 1
                        #print c_mountp
                        while counter < c_mountp:
                                for li in [y]:
                                        disk = psutil.disk_usage(li);
                                        #print "Total partition size (GB):  "+li+"     | ",round((disk.total / 1024 / 1024 / float(1024)),2),"GB"
                                        useSizePer =  round(((round((disk.used / 1024 / 1024 / float(1024)),2))*100 / round((disk.total / 1024 / 1024 / float(1024)),2)),2)
                                        #print "Used  partition size (GB):  "+li+"     | ",round((disk.used / 1024 / 1024 / float(1024)),2),"GB"
                                        if useSizePer > 80 and useSizePer < 90:
                                                status  = "Status Warning." + " Part. " + li  + " Utilization memory is between 80% and 90% Current value is "+ str(useSizePer) + "%"
                                                sta.append(status)
                                        if useSizePer >= 90:
                                                status =  "Status Critical." + " Part. "+ li + " Current uses memory: " +str(useSizePer)+"%"+ "............\n";
                                                sta.append(status)
                                        if useSizePer < 80:
                                                status = "Status Ok." + " Part. " + li + " Utilization memory status is OK.",str(useSizePer)+"%"

                                                sta.append(status)
                                        counter = counter + 1
        res = (str(sta).replace("[","")).replace("]","").replace("'","").replace("(","").replace(")","")
        return res

util_disk_u = str(stamp_now) + " .:SECTION DISKS:. " + util_disk()
with open ('localhost-5656', 'a') as f: f.write (util_disk_u + '\n')

# -- Section Network
def util_network_nic():
        " ... Utilization networking NIC:   ..."
        nnic = psutil.net_if_addrs()
        nlist =list(nnic)
        i = 0
        for itemn in nlist:
                ninfo = nnic.get(itemn)
                for niccont in ninfo:
                        gen_net_info = str(itemn) + " " + str(niccont)
                        print itemn,niccont
        nco = psutil.net_io_counters(pernic=True)
        colist = list(nco)
        for itemco in nco:
                cod = nco.get(itemco)
                ncont = (str(cod)).split(",")
                #print itemco, itemn
                """for el in ncont:
                        if 'errin' in el:
                                if int(((el).split("="))[1]) >= 0:
                                        status_in = "Issue on NIC: " + itemco + ": " + el
                                        netsta_in.append(status_in)
                                        #print  "Issue",itemco, el
                        if 'errout' in el:
                                if int(((el).split("="))[1]) >= 0:
                                        status_out = "Issue on NIC: " + itemco + ": " + el
                                        netsta_out.append(status_out)
                                        #print  "Issue",itemco, el
                                status = str(status_in) + " " + str(status_out)
                        #print n_i_c; print"""
util_network_nic()

def util_network_issue():
        " ... Utilization networking issue:   ..."
        nnic = psutil.net_if_addrs()
        nlist =list(nnic)
        i = 0
        netsta_in = []
        netsta_out = []
        netsta = []
        for itemn in nlist:
                ninfo = nnic.get(itemn)
                for niccont in ninfo:
                        gen_net_info = str(itemn) + " " + str(niccont)
        nco = psutil.net_io_counters(pernic=True)
        colist = list(nco)
        for itemco in nco:
                cod = nco.get(itemco)
                ncont = (str(cod)).split(",")
                for el in ncont:
                        if 'errin' in el:
                                if int(((el).split("="))[1]) > 0:
                                        status_in = "Issue on NIC: " + itemco + ": " + el
                                        netsta_in.append(status_in)
                                elif int(((el).split("="))[1]) == 0:
                                        status_in = "Status OK. NIC for input. NIC: " + itemco
                                        netsta_out.append(status_in)
                        if 'errout' in el:
                                if int(((el).split("="))[1]) > 0:
                                        status_out = "Issue on NIC: " + itemco + ": " + el
                                        netsta_out.append(status_out)
                                elif int(((el).split("="))[1]) == 0:
                                        status_out  = "Status OK. NIC for output. NIC: " + itemco
                                        netsta_out.append(status_out)
        status = str(status_in) + " " + str(status_out)
        result = str(netsta_in) + " " + str(netsta_out)
        res =  (result).replace("[","").replace("]","").replace("'","")
        return res
util_network_issue_u = str(stamp_now) + " .:SECTION NETWORK ISSUE :. " + util_network_issue()
with open ('localhost-5656', 'a') as f: f.write (util_network_issue_u + '\n')


</pre>
</pre>
