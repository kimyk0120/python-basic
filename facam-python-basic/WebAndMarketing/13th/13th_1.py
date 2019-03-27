'''
    chrome - 시크릿 모드를 사용
    분석 환경과 크롬드라이버의 접근환경을 동일시 하기 위함
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')

try:
    driver.get('https://naver.com')

    elem = driver.find_element_by_id('query')
    elem.send_keys('패스트캠퍼스')
    elem.send_keys(Keys.RETURN) # enter input

    elem = driver.find_element_by_class_name('_blogBase')
    lis = elem.find_elements_by_tag_name('li')

    for idx, li in enumerate(lis):  # index 출력을 위한 enumerate 내장 합수 사용
        # print(idx, li.text)
        a = li.find_element_by_class_name('sh_blog_title')
        # print(idx, a.text)
        print(idx, a.get_attribute('title'), "/ href : ", a.get_attribute('href'))

    # input()
except Exception as e:
    print(e)
finally:
    driver.quit()




