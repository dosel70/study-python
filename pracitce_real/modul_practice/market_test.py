from market_module import *
from message01_module import *

if __name__ == '__main__':
    while True:
        product_choice = int(input(f"{title}{product1}"))

        menu_choice = int(input(f"{menu}"))
        if product_choice > len(product1):
            continue

        if menu_choice == 1:
            name = input("사용자 이름을 입력하세요 : ")
            while True:
                product = input("추가하실 상품명을 입력하세요 : ")
                if Product.check_product_name(product_name=product) is None:
                    break
            while True:
                price = input("설정 가격을 입력해주세요 : ")
                if Product.check_price(price=price) is None:
                    break
            while True:
                password = input("비밀번호를 입력해주세요 : ")
                if len(password) == 4:
                    break
                else:
                    continue
            while True:
                famous = (input("인기도를 입력해주세요 : "))
                if Product.check_famous(famous=famous) is None :
                    break
            user = Product.insert(product_choice, user_name = product,name=name, price=price, password=password,famous=famous)


        elif menu_choice == 2:
            name = input("수정할 상품명을 입력하세요 : ")
            password = input("패스워드 입력 : ")
            if name is not None and password is not None:
                new_name = input("새 상품명을 입력하세요 : ")
                user = Product.update(product_choice, name=name, password=password, new_name=new_name, product=product)



        elif menu_choice == 3:
            name = input("삭제할 상품명 : ")
            try:
                if name is not None:
                    user = Product.delete(product_choice, name=name)
                    print("삭제 처리 되었습니다.")
                else :
                    print("다시 입력")
                    break
            except TypeError :
                print("뭔가 오류가 발생했다.")

        elif menu_choice == 4:
            pass
        elif menu_choice == 5:
            pass
        elif menu_choice == 6:
            print("프로그램을 종료합니다 ^_^")
            break