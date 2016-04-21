<pre>
>>> import psutil, datetime
>>> psutil.boot_time()
1460972250.0
>>> datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
'2016-04-18 12:37:30'
>>>

</pre>
