

<pre>
#!/usr/bin/python
import os.path

file_log_name = "/opt/python/checklog.log"

val_exists_file =  os.path.exists("/opt/python/teste")

def check_exists_log(get_val_exists_file):
        if val_exists_file == True:
                return "1"
        else:
                return "2"

print check_exists_log(val_exists_file)

def update_log(get_val_exists_file):
        if val_exists_file == True:
                with open (file_log_name, 'a') as f: f.write (check_exists_log(val_exists_file) + '\n')
        else:
                with open (file_log_name, 'w') as f: f.write (check_exists_log(val_exists_file) + '\n')


update_log(val_exists_file)

</pre>
