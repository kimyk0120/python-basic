

# def sum(a,b):
#     return a+b
#
# print(sum(3,4))

# def sat():
#     return "Hello"
#
# print(sat())

# def say():
#     print("test")
#
# say()

# def sum_many(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
#
# print(sum_many(1,2,3,4,5))

# def testArgs(*args):
#     print(args)
#
# testArgs([1,2,3,4,5],(1,2,3,4,5),{"a":"test"},1,2)

# def sum_and_mul(a,b):
#     return a+b, a*b

# print(sum_and_mul(3,4)) #(7, 12)

# sum,mul = sum_and_mul(3,4)
# print(sum)
# print(mul)


# def test_return(*args):
#     if args[0] == "test":
#         return False
#     print("test2")
#
# test_return("test")

# def default_val_test(a,b,c=True):
#     print(a, b)
#     if c:
#         print(c)
#
# default_val_test("test1","test2")
# default_val_test("test1","test2",False)

# a = 1
# def var_test():
#     global a # 전역변수 사용방법
#     a += 1
#     # return a
#
# var_test()
# print(a)

# a = input("input: ")
# print(a)

# print("a","b",'c')

# for x in range(0,10):
#     print(x*2,end=' ')

# f = open("test.txt",'w')
# f.close()
#
# f = open("/Users/youngkwangkim/Downloads/test.txt",'w')
# f.close()
#
# f = open("test.txt",'w')
# for i in range(1,10):
#     data = "%d line \n" % i
#     f.write(data)
#
# f.close()

# f = open("test.txt",'r')
# line = f.readline()
# print(line)

# while True:
#     line = f.readline()
#     if not line: break
#     print(line)

# print(f.readlines()) # ['1 line \n', '2 line \n', '3 line \n', '4 line \n', '5 line \n', '6 line \n', '7 line \n']
# lines = f.readlines()
# for line in lines:
#     print(line)
#
# f.close()

# f = open("test.txt",'a')
# for add_lind in range(0,10):
#     data = "add %dth text  \n" % add_lind
#     f.write(data)
# f.close()

# with open("test.txt",'a') as f:
#     f.write("test add with")

# import sys
# args = sys.argv[0:]
# print(args)

# function q1
# 피보나치 수열 구하기

# a = 10
#
# def fib(a):
#     if a == 0:
#         return 0
#     if a == 1:
#         return 1
#     if a >= 2:
#       return fib(a-2) + fib(a-1)
#
# for i in range(10):
#     print(fib(i))

# file io q1
# f = open("test.txt",'r')
# lines = f.readlines()
# total_sum = 0
# for line in lines:
#     total_sum += int(line)
# print("total_sum : " , total_sum)
# average = total_sum/len(lines)
# print("average : " , average)
# f.close()



# class
# class Calculator:
#     def __init__(self):
#         self.result = 0
#
#     def adder(self,num):
#         self.result += num
#         return self.result
#
# cal1 = Calculator()
# cal2 = Calculator()
#
# print(cal1.adder(3))
# print(cal1.adder(4))
# print(cal2.adder(3))
# print(cal2.adder(4))









