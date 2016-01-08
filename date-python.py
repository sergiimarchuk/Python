
<pre>
>>> import subprocess, sys, datetime, time, csv
>>> #Get current date and time
... def get_datetime():
...         localtime = time.localtime(time.time())
...         datetime = str(localtime[0]) + """-""" + str(localtime[1]) + """_"""  + str(localtime[2]) + '-'  + str(localtime[3]) + '-' + str(localtime[4])
...         return(datetime)
...
>>>
>>> get_datetime()
'2016-1_8-16-18'


</pre>
