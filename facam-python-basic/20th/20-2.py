'''
    20. text file 활용

file 쓰기
'''

values = []

values.append(("test1","test2"))
values.append(("test3","test4"))
values.append(("tes5","test6"))
values.append(["tes7","test8"])
print(values)

datafile = open("data2.csv",'a')
# datafile = open("data2.csv",'w')

for line in values:
    data = ",".join(line)
    print(data)
    datafile.write(data+"\n")

datafile.close()

