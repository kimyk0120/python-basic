def line_separate():
    print("\n*" * 5)


""" Exception """


def ten_div(x):
    return 10 / x


# print(ten_div(2))
# print(ten_div(0))

line_separate()

# try:
#     x = int(input(':'))
#     y = 10 / x
#     print(y)
# except:
#     print("test")


# y = [10, 20, 30]
#
# try:
#     index, x = map(int, input(':').split())
#     print(y[index] / x)
#     # print(y[index] / x)
# except ZeroDivisionError as e:
#     print("e : ", e)
# except IndexError as e:
#     print("e : ", e)



# try:
#     x = int(input(':'))
#     y = 10 / x
# except ZeroDivisionError as e:
#     print("e : ", e)
# else:
#     print(y)
# finally:
#     print("script end")
#

'''raise'''

# try:
#     x = int(input(':'))
#     if x % 3 != 0:
#         raise Exception("test exception")
# except Exception as e:
#     print(e)


# def three_multiple():
#     x = int(input(":"))
#     if x % 3 != 0:
#         raise Exception("nono")
#     print(x)
#
#
# try:
#     three_multiple()
# except Exception as e:
#     print("test ex : ", e)


''' extend Exception '''


# class NotThreeMultipleError(Exception):
#     def __init__(self):
#         super().__init__('not 3 multiple')
#
#
# def three_multiple():
#     try:
#         x = int(input('\n : '))
#         if x % 3 != 0:
#             raise NotThreeMultipleError
#         print(x)
#     except Exception as e:
#         print("Exception : ", e)
#
#
# three_multiple()


''' iterator '''

print(dir([1,2,3]))
print([1,2,3].__iter__())

it = [1,2,3].__iter__()
print(it.__next__())
print(it.__next__())
print(it.__next__())
# print(it.__next__()) #  StopIteration

line_separate()


class Counter:
    def __init__(self, stop):
        self.current = 0
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.stop:
            r = self.current
            self.current += 1
            return r
        else:
            raise StopIteration


for i in Counter(3):
    print(i, end=' ')


line_separate()

a, b, c = Counter(3)
print(a, b, c)
a,b,c,d,e = Counter(5)
print(a,b,c,d,e)


# a = list(map(int, [1.2, 2.2]))
# print(a)

line_separate()


class Counter:
    def __init__(self, stop):
        self.stop = stop

    def __getitem__(self, index):
        if index < self.stop:
            return index
        else:
            raise IndexError


print(Counter(3)[0], Counter(3)[1], Counter(3)[2])
for i in Counter(3):
    print(i, end=' ')

line_separate()

it = iter(range(3))
print(next(it))
print(next(it))
print(next(it))

line_separate()

import random

# it = iter(lambda :random.randint(0,5),2)
# print(next(it))
# print(next(it))
# print(next(it))

line_separate()
# for i in iter(lambda : random.randint(0,5), 2):
#     print(i, end=' ')

while True:
    i = random.randint(0, 5)
    if i == 2:
        break
    print(i, end=' ')


line_separate()


''' generator '''


def number_generator():
    yield 0
    yield 1
    yield 2


for i in number_generator():
    print(i)

n = number_generator()
print(n)
print(dir(n))


line_separate()

''' regular expression '''

import re

print(re.match('Hello', 'Hello, world'))
print(re.match('Python', 'Hello, world'))  # None
a = re.match('Hello', 'Hello, world')
print(dir(a))
# print(a.string)
line_separate()
print(re.search('^Hello', 'Hello, world'))
print(re.search('world$', 'Hello, world'))
print(re.search('hello|world', 'hello, world'))

# * 0개 이상
# + 1개 이상
line_separate()
print(re.match('[0-9]*', '1234'))
print(re.match('[0-9]+', '1234'))
print(re.match('[0-9]+', 'abcd'))

# ? 뒤에 0개 또는 1개
# . 뒤에 문자 1개
line_separate()
print(re.match('H?','HH'))
print(re.match('H?','Hi'))
print(re.match('H.','Hi'))
print(re.match('H.','H'))  # None

# 문자{개수}
# (문자열){개수}
line_separate()
print(re.match('h{3}','hhhi'))
print(re.match('(hi){1}','hhhi'))  # None
print(re.match('(hh){1}','hhhi'))
print(re.match('(hi){3}','hhhi'))  # None

line_separate()
print(re.match('[0-9]{3}-[0-9]{4}-[0-9]{4}', '010-0000-0000'))
print(re.match('[0-9]{3}-[0-9]{4}-[0-9]{4}', '010-0000-000'))  # None
print(re.match('[0-9]{2,3}-[0-9]{3,4}-[0-9]{3,4}', '010-0000-0000'))
print(re.match('[0-9]{2,3}-[0-9]{3,4}-[0-9]{3,4}', '010-00-0000'))  # None

line_separate()
print(re.match('[a-zA-Z0-9]+', 'Hello1234'))
print(re.match('[A-Z0-9]+', 'hello'))  # None

# Not
line_separate()
print(re.match('[^A-Z]+', 'Hello'))  # None
print(re.match('[^A-Z]+', 'hello'))

# 범위로 시작하는지
line_separate()
print(re.search('^[A-Z]+', 'Hello'))
print(re.search('^[A-Z]+', 'hello'))  # None
# 범위로 끝나는지
print(re.search('[0-9]+$', 'hello1234'))
print(re.search('[0-9]+$', 'hello'))  # None

'''
    re.match()와 re.search()의 차이
    re.match()의 경우 대상 문자열의 시작부터 검색을 하지만,
    re.search()함수는 대상 문자열 전체에 대해서 검색을 수행한다.
'''

line_separate()
print(re.search('\*+', '1 ** 2'))
print(re.search('\*+', '1  2'))  # None
print(re.match('[$()a-zA-Z0-9]+', '$(document)'))

# \d = [0-9]
# \D = [^0-9]
# \w = [a-zA-Z0-9]
# \W = [^a-zA-Z0-9]

line_separate()
print(re.match('\d', '1234'))
print(re.match('\D', 'he'))
print(re.match('\w+', 'he_1234'))
print(re.match('\W+', '(:)'))

# \s = 공백
line_separate()
print(re.match('[a-zA-Z0-9 ]+', 'Hello 1234'))
print(re.match('[a-zA-Z0-9\s]+', 'Hello 1234'))

print(re.findall('[0-9]+', '1 2 fii fii 4 fii5 89'))

print(re.sub('apple|orange', 'fruit', 'apple box orange tree'))
print(re.sub('[0-9]+', 'n', '1 2 fizz buzz 4 buzz 45'))

line_separate()


import math
print(math.pi)

line_separate()
# import urllib.request
# response = urllib.request.urlopen('http://www.google.co.kr')


import requests
r = requests.get('http://www.google.com')
print(r.status_code)



'''
    module
'''

line_separate()
import calc
print(calc.add(50, 100))
print(calc.mul(50, 100))


line_separate()

# import calcpkg.operation
# import calcpkg.geometry
#
# print(calcpkg.operation.add(10, 20))
# print(calcpkg.geometry.rectangle_area(30, 40))

# from calcpkg.operation import add, mul
# from calcpkg.geometry import rectangle_area, triangle_area
#
# print(mul(10, 20))
# print(triangle_area(10, 20))
#
# import sys
# print(sys.path)

import calcpkg

print(calcpkg.operation.add(10, 20))
print(calcpkg.geometry.triangle_area(10, 20))


