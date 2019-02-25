class Email:
    def __init__(self):
        self.from_email = ""
        self.to_email = ""
        self.subject = ""
        self.contents = ""

    def send_email(self):
        print("from_email : " + self.from_email)
        print("to_email : " + self.to_email)
        print("subject : " + self.subject)
        print("contents : " + self.contents)


# print(__name__) # 내장변수 . 파일 직접실행시 __ main__
if __name__ == '__main__':
    e = Email()
    e.contents = "testest"
    e.send_email()



