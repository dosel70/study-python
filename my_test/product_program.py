# 추가, 수정, 삭제, 검색, 목록
# 수정 시 상품명으로 검색하고 새로운 상품명과 가격으로 수정한다(상품명 가격을 따로 수정하지 않고 한번에!)
# 검색 시 상품명, 가격을 따로 검색하도록 구현한다.
# 가격 검색 시 오차 범위는 ±50%로 설정한다.
data_dict = {} # 저장된 딕셔너리 (상품 정보 등이 기입됨)

title = "------과일 가게 키오스크--------"
menu = "1.추가하기\n2.수정하기\n3.삭제하기\n4.검색하기\n5.목록보기\n6.나가기\n원하시는 메뉴번호를 선택해주세요 : "

search_menu = "1.상품명으로 검색\n2.가격으로 검색\n"
append_message = '추가하실 상품명과 가격을 입력하세요. (엔터키 누르면 종료)\n'
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



def insert(**kwargs) : # 상품정보 추가
    name,price = kwargs.values() # 키워드 인자에 name,price로 설정
    data_dict[name] = int(price) # data_dict 에 name 을 키 값으로 하는 value(가격)을 추가 한다.

def update(name, **kwargs) : # 상품 정보 수정
    new_name,new_price = kwargs.items() #새 상품의 이름과 가격을 키워드 인자로 선언함
    del data_dict[name]  # (먼저 키값(이름)을 제거 / 딕셔너리는 키 값이 수정이 안되기 때문에 키 값을 제거 후에 추가해줘야된다.)
    data_dict[new_name] = int(new_price)  # 새로운 이름으로 변경한다.


def delete(name): # 상품 제거 (이름이 키값으로 설정되었기 때문에 이름만 지우면 가격도 같이 지워진다.)
    if name in data_dict : # 이름이 딕셔너리에 있을 때
        del data_dict[name] # 상품 제거
    else : # 상품이 존재하지 않을 때
        print("해당 상품은 존재하지 않습니다.")
def name_search(name): # 상품명으로 검색
    result = {} # result라는 딕셔너리를 따로 만들어놓는다.
    if name in data_dict : # 만약 상품명이 data_dict에 있을 때
        result = {"name":name, "price":data_dict[name]}
    return result

def price_search(price,range=50):
    result = []
    min = price * 0.01 * range
    max = price * (range * 0.01 + 1)
    for name, price in data_dict.items() :
        if min < price < max :
            result.append({"name":name,"price":price})
        else :
            print(search_error_message)
    return result

while True :
    print(title)
    choice = int(input(menu))



    if choice == 1 :
        new_name, new_price = input(append_message).split()
        if new_name == '':
            break
        insert(name=new_name, price=new_price)


    elif choice == 2 :
        old_name = input(search_name_message_for_update)
        new_name = input("새로운 상품명을 입력해주세요 : ")
        new_price = int(input("새로운 가격을 입력해주세요 : "))
        update(old_name,new_name=new_name, new_price=new_price)


    elif choice == 3 :
        del_name = input("삭제할 상품명을 입력하세요 : ")
        delete(del_name)

    elif choice == 4 :
        choice1 = int(input(search_menu))
        if choice1 == 1 :
            keyword = input("검색할 상품명을 입력하세요 : ")
            result = name_search(name=keyword)
            print(result)
        elif choice1 == 2 :
            keyword_price = int(input("검색할 가격을 입력하세요 : "))
            result = price_search(price=keyword_price,range=50)
            print(result)


    elif choice == 5 :
        print(data_dict)
    elif choice == 6 :
        print("프로그램 종료")
        break
    else :
        print("다시 입력해주세요")

