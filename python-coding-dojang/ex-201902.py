# a = list(range(0,100,10))
# print(a)

# print(30 in a)
# if 100 not in a: print("test")
# print(len(a))
#
# a = "한글테스트"
# print(len(a))
# print(len(a.encode("utf-8")))

# print(a)
# print(a.__getitem__(2))

# a = range(2)
# print(a)
# print(type(a))

# print(a[0:4])
# print(a[0:10])
# print(a[4:7])
#
# print(a[2:8:3])
# print(a[2:9:3])

# print(a[:7:2])

# a[2:5] = ["a","b","c","d","e"]
# print(a)

# a[2:7:2] = ["tes1","test2","test3"]
# print(a)

# del(a[2:5])
# del(a[2:8:2])
# print(a)

# del(a[len(a)-1])
# print(a)

# dic_var = {"test1":1,"test2":"2"}
# print(dic_var)

# a = {}
# print(a)

# a = dict()
# print(a)

# a = dict(test1=490, test2="test", test3=18.72) # dict함수로 생성시 key 는 문자열로 변환됨
# print(a)

# character = {"health":880, "name":"test", 'armor':18.72}
# character['health'] = 1000
# character['test2'] = "test2"
# print(character)
# # print(character["noKey"]) # keyErr
# print('test2' in character)

# 20190218
# if
# x = 11
# if x == 10:
#     print("test")
# else:
#     print("test2")

# if 0 < x < 20:
#     print("test")
# else:
#     print("test2")

# a = 10
# if a == 11:
#     print("test")
# elif a == 10:
#     print("test2")
# else:
#     print("test3")

# is는 레퍼런스를 비교하고 ==는 값을 비교

# a = -25555
# b = 202
# print(a is -25555)
# print(id(a))
# print(id(-25555))

# for x in range(10):
#     print(x)

# for x in range(10, 20):
#     print(x)

# for x in range(10, 20, 2):
#     print(x)

# for x in range(10, 0, -1):
#     print(x)

# a = [x for x in range(10, 51, 10)]
# print(a)
# for i in a:
#     print(i)

# b = ("test1", "2", "t3")
# for t in b:
#     print(t)

# c = "python"
# for i in c:
#     print(i)

# for i in c:
#     print(i, end=" ")

# for i in reversed(c):
#     print(i)

# 20 to 10
# for i in range(20, 9, -1):
#     print(i)

# for i in reversed(range(10, 21)):
#     print(i)

# 구구단
# a = int(input("no:"))
# print("input num : ", a)
#
# for i in range(1, 10):
#     print("%d * %d = %d" % (a, i, a*i))


# while
# i = 0
# while i < 100:
#     print(i)
#     i += 1

# import random
# print(random.randint(1, 6))

# i = 0
# while i != 3:
#     i = random.randint(1, 6)
#     print(i)


# 20190220
# q
# i = 2
# j = 5
#
# while i <= 32 or j > 0:
#     print(i, j, end=" ")
#     i *= 2
#     j -= 1

# q2
# amount = int(input("amount : "))
# fee = 1350
# while amount > fee:
#     amount -= fee
#     print(amount)

'''
    break, continue
'''

# i = 0
# while True:
#     print(i)
#     i += 1
#     if i >= 100:
#         break

# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)

# q : 0과 73 사이의 숫자 중 3으로 끝나는 숫자만 출력
i = 0
# while True:
#     if i % 10 != 3:
#         i += 1
#         continue
#     if i > 73:
#         break
#     print(i, end=" ")
#     i += 1

# while True:
#     if i % 10 == 3:
#         print(i, end=" ")
#         i += 1
#     if i > 73:
#         break
#     i += 1


# q : 두 수 사이의 숫자 중 3으로 끝나지 않는 숫자 출력
# a = 1
# b = 20
#
# i = a
# while True:
#     if i % 10 == 3:
#         i += 1
#         continue
#     print(i)
#     if i >= 20:
#         break
#     i += 1


# 중첩 루프
# for i in range(10):
#     for j in range(10):
#         print("j : ", j)
#     print("\ti : ", i)

# for i in range(5):
#     for j in range(5):
#         print("j:", j, sep="", end=" ")
#     print("i:", i, '\\n', sep="")
#     print("i:", i, sep="", end="\n")

# for i in range(5):
#     for j in range(5):
#         print('*', end="")
#     print()

# for i in range(3):
#     for j in range(7):
#         print('*', end="")
#     print()

# for i in range(5):
#     for j in range(5):
#         if i >= j: # 0 0 , ... 1 0 , 1 1 ....
#             print("*",end="")
#     print()

# for i in range(5):
#     for j in range(5):
#         if j == i:
#             print("*", end='')
#         else:
#             print(' ',end='')
#     print()


# 20190221
# q : 역삼각형 별 출력

# for i in range(5):
#     for j in range(5):
#         if j >= i:
#             print("*", end='')
#     print()

# for i in range(5):
#     for j in range(5):
#         if j < i:  # 0 0, 1 0 ~~ 0 < 1
#             print(" ", end='')
#         else:
#             print('*', end='')
#     print()


# 피라미드 별찍기
# n = int(input('number :'))
# for i in range(1, n+1):
#     print(" "*(n-i), "*"*(2*i-1))

# # FizzBuzz
# for i in range(1, 101):
#
#     if i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)


# 공배수 처리
# for i in range(1, 101):
#
#     if i % 3 == 0 and i % 5 ==0:
#         print(i, 'FizzBuzz')
#     elif i % 3 == 0:
#         print(i, 'Fizz')
#     elif i % 5 == 0:
#         print(i, 'Buzz')
#     else:
#         print(i)

# for i in range(1, 101):
#
#     if i % 15 == 0:  # 최소공배수
#         print(i, 'FizzBuzz')
#     elif i % 3 == 0:
#         print(i, 'Fizz')
#     elif i % 5 == 0:
#         print(i, 'Buzz')
#     else:
#         print(i)









































