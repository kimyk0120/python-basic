def linn_sef():
    print("\n*" * 5)


a = [[10, 20], [30, 40], [50, 60]]

i = 0
while i < len(a):
    j = 0
    while j < len(a[i]):
        print(a[i][j], end=' ')
        j += 1
    print()
    i += 1

linn_sef()

a = []
for i in range(10):
    a.append(0)

print(a)

linn_sef()

a = []

for i in range(3):
    line = []
    for j in range(2):
        line.append(0)
    a.append(line)

print(a)

linn_sef()

a = [[0 for j in range(2)] for i in range(3)]

print(a)

linn_sef()

a = [[0]*2 for i in range(3)]

print(a)

linn_sef()

a = [3,1,3,2,5]
b = []

for i in a:
    line = []
    for j in range(i):
        line.append(0)
    b.append(line)

print(b)

linn_sef()

a = [[0]*i for i in [3,1,3,2,5]]
print(a)
linn_sef()

a = [[10, 20],[30, 40]]
b = a
b[0][0] = 500
print(a)
print(b)
linn_sef()
a = [[10, 20],[30, 40]]
b = a.copy()
b[0][0] = 500
print(a)
print(b)
linn_sef()
a = [[10, 20],[30, 40]]
import copy
b = copy.deepcopy(a)
b[0][0] = 500
print(a)
print(b)
linn_sef()
a = [[[0 for col in range(3)]for row in range(4)]for depth in range(2)]  # 가로 세로 높이
print(a)
linn_sef()
table = str.maketrans('a', '1')
result = 'apple'.translate(table)
print(result)
table = 'apple pear grape'
fruits = table.split()
print(fruits)
linn_sef()
table = 'apple,pear,grape'
fruits = table.split(",")
print(fruits)
linn_sef()
join_str = " ".join(fruits)
print(join_str)
join_str = "-".join(fruits)
print(join_str)
linn_sef()
a = '35'.zfill(4)
print(a)
a = '3.5'.zfill(6)
print(a)
a = 'hello'.zfill(10)
print(a)
linn_sef()
a = 'apple pineapple'.find('pl')
print(a)
a = 'apple pineapple'.rfind('pl')
print(a)  # 12
a = 'apple pineapple'.rfind('xy')
print(a)  # -1
linn_sef()
print('%s %s' % ('test1', 'test2'))
print('%d age' % 20)
linn_sef()
print('%f' % 2.3)
print('%.3f' % 2.3)
print('%.2f' % 2.3)
print('%.1f' % 2.3)
linn_sef()
print('Hello, {0}'.format('world!'))
print('Hello, {0}'.format(100))
print('Hello, {0} {2} {1}'.format('python', 'script', 3.6))
print('{0} {0} {1} {1}'.format('python', 'script'))
print('{} {}'.format('python', 'script'))
print('abc, {lang} {version}'.format(lang='ko', version=1.1))
lang = 'Python'
version = 3.6
print(f'Hello, {lang} {version}')
print('{0:<10}'.format('python'))
print('{0:>10}'.format('python'))
print('{:>10}'.format('python'))
linn_sef()
print('%03d' % 1)
print('{0:03d}'.format(35))
print('%08.2f' % 3.6)
print('{0:08.2f}'.format(150.37))
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.setdefault('e')
print(x)
x.setdefault('f', 100)
print(x)
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.update(a=90)
print(x)
x.update(e=100)
print(x)
x.update(a=900, f=200)
print(x)
y = {1: 'one', 2: 'two'}
y.update({1: 'ONE', 2: 'TWO'})
print(y)  # {1: 'ONE', 2: 'TWO'}
y.update([(2, "TWO2"), [3, 'THREE'], [4, 'FOUR']])
print(y)
linn_sef()
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.pop('a'))
print(x)
print(x.pop('z', 0))
print(x)
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
del x['a']
print(x)
print(x['c'])
print(x.popitem())
linn_sef()
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# x.clear()
# print(x)
print(x.get('a'))
print(x.get('z', 10))
print(x.items())
print(x.keys())
print(x.values())
keys = {'a', 'b', 'c', 'd'}
x = dict.fromkeys(keys)
print(x)
y = dict.fromkeys(keys, 100)
print(y)
print(int())


linn_sef()

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for i in x:
    print(i, end=' ')
linn_sef()
for k, v in x.items():
    print(k, v)

linn_sef()

for key, value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.items():
    print(key, value)

linn_sef()
for key in x.keys():
    print(key, end=' ')

linn_sef()
for v in x.values():
    print(v, end=' ')
linn_sef()
keys = ['a', 'b', 'c', 'd']
x = {key: value for key, value in dict.fromkeys(keys).items()}
print(x)

linn_sef()

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x = {key: value for key, value in x.items() if value != 20}
print(x)

linn_sef()
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x = {key: 0 for key, value in x.items()}
print(x)
y = x
print(y)
print(x is y)
# y['a'] = 99
# print(x)

y = x.copy()
print(x)
print(y)
print(x is y)
print(x == y)

y['a'] = 99
print(x)
print(y)

linn_sef()
x = {'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
y = x.copy()
print(x)
print(y)
# y['a']['python'] = '2.7.15'
# print(x)
# print(y)
import copy
y = copy.deepcopy(x)
y['a']['python'] = '2.7.15'
print(x)
print(y)

linn_sef()
maria = {'a': 90, 'b': 87, 'c': 98, 'd': 67}
average = sum(maria.values()) / len(maria)
print(average)

linn_sef()

xSet = {'a', 'b', 'c', 'd', 'a', 'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
print(xSet)
# print(xSet['a'])
print('a' in xSet)
print('f' in xSet)
print('a' not in xSet)
print('f' not in xSet)
linn_sef()
a = set('apple')
print(a)
b = set(range(5))
print(b)
c = set()
print(c)
print(type(c))
c = {}
print(type(c))

linn_sef()
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)
print(set.union(a, b))
print(a & b)
print(set.intersection(a, b))
print(a - b)
print(set.difference(a, b))
print(set.difference(b, a))
print(a ^ b)  # 대칭차집합
print(set.symmetric_difference(a, b))
linn_sef()
a = {1, 2, 3, 4}
a |= {5}
print(a)
a = {1, 2, 3, 4}
a.update({5})
print(a)
linn_sef()
a = {1, 2, 3, 4}
a &= {1, 2, 3, 4, 5}
print(a)
a = {1, 2, 3, 4}
a.intersection_update({0,1,2,3,4})
print(a)
a = {1, 2, 3, 4}
a -= {3}
print(a)

a = {1, 2, 3, 4}
a.difference_update({3})
print(a)

a = {1, 2, 3, 4}
a ^= {3,4,5,6}
print(a)
a = {1, 2, 3, 4}
a.symmetric_difference_update({3,4,5,6})
print(a)

linn_sef()
a = {i for i in range(1, 101) if i % 3 == 0}
b = {i for i in range(1, 101) if i % 5 == 0}
print(set.intersection(a, b))

linn_sef()
file = open('hello.txt', 'r')
a = file.read()
print(a)
file.close()
linn_sef()
with open('hello.txt', 'r') as file:
    s = file.read()
    print(s)

linn_sef()
with open('hello.txt', 'w') as file:
    for i in range(3):
        file.write(' text {0}\n'.format(i))

lines = ['a\n', 'b\n', 'c\n']
with open('hello.txt', 'w') as file:
    file.writelines(lines)

with open('hello.txt', 'r') as file:
    print(file.readlines())

with open('hello.txt', 'r') as file:
    print(file.read())

with open('hello.txt', 'r') as file:
    line = None
    while line != '':
        line = file.readline()
        print(line, end='')

linn_sef()

with open('hello.txt', 'r') as file:
    for line in file:
        print(line.strip('\n'))

linn_sef()

import pickle

name = 'james'
age = 17
address = "ui-wang, korea"
scores = {'kor': 90, 'eng': 95, 'math': 80, 'science': 82}
with open('james.p', 'wb') as file:
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)

with open('james.p', 'rb') as file:
    a = pickle.load(file)
    b = pickle.load(file)
    c = pickle.load(file)
    d = pickle.load(file)
    print(a)
    print(b)
    print(c)
    print(d)

linn_sef(); linn_sef()

'''
    회문판별
'''

word = 'level'
word_len = len(word)
quotient = word_len // 2
print(word_len)
print(quotient)
is_palindrome = True
for i in range(len(word) // 2):  # // -> 몫
    if word[i] != word[-(1+i)]:
        is_palindrome = False
        break
print(is_palindrome)

linn_sef()

# is 는 레퍼런스 체크
# == 는 값 체크

word = 'level'
print(word[::-1])  # a[ start : end : step ]
print(word == word[::-1])

word = 'level'
print(list(word) == list(reversed(word)))

linn_sef()

'''
    N-gram : N개의 연속된 요소를 추출
'''
text = 'hello'
for i in range(len(text)-1):
    print(text[i], text[i+1], sep='')

two_gram = zip(text, text[1:])
# print(two_gram)
for i in two_gram:
    print(i)

# zip(*iterable)은 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수이다.
'''
>>> list(zip([1, 2, 3], [4, 5, 6]))
[(1, 4), (2, 5), (3, 6)]
>>> list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
>>> list(zip("abc", "def"))
[('a', 'd'), ('b', 'e'), ('c', 'f')]
'''
text = 'this is python script'
words = text.split()
print(words)
a = list(zip(words, words[1:]))
print(a)

text = 'level'
print(list(zip(*[text[i:] for i in range(3)])))


''' 함수 '''


def add_sub(a, b):
    return a + b, a - b


x, y = add_sub(10, 2)
print(x)
print(y)
print(type(x))
x = add_sub(10, 2)
print(x)
print(type(x))

linn_sef()
x = [10, 20, 30]


def print_numbers(a, b, c):
    print(a, b, c)


# unpacking
print_numbers(*x)
print(*x)

print(words)
print(*words)

print_numbers(*[10,20,30])
# print_numbers(*[10,20])
linn_sef()


# variable arguments
def print_numbers(*args):
    for arg in args:
        print(arg)


print_numbers(11)
print_numbers(10, 20, 30, 40)
linn_sef()
x = [10]
y = [10, 20, 30, 40]
print_numbers(*x)
print_numbers(*y)


def p_info(n, a, add):
    print(n, a, add)


p_info(a=12, n='kyk', add='kor')
p_info(add='kor', a=12, n='kyk')

x = {'add': 'kor', 'n': 'kyk', 'a': 13}
# print(x)
p_info(*x)  # key
p_info(**x)


def p_info2(**kwargs):
    if 'name' in kwargs:
        print("name in")
    for kw, arg in kwargs.items():
        print(kw, arg, sep=',')


p_info2(**x)
linn_sef()
p_info2(name='kim')
p_info2(name='kim', age=12)


'''recursion'''


# def recursion_say():
#     print("recursion")
#     recursion_say()

# recursion_say()
linn_sef()


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


print(factorial(5))
