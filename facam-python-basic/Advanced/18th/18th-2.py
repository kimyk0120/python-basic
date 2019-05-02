"""
    11번가 수집내용 변경됐을 시 메신져로 보내기
"""

from selenium import webdriver
import datetime
import os
import telepot

# selenium 크롬 headless 옵션
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
# 혹은 options.add_argument("--disable-gpu")

f = open("product.txt", 'r')
products = f.readlines() # 행 단위로 끊어서 list 형으로 반환
f.close()

prices= None
if os.path.exists('output.csv'):
    # output = open('output.csv', 'w')
    output = open('output.csv', 'r')
    prices = output.readlines().pop().strip().split(',')
    output.close()

print(prices)
# print(products)

driver = webdriver.Chrome("chromedriver",options=options)

try:
    idx = 1
    header = ['']
    data = [str(datetime.datetime.now())]
    diff = []
    for index, url in enumerate(products):
        print(url)
        url = url.strip()
        driver.get(url)

        elem = driver.find_element_by_class_name("heading")
        elem = elem.find_element_by_tag_name("h2")
        name = elem.text
        print("name : ", name)

        elem = driver.find_element_by_class_name("prdc_default_info")
        elem = elem.find_element_by_class_name("sale_price")
        price = elem.text.replace(",","")
        print("price : ", price)

        if prices and price != prices[idx]:
            diff.append((name, prices[idx], price))

        header.append(name)
        data.append(price.replace(",", ""))

        idx += 1

    print("#" * 120)
    print(diff)

    if diff:
        bot = telepot.Bot('850452568:AAHw3xxLmmZX8kkxwIt0LcutMVud_9pzAqg')
        keyF = open("idKey", 'r')
        telegram_id = keyF.readline()

        msg = ''
        for info in diff:
            msg += '- %s\n%s => %s\n' % info
        bot.sendMessage(telegram_id, msg)

    # print(header)
    # if not os.path.exists('output.csv'):
    #     output.write(','.join(header)+"\n")

    # output.write(",".join(data)+'\n')
    # .for

# .try
except Exception as e:
    print(e)
finally:
    driver.quit()
    # output.close()
    f.close()

