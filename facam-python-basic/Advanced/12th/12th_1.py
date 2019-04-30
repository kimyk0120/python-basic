"""
    API DART http://dart.fss.or.kr/
"""
import requests

# requests.get("https://google.com")
# requests.post()

# http://dart.fss.or.kr/api/search.xml?auth=xxx     xml 응답
# http://dart.fss.or.kr/api/search.json?auth=xxx    json 응답

f = open("dartAuthKey", 'r')
authKey = f.readline()
# print(authKey)

args = {
    'start_dt': '20190301',
    'end_dt': '20190430',
    'sort': 'crp'
}

args_str = ''
for k, v in args.items():
    args_str += '&%s=%s' % (k, v)

res = requests.get('http://dart.fss.or.kr/api/search.json?auth=%s%s' % (authKey, args_str))
# print(res.status_code)
# if res.status_code == 200:
data = res.json()
print(data)
# print(data['err_code'])

if data['err_code'] != '000':
    print('err msg : ', data['err_msg'])
else:
    print("\n" + ("#" * 200) + "\n")
    data_list = data['list']
    for d in data_list:
        print(d['crp_nm'])
        # print(d)




