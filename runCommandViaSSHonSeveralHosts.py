#!/usr/bin/python
import subprocess, sys, datetime, time, csv
#Get current date and time
def get_datetime():
        localtime = time.localtime(time.time())
        datetime = str(localtime[0]) + """-""" + str(localtime[1]) + """_"""  + str(localtime[2]) + '-'  + str(localtime[3]) + '-' + str(localtime[4])
        return(datetime)
#Create new log file according current date and time
def log_namefileCSV():
        filename = '/tmp/python/logname'+get_datetime()+'.csv'
        return(filename)
def log_namefile():
        filename = '/tmp/python/logname'+get_datetime()+'.log'
        return(filename)
#Add info into log file
def collect_data_into_CSV_logfile(info_outcsv):
        ofile = csv.writer(open(log_namefileCSV(),'a'))
        ofile.writerow([info_outcsv])
def collect_data_into_logfile(info_out):
        ofile = open(log_namefile(),'a')
        ofile.write(str(info_out))
        ofile.close()
#Connecting to servers via ssh and run command
def ssh_command(hostname,mycommand):
        ssh = subprocess.Popen(["ssh", hostname, mycommand ], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = ssh.stdout.readlines()
        return(result)
def dictionarycommand(dcommand,get_call_f_ssh_command):
    info_data1 ='[\''+ (diclista1.get(dcommand))+'\\n\']' +' '+ str(get_call_f_ssh_command)
    return(info_data1)
#Main part because
def commandlist(hostlist,commandlist):
   for hlist in hostlist:
        counter = 0
        for clist in commandlist:
           call_f_ssh_command = ssh_command(hlist,clist)
           counter = counter + 1
           inf1 = dictionarycommand(clist,call_f_ssh_command)
           collect_data_into_CSV_logfile((inf1))


diclista1 = {'hostname':'Hostname is ','uptime':'Uptime is ','uname -r':'Uname is ','who':'Users are on system ','last':'Last users were connections '}
lista1 = ['hostname','uptime','uname -r','who','last']
hostl = ['localhost','localhost']


testcommand = commandlist(hostl,lista1)
