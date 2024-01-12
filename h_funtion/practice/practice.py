# 상품 정보(상품명, 가격)를 여러 개 전달받은 뒤 번호를 1부터 순서대로 붙여준다.
# 함수1. 상품의 정보를 추가하는 함수
# 함수2. 상품의 정보를 수정하는 함수
# 함수3. 상품의 전체 정보를 조회하는 함수
# 함수1, 함수2, 함수3을 합쳐서 하나의 함수로 만든다.
# ----------------------------------------------------------------------------------------------------------------------
# 알고리즘
# 1. 첫번째로 상품을 정의 하는 함수 선언
#(상품명, 가격)을 여러개 받아야 하므로 개수는 1씩 증가한다. 전역변수로 처음에 count라는 전역 변수 선언
# 필요한 변수(keyword) : name , price
# 2. 상품 정보 추가 함수 (상품 함수 안의 변수) 즉 closure 함수를 선언한다.
# 3. 상품 전체 정보를 수정 하는 함수
# 4. 상품의 전체 정보를 조회 하는 함수
# 5. 함수1+함수2+함수3

# def set_product(*args): # 초기 상품 정보 함수
#     number = 0 # 상품 번호
#
#     for product in args: # args : 상품 리스트
#         number += 1 # number는 1씩 커진다.
#         product['number'] = number # product 리스트의 number 키 값은 number
#
#     def insert(**kwargs):
#         nonlocal number, args
#         number += 1
#         args += {'name': kwargs.get('name'), 'price': kwargs.get('price'), 'number': number},
#
#     def update(**kwargs):
#         for product in args:
#             if product['number'] == kwargs.get('number'):
#                 product['name'] = kwargs.get('name')
#                 product['price'] = kwargs.get('price')
#                 break
#
#     def select_all():
#         return args
#
#     return {'insert': insert, 'update': update, 'select_all': select_all}
#
#
# products = [
#     {'name': '마우스', 'price': 5000},
#     {'name': '키보드', 'price': 25000}
# ]
#
# product_service = set_product(*products)
# print(products)
# product_service.get('insert')(name='모니터', price=80000)
# print(product_service.get('select_all')())
# product_service.get('update')(name='키보드', price=20000, number=2)
# print(product_service.get('select_all')())

# ----------------------------------------------------------------------------------------------------------------------
# def blog_printer(*blogs):
#     for post in blogs:
#         print(post)
#
# blog1 = "첫 번째 블로그"
# blog2 = "두 번째 블로그"
# blog3 = "세 번째 블로그"
#
# blog_printer(blog1, blog2, blog3)
# ----------------------------------------------------------------------------------------------------------------------
# [과제 문제]
# 회원의 주문 금액(pay)과 회원의 쿠폰 할인율과 개수(coupons, count)를 전달받은 뒤
# 회원이 보유한 쿠폰의 할인율을 주문 금액에 순차 적용하는 함수를 제작
# 할인율이 적용된 주문 금액이 정수로 리턴된다.
# 쿠폰의 할인율은 백분율로 되어있다.
# 쿠폰의 개수는 주문 개수보다 많을 수 있다.
# (권장) comprehension을 사용한다
# 주문 금액 = pay 쿠폰 할인율,개수 (coupon,count)

def discount_sale(*args,**kwargs) :
    '''
    :param pay : 주문금액
    :param coupons:
    :param count:
    :return: pay - (pay * (0.01 * coupon))
    '''
    result = [int(args[i] - (args[i]*(0.01 * kwargs["coupons"])))for i in range(kwargs["count"]) if len(args) >= i+1]
    return result

args1 = [3000,2000,4000]
kwargs1 = {'coupons':50,
            'count': 3}

total_result = discount_sale(*args1,**kwargs1)
print(total_result)
# ----------------------------------------------------------------------------------------------------------------------

