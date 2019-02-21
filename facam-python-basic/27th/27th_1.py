'''
    메일 전송과 파일 첨부

'''

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import re

f = open("../../user.properties",'r')
user_id = f.readline().strip()
user_pwd = f.readline().strip()
# print("user_id : " + user_id)
# print("user_pwd : " + user_pwd)

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465
SMTP_USER = user_id
SMTP_PASSWORD = user_pwd


def send_mail(name, addr, subject, contents, attachment=None):
    if not re.match("(^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", addr):
        print("Wrong Mail Format")
        return

    msg = MIMEMultipart('alternative')
    if attachment:
        msg = MIMEMultipart("mixed")

    msg['From'] = SMTP_USER
    msg['To'] = addr
    msg['Subject'] = name + '님,' + subject

    text = MIMEText(contents, _charset='utf-8')
    msg.attach(text)

    if attachment:
        from email.mime.base import MIMEBase
        from email import encoders

        file_data = MIMEBase('application', 'octect-stream')
        file_data.set_payload(open(attachment,'rb').read()) # read() : 전체내용 가져오기
        encoders.encode_base64(file_data)

        import os
        filename = os.path.basename(attachment)
        file_data.add_header('Content-Disposition', 'attachment; filename="'+filename+'"')
        msg.attach(file_data)

    smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    smtp.login(SMTP_USER, SMTP_PASSWORD)
    smtp.sendmail(SMTP_USER, addr, msg.as_string())
    smtp.close()


if __name__ == "__main__":
    contens = '''
            자동화로 보내지는 메일입니다. 
            이이이이이이ㅣ이
            싸사사사
    '''
    send_mail("김영광","kimyk0120@gmail.com","자동화 메일입니다.", contens, 'test.txt')
