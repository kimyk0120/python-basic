from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome("./chromedriver")

try:
    driver.get("http://cafe.naver.com/joonggonara")

    elem = driver.find_element_by_id("topLayerQueryInput")

    elem.send_keys("아이폰")
    elem.send_keys(Keys.RETURN)

    time.sleep(1)

    # elem = driver.find_element_by_class_name("result-board") # iframe 영역일 시 바로 접근이 되지 않는다.
    iframe = driver.find_element_by_id("cafe_main")
    driver.switch_to.frame(iframe)

    # css 셀렉터 이용시 class 기중으로는 처음 css class 만 선택되어짐
    elem = driver.find_element_by_xpath("//div[@id='upperArticleList']/"
                                        "following-sibling::div[contains(@class,'article-board ')]")

    aEls = elem.find_elements_by_xpath("./table/tbody/tr//a[@class='article']")

    for idx, a in enumerate(aEls):
        print(idx, a.text)

    input()
except Exception as e:
    print(e)
finally:
    driver.quit()

