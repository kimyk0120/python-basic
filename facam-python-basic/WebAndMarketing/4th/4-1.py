import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name("facamOnline-8a69e42a656e.json", scope)

gs = gspread.authorize(credentials)

'''
       A       B      C
1   A1data	B1data	C1data
2   A2data	B2data	C2data
3   A3data	B3data	C3data
'''
doc = gs.open_by_url("https://docs.google.com/spreadsheets/d/1EUXbm5youf7S6TVNQJozuUD1rgogTRsbSUu4xhMApRA/edit#gid=0")


# read
ws = doc.get_worksheet(0)

val = ws.acell("B1").value

print(ws.get_all_values()) # [['A1data', 'B1data', 'C1data'], ['A2data', 'B2data', 'C2data'], ['A3data', 'B3data', 'C3data']]
print(val) # B1data

val = ws.row_values('1')
print(val) # ['A1data', 'B1data', 'C1data']

val = ws.col_values('1')
print(val) # ['A1data', 'A2data', 'A3data']

val = ws.range('A2:B3')
print(val) # [<Cell R2C1 'A2data'>, <Cell R2C2 'B2data'>, <Cell R3C1 'A3data'>, <Cell R3C2 'B3data'>]
print(val[0].value) # A2data

# update
ws.update_acell('B1', 'B1data_updated')
ws.update_acell('L1', 'L1data_insert')

ws.append_row(['newA','newB','newC'])






