from selenium import webdriver
import telepot
import datetime
import os

f = open('products.txt', 'r')
products = f.readlines()
f.close()

prices = None
if os.path.exists('output.csv'):
    f = open('output.csv', 'r')
    prices = f.readlines().pop().strip().split(',')
    f.close()

output = open('output.csv', 'a')

driver = webdriver.Chrome('./chromedriver')

try:
    idx = 1
    header = ['']
    data = [str(datetime.datetime.now())]
    diff = []
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
        bot = telepot.Bot('661295548:AAFJ6__a7HvM3qchm76BlA5lfavPW1pSkV8')
        msg = ''
        for info in diff:
            msg += '- %s\n%s => %s\n' % info
        bot.sendMessage('57841042', msg)

    if not os.path.exists('output.csv'):
        output.write(','.join(header)+'\n')

    output.write(','.join(data)+'\n')

except Exception as e:
    print(e)
finally:
    driver.quit()
