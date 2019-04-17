from selenium import webdriver
import datetime
import os

f = open("product.txt", 'r')

# output = open('output.csv', 'w')
output = open('output.csv', 'a')

products = f.readlines() # 행 단위로 끊어서 list 형으로 반환

# print(products)

driver = webdriver.Chrome("chromedriver")

try:
    header = ['']
    data = [str(datetime.datetime.now())]
    for idx, url in enumerate(products):
        print(url)
        url = url.strip()
        driver.get(url)

        elem = driver.find_element_by_class_name("heading")
        elem = elem.find_element_by_tag_name("h2")
        name = elem.text
        print("name : ", name)

        elem = driver.find_element_by_class_name("prdc_default_info")
        elem = elem.find_element_by_class_name("sale_price")
        price = elem.text
        print("price : ", price)
        header.append(name)
        data.append(price.replace(",", ""))

    # print(header)
    if not os.path.exists('output.csv'):
        output.write(','.join(header)+"\n")

    output.write(",".join(data)+'\n')

# .try
except Exception as e:
    print(e)
finally:
    driver.quit()

