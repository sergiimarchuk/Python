#!/usr/bin/python

html=''

html=html + '<html><body>'
html=html + '<h1>Test</h1>'
html=html + '<font color="red"><h2>Test2</h1></font>'
html=html + '<br>'
html=html + '<br>'
html=html + 'dawefasdfasdfasdfasdfasdfasdfa<br>'
html=html + '111111111111111111111111111<br>'
html=html + '</body></html>'

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

me = "test@gmail.com" 
you = ['test1@gmail.com']

msg = MIMEMultipart('alternative')
msg['Subject'] = "My test email"
msg['From'] = me
msg['To'] = ','.join(you)

part2 = MIMEText(html, 'html')

msg.attach(part2)

s = smtplib.SMTP('127.0.0.1')
s.sendmail(me, you, msg.as_string())
s.quit()
