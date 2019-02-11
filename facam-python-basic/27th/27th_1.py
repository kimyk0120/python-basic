from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465
SMTP_USER = "userEmail"
SMTP_PASSWORD = "userPW"


def send_mail(name, addr, subject , contents):
        msg = MIMEMultipart('alternative')

        msg['From'] = SMTP_USER
        msg['To'] = addr
        msg['Subject'] = name + '님,' + subject

