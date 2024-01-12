# '택시'에서 승객들에게 공통적으로 적용되는 자료
# - 기본 요금 : 5800원
# - 기본 주행 거리 : 2km
# - 택시 요금(기본 주행 거리 이후 거리 1km 당 요금)  : 1000원

# 1. 택시 객체 생성 시 승객 별로 돈과, 거리를 받아서 생성
# 2. 택시 객체 생성 시 택시 수익을 초기화한다.

# 1. 거리에 따른 요금 계산 메소드 정의
# 2. 거리에 따른 요금 계산 메소드 정의(승객의 돈과 거리를 전달받는다)
# 거리에 따른 잔돈 계산 메소드 정의

# 1.
# class Taxi:
#     default_fare = 5800
#     default_distance = 2
#     fare_per_km = 1000
#
#     def __init__(self, money, distance):
#         self.money = money
#         self.distance = distance
#
#     def calculate_fare(self):
#         cost = Taxi.default_fare
#         if self.distance > Taxi.default_distance:
#             cost += (self.distance - Taxi.default_distance) * Taxi.fare_per_km
#
#         return cost
#
#     def get_change(self):
#         return self.money - self.calculate_fare()
#
#
# taxi = Taxi(20000, 1)
# print(taxi.calculate_fare(), taxi.get_change())
#
# taxi = Taxi(30000, 10)
# print(taxi.calculate_fare(), taxi.get_change())


# 2.
class Taxi:
    default_fare = 5800
    default_distance = 2
    fare_per_km = 1000

    def __init__(self):
        self.income = 0

    def calculate_fare(self, money, distance):
        cost = Taxi.default_fare
        if distance > Taxi.default_distance:
            cost += (distance - Taxi.default_distance) * Taxi.fare_per_km

        self.income += cost

        def get_change():
            return money - cost

        return cost, get_change()


taxi = Taxi()
print(taxi.calculate_fare(20000, 1))
print(taxi.calculate_fare(30000, 10))
print(taxi.income)







