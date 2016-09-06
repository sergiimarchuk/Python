<pre>
#!/opt/python27/bin/python
import psutil
a = psutil.pids()
for i in a:
        p = psutil.Process(i)
        if 'init' in str(p):
                print "Process Number ",i
</pre>
