# line_seperate = lambda: print('\n*' * 5)
def line_separate():
    print("\n*" * 5)


''' lambda '''


def plus_ten(x):
    return x + 10


print(plus_ten(2))

print(lambda x: x + 10)  # <function <lambda> at 0x104fbc620>
a = lambda x: x + 10
print(a(3))
print((lambda x: x + 10)(5))

print(list(map(plus_ten, [1, 2, 3])))
print(list(map(lambda x: x + 10, [1, 2, 3])))

a = map(plus_ten, [1, 2, 3])
print(*a)

line_separate()

a = [x for x in range(1, 11)]
print(a)

b = list(map(lambda x: str(x) if x % 3 == 0 else x, a))
print(b)

line_separate()

a = [i for i in range(1, 6)]
b = [i for i in range(2, 11) if i % 2 == 0]
print(a)
print(b)

c = list(map(lambda x, y: x * y, a, b))
print(c)


def f(x):
    return 5 < x < 10


a = [i for i in range(1, 11)]
print(a)
print(list(filter(f, a)))
print(list(filter(lambda x: 5 < x < 10, a)))

line_separate()

''' closure '''

x = 10


def foo():
    global x
    x = 20
    print(x)


foo()
print(x)

line_separate()


def A():
    x = 10

    def B():
        nonlocal x
        x = 20

    B()
    print(x)


A()

line_separate()

import random

a = []
while True:
    # print("%d len : " % len(a))
    a.append(random.randrange(1, 101))
    a = list(set(a))
    if len(a) == 10:
        break

print(len(a))
print(a)

line_separate()


def calc():
    a = 3
    b = 5

    def mul_add(x):
        return a * x + b

    return mul_add


c = calc()
print(c(1))


def calc():
    a = 3
    b = 5
    return lambda x: a * x + b


c = calc()
print(c(2))
line_separate()

''' class'''


class Person:
    def __init__(self):
        self.hello = 'hello'

    def print_greeting(self):
        print(self.hello)


lbj = Person()
lbj.print_greeting()
line_separate()


class Person:
    def __init__(self, nm, age, addr):
        self.hello = 'hello'
        self.nm = nm
        self.age = age
        self.addr = addr

    def print_greeting(self):
        print('{0}, {1}'.format(self.hello, self.nm))


person = Person('kim', 12, 'kor')
person.print_greeting()
print(person.nm)
print(person.age)
print(person.addr)
line_separate()


class Person:
    def __init__(self, nm, age, addr, wallet):
        self.hello = 'hello'
        self.nm = nm
        self.age = age
        self.addr = addr
        self.__wallet = wallet

    def pay(self, amount):
        if amount > self.__wallet:
            print('insufficient')
            return
        self.__wallet -= amount
        print('{0} left'.format(self.__wallet))


person = Person('kim', 12, 'kor', 2000)
person.pay(300)
line_separate()


class Person:
    bag = []

    def put_bag(self, stuff):
        self.bag.append(stuff)


james = Person()
james.put_bag('book')

maria = Person()
maria.put_bag('key')

print(james.bag)
print(maria.bag)
line_separate()


class Person:
    def __init__(self):
        self.bag = []

    def put_bag(self, stuff):
        self.bag.append(stuff)


james = Person()
james.put_bag('book')

maria = Person()
maria.put_bag('key')

print(james.bag)
print(maria.bag)
line_separate()


class Person:
    __bag = []

    def put_bag(self, stuff):
        self.bag.append(stuff)


class Calc:
    @staticmethod
    def add(a, b):
        print(a + b)


Calc.add(1, 2)


class Person:
    count = 0

    def __init__(self):
        Person.count += 1

    @classmethod
    def print_count(cls):
        print('{0}명 생성'.format(cls.count))


james = Person()
maria = Person()

Person.print_count()

line_separate()


class Date:
    @staticmethod
    def is_date_valid(date_string):
        # print(date_string.split('-'))
        # print(list(map(int, date_string.split('-'))))
        year, month, day = map(int, date_string.split('-'))
        # print(year)
        # print(month)
        # print(day)
        return month <= 12 and day <= 31


if Date.is_date_valid("2019-05-21"):
    print("valid")
else:
    print("invalid")

line_separate()

''' 상속 '''


class Person:
    def greeting(self):
        print("hello")


class Student(Person):
    def study(self):
        print("study")


james = Student()
james.greeting()
james.study()

print(issubclass(Student,Person))






