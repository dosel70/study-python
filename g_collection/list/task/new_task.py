name_list = []
price_list = []


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

while True:
    title = "------------과일 가게-------------\n"
    menu = "1.추가하기\n2.수정하기\n3.삭제하기\n4.검색하기\n5.목록보기\n6.나가기\n------------과일 가게-------------\n"
    choice = int(input(f'{title}{menu}\n메뉴를 입력하세요 : '))
    # choice변수에 입력을 받으면, 제목과 메뉴를 보여준다.




    # if choice == 1 :
    # new_name, new_price = input(append_message).split()
    # if new_name not in name_list :
    #   name_list.append(new_name)
    #   price_list.append(new_price)
    # else :
    #   result_message = append_error_message

    if choice == 1:
        # 1번 추가 메뉴로 들어왔다면
        while True:
            # 계속 상품 및 가격들을 입력할 수 있도록 반복한다. (but 엔터키를 누르면 이전 화면으로 break 함수로 탈출
            append_message = '추가하실 상품명을 입력하세요: '
            # 추가할 상품 메세지 저장
            append_message1 = '추가하실 가격을 입력하세요(나가려면 엔터!): '
            # 추가할 가격 메세지 저장
            choice1 = input(append_message)
            # 추가할 상품명 입력
            choice2 = input(append_message1)
            # 추가할 가격 입력

            if choice1 == '' and choice2 == '':
                # choice1,choice2 입력할 때 Enter키를 누르면 이전 화면으로 돌아감
                break
                # 탈출문을 써서

            if choice1 in name_list and choice2 in price_list:
                # 만약 상품명과 가격이 중복되었다면
                append_error_message = "추가 실패(중복된 상품명)"
                # 오류메시지 출력
                print(append_error_message)
            else:
                # 상품명,가격 이 중복이 아니라면 출력
                name_list.append(choice1) #name_list에 추가됨
                price_list.append(choice2) #price_list에 추가됨



    elif choice == 2:
        # 2번 메뉴로 들어왔다면

        while True:
            # 수정 메뉴 화면을 계속 이용할 수 있도록 반복한다. (but 엔터키를 누르면 이전 화면으로 break 함수로 탈출
            search_name_message_for_update = '수정하실 상품명과 가격을 입력하세요(상품명, 가격)(나가려면 엔터!): '

            input_values = input(search_name_message_for_update) # 수정할 상품명과 가격을 동시에 입력받는다.


            if not input_values.strip():
                break
            # 공백문자 제거를 해주는 strip()가 아니라면 즉 공백(Enter)이라면 break를 사용하여 이전 메뉴로 탈출



            input_values = input_values.split(",")
            # 상품명과 가격 사이에 split 함수를 이용해서 ","로 간격을 나눈다.



            if len(input_values) != 2:
            #상품명과 가격 외에 다른 값을 더 입력 했거나 안했을 때
                print("올바른 형식으로 입력하세요.")
            #오류 메시지 출력
                continue
            #continue로 2번 초기 메뉴로 돌아간다.
            search_name_message, search_price_message = map(str, input_values)
            # 음식 수정과, 가격 수정을 동시에 입력 받기 위해 map함수로 감싸고 변수로 저장된 input_values를 str(문자열)형태로 출력한다.
            if search_name_message not in name_list:
            # 수정 할 음식이 name_list에 없다면
                search_name_error_message = "검색 실패(존재하지 않는 상품명)"
            # 오류 메시지 출력
                print(search_name_error_message)

            else:
            # 수정할 음식명이 name_list에 있다면
                index = name_list.index(search_name_message)
                name_list[index] = search_name_message
            # name_list와 price_list에 저장된 각각의 정보를 수정한다.
                price_list[index] = search_price_message


    elif choice == 3:
        # 3번 메뉴로 들어왔다면,
        while True:
            #삭제 화면을 계속 이용 할 수 있도록 while 반복문을 사용한다. (엔터키를 누르면 이전 화면으로 돌아가고 탈출)
            delete_message = '삭제하실 상품명을 입력하세요(나가려면 엔터!): '
            delete_name = input(delete_message)
            # 삭제할 상품명을 입력한다.
            if delete_name == "":
                break
            # 엔터키를 누르면 이전 메뉴 고르기 화면으로 전환
            if delete_name not in name_list:
            # 상품명이 기존 name_list에 없다면
                delete_error_message = "삭제 실패(존재하지 않는 상품명)"
            # 에러메시지를 출력한다.
                print(delete_error_message)
            else:
                # 인덱스를 찾고 삭제할 아이템을 pop() 함수로 인덱스에서 삭제 시킨다.
                index = name_list.index(delete_name)
                name_list.pop(index)
                price_list.pop(index)

    elif choice == 4:

        # 4번 메뉴로 들어 왔다면
        search_menu = "1.상품명으로 검색\n2.가격으로 검색(나가려면 엔터!)\n"
        sh_menu = int(input(search_menu))
        # 사용자에게 2가지 메뉴를 보여주고 선택할 번호를 입력 받는다.
        if sh_menu == 1:
        # 1번 검색 메뉴 선택 시
            search_name = input("검색할 상품명을 입력하세요: ")
        # 검색할 상품명 입력
            if search_name in name_list:
                print(f"가격: {price_list[name_list.index(search_name)]}원")
                # 검색한 상품이 name_list에 있으므로 price_list를 키로 갖는 인덱스를 가져와서 볼 수 있다.
            else:
                print("검색 결과가 없습니다.")
                continue
            # 검색한 상품명이 name_list에 없다면 break를 사용하여 종료

        elif sh_menu == 2:
            # 2번 검색 메뉴 선택 시
            search_price = float(input("검색할 가격을 입력하세요: "))
            # 사용자에게 검색할 가격을 입력받는다.
            for i in range(len(price_list)):
                if 0.5 * float(price_list[i]) <= search_price <= 1.5 * float(price_list[i]):
                    print(f"상품명: {name_list[i]}, 가격: {price_list[i]}원")
            # price_list의 길이(len)를 반환하여 반복하는 동안(price_list의 리스트 크기) 오차범위는 +-=50로 설정하여 찾을 수 있게 하며,
            # 상품명과 가격을 보여준다.
                else:
                    print("검색 결과가 없습니다.")
                    break
            # 검색한 가격의 오차범위를 벗어났을 때 오류 메시지 출력 후 종료
    elif choice == 5:
        # 5번 메뉴를 선택 하였을 때
        print("상품 목록:")
        #1. 상품 목록을 보여준다.
        for i in range(len(name_list)):
            print(f"상품명: {name_list[i]}, 가격: {price_list[i]}원")
        # name_list에 길이를 반환해주어서(len) 입력된 상품명,가격을 [i] 리스트 형태로
        # 명단이 끝날 때 까지 계속 보여준다.
    elif choice == 6:
        # 6번 메뉴 클릭 시
        print("프로그램을 종료합니다.")
        break
        # 종료 메시지 출력 후 종료 합니다.
    else :
        pass
    # 사용하지 않음 처리로 pass
