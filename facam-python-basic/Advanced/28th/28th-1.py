"""
    11번가 수집내용 변경됐을 시 메신져로 보내기
"""

from selenium import webdriver
import datetime
import os
import telepot


def write_log(msg):
    _base_dir = os.path.dirname(os.path.realpath(__file__))
    f = open(os.path.join(_base_dir, 'auto.log'), 'a')
    f.write('[%s] %s \n' % (str(datetime.datetime.now()), msg))
    f.close()


base_dir = os.path.dirname(os.path.realpath(__file__))

write_log('제품 리스트 get')

f = open(os.path.join(base_dir, "product.txt"), 'r')
products = f.readlines() # 행 단위로 끊어서 list 형으로 반환
f.close()

output_filename = os.path.join(base_dir, 'output.csv')
prices= None
if os.path.exists(output_filename):
    # output = open('output.csv', 'w')
    output = open(output_filename, 'r')
    prices = output.readlines().pop().strip().split(',')
    output.close()

print(prices)
# print(products)
output = open(output_filename, 'a')

write_log('Chrome 브라우저 실행')
# selenium 크롬 headless 옵션
options = webdriver.ChromeOptions()
options.add_argument('headless')
# options.add_argument('window-size=1920x1080')
# options.add_argument("disable-gpu")
# 혹은 options.add_argument("--disable-gpu")

driver = webdriver.Chrome(os.path.join(base_dir, "chromedriver"),options=options)

try:
    idx = 1
    header = ['']
    data = [str(datetime.datetime.now())]
    diff = []
    write_log('상품 정보 조회')
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

        keyF = open(os.path.join(base_dir, 'idKey'), 'r')
        telegram_id = keyF.readline()

        msg = ''
        for info in diff:
            msg += '- %s\n%s => %s\n' % info
        write_log('텔레그램 전송')
        bot.sendMessage(telegram_id, msg)

    print(header)
    if not os.path.exists(output_filename):
        output.write(','.join(header)+"\n")

    output.write(",".join(data)+'\n')
    # .for

# .try
except Exception as e:
    print(e)
finally:
    driver.quit()
    output.close()
    f.close()

