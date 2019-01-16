from selenium import webdriver
import telepot
import datetime
import os


def write_log(msg):
    base_dir = os.path.dirname(os.path.realpath(__file__))
    f = open(os.path.join(base_dir, 'auto.log'), 'a')
    f.write('[%s] %s\n' % (str(datetime.datetime.now()), msg))
    f.close()

base_dir = os.path.dirname(os.path.realpath(__file__))

write_log('제품 리스트를 가져옵니다.')

f = open(os.path.join(base_dir, 'products.txt'), 'r')
products = f.readlines()
f.close()

output_filename = os.path.join(base_dir, 'output.csv')
prices = None
if os.path.exists(output_filename):
    f = open(output_filename, 'r')
    prices = f.readlines().pop().strip().split(',')
    f.close()

output = open(output_filename, 'a')

write_log('크롬 브라우저를 실행합니다.')
opts = webdriver.ChromeOptions()
opts.add_argument('headless')
driver = webdriver.Chrome(os.path.join(base_dir, 'chromedriver'), chrome_options=opts)

try:
    idx = 1
    header = ['']
    data = [str(datetime.datetime.now())]
    diff = []
    write_log('상품 정보를 조회합니다')
    for url in products:
        url = url.strip()
        driver.get(url)

        elem = driver.find_element_by_class_name('heading')
        elem = elem.find_element_by_tag_name('h2')
        name = elem.text

        elem = driver.find_element_by_class_name('prdc_default_info')
        elem = elem.find_element_by_class_name('sale_price')
        price = elem.text.replace(',', '')

        if prices and price != prices[idx]:
            diff.append((name, prices[idx], price))

        header.append(name.replace(',', ''))
        data.append(price)

        idx += 1

    if diff:
        write_log('텔레그램으로 알림을 보냅니다')
        bot = telepot.Bot('661295548:AAFJ6__a7HvM3qchm76BlA5lfavPW1pSkV8')
        msg = ''
        for info in diff:
            msg += '- %s\n%s => %s\n' % info
        bot.sendMessage('57841042', msg)

    if not os.path.exists(output_filename):
        output.write(','.join(header)+'\n')

    output.write(','.join(data)+'\n')

except Exception as e:
    write_log(e)
finally:
    driver.quit()
