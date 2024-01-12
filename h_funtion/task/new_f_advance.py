# 추가, 수정, 삭제, 검색, 목록
# 수정 시 상품명으로 검색하고 새로운 상품명과 가격으로 수정한다(상품명 가격을 따로 수정하지 않고 한번에!)
# 검색 시 상품명, 가격을 따로 검색하도록 구현한다.
# 가격 검색 시 오차 범위는 ±50%로 설정한다.
data_dict = {} # 저장된 딕셔너리 (상품 정보 등이 기입됨)

title = "또와 과일"
menu = "1.추가하기\n2.수정하기\n3.삭제하기\n4.검색하기\n5.목록보기\n6.나가기\n"
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


def insert(**kwargs): # 상품 정보 추가 함수
    '''

    :param kwargs: {'name': '상품명', 'price': 가격}
    '''
    name, price = kwargs.values() # 추가 기능의 키워드 인자에 value 값을 상품명과 가격에 담아 놓는다.
    data_dict[name] = int(price) # 저장된 딕셔너리의 상품명에 가격을 함께 저장한다.


def update(*, name, new_name, new_price): # 상품 정보 수정 함수
    del data_dict[name] # 먼저 이름을 제거후에
    data_dict[new_name] = int(new_price) # 새로운 이름으로 변경한다.


def delete(name):
    del data_dict[name]

def select_by_name(keyword): # 매개변수는 키워드 ( 상품 명만 입력하면 되므로 변수는 1)
    result = {} # 검색한 정보 출력 딕셔너리 초기값
    if keyword in data_dict: # 저장된 딕셔너리에 검색한 키워드가 있다면
        result = {'name': keyword, 'price': data_dict[keyword]} # 해당 정보 출력

    return result # 결과값을 반환

def select_by_price(price, range=50):
    result = []
    min = price * range * 0.01
    max = price * (range * 0.01 + 1)

    for name, price in data_dict.items():
        if min <= price <= max:
            result.append({'name': name, 'price': price})

    return result

def select_all():
    return data_dict

while True:
    # 사용자에게 메뉴를 보여주고 선택한 번호를 choice에 저장
    choice = int(input(title + '\n' + menu))

    # 추가
    if choice == 1:
        new_name, new_price = input(append_message).split() # 상품명과 가격을 입력받는다.

        if len(select_by_name(new_name)) == 0: # 검색 함수의 길이가 0이라면 즉 검색 했을 때 나오는 정보가 없다는것은 입력된 상품명이 중복이 안되있다는 뜻
            insert(name=new_name, price=new_price) # 그러므로 추가 함수의 매개변수였던 키워드 인자인 name,price에 값을 넣어준다.
            continue #메뉴 선택 화면으로 이동
        else:
            result_message = append_error_message # 중복된 상품명이면 에러 메세지 출력

    # 수정
    elif choice == 2:
        name = input(search_name_message_for_update)
        if len(select_by_name(name)) != 0:
            new_name, new_price = input(update_message).split()
            if len(select_by_name(new_name)) == 0:
                update(name, new_name, new_price)
                continue
            else:
                data_dict[new_name] = int(new_price)
        else:
            result_message = update_error_message1

    # 삭제
    elif choice == 3:
        name = input(delete_message)
        if len(select_by_name(name)) != 0:
            delete(name)
            continue

        else:
            result_message = delete_error_message

    # 검색
    elif choice == 4:
        choice = int(input(search_menu))

        # 상품명으로 검색
        if choice == 1:
            keyword = input(search_name_message) # 검색할 키워드 입력
            result = select_by_name(keyword) # 상품 검색 함수가 result에 담아진다. // result라는 변수에 저장하였따. << 상품 검색 함수를
            if len(result) != 0: # 검색한 내용이 있다면
                print(f"{result.get('name')}, {result.get('price')}") # 상품 검색 함수에서 기입 했던 name, price 가격을 불러온다.
                continue

            else:
                result_message = search_name_error_message

        # 가격으로 검색
        elif choice == 2:
            price_input = int(input(search_price_message))

            result = select_by_price(price_input)

            if len(result) != 0:
                for product in result:
                    print(f"{product.get('name')}, {product.get('price')}")
                continue

            else:
                result_message = search_error_message

    # 목록
    elif choice == 5:
        if len(select_all()) == 0:
            result_message = no_item_message
        else:
            for name, price in data_dict.items():
                print(f'{name}, {price}')
                continue

    # 나가기
    elif choice == 6:
        break

    # 그 외
    else:
        result_message = error_message

    print(result_message)
    result_message = ""






