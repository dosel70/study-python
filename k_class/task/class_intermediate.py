# 상품
# 상품명, 가격
# 상품의 정보를 print()로 출력하는 함수
class Product: # 상품 클래스
    def __init__(self,product_name,product_price,product_count): # 상품 이름과 상품 가격을 정의
        self.product_name = product_name # 상품 이름
        self.product_price = product_price # 상품 가격
        self.product_count = product_count # 상품 재고

    def print_product_info(self): # 상품 정보
        print(f'상품명 : {self.product_name}, 가격 : {self.product_price}원 , 재고 : {self.product_count}개\n')


# 손님
# 이름, 나이, 할인율, 잔액
class User : # 회원 클래스
    def __init__(self,user_name,user_Age,user_discount,user_money): # 유저 이름, 나이, 할인율, 잔액 정보
        self.user_name = user_name
        self.user_Age = user_Age
        self.user_discount = user_discount
        self.user_money = user_money


# 마켓
# 상품, 재고
# 손님 한 명에게 한 개의 상품을 판매한다.
# 판매 시 손님의 할인율을 적용하여 판매한다.
class Marcket:
    def __init__(self,product,count = 5):
        self.product = product
        self.count = count
    def sell_product(self,user):
        if self.count > 0: # 재고가 있을 때
            discount_price = self.product.product_price * (1 - user.user_discount * 0.01)
            # 할인율을 적용구하는 법을 까먹어서 이거는 구글링 함
            if discount_price < user.user_money: # 사용자 금액이 더 클때 구매도 할 수 있고 할인도 받을 수 있다.
                user.user_money -= discount_price
                self.count -= 1
                self.product.product_count -= 1
                print(f"{user.user_name}님 , {self.product.product_name}을 {discount_price}원에 구매하셨습니다. "
                      f"\n남은 잔액 : {user.user_money}원 "
                      f"\n남은 재고 : {self.product.product_count}개"
                      f"\n적용된 할인율 : {user.user_discount}%\n\n")


            else :
                print(f"{user.user_name}님 잔액이 부족하여 구매할 수 없습니다.")
        else : # 재고가 없을 때 (count =< 0)
            print("상품 재고가 부족합니다.")
# class Market():
#     def __init__(self, product, stock):
#         self.product = product
#
#     def sell(self, customer):
#         self.product.price - customer.discount

# 상품 객체
phone = Product("핸드폰",900000,30)
air_conditioner = Product("에어컨", 150000000,5)


# 마켓 객체
market = Marcket(air_conditioner)
market1 = Marcket(phone)

# 손님 객체
customer = User("홍길동", 25, 50, 2000000000)


# 상품 정보 출력
air_conditioner.print_product_info()
phone.print_product_info()

# 상품 판매
market.sell_product(customer)
market1.sell_product(customer)


# class Product():
#     pass
#
#

#
#
# class Customer():
#     pass





