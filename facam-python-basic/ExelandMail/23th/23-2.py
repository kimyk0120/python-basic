'''
    23 . 엑셀 파일

'''


from openpyxl import load_workbook

wb = load_workbook(filename='test.xlsx')
data = wb.active

row = data['2']
print(row)

for cell in row:
    print(cell.value)

col = data['A']
print(col)
for cell in col:
    print(cell.value)

print("-"*30)






