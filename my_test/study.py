class Car :
    brand = ""
    color = ""
    price = 0

    def __init__(self, brand, color, price) :
        # 초기화 목적
        self.brand = brand
        self.color = color
        self.price = price
    def engineStart(self):
        print(self.brand + "시동 킴")
        print(self.color + "색 차를 가지셨네요")
        print(self.price , "원이라구요??")


# momcar = Car("Mercedes", "Blue", 45000)
# print(momcar)
# momcar.engineStart()
#
# # n = input()
# # numbers = list(input())
# # sum = 0
# #
# # for i in numbers:
# #     sum = sum + int(i)
# #
# # print(sum)
#
# n = int(input())
# mylist = list(map(int, input().split()))
# mymax = max(mylist)
# sum = sum(mylist)
# print(sum * 100 / mymax / int(n))