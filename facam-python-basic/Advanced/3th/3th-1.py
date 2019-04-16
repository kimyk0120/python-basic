from selenium import webdriver


f = open("product.txt", 'r')

products = f.readlines() # 행 단위로 끊어서 list 형으로 반환

# print(products)

driver = webdriver.Chrome("chromedriver")

try:

    for idx, url in enumerate(products):
        print(url)
        url = url.strip()
        driver.get(url)

        elem = driver.find_element_by_class_name("heading")
        elem = elem.find_element_by_tag_name("h2")
        name = elem.text
        print("name : ", name)

        elem = driver.find_element_by_class_name("prdc_default_info")
        price = elem.find_element_by_class_name("sale_price")
        print("price : ", price.text)
        break


except Exception as e:
    print(e)
finally:
    driver.quit()

