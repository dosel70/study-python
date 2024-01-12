# [과제 문제]
# 회원의 주문 금액(pay)과 회원의 쿠폰 할인율과 개수(coupons, count)를 전달받은 뒤
# 회원이 보유한 쿠폰의 할인율을 주문 금액에 순차 적용하는 함수를 제작
# 할인율이 적용된 주문 금액이 정수로 리턴된다.
# 쿠폰의 할인율은 백분율로 되어있다.
# 쿠폰의 개수는 주문 개수보다 많을 수 있다.
# (권장) comprehension을 사용한다
# 주문 금액 = pay 쿠폰 할인율,개수 (coupon,count)


# def discount_amount(*args,**kwargs) :
# *args는 가변 인자로 여러 개의 가격을 받을 수 있다
# **kwargs는 키워드 인자로 쿠폰 할인율과 쿠폰 개수를 받는다.

# result = []
# 결과를 담을 리스트를 생성한다.

# for i in range(kwargs["count"]):
# kwargs 변수의 count(개수) 만큼 반복한다!

#     if len(args) >= i+1 :
# args 변수를 길이로 반환하려면 (가격을 담을 변수) 무조건 값이 1보다 크거나 같아야하기 때문에
# 길이 값이 0이 되버리면 가격을 담은게 의미가 없어져버린다.

#         pay = int(args[i] - (args[i] * (0.01 * kwargs["coupon"])))
# 할인율이 적용된 금액을 담는 변수인 pay에 (전달받은 가격 - (전달받은 가격 x (백분율 x 할인율)) 이러한 값을 선언한다.

#         result.append(pay)
# 결과를 담을 리스트에 pay값을 계속 추가시킨다.

# return result
# 결과 값을 반환한다.

# comprehension 을 활용 (값 for 반복문 if 조건식)
# 결과를 담을 리스트를 생성한다.
# 결과 리스트의 각 요소는 쿠폰 할인이 적용된 가격을 나타낸다.
#     result = [int(args[i] - (args[i] * (0.01 * kwargs["coupon"])))for i in range(kwargs["count"]) if len(args) >= i+1]

#     # 최종적으로 결과 리스트를 반환한다.
#     return result


# args1 = [2000 ,4000 , 5000] # 전달할 가격 리스트

# kwargs1 = { # 전달할 쿠폰 할인율과 쿠폰 개수 >> (쿠폰정보)
#     "coupon" : 50,
#     "count" : 2
#     }

# total_result1 = discount_amount(*args1,**kwargs1) # discount_amount 함수를 호출하여 결과를 받아온다.

# print(total_result1) 출력!


# def discount_sale(*args, **kwargs):
#     # result = []
#     # for i in range(kwargs['count']):
#     #     if len(args) >= i + 1:
#     #         pay = int(args[i] - (args[i] * (0.01 * kwargs['coupon'])))
#     #         result.append(pay)
#     # return result
#
#
#     # comprehension 을 활용 (값 for 반복문 if 조건식)
#     # 결과를 담을 리스트를 생성한다.
#     # 결과 리스트의 각 요소는 쿠폰 할인이 적용된 가격을 나타낸다.
#
#     result = [int(args[i] - (args[i] * (0.01 * kwargs["coupon"])))
#         for i in range(kwargs["count"]) if len(args) >= i+1]
#     return result
#
#
#
#
#
# args1 = [1000, 4000, 5000]
# kwargs1 = {
#     "coupon": 50,
#     "count": 2
# }
#
# result1 = discount_sale(*args1, **kwargs1)
# print(result1)
#
# args2 = [1000, 4000, 5000]
# kwargs2 = {
#     "coupon": 30,
#     "count": 100
# }
#
# result2 = discount_sale(*args2, **kwargs2)
# print(result2)
#
# # comprehension 을 활용 (값 for 반복문 if 조건식)
# # 결과를 담을 리스트를 생성한다.
# # 결과 리스트의 각 요소는 쿠폰 할인이 적용된 가격을 나타낸다.
# #     result = [int(args[i] - (args[i] * (0.01 * kwargs["coupon"])))for i in range(kwargs["count"]) if len(args) >= i+1]

def use_coupon(*pay,**kwargs) :
    '''
    :param pay: 주문금액들
    :param kwargs: {coupon : 할인율, count : 쿠폰의 개수}
    :return: 결과값
    '''
    if 'coupon' in kwargs :
        return[
            int((1 - kwargs['coupon'] * 0.01) * pay[i])
            for i in
            range(kwargs.get('count')if kwargs.get['count'] <= len(pay) else len(pay))
        ]
    return None

help(use_coupon)
result = use_coupon(1000,2000,3000,coupon=50,count=100)
if result:
    print(result)
else:
    print('쿠폰이 없습니다.')

