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




