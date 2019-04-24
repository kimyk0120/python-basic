a = [[10, 20],[30, 40],[40, 50]]
for i in a:
    for j in i:
        print(j, end=" ")
    print()
print("#"*20)
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=" ")
    print()
print("#"*20)




