'''
    23 . 엑셀 파일

'''


from openpyxl import load_workbook

wb = load_workbook(filename='test.xlsx')
data = wb.active

print(data['A1'].value)
print(data['A2'].value)
print(data['B1'].value)
print(data['B2'].value)






