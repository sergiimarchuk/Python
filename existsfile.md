

<pre>
#!/usr/bin/python
import os.path

val_exists_file =  os.path.exists("/opt/python/teste")

def check_exists_log(get_val_exists_file):
	if val_exists_file == True:
		return "1"
	else:
		return "2"

print check_exists_log(val_exists_file)
</pre>
