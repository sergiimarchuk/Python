#!/opt/python27/bin/python

import glob
import os

a = glob.glob("*")

_pwd_ = os.getcwd()


#print "Mass:",a

"""for el in a:
        if "local" in el:
            pars_log(el)

"""

# function do parsing log file for Memory.
def pars_log(element):
        with open(os.getcwd() +  "/" + el, "rb") as log_f:
                for line in log_f:
                        if ".:SECTION MEMORY:." in line:
                                print line.split(" ")
                                fqdn_ = line.split(" ")[2]
                                hn_ = line.split(" ")[4]
                                memory_col_ = line.split(" ")[6]
                                status_ = line.split(" ")[7]
                                status_value_ = line.split(" ")[8]
                                print fqdn_
                                print hn_.replace(":","")
                                print memory_col_.replace(":.","")
                                print status_
                                print status_value_


#read files in current directory from where we run this script and as result we got list all files in this directory, tring to find file which containts file name with suf' or pref' 'local' and after all file we do transfer to 'function pars_log(file_name)'
for el in a:
        if "local" in el:
            pars_log(el)
            pars_log(el)


# function do parsing log file for Memory.
def pars_log():
        with open("/opt/python27/working-scripts/test-collection/localhost-5656.log", "rb") as log_f:
                for line in log_f:
                        if ".:SECTION MEMORY:." in line:
                                print line.split(" ")
                                fqdn_ = line.split(" ")[2]
                                hn_ = line.split(" ")[4]
                                memory_col_ = line.split(" ")[6]
                                status_ = line.split(" ")[7]
                                status_value_ = line.split(" ")[8]
                                print "    ###   Run Function Test Memory Pars"
                                print fqdn_
                                print hn_.replace(":","")
                                print memory_col_.replace(":.","")
                                print status_
                                print status_value_

pars_log()
