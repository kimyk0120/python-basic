'''
    23 . 엑셀 파일

'''


from openpyxl import load_workbook

wb = load_workbook(filename='test.xlsx')
data = wb['sheet_test']
# print(data['A1'].value)

# area = data['A1:B2']
# area = data['A:B']
area = data[1:2]
print(area)
for row in area:
    for cell in row:        
        print(cell.value)

print("-"*30)






