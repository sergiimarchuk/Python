````python
#!/usr/bin/python
import subprocess
print "test"
for i in range(1,255,1):
	print i	
	args = ("/bin/ping", "-c", "3", "192.168.1." + str(i))
	popen = subprocess.Popen(args, stdout=subprocess.PIPE)
	popen.wait()
	output = popen.stdout.read()
	#print output
	if "Unreachable" not in output:
		print output
