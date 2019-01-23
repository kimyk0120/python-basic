'''
    CLASS
'''


# class HouseP:
#     lastNm = "park"
#
#     # def setNm(self,name):
#     #     self.fullNm = self.lastNm + name
#
#     def __init__(self, name):
#         self.fullNm = self.lastNm + name
#
#     def travel(self, where):
#         print("%s go to" % self.fullNm, where)
#
#     def love(self, other):
#         print("%s, %s fall in love" % (self.fullNm, other.fullNm))
#
#     def fight(self, other):
#         print("%s , %s fight" % (self.fullNm, other.fullNm))
#
#     def __add__(self, other):
#         print("%s, %s married " % (self.fullNm, other.fullNm))
#
#     def __sub__(self, other):
#         print("%s , %s divorced" % (self.fullNm, other.fullNm))
#
# class HouseK(HouseP):
#     lastNm = "kim"
#
#     # 동일한 메소드명으로 오버라이딩(overriding) 한다.
#     def travel(self, where , days):
#         print("%s go to " % self.fullNm, where , "for %d days" % days )
#
#     def __add__(self, other):
#         print("test3")
#
# # a = HouseP("test")
# # print(a.lastNm)
# # a.setNm("test")
# # print(a.fullNm)
# # a.travel("seoul")
# # b = HouseK("test2")
# # b.travel("busan",4)
#
#
# # a = HouseP("1")
# # b = HouseK("2")
# # a.love(b)
# # a + b
# # b + a # 앞 쪽 인스턴스의 __add__ 메서드가 실행
#
# a = HouseP("seri")
# b = HouseK("yk")
# a.travel("seoul")
# b.travel("busan", 3)
# a.love(b)
# a + b
# a.fight(b)
# a - b


'''
    Module
'''
# import mod1
# mod1.safe_sum(2, 3)
# mod1.safe_sum(2, "3")
# mod1.safe_sum("a", "1")

# from mod1 import safe_sum, sum
# from mod1 import *
# safe_sum(2,3)
# sum(1,2)

# import mod1

# print("mod1.__name__ : ", mod1.__name__)

# import mod2
#
# print(mod2.PI)
# a = mod2.Math()
# print(a.solv(3))

# import sys
# print(sys.path)
# print(sys.path[0])
# sys.path.append(sys.path[0] + "/MyModules")
# print(sys.path)

# import MyModules.mod2 as mod2
# print(mod2.PI)

'''
    Package
'''

# from game.sound import echo
# echo.echo_test()
# from game.sound.echo import echo_test
# echo_test()

# * 사용시 __init__ 안에 __all__ 변수 설정
# from game.sound import *
# echo.echo_test()

# from game.graphic.render import render_test
# render_test()


'''
    Exception
'''

# f = open("test",'r')
# a = 4/0
# a = [1,2,3]
# a[4]

# try:
#     4 / 0
# except ZeroDivisionError as e:
#     print("test exception  : ", e)

# try:
#     f = open("foo.txt", 'r')
# except FileNotFoundError as e:
#     print(e)
# else:
#     data = f.read()
#     f.close()

# try:
#     f = open("nofile",'r')
# except FileNotFoundError as e:
#     pass


# class Bird:
#     def fly(self):
#         raise NotImplementedError
#
#
# class Eagle(Bird):
#     def fly(self):
#         print("test")
#
#
# eagle = Eagle()
# eagle.fly()



'''
    내장 함수
'''

# print(abs(3))
# print(abs(-3))
# print(abs(-0.8))

# print(all([1,2,4]))
# print(all([1,2,0]))
# print(all([1,2,4,False]))

# print(any([1,2,3,4]))
# print(any([0,0,0,0]))
# print(any([0,0,0,1]))
# print(any([1,""]))

# print(chr(97))
# print(chr(48))
# print(chr(125))
# print(chr(126))

# print(dir([1,2,3]))
# print(dir({"1":1}))

# print(divmod(6,5))
# print(divmod(7,3))
# print(divmod(1.3,0.2))

# for i, name in enumerate(['test1','test2','test3']):
#     print(i, name)

# from MyModules import filter1
#
# print(list(filter(filter1.positive,[1,2,3,-1])))

# a = list(filter(lambda x:x >0 , [1,2,3,-1,0]))
# print(a)

# a = 3
# print(id(a))
# print(id(3))
# b = a
# print(id(b))


# class Person:
#     pass
#
#
# a = Person()
# print(isinstance(a,Person))
# b = 3
# print(isinstance(b, Person))


# sum = lambda a,b: a+b
# print(sum(3,4))

# myList = [lambda a,b:a+b, lambda a,b:a*b]
# print(myList)
# print(myList[0])
# print(myList[0](3,4))
# print(myList[1](3,4))

# print(list("test"))
# print(list((1,2,3)))


# a = [1,2,3]
# b = list(a)
# print(id(a))
# print(id(b))


# def two_times(number_list):
#     result = []
#     for number in number_list:
#         result.append(number*2)
#     return result
#
#
# result = two_times([1,2,3,4])
# print(result)


# def two_times(x): return x*2
#
#
# a = list(map(two_times,[1,2,3,4]))
# print(a)


# a = list(map(lambda x:x*2,[1,2,3,4]))
# print(a)


# print(list(map(lambda x:x+1,[1,2,3,4,5])))

# print(max("test"))
# print(max([1,2,3,4]))

# f = open("test.txt", 'rb')
# print(f.read())

# print(list(range(5)))
# print(list(range(5,10)))
# print(list(range(1,10,2)))
# print(list(range(0,-10,-1)))


'''
    Library
'''

# $ python3 jumpToPythonEx-20190122.py test1 guido
# import sys
# print(sys.argv) # ['jumpToPythonEx-20190122.py', 'test1', 'guido']
# sys.exit() # interpreter exit

# import pickle
# f = open("test.txt", 'wb')
# data = {1:'python', 2:'guido'}
# pickle.dump(data, f)
# f.close()

# import pickle
# f = open("test.txt", 'rb')
# data = pickle.load(f)
# print(data)

# import os
# print(os.environ)
# print(os.environ['PATH'])
# print(os.getcwd())
# f = os.system("ls -a")
# print(f)

# import shutil
# shutil.copy("test.txt", "text_copy.txt")

# import glob
# print(glob.glob("/Users/youngkwangkim/PycharmProjects/python-basic/jumpToPython/t*"))

import tempfile
# file_name = tempfile.mktemp()
# print(file_name)
# f = tempfile.TemporaryFile()
# f.close()

import time
# print(time.localtime(time.time()))
# print(time.asctime(time.localtime(time.time())))
# print(time.ctime())
# print(time.strftime("%a", time.localtime(time.time())))
# print(time.strftime("%A", time.localtime(time.time())))
# print(time.strftime("%x", time.localtime(time.time())))
# print(time.strftime("%X", time.localtime(time.time())))
# print(time.strftime("%c", time.localtime(time.time())))

# for i,v in enumerate(range(10)):
#     print(i,v)
#     time.sleep(1.0)

# import random
# print(random.random())
# print(random.randint(1,10))
#
#
# def random_pop(data):
#     number = random.randint(0,len(data)-1)
#     return data.pop(number)


# import random
# def random_pop(data):
#     number = random.choice(data)
#     data.remove(number)
#     return number
#
#
# if __name__=="__main__":
#     data = [1,2,3,4,5]
#     while data:
#         print(random_pop(data))


# import webbrowser
# webbrowser.open("http://google.com")


# import threading
# import time
#
# def say(msg):
#     while True:
#         time.sleep(1)
#         print(msg)
#
# for msg in ['test1','test2','test3']:
#     t = threading.Thread(target=say, args=(msg,))
#     t.daemon = True
#     t.start()
#
#
# for i in range(100):
#     time.sleep(0.1)
#     print(i)



# import threading
# import time
#
#
# class MyThread(threading.Thread):
#     def __init__(self, msg):
#         threading.Thread.__init__(self) # thred를 클래스로 정의할 경우 반드시
#         self.msg = msg
#         self.daemon = True
#
#     def run(self):
#         while True:
#             time.sleep(1)
#             print(self.msg)
#
#
# for msg in ['you','need','python']:
#     t = MyThread(msg)
#     t.start()
#
# for i in range(100):
#     time.sleep(0.1)
#     print(i)


# class q1
# class Calculator:
#     _result = 0
#     def __init__(self, number_list):
#         self.number_list = number_list
#
#     def sum(self):
#         self._result = 0
#         for i in self.number_list:
#             self._result += i
#         print(self._result)
#         return self._result
#
#     def avg(self):
#         avg = self._result / len(self.number_list)
#         print(avg)
#
#
# cal1 = Calculator([1,2,3,4,5])
# cal1.sum()
# cal1.avg()


# def GuGu(n):
#     result = []
#     for i in range(1,10):
#         result.append(n*i)
#     return result
#
# result = GuGu(2)
# print(result)

# result = 0
# for n in range(1,1000):
#     if n % 3 == 0 or n % 5 == 0 :
#         result += n
# print(result)


# def getTotalPage(m,n):
#     if m % n ==0:
#         a = m // n
#         print(a)
#         return a
#     else:
#         a = m // n + 1
#         print(a)
#         return a
#
# getTotalPage(5,10)
# getTotalPage(15,10)
# getTotalPage(30,10)


# import sys
# option = sys.argv[1]
# print(option)
#
# if option == '-a':
#     memo = sys.argv[2]
#     print(memo)
#     f = open("memo.txt",'a')
#     f.write(memo)
#     f.write("\n")
#     f.close()


# import os
#
#
# def search(dir_name):
#     try:
#         fnames = os.listdir(dir_name)
#         for fnm in fnames:
#             full_file_name = os.path.join(dir_name,fnm)
#             if os.path.isdir(full_file_name):
#                 search(full_file_name)
#             else:
#                 ext = os.path.splitext(full_file_name)[-1]
#                 # print((ext))
#                 # print(full_file_name)
#                 if ext == '.py':
#                     print(full_file_name)
#     except PermissionError as e:
#         print(e)
#
#
# print("~~"*30)
# search("/Users/youngkwangkim/PycharmProjects/python-basic/jumpToPython")


# import re
#
# p = re.compile('[a-z]+')
#
# m = p.match("python")
# print(m.group())
# m = p.match("3 python")
# print(m)
#
# m = p.search("python")
# print(m)
# m = p.search("3 python")
# print(m)
#
# result = p.findall("life is too short")
# print(result)


# from xml.etree.ElementTree import Element, SubElement, dump
#
# note = Element("note")
# # to = Element("to")
# # to.text = "Tove"
# # note.append(to)
# SubElement(note,"from").text = 'Jani'
# SubElement(note,"to").text = 'Tove'
# note.attrib["date"] = "20151231"
#
#
# def indent(elem, level=0):
#     i = "\n" + level*"  "
#     j = "\n" + (level-1)*"  "
#     if len(elem):
#         if not elem.text or not elem.text.strip():
#             elem.text = i + "  "
#         if not elem.tail or not elem.tail.strip():
#             elem.tail = i
#         for subelem in elem:
#             indent(subelem, level+1)
#         if not elem.tail or not elem.tail.strip():
#             elem.tail = j
#     else:
#         if level and (not elem.tail or not elem.tail.strip()):
#             elem.tail = j
#     return elem
#
# indent(note)
# dump(note)
