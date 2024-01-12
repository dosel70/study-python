# 상품 추가, 상품 검색(가격), 상품 수정(상품명), 상품 삭제(가격 오차범위 +- 50%), 상품 조회(상품명으로 검색)
# 자동차, 가전제품, 전자기기

def check(*,key:str,value:str) -> dict:
# 저장소에서 각 상품들의 정보를 가져와야 함
    for product in Product.products :
        # Product 클래스 내의 상품 정보들에 사용자(user)의 정보인 key , value가 일치하다면
        # user를 리턴해라
        for user in product:
            if user[key] == value :
                return user
    # 해당 없으면 None을 리턴
    return None


class Product:
    total = 3
    # 상품의 개수
    products = [[] for i in range(total)]
    # comprehension으로 이차원 리스트를 만든다.
    def __init__(self,user_name:str,name:str,price:int,password:str,famous:int):

        self.object = self # object를 주소 값으로 받는다.
        self.user_name = user_name # 사용자 이름
        self.name = name  # 상품 명
        self.price = price # 잔액
        self.password = password
        self.famous = famous # 인기도 (상품의 인기도)
        # 각 제품의 정보 또는 규격들을 정의

    @classmethod # why ? >> Product 클래스에 접근하기 위함
    def insert(cls,product_choice,**kwargs):
        # 회원이 어떤 상품을 살 것인지는 알 수 없고,
        # 전달 받은 product_choice 의 값을 입력받아서
        # ex) 자동차,가전제품,핸드폰 총 3개의 인덱스값을 가지고 있는
        #products 리스트에는 각각 인덱스 번호가 0~2 까지이므로, products_choice -1를 해줘야 각각
        # 인덱스 번호 값에 들어간다. but 현재 상품의 종류는 3개 뿐이므로 만약 products_choice가
        # 4또는 5를 넘어버리면 out of index range 라는 오류가 뜨게 된다. (4-1 : 3, 5-1: 4,,)
        product = [Car,Appliance,Electronics][product_choice - 1](**kwargs)
        cls.products[product_choice - 1].append(product.__dict__)
        # check 함수에서 key와 value 값을 받아서 상품 정보 에 dict 형태로 추가한다.
        return product

    @staticmethod
    def check_product_name(product_name:str)-> dict:
        return check(key='product_name',value=product_name)

    @staticmethod
    def check_password(password) :
        if len(password) >= 4:
            return check(key='password', value=password)
        else :
            print("Password is too short")

    def check_name(self, user_name):
        self.user_name = user_name
        if user_name not in Product.products:
            Product.products.append(user_name)
        elif user_name is None:
            print("중복된 이름")

    @staticmethod
    def check_price(price:str)->dict:
        return check(key='price', value=price)

    @classmethod
    def update(cls,new_name,**kwargs):
        name = kwargs.get("name")
        password = kwargs.get("password")
        if name is not None and password is not None:
            # 계좌번호를 변경하는 로직을 수행하고, 변경이 성공하면 결과를 리턴
            # 예시로 변경이 성공했다고 가정
            Product.account_number = new_name
            return f"계좌번호 {new_name}으로 성공적으로 변경되었습니다."

        else:
            # 필요한 입력값이 부족한 경우 None을 리턴하거나, 적절한 에러 메시지를 출력
            return None

    @classmethod
    def delete(cls,name):
        del Product.products[name]


class Car(Product):
    pass

class Appliance(Product):
    pass

class Electronics(Product):
    pass

if __name__ == '__main__':

    title = "전자상가 키오스크(어드민 전용)\n"
    product1 = "1.자동차\n2.가전제품\n3.핸드폰\n"
    menu = ("1. 상품 추가하기\n2. 상품 정보 수정하기\n3. 상품 삭제하기\n"
            "4. 상품 검색하기\n5. 상품 목록보기\n6. 나가기\n")
    search_menu = "1.상품명으로 검색\n2.가격으로 검색\n"
    append_message = '추가하실 상품명과 가격을 입력하세요.\n예)상품명 가격'
    search_name_message_for_update = '수정하실 상품명을 입력하세요.'
    update_message = '새로운 상품명과 가격을 입력하세요.\n예)상품명 가격'
    delete_message = '삭제하실 상품명을 입력하세요.'
    search_name_message, search_price_message = '상품명: ', '가격: '

    result_message = ""
    append_error_message = "추가 실패(중복된 상품명)"
    update_error_message1 = "수정 실패(존재하지 않는 상품명)"
    update_error_message2 = "수정 실패(중복된 상품명)"
    delete_error_message = "삭제 실패(존재하지 않는 상품명)"
    search_name_error_message = "검색 실패(존재하지 않는 상품명)"
    search_error_message = "검색 결과가 없습니다."
    error_message = "다시 입력해주세요."
    no_item_message = "목록이 없습니다."

    while True :
        product_choice = int(input(f"{title}{product1}"))

        menu_choice = int(input(f"{menu}"))
        if product_choice > len(product1) :
            continue

        if  menu_choice == 1:
            name = input("사용자 이름을 입력하세요 : ")
            while True :
                product = input("추가하실 상품명을 입력하세요 : ")
                if Product.check_product_name(product_name=product) is None:
                    break
            while True:
                price = input("설정 가격을 입력해주세요 : ")
                if Product.check_price(price=price) is None:
                    break
            while True :
                password = input("비밀번호를 입력해주세요 : ")
                if len(password) == 4:
                    break
                else :
                    continue

            user = Product.insert(product_choice, name=name, price=price,password=password)


        elif menu_choice == 2:
            name = input("수정할 상품명을 입력하세요 : ")
            password = input("패스워드 입력 : ")
            if name is not None and password is not None:
                new_name = input("새 상품명을 입력하세요 : ")
                user = Product.update(product_choice, name=name, password=password,new_name=new_name,product=product)



        elif menu_choice == 3:
            name = input("삭제할 상품명 : ")
            if name is not None :
                user = Product.delete(product_choice,name=name)

        elif menu_choice == 4:
            pass
        elif menu_choice == 5:
            pass
        elif menu_choice == 6:
            print("프로그램을 종료합니다 ^_^")
            break




