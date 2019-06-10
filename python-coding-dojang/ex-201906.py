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


