def linn_sef():
    print("\n*" * 5)
#
#
# a = [[10, 20], [30, 40], [50, 60]]
#
# i = 0
# while i < len(a):
#     j = 0
#     while j < len(a[i]):
#         print(a[i][j], end=' ')
#         j += 1
#     print()
#     i += 1
#
# linn_sef()
#
# a = []
# for i in range(10):
#     a.append(0)
#
# print(a)
#
# linn_sef()
#
# a = []
#
# for i in range(3):
#     line = []
#     for j in range(2):
#         line.append(0)
#     a.append(line)
#
# print(a)
#
# linn_sef()
#
# a = [[0 for j in range(2)] for i in range(3)]
#
# print(a)
#
# linn_sef()
#
# a = [[0]*2 for i in range(3)]
#
# print(a)
#
# linn_sef()
#
# a = [3,1,3,2,5]
# b = []
#
# for i in a:
#     line = []
#     for j in range(i):
#         line.append(0)
#     b.append(line)
#
# print(b)
#
# linn_sef()
#
# a = [[0]*i for i in [3,1,3,2,5]]
# print(a)
# linn_sef()
#
# a = [[10, 20],[30, 40]]
# b = a
# b[0][0] = 500
# print(a)
# print(b)
# linn_sef()
# a = [[10, 20],[30, 40]]
# b = a.copy()
# b[0][0] = 500
# print(a)
# print(b)
# linn_sef()
# a = [[10, 20],[30, 40]]
# import copy
# b = copy.deepcopy(a)
# b[0][0] = 500
# print(a)
# print(b)
# linn_sef()
# a = [[[0 for col in range(3)]for row in range(4)]for depth in range(2)]  # 가로 세로 높이
# print(a)
# linn_sef()
# table = str.maketrans('a', '1')
# result = 'apple'.translate(table)
# print(result)
# table = 'apple pear grape'
# fruits = table.split()
# print(fruits)
# linn_sef()
# table = 'apple,pear,grape'
# fruits = table.split(",")
# print(fruits)
# linn_sef()
# join_str = " ".join(fruits)
# print(join_str)
# join_str = "-".join(fruits)
# print(join_str)
# linn_sef()
# a = '35'.zfill(4)
# print(a)
# a = '3.5'.zfill(6)
# print(a)
# a = 'hello'.zfill(10)
# print(a)
# linn_sef()
# a = 'apple pineapple'.find('pl')
# print(a)
# a = 'apple pineapple'.rfind('pl')
# print(a)  # 12
# a = 'apple pineapple'.rfind('xy')
# print(a)  # -1
# linn_sef()
# print('%s %s' % ('test1', 'test2'))
# print('%d age' % 20)
# linn_sef()
# print('%f' % 2.3)
# print('%.3f' % 2.3)
# print('%.2f' % 2.3)
# print('%.1f' % 2.3)
# linn_sef()
# print('Hello, {0}'.format('world!'))
# print('Hello, {0}'.format(100))
# print('Hello, {0} {2} {1}'.format('python', 'script', 3.6))
# print('{0} {0} {1} {1}'.format('python', 'script'))
# print('{} {}'.format('python', 'script'))
# print('abc, {lang} {version}'.format(lang='ko', version=1.1))
# lang = 'Python'
# version = 3.6
# print(f'Hello, {lang} {version}')
# print('{0:<10}'.format('python'))
# print('{0:>10}'.format('python'))
# print('{:>10}'.format('python'))
# linn_sef()
# print('%03d' % 1)
# print('{0:03d}'.format(35))
# print('%08.2f' % 3.6)
# print('{0:08.2f}'.format(150.37))
# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# x.setdefault('e')
# print(x)
# x.setdefault('f', 100)
# print(x)
# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# x.update(a=90)
# print(x)
# x.update(e=100)
# print(x)
# x.update(a=900, f=200)
# print(x)
# y = {1: 'one', 2: 'two'}
# y.update({1: 'ONE', 2: 'TWO'})
# print(y)  # {1: 'ONE', 2: 'TWO'}
# y.update([(2, "TWO2"), [3, 'THREE'], [4, 'FOUR']])
# print(y)
# linn_sef()
# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# print(x.pop('a'))
# print(x)
# print(x.pop('z', 0))
# print(x)
# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# del x['a']
# print(x)
# print(x['c'])
# print(x.popitem())
# linn_sef()
# x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# # x.clear()
# # print(x)
# print(x.get('a'))
# print(x.get('z', 10))
# print(x.items())
# print(x.keys())
# print(x.values())
# keys = {'a', 'b', 'c', 'd'}
# x = dict.fromkeys(keys)
# print(x)
# y = dict.fromkeys(keys, 100)
# print(y)
# print(int())


linn_sef()
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for i in x:
    print(i, end=' ')
linn_sef()
for k, v in x.items():
    print(k, v)





