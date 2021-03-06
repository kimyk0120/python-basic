from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')

try:
    driver.get('https://www.fastcampus.co.kr/category_dev_camp/')

    courses = driver.find_elements_by_class_name('course')
    for course in courses:
        name = course.find_element_by_tag_name('strong')
        print(name.text.replace('\n', ''))
        print('-'*10)

except Exception as e:
    print(e)
finally:
    driver.quit()
