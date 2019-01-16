# 자료형의 참과 거짓
# print(type(None))
# print(None)
# a = [1,2,3,4]
# while a:
#     a.pop()
#     print(a)
#
# print("while done")
# if []:
#     print("test1")
# else:print("test2")

# if ['2','3']:
#     print("test1")
# else:print("test2")

# a = 3
# b = 3
# del a
# del b

# a = [1,2,3]
# b = a[:]
# # b = a
# a[1] = 4 # b = a 의 경우 같은 메모리 참조로 인해 b 도 변경됨
# print(b)

# from copy import copy
# a =[1,2,3]
# b = copy(a)
# print(b)
# print(b is a)

# p106-연습문제
# q1
# pin = "881120-1068234"
# #yyyymmdd = pin.split("-")[0]
# yyyymmdd = pin[:6]
# #num = pin.split("-")[1]
# num = pin[7:]
# print(yyyymmdd)
# print(num)

# q2
# pin = "881120-1068234"
# gender = pin[7]
# if gender == "1":
#     gender = "man"
# else:
#     gender = "woman"
# print(gender)

# q3
# a = [1,3,5,4,2]
# a.sort()
# a.reverse()
# print(a)

# q4
# a = ["Life","is","too","short"]
# result = " ".join(a)
# print(result)

# tuple q1
# a = (1, 2, 3)
# b = (4,) # tuple 의 값이 1개 일 때는 value 뒤에 comma 를 붙인다.
# print(a + b)

# dictionary q1
# a = {"A":90, "B":80, "C":70}
# result = a.pop('B')
# print(a)
# print(result)

# set q1
# a = [1,1,1,2,2,3,3,3,4,4,5]
# aSet = set(a)
# b = list(aSet)
# print(b)

# variable q1
# a = b = [1,2,3]
# a[1] = 4
# print(b) # a와 b가 같은 메모리 (1,2,3)을 참조하고 있다.


# if 0:
#     print("test1")
# else:
#     print("test2")

# if 1 not in [2,3,4]:
#     print("test1")
# else:
#     print("test2")

# a = [1,2,3]
# if 4 in a:
#     pass
# else:
#     print(a[1:2])
# if 1 in a: pass
# else:print("test")

# while문
# hit =0
# while hit < 10:
#     hit+=1
#     print("test" , "hit : " ,hit)

# while 1:
#     print("test")
#     break

for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=" ")
    print("")









