# Jump To Python
# "Life is too short, You need Python"

# if 4 in [1,2,3,4]:
#     print(4)

# lang_list = ['python', 'perl' ,'c', 'java']
# for lang in lang_list:
#     if lang in ['python','perl']:
#         print('%6s need interpreter' % lang)
#     elif lang in ['c','java']:
#         print('%6s need compiler' % lang)
#     else:
#         print("should not reach here")

# a = 2
# b = 3
# c = 2**3
# print(c)

# print("%"*100)
# a= "Life is too short, You need Python"
# print(a[3])
# print(a[-2])

# a = 'Pythin'
# b = a[:4]
# c = a[-1]
# print(b , c)
# d = b + "o" + c
# print(d)

# a = "Test formatting number : %d"
# print(a % 3)
# b= "Test formatting string : %s"
# print(b % 'kim')

# c = 5
# a = "Test formatting number : %d"
# print(a % c)
# d = 'text'
# a = "Test formatting n,s : %d %s"
# print(a % (c,d))

# b  = 5
# c = 3.42
# a = "Test formatting: %s , %s"
# print(a % (b,c))

# a = "Error is %d%%"
# print(a % 56)

# print("%10s" % 'test')
# print("%10s" % 'test1',"%-10s" % 'test2' )

# a = 'tessst'
# print(a.count('s')) # 해당 텍스트 개수 반환
# print(a.find('s'))
# print(a.find('k'))
# print(a.index('s'))
# print(a.index('k'))

# a = ','
# b = a.join('abcd')
# print(b)

# a = 'Hello'
# print(a.upper());
# print(a.lower());

# a = "  hi  ";
# print(a.rstrip()); print(a.lstrip()); print(a.strip())

# a = ' a replace b '
# a = a.replace('a','c'); a = a.replace('b', 'd')
# print(a)

# a = 'a, b, c, d'
# b = a.split(',')
# print(b)

# a = ['a','b','c']
# b= len(a)
# print(b)
# print(a[b-1])
# print(a[-1])

# a = [1, 2, 3, [4, 5, 6]]
# print(a[-1][0])

# a = [1,2,3,4,5]
# print(a[2:4]) # 2번부터 3번까지

# a = [1,4,3]
# b = [4,5,6]
# print(a+b) #[1, 4, 3, 4, 5, 6]

# a = [1,2,3]
# print(a*3)
# print('test'+str(a[2]) , ' type : ', type(a[0]), type(str(a[2])))
# a[2] = 4
# print(a)
# print(a[1:2]) # 1번부터 1번까지
# # a[1:2] = ['a','b','c']
# # print(a)
# print(a)
# a[1:3] = ['a','b','c'] #[1, 'a', 'b', 'c']
# print(a)

# a = [1,2,3]
# a[1] = ['a','b','c']
# print(a)

# a = [1,2,3]
# a[1:2] = ['a','b','c']
# print(a) #[1, 'a', 'b', 'c', 3]
# a[1:3] = [] #[1, 'c', 3]
# a[2] = 4
# print(a)
# del a[1]
# print(a)
#
# b = 'a'
# del b
# print(b) #name 'b' is not defined

# a = [1,2,3]
# a.append(4)
# print(a)
# a.append([5,6])
# print(a)
# a = [1,4,3,2]
# print(a)
# a.sort()
# print(a)
# a = ['a','b','c']
# a.reverse()
# print(a)
# a = [1,2,3]
# print(a)
# print(a.index(3)) #Return first index of value.

# a = [1,2,3]
# a.insert(5,4)
# print(a)
# a.insert(2,'a')
# print(a)
# a.remove(2)
# print(a) #Remove first occurrence of value.
#
# a = [1,2,3]
# print(a)
# print(a.pop()) #Remove and return item at index (default last).
# print(a)
#
# a = [1,2,3]
# print(a.pop(1))
# print(a)

# a = [1,2,3,1]
# print(a.count(1))

# a = [1,2,3]
# a.extend([4,5])
# print(a)

# a = {'a':1,'b':2,'c':3,'d':[4,5,6]}

# a = {1: "z"}
# a[2] = 'b'   # a[key] = value 수정/추가
# print(a)
# a[1] = 'a'
# print(a)
# a['name'] = 'yk'
# print(a)
# del a[1]
# print(a)
# a[3] = [1,2,3]
# print(a)
# del(a[3])
# print(a)
# print(len(a))
# print(a['name'])

# a = {[1,2]:'a'} #unhashable
# a = {(1,2):'a'}
# print(a[(1,2)])






