'''
    20. text file 활용

csv = , column 구분, 개행문자로 행 구분
'''

datafile = open("data.csv","r")
# print(datafile)
# print(datafile.readlines()) # 행단위로 잘라서 list return
for line in datafile.readlines():
    data = line.strip().split(',')
    print(data[0])
    print(data[1])
    print(data[2])
    print("-"*20)





