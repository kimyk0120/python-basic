
# print("test")

# a = [21,23,24]
# for x in a:
#     print(x)
#
# for index, value in enumerate(a):
#         print(index, value)
#
# for index, value in enumerate(a, start=1):
#         print(index, value)
#

# i = 0
# while i < len(a):
#     print(a[i])
#     i += 1
#
'''
a = [38, 21, 53, 62, 19]
smallest = a[0]
for i in a:
    if i < smallest:
        smallest = i

print(smallest)

# a.sort()
# print(a[0])

print(min(a))
print(max(a))

print(sum(a))


# list comprehension
# [식 for 변수 in 리스트]

a = [i for i in range(10)]
print(a)
b = list(i for i in range(10))
print(b)
c = [i+5 for i in range(10)]
print(c)
d = [i*2 for i in range(10)]
print(d)

# [식 for 변수 in 리스트 if 조건식]
a = [i for i in range(10) if i % 2 == 0]
print(a)

b = [i + 5 for i in range(10) if i % 2 == 1]
print(b)

# [식 for 변수 in 리스트 if 조건식 식 for 변수 in 리스트 if 조건식 ... 식 for 변수 in 리스트 if 조건식]
a = [i * j for j in range(2, 10) for i in range(1, 10)]
print(a)

a = [i * j for j in range(2, 10) # 2 ~ 9 - j
           for i in range(1, 10)] # 1~9 - i
print(a)


# map
a = [1.2, 2.5, 3.7, 4.6]
# for i in range(len(a)):
#     # print(i)
#     a[i] = int(a[i])
#
# print(a)

a = list(map(int, a))
print(a)

# map
# map은 입력받은 자료형의 각 요소가
# 함수 f에 의해 수행된 결과를 묶어서 리턴하는 함수


a = list(map(str, range(10)))
print(a)


a, b = map(int, [10, 20])
print(a)
print(b)


a = (38, 21, 53, 21, 21, 53)
b = a.index(53)
print(b)
print(a.count(21))
'''

a = [[10,20],
     [30,40],
     [50,60]]
print(a)
print(a[0][0])
print(a[1][1])
print(a[2][1])
a[0][1] = 1000
print(a[0][1])

from pprint import pprint
pprint(a, indent=3, width=15)

for x, y in a:
    print(x, y)

for i in a:
    for j in i:
        print(j, end=' ')


























































































































