import requests

AUTH_KEY='7508d2641cd078571274bca886016990fa395730'

args = {
    'start_dt': '20180801',
    'end_dt': '20180701',
    'sort': 'date',
    'page_no': '3'
}

args_str = ''
for k, v in args.items():
    args_str += '&%s=%s' % (k, v)

res = requests.get('http://dart.fss.or.kr/api/search.json?auth=%s%s' % (AUTH_KEY, args_str))
data = res.json()

if data['err_code'] != '000':
    print(data['err_msg'])
else:
    data_list = data['list']
    for d in data_list:
        print(d['crp_nm'])
