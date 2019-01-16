import requests
import datetime
import telepot

AUTH_KEY='7508d2641cd078571274bca886016990fa395730'

today = datetime.date.today()
start_dt = today - datetime.timedelta(days=30)

args = {
    'start_dt': start_dt.strftime('%Y%m%d'),
    'end_dt': today.strftime('%Y%m%d'),
    'sort': 'date',
    'page_no': '3'
}

args_str = ''
for k, v in args.items():
    args_str += '&%s=%s' % (k, v)

res = requests.get('http://dart.fss.or.kr/api/search.json?auth=%s%s' % (AUTH_KEY, args_str))
data = res.json()

bot = telepot.Bot('661295548:AAFJ6__a7HvM3qchm76BlA5lfavPW1pSkV8')

if data['err_code'] != '000':
    bot.sendMessage('57841042', '공시정보 조회 실패: ' + data['err_msg'])
else:
    msg = ''
    data_list = data['list']
    for d in data_list:
        for k, v in d.items():
            msg += '%s,' % v
        msg += '\n'

    bot.sendMessage('57841042', '공시정보 조회 성공\n' + msg)
    