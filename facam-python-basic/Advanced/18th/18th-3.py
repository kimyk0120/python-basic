import requests
import telepot
import datetime

f = open("dartAuthKey", 'r')
authKey = f.readline()

today = datetime.date.today()
start_dt = today - datetime.timedelta(days=30)

# print(today)

args = {
    'start_dt': start_dt.strftime('%Y%m%d'),
    'end_dt': today.strftime('%Y%m%d'),
    'sort': 'crp',
    'page_no': '1'
}

# print(args) # {'start_dt': '20190402', 'end_dt': '20190502', 'sort': 'crp', 'page_no': '1'}
# quit()

args_str = ''
for k, v in args.items():
    args_str += '&%s=%s' % (k, v)

res = requests.get('http://dart.fss.or.kr/api/search.json?auth=%s%s' % (authKey, args_str))
# print(res.status_code)
# if res.status_code == 200:
data = res.json()
print(data)
# print(data['err_code'])

bot = telepot.Bot('850452568:AAHw3xxLmmZX8kkxwIt0LcutMVud_9pzAqg')
keyF = open("idKey", 'r')
telegram_id = keyF.readline()


if data['err_code'] != '000':
    print('err msg : ', data['err_msg'])
    bot.sendMessage(telegram_id, '공시정보조회실패 : ' + data['err_msg'])
else:
    msg = ''
    print("\n" + ("#" * 200) + "\n")
    data_list = data['list']
    for d in data_list:
        # print(d['crp_nm'])
            for k, v in d.items():
                msg += '%s, ' % v
            msg += '\n'

    bot.sendMessage(telegram_id, '공시정보조회 : ' + msg)





