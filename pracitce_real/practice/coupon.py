# [과제 문제]
# 회원의 주문 금액(pay)과 회원의 쿠폰 할인율과 개수(coupons, count)를 전달받은 뒤
# 회원이 보유한 쿠폰의 할인율을 주문 금액에 순차 적용하는 함수를 제작
# 할인율이 적용된 주문 금액이 정수로 리턴된다.
# 쿠폰의 할인율은 백분율로 되어있다.
# 쿠폰의 개수는 주문 개수보다 많을 수 있다.
# (권장) comprehension을 사용한다
# 주문 금액 = pay 쿠폰 할인율,개수 (coupon,count)

# 1. 할인율이 적용된 discount_amount 함수를 제작
# > 매개변수 : 주문금액,할인율,개수가 필요
# > 각각 주문금액의 개수동안 반복해야함
# > total_discount = 주문금액 - ((할인율 *0.01) + 주문금액))

# 2. 주문금액에 대한 변수
# 3. 할인율, 개수에 대한 변수

def discount_amout(*args, **kwargs):
    '''
    args = 주문금액 리스트 , kwargs = 할인율과 쿠폰 개수 딕셔너리
    '''

    # comprehension 풀이
    pay = [int(args[i] - (args[i] * (kwargs["coupon"] * 0.01))) for i in range(kwargs["count"]) if len(args) >= i+1]

    return pay

args1 = [1000, 2000, 3000]

kwargs1 = {
    "coupon": 30,
    "count": 20
}
total = discount_amout(*args1,**kwargs1)
print(total)




