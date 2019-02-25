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

    def test_test(self):
        print("test")


class TestPrint:
    def __init__(self):
        pass

    def testPrint(self):
        print("test")
