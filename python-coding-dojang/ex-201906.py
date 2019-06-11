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






