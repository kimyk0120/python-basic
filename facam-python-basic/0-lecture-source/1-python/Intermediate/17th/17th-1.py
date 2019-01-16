from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from myid import ID, PW
import time

driver = webdriver.Chrome('./chromedriver')

try:
    driver.get('https://instagram.com')

    elem = driver.find_element_by_link_text('로그인')
    elem.click()

    time.sleep(1)

    elem = driver.find_element_by_name('username')
    elem.send_keys(ID)
    elem = driver.find_element_by_name('password')
    elem.send_keys(PW)
    elem.send_keys(Keys.RETURN)

    time.sleep(2)

    elem = driver.find_element_by_xpath("//span[text()='검색']/..")
    ac = ActionChains(driver)
    ac.move_to_element(elem)
    ac.click()
    ac.key_down('#패스트캠퍼스')
    ac.perform()

    time.sleep(2)

    ac.reset_actions()
    ac.move_by_offset(0, 50)
    ac.click()
    ac.perform()

    time.sleep(2)

    divs = driver.find_elements_by_xpath("//*[text()='인기 게시물']/../..//a[contains(@href, '?tagged=패스트캠퍼스')]/..")
    ac = ActionChains(driver)

    for div in divs:
        ac.reset_actions()
        ac.move_to_element(div)
        ac.click()
        ac.perform()

        time.sleep(1)

        ac.reset_actions()
        elem = driver.find_element_by_xpath("//*[contains(@aria-label,'좋아요')]")
        ac.move_to_element(elem)
        ac.click()
        ac.perform()

        ac.reset_actions()
        ac.send_keys(Keys.ESCAPE)
        ac.perform()

        time.sleep(1)

    input()
except Exception as e:
    print(e)
finally:
    driver.quit()
