'''
    만들기, 공유

'''

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/drive', 'https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name("facamOnline-8a69e42a656e.json", scope)

gs = gspread.authorize(credentials)

doc = gs.create('online create test')

ws = doc.get_worksheet(0)

for i in range(5):
    ws.append_row([i, str(i)+' data'])


doc.share('kimyk0120@gmail.com', perm_type='user', role='owner')


