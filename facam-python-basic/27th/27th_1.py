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

        text = MIMEText(contents, _charset='utf-8')
        msg.attach(text)
        # msg.attach(file)

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
        send_mail("김영광","kimyk0120@gmail.com","자동화 메일입니다.", contens)
