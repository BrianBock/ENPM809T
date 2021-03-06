import os
from datetime import datetime
import smtplib
from smtplib import SMTP
from smtplib import SMTPException
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Define Time stamp and record an image
pic_time = datetime.now().strftime('%Y%m%d%H%M%S')
command = 'sudo raspistill -vf -hf -o '+ pic_time +'.jpg'
os.system(command)

# Email info
smtpUser ='team3.14809t@gmail.com'
smtpPass ='R@spbian'

#destination Info
toAdd = ['mitchels@umd.edu','skotasai@umd.edu','bbock@umd.edu','yashsavle@gmail.com']
fromAdd = smtpUser
subject = 'Team 3.14 Assignment 7'
msg = MIMEMultipart()
msg['Subject']= subject
msg['From']= fromAdd
#msg['To']= toAdd
msg['To']=",".join(toAdd)
msg.preamble= "Assignment 7"

# Email Text
body = MIMEText("Homework Submission for Brian Bock, Yash Savle")
msg.attach(body)

# Attach image
fp = open(pic_time + '.jpg','rb')
img = MIMEImage(fp.read())
fp.close()
msg.attach(img)

# send email
s = smtplib.SMTP('smtp.gmail.com',587 )

s.ehlo()
s.starttls()
s.ehlo()

s.login(smtpUser, smtpPass)
s.sendmail(fromAdd, toAdd, msg.as_string())

print("Email Sent")
