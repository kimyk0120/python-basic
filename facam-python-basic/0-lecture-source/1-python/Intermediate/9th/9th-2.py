from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')

try:
    driver.get('http://news.naver.com')

    elem = driver.find_element_by_id('right.ranking_contents')

    lis = elem.find_elements_by_tag_name('li')

    for li in lis:
        atag = li.find_element_by_tag_name('a')
        print(atag.text)

    input()
except Exception as e:
    print(e)
finally:
    driver.quit()