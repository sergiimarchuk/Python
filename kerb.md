
```python
#!/usr/bin/python
import datetime, time
import os, os.path
from datetime import datetime
from subprocess import Popen, PIPE

hostname = os.environ['HOSTNAME']

# define path for file which has contains logs
file_log_name = "/home/sergiimarchuk/checklog.log"
cmd_klist = "/usr/bin/klist"
cmd_kinit = "/usr/bin/kinit -kt /etc/krb5.keytab"
cmd_df_

# let's get infor about status kerb tickets etc..
def run_binary_command(system_command):
        cmd = system_command
        p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
        out, err = p.communicate()
        return out

# let's get info about exists file acording to variable file_log_name
val_exists_file =  os.path.exists(file_log_name)

# check log file and update it create new and write info into or update info into this file
def update_log(get_val_exists_file):
        if val_exists_file == True:
                with open (file_log_name, 'a') as f: f.write ("Checking was run at : " + str(datetime.now()) + '\n' + (run_binary_command(cmd_klist)) + '\n')
        else:
                with open (file_log_name, 'w') as f: f.write ("Checking was run at : " + str(datetime.now()) + '\n' + (run_binary_command(cmd_klist)) + '\n')

update_log(val_exists_file)

def get_date_expires_in_sec():
        # let's pars output function run_binary_command(system_command)
        output_run_binary_klist = run_binary_command(cmd_klist)

        exp_date_list = []
        # let's get value for pars exipre date
        for i in output_run_binary_klist.split('\n'):
                if "renew" in i:
                        exp_date_list.append(i)
        val = exp_date_list[0]
        # let's get values after parsing year month day hour and minutes seconds
        val_date = ((str(val).split(" "))[2]).split("/");
        val_time =((str(val).split(" "))[3].replace("'])","")).split("/");
        val_date_year = "20" + ((str(val).split(" "))[2]).split("/")[2];
        val_date_month = ((str(val).split(" "))[2]).split("/")[1];
        val_date_day = ((str(val).split(" "))[2]).split("/")[0];
        val_time_hour = ((str(val).split(" "))[3].replace("'])","")).split(":")[0];
        val_time_minute = (str(val).split(" "))[3].replace("'])","").split(":")[1];
        val_time_second = (str(val).split(" "))[3].replace("'])","").split(":")[2];
        # let's convert expire date into seconds
        until_ticket_in_second = datetime(int(val_date_year), int(val_date_month), int(val_date_day), int(val_time_hour), int(val_time_minute), int(val_time_second));
        val_until_ticket_in_second = int(until_ticket_in_second.strftime('%s'));
        return val_until_ticket_in_second
def curr_time_in_sec():
        now = datetime.now();
        now_year = str(now.year);
        now_month = str(now.month);
        now_day = str(now.day);
        now_hour = str(now.hour);
        now_minite = str(now.minute);
        now_second=str(now.second);
        # let's convers current time from now in seconds
        val_curr_time = datetime(int(now_year), int(now_month), int(now_day), int(now_hour), int(now_minite), int(now_second))
        val_curr_time_in_sec = int(val_curr_time.strftime('%s'))
        return val_curr_time_in_sec



print type(get_date_expires_in_sec())
print curr_time_in_sec()


def check_kerberos_ticket():
        if get_date_expires_in_sec() - curr_time_in_sec() <= 86400:
                return "we have to update kerberos ticket, expiration date so close."
        else:
                return "kerberos ticket looks good"



def  send_html_report(html):
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText
            import smtplib

            #me = hfqdn
            me = 'root@' + str(hostname) + '.local'
            you = ['sergii.marchuk@evry.com']

            msg = MIMEMultipart('alternative')
            msg['Subject'] = "Check kerberos ticket expires date. " + str(datetime.now())
            msg['From'] = me
            msg['To'] = ','.join(you)

            part2 = MIMEText(html, 'html')

            msg.attach(part2)

            s = smtplib.SMTP('smtp.cosng.net')
            s.sendmail(me, you, msg.as_string())
            s.quit()
            print(html)
html = ""

c = 0
html = html + "<table>"
html = html +   "<tr>"
html = html +     "<th colspan=\"6\">Ticket for kerberos ... "  + str(datetime.now()) + "</th>"
html = html +   "</tr>"
html = html +   "<tr>"
while c < 10:
        html = html +     "<td>No</td>"
        html = html +     "<td>" + (str(datetime.now()).split(".")[0]) + "</td>"
        html = html +     "<td>" + check_kerberos_ticket() + "</td>"
        html = html +     "<td>Adam</td>"
        html = html +     "<td>Robert</td>"
        html = html +     "<td>Paul</td>"
        html = html +   "</tr>"
        c = c + 1
n = 0
while n < 5:
        html = html +   "<tr>"
        html = html +     "<td>1</td>"
        html = html +     "<td>Swimming</td>"
        html = html +     "<td>1:30</td>"
        html = html +     "<td>2:05</td>"
        html = html +     "<td>1:15</td>"
        html = html +     "<td>1:41</td>"
        html = html +   "</tr>"
        n = n + 1
html = html + "</table>"

send_html_report(html);
