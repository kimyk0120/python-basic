from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

f = open("../../user.properties",'r')
user_id = f.readline().strip()
user_pwd = f.readline().strip()
# print("user_id : " + user_id)
# print("user_pwd : " + user_pwd)

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465
SMTP_USER = user_id
SMTP_PASSWORD = user_pwd


def send_mail(name, addr, subject , contents):
        msg = MIMEMultipart('alternative')

        msg['From'] = SMTP_USER
        msg['To'] = addr
        msg['Subject'] = name + '님,' + subject

