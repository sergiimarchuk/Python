#!/opt/python27/bin/python
from collections import Counter
import glob
import os

#Current directory path
_pwd_ = os.getcwd()

#Read all files with .ext in current directory
a = glob.glob("*")

# function do parsing log file for Memory. 
def pars_log_mem(log_name):
	""" Parsing Memory log """
	print "MEMORY STATUS."
	with open(_pwd_ +  "/" + el, "rb") as log_f:
		for line in log_f:
			if ".:SECTION MEMORY:." in line:
				print line.split(" ")
                                date_ = line.split(" ")[0]
                                time_ = line.split(" ")[1]
                                fqdn_ = line.split(" ")[2]
                                hn_ = line.split(" ")[4]
                                memory_col_ = line.split(" ")[6]
                                status_ = line.split(" ")[7]
                                status_value_ = line.split(" ")[8]
                                print date_
                                print time_
                                print fqdn_
                                print hn_.replace(":","")
                                print memory_col_.replace(":.","")
                                print status_
                                print status_value_
                                #print date_ + " " + time_ +  " " + fqdn_ + " " + hn_.replace(":","") + " " + memory_col_.replace(":.","") + " " + status_ + " " +  status_value_
	
# function do parsing log file for SWAP.
def pars_log_swap(log_name):
        """ Parsing SWAP log """
        print "SWAP STATUS"
        with open(_pwd_ +  "/" + el, "rb") as log_f:
                for line in log_f:
                        if ".:SECTION SWAP:." in line:
                                print line.split(" ")
                                date_ = line.split(" ")[0]
                                time_ = line.split(" ")[1]
                                fqdn_ = line.split(" ")[2]
                                hn_ = line.split(" ")[4]
                                swap_ = line.split(" ")[6]
                                status_ = line.split(" ")[7]
                                status_value_ = line.split(" ")[8]
                                #print "    ###   Run Function Test SWAP Pars"
                                print date_
                                print time_
                                print fqdn_
                                print hn_.replace(":","")
                                print swap_.replace(":.","")
                                print status_
                                print status_value_
                                #print date_ + " " + time_ +  " " + fqdn_ + " " + hn_.replace(":","") + " " + memory_col_.replace(":.","") + " " + status_ + " " +  status_value_


def pars_log_cpu(log_name):
        """ Parsing CPU log """
        print "...............................CPU STATUS"
        with open(_pwd_ +  "/" + el, "rb") as log_f:
                c = 0
                for line in log_f:
                        if ".:SECTION CPU:." in line:
                                #print line.split(" ")
                                date_ = line.split(" ")[0]
                                time_ = line.split(" ")[1]
                                fqdn_ = line.split(" ")[2]
                                hn_ = line.split(" ")[4]

                                core_arr= (str((str(str((line).split(" ")[7:])).replace("[","").replace("]","").replace("'","").replace(",","").replace("\\n","")).split("::")).replace("[","").replace("]","").replace(" ","").replace("''","").replace(",","")).split("''")
                                #print (core_arr)
                                for yi in (core_arr):
                                        c = c + 1
                                        #var = "var1" + str(c)
                                        var  =  (yi).replace("'","")
                                        print str(date_) + " " + str(time_) + " " + str(fqdn_) + " " + str(hn_) + " " + var

###
def pars_log_disk(log_name):
        """ Parsing Partition log """
        print "...............................Partition STATUS"
        with open(_pwd_ +  "/" + el, "rb") as log_f:
                c = 0
                for line in log_f:
                        if ".:SECTION DISKS:." in line:
                                #print line.split(" ")
                                part = str(line.split(" ")[7:]).split(",', ")

                                date_ = line.split(" ")[0]
                                time_ = line.split(" ")[1]
                                fqdn_ = line.split(" ")[2]
                                hn_ = line.split(" ")[4]

                                #print part
                                for p in part:
                                        #print (p.replace("[","").replace("]","").replace("'","").replace("\\n","")).split()
                                        status_ = ((p.replace("[","").replace("]","").replace("'","").replace("\\n","")).split()[0]).replace(",","")
                                        status_val_ = ((p.replace("[","").replace("]","").replace("'","").replace("\\n","")).split()[1]).replace(",","")
                                        part_ = ((p.replace("[","").replace("]","").replace("'","").replace("\\n","")).split()[2]).replace(",","")
                                        part_name_ = ((p.replace("[","").replace("]","").replace("'","").replace("\\n","")).split()[3]).replace(",","")
                                        print status_
                                        print status_val_
                                        print part_
                                        print part_name_
                                        inf_mess_= status_ + " " + status_val_ + " " + part_ + " " + part_name_
                                        print str(date_) + " " + str(time_) + " " + str(fqdn_) + " " + str(hn_) + " " + inf_mess_

###
#read files in current directory from where we run this script and as result we got list all files in this directory, tring to find file which containts file name with suf' or pref' 'local' and after all file we do transfer to 'function pars_log(file_name)'
for el in a:
        if "local" in el:
	    print ""
	    print "......................................................................................................................................... File name :",el
            pars_log_mem(el)
	    pars_log_swap(el)
	    pars_log_cpu(el)
	    pars_log_disk(el)
# function do parsing log file for Memory.
def pars_log():
	""" Parsing Partition log """
	#print "...............................Partition STATUS"
        with open("localhost-5656", "rb") as log_f:
		c = 0
                for line in log_f:
                        if ".:SECTION DISKS:." in line:
				#print line.split(" ")
				part = str(line.split(" ")[7:]).split(",', ")
				
                                date_ = line.split(" ")[0]
                                time_ = line.split(" ")[1]
                                fqdn_ = line.split(" ")[2]
                                hn_ = line.split(" ")[4]

				#print part					
				for p in part:
					#print (p.replace("[","").replace("]","").replace("'","").replace("\\n","")).split()
					status_ = ((p.replace("[","").replace("]","").replace("'","").replace("\\n","")).split()[0]).replace(",","")
					status_val_ = ((p.replace("[","").replace("]","").replace("'","").replace("\\n","")).split()[1]).replace(",","")
					part_ = ((p.replace("[","").replace("]","").replace("'","").replace("\\n","")).split()[2]).replace(",","")
					part_name_ = ((p.replace("[","").replace("]","").replace("'","").replace("\\n","")).split()[3]).replace(",","")
					print status_
				 	print status_val_	
					print part_
					print part_name_	
					inf_mess_= status_ + " " + status_val_ + " " + part_ + " " + part_name_ 
					print str(date_) + " " + str(time_) + " " + str(fqdn_) + " " + str(hn_) + " " + inf_mess_
						
#pars_log()
#2016.07.11 15:34

#listMon.get(monthLic)
