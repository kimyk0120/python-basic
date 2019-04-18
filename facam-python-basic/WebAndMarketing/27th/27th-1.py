from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials


# selenium 크롬 headless 옵션
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
# 혹은 options.add_argument("--disable-gpu")

# driver = webdriver.Chrome("./chromedriver")
driver = webdriver.Chrome('./chromedriver', options=options)

try:
    driver.get("http://cafe.naver.com/joonggonara")

    elem = driver.find_element_by_id("topLayerQueryInput")

    elem.send_keys("아이폰")
    elem.send_keys(Keys.RETURN)

    time.sleep(1)

    # page 하단의  불필요한  부분 닫기
    elem = driver.find_element_by_xpath("//button[@class='Flash_det_close']")
    elem.click()

    # elem = driver.find_element_by_class_name("result-board") # iframe 영역일 시 바로 접근이 되지 않는다.
    iframe = driver.find_element_by_id("cafe_main")
    driver.switch_to.frame(iframe)

    scope = ['https://www.googleapis.com/auth/drive', 'https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name("facamOnline-8a69e42a656e.json", scope)
    gs = gspread.authorize(credentials)
    doc = gs.create('selenium test')
    ws = doc.get_worksheet(0)

    current_page = 1
    while True:
        # css 셀렉터 이용시 class 기중으로는 처음 css class 만 선택되어짐
        elem = driver.find_element_by_xpath("//div[@id='upperArticleList']/"
                                            "following-sibling::div[contains(@class,'article-board ')]")
        # 게시글 내용 list
        aEls = elem.find_elements_by_xpath("./table/tbody/tr//a[@class='article']") # xpath - ./ 은 현재 위치를 나타냄
        for idx, a in enumerate(aEls):
            print(idx, a.text)
            ws.append_row([a.text])

        current_page += 1

        # page 이동
        page = driver.find_element_by_link_text(str(current_page))
        page.click()

        time.sleep(1)

        if current_page >= 5:
            break

    doc.share('kimyk0120@gmail.com', perm_type='user', role='owner')

    # input()
except Exception as e:
    print(e)
finally:
    driver.quit()

