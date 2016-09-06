#!/opt/python27/bin/python
import psutil
import time
import datetime
import json
import logging
import socket

#Comm: FQDN
fqdn_srv = "FQDN Server: " +  socket.getfqdn() + ":"
print fqdn_srv


#Comm: Date stamp 
stamp_now = datetime.datetime.now()

# -- Section memory 
percentUsed = psutil.virtual_memory().percent
def memory_usage_status():
        """ Check Usage memory """
        virt = psutil.virtual_memory()

        total_threshold1= int(virt.total / 1024 / 1024)

        if percentUsed > 80 and percentUsed < 90:
		return "Status Warning."
        if percentUsed >= 90:
		return "Status Crtitacal."
        if percentUsed < 80:
		return "Status Ok."

memory_usage_status_u = str(stamp_now)  + " " + fqdn_srv  + " .:SECTION MEMORY:. " +memory_usage_status()
with open ('localhost-5656', 'a') as f: f.write (memory_usage_status_u + '\n')


percentUsed = psutil.virtual_memory().percent
def memory_usage_collect():
        """ Check Usage memory """
        virt = psutil.virtual_memory()

        total_threshold1= int(virt.total / 1024 / 1024)

        return str(total_threshold1) + " Mb. " + "Current Usage Memory is "  + str(percentUsed) + "%"

memory_usage_collect_u = str(stamp_now)  + " " + fqdn_srv  + " .:COLLECT INFO MEMORY:. " + memory_usage_collect()
with open ('localhost-5656', 'a') as f: f.write (memory_usage_collect_u + '\n')


# -- Section SWAP
def util_swap_status():
        """ Percent uses swap: (int(swap.used / 1024)*100%) / (int(swap.total / 1024) """
        swap = psutil.swap_memory()
        perUsSw = ((int(swap.used / 1024)*100) / (int(swap.total / 1024)));
        SWAP_Total = "Swap Total " + str(int(swap.total / 1024 / 1024)) + " Mb."
        SWAP_Used = " SWAP Used " + str(int(swap.used / 1024 /1024)) + " Mb." + " Percent value " + str(perUsSw) + "%"
	
	#Comm: Common variable SWAP include genaral info about this. 
        #print " SWAP Free:                    | " + str(int(swap.free / 1024)) + " K"
        if perUsSw  >= 30 and perUsSw < 50:
                return "Status Warning."
        if perUsSw >= 50:
                return "Status Critical."
                #print ".................. Current uses SWAP: " +str(perUsSw)+"%"+ ".....................\n\n"
                #print ".................. Critical, please take care. .................";
        if perUsSw >=0 and perUsSw < 10:
                #print ".................. Current uses SWAP: " +str(perUsSw)+"%"+ "..................."
                return "Status Ok."

util_swap_status_u = str(stamp_now)  + " " + fqdn_srv  + " .:SECTION SWAP:. " + util_swap_status()
with open ('localhost-5656', 'a') as f: f.write (util_swap_status_u + '\n')

def util_swap_collect():
        """ Percent uses swap: (int(swap.used / 1024)*100%) / (int(swap.total / 1024) """
        swap = psutil.swap_memory()
        perUsSw = ((int(swap.used / 1024)*100) / (int(swap.total / 1024)));
        SWAP_Total = "Swap Total " + str(int(swap.total / 1024 / 1024)) + " Mb."
        SWAP_Used = " SWAP Used " + str(int(swap.used / 1024 /1024)) + " Mb." + " Percent value " + str(perUsSw) + "%"

        #Comm: Common variable SWAP include genaral info about this.
        #print " SWAP Free:                    | " + str(int(swap.free / 1024)) + " K"
                #print ".................. Current uses SWAP: " +str(perUsSw)+"%"+ ".....................\n\n"
                #print ".................. Critical, please take care. .................";
                #print ".................. Current uses SWAP: " +str(perUsSw)+"%"+ "..................."
        return (SWAP_Total + " Current uses SWAP: " + str(perUsSw)+"%")

util_swap_collect_u = str(stamp_now)  + " " + fqdn_srv  + " .:COLLECT INFO SWAP:. " + util_swap_collect()
with open ('localhost-5656', 'a') as f: f.write (util_swap_collect_u + '\n')



# -- Section CPU 
def util_cpu_status():
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
				status  = "Core " + str(c) + " Status Critical." #+ " Util CPU " + str(cn) + "%"
				m.append(status)
                	if cn >= 75 and cn <90:
                        	#return "Status Warning. Usage CPU count" + str(c) + str(cn) + "%"
				status  = "Core " + str(c) + " Status Warning."#+ " Util CPU " + str(cn) + "%"
				m.append(status)
                	if cn < 75:
                        	#return "Status OK. Utilization is OK","Kernel count :" + str(c)
				status  = " ::Core " + str(c) + ". Status OK.::" # + " Util CPU " + str(cn) + "%"
				m.append(status)
			c = c + 1
		rs = (str(m).replace("[","")).replace("]","").replace("'","").replace(",","")
		print (rs)
		return (rs)

util_cpu_status_u = str(stamp_now) + " " + fqdn_srv  + " .:SECTION CPU:. " + str(util_cpu_status())
with open ('localhost-5656', 'a') as f: f.write (util_cpu_status_u + '\n')


def util_cpu_collect():
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

util_cpu_collect_u = str(stamp_now) + " " + fqdn_srv  + " .:COLLECT INFO CPU:. " + str(util_cpu_collect())
with open ('localhost-5656', 'a') as f: f.write (util_cpu_collect_u + '\n')

# -- Section Utilization disk space
def util_disk_status():
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
        	              			status  = "Status Warning." + " Part. " + li + " Utilization memory is between 80% and 90% Current value is "+ str(useSizePer) + "%"
						sta.append(status)
                               		if useSizePer >= 90:
                               			status =  "Status Critical." + " Part. "+ li + " Current uses memory: " +str(useSizePer)+"%"+ "............\n";
						sta.append(status)
                               		if useSizePer < 80:
                               			status = "Status Ok." + " Part. " + li + " " + str(useSizePer)+"%"
						sta.append(status)
					counter = counter + 1
	res = (str(sta).replace("[","")).replace("]","").replace("'","").replace("(","").replace(")","")
	return res

util_disk_status_u = str(stamp_now) + " " + fqdn_srv  + " .:SECTION DISKS:. " + util_disk_status()
with open ('localhost-5656', 'a') as f: f.write (util_disk_status_u + '\n')

def util_disk_collect():
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
                                                status  = " Part. " + li  + " Current uses memory: " + str(useSizePer) + "%"
                                                sta.append(status)
                                        if useSizePer >= 90:
                                                status =  " Part. "+ li + " Current uses memory: " + str(useSizePer)+"%"+ "............\n";
                                                sta.append(status)
                                        if useSizePer < 80:
                                                status = " Part. " + li + " Current uses memory: " + str(useSizePer)+"%"

                                                sta.append(status)
                                        counter = counter + 1
        res = (str(sta).replace("[","")).replace("]","").replace("'","").replace("(","").replace(")","")
        return res

util_disk_collect_u = str(stamp_now) + " " + fqdn_srv  + " .:COLLECT INFO DISK:. " + util_disk_collect()
with open ('localhost-5656', 'a') as f: f.write (util_disk_collect_u + '\n')


# -- Section Network
def util_network_nic():
        " ... Utilization networking NIC:   ..."
        nnic = psutil.net_if_addrs()
        nlist =list(nnic)
        i = 0
	net_arr_nic = []
	net_arr_stat = []
	net_arr = []
        for itemn in nlist:
                ninfo = nnic.get(itemn)
                for niccont in ninfo:
			gen_net_info = str(itemn) + " " + str(niccont)
			g1 =  str(itemn)
			g2 = str((str(niccont).replace("snic(family=","").replace(", ptp=None)","")).split(", ")[1:3]).replace("\"]","").replace("[\"","").replace("\"","")
			g = "NIC: " + g1 + ": " + g2
			net_arr.append(g)			
#	res = str(net_arr).replace("[","").replace("]","").replace("\"",""); #print res	
	return " .:STAT NET_INFO:. " + str(net_arr)

util_network_nic_u = str(stamp_now) + " " + fqdn_srv  + util_network_nic()
with open ('localhost-5656', 'a') as f: f.write (util_network_nic_u + '\n')

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
util_network_issue_u = str(stamp_now) + " " + fqdn_srv  + " .:SECTION NETWORK:. " + util_network_issue()
with open ('localhost-5656', 'a') as f: f.write (util_network_issue_u + '\n')

# -- Section Boot Time

def boot_time_stat():
	" ... Boot time From ... "
	dati = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
	return dati 

boot_time_stat_u = str(stamp_now) + " " + fqdn_srv  + " .:SECTION BOOT:. Server UP from: " + boot_time_stat()
with open ('localhost-5656', 'a') as f: f.write (boot_time_stat_u + '\n')


# -- Section Users

def user_logged():
	u_logged = psutil.users()
	return str(u_logged)

user_logged_u = str(stamp_now) + " " + fqdn_srv  + " .:STAT USERS LOGGED:. " +  user_logged()
with open ('localhost-5656', 'a') as f: f.write (user_logged_u + '\n')



#2016.07.11 15:37
