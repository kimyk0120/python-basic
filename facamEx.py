#print("Hello World")

#
# a = {'a': 1, "b": 22}
# print(a)
# a['c'] = 30
# print(a)
# a['a'] = 11
# print(a)


# 조건문 if 
# payment = 'complete'
# payment = 'test'
# if payment == 'complete':
#     print("complete")
# elif payment == 'inprogress':
#     print("inprogress")
# else:
#     print('nope')

# first =  'somthing'
# second = ''
# if first:
#     if second:
#         print("test2")
#     print("test1")

# list_a = [1,2]
# if 1 in list_a:
#     print("test")

# if 3 in list_a:
#     print("test")

# if 1 in list_a or 3 in list_a:
#     print("test")


# 반복문 for
# list_a = [1,2,3,5]
# for looper in list_a:
#     print(looper)
# for looper in range(10):
#     print(looper)

# for key in dict_val.keys():
#     print(key)
# for key in dict_val.keys():
#     print(dict_val[key])
# for val in dict_val.values():
#     print(val)
# dict_val = {"a":1,"b":2}
# for(key, val) in dict_val.items(): # 튜플로 반환
#     print(key)
#     print(val)


# 반복문 while
# data_a = ['data1','data2','data3','data4']
# while data_a:
#     print(data_a.pop())
#
# print(data_a)

# for looper in [0,1,2]:
#     print(looper)
#     continue
#     print("continue")

# while True:
#     print("test")
#     break
#     print("test1")

# for num in range(100):
#     if num > 50 :
#         break
#     if num % 2 ==0:
#         continue
#     print(num)


# 함수
# def testFunc(a,b="2"):
#     print(a, " " ,b)
# testFunc("a","3")

# def print_name(a,b=2):
#     print("test")
#     print("test2\n")
#     return a+b

# print(print_name(1,4))
# print(print_name(12,43))
# print(print_name(14))


# # 함수의 활용
# def send_mail(from_email, to_email, contents, subject="testSubject"):
#     print(from_email)
#     print(to_email)
#     print(subject)
#     print("*"*10)
#     print(contents)
#     print("*" * 10)
#     print("-" * 10)
#
# users = []
# users.append({'name':'kim','email':'kimyk@email.com'})
# users.append({'name':'kim2','email':'kimyk2email.com'})
#
# # print(users)
#
# content = ''' test
# test'''
#
# for user in users:
#     title = "to " + user['name']
#     if '@' not in user['email']:
#         continue
#     send_mail("me",user['email'],content)


'''
    14.내장함수
'''
# a = '2'
# a = int(a)
# print(a)

# str_va = '100'
# a= int(str_va)+1
# print(a)
#
# print(type(str_va))

# int_val = 100
# a = str(int_val)
# print(a)
# print(type(a))
# a += " test"
# print(a)

# str_var = 'test'
# tuple_var = (1,2,3)
# print(list(str_var)) #['t', 'e', 's', 't']
# print(list(tuple_var))
#
# list_var = [1,2,3]
# print(tuple(list_var))
#
# int_val = 100
# print(list(int_val)) # 'int' object is not iterable

# list_val = range(3)
# print(list_val)

# a = 'test'
# print(len(a))
# a = [1,2,3]
# print(len(a))
# a = {"2":2}
# print(len(a))

# for idx in range(5):
#     print(idx)

# a = [1,2,3,4]
# print(max(a))
# print(min(a))


'''
    15. class
'''

# class Test():
#
#     def __init__(self):
#         test_val = ''
#
#     def test_val_print(self):
#         print("test")
#
# test = Test()
# test.test_val_print()


'''
    16. class 
'''

# class Test():
#
#     test_val2 = "test_val2"
#
#     def __init__(self):
#         self.test_val = ''
#
#     def test_val_print(self,a):
#         print(self.test_val , a)
#     def print_textval2(self):
#         print(self.test_val2)
#
# test = Test()
# test.test_val = "test2"
# test.test_val_print("test3")
# test.print_textval2()

# class Test():
#     def __init__(self):
#         self.myData = 100
#         print("__init called")
#
# test = Test()
# test2 = Test()
# print(test.myData)
# print(test2.myData)
# test2.myData = 10
# print(test2.myData)

# class SimpleTest():
#     def print_skip(self,str):
#         if 'skip' in str:
#             print("skip")
#             return
#
#         print(str)
#
# simple = SimpleTest()
# simple.print_skip("ddad")
# simple.print_skip("skip text")
# simple.print_skip("ssfsdf")




