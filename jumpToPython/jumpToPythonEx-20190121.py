'''

    class class_name(extends_class_name):
        class_var = ''

        def func_name(self, arg1, arg2...):
            func_contents


'''


class FourCal():
    def set_data(self, first, second):
        self.first = first
        self.second = second

    def sum_mul_sub_div(self):
        return self.first + self.second, self.first * self.second, self.first - self.second, self.first / self.second


a = FourCal()
b = FourCal()
# print(type(a))
# FourCal.set_data(a,4,2)
a.set_data(2,4)
# b.set_data(3,7)
# print("first",a.first)
# print("second",a.second)
# print("first",b.first)
# print("second",b.second)
c = a.sum_mul_sub_div()
c = list(c)
print(c)

