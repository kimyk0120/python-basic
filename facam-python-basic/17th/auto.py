from my_email import Email
import my_news
# from my_news import News
from my_excel import Excel
from my_email import TestPrint

m_email = Email()
m_news = my_news.News()
m_excel = Excel()

test = TestPrint()
test.testPrint()

news_lise = m_news.find_news("test1")

m_email.from_email = "test@test.com"
m_email.to_email = "test1@test1.com"
m_email.subject = "test1@test1.com"
m_email.contents = "contentess"

for news in news_lise:
    m_email.contents = m_email.contents + news + "\n"


m_email.send_email()

m_excel.excel_file = "test.xlsx"
m_excel.save_to_excel(news_lise)
