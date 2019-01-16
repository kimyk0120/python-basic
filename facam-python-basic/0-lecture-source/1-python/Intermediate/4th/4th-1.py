import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('cred.json', scope)

gs = gspread.authorize(credentials)

doc = gs.open_by_url('https://docs.google.com/spreadsheets/d/1LAm_yERaVnOHm4UuWQyG3iKkcDiScJobxgwUmLLcyDg/edit#gid=0')
ws = doc.get_worksheet(0)

# val = ws.acell('B1').value
# print(val)
# val = ws.row_values('1')
# print(val)
# val = ws.col_values('1')
# print(val)
# vals = ws.range('A2:B3')
# for val in vals:
#    print(val.value)
# ws.update_acell('B1', 'B1data_updated')
ws.append_row(['newA', 'newB', 'newC'])