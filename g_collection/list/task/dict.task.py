
data_dict = {}

while True:
    print("\n===== 상품 관리 프로그램 =====")
    print("1. 상품 추가")
    print("2. 상품 수정")
    print("3. 상품 삭제")
    print("4. 상품 검색")
    print("5. 상품 목록")
    print("6. 종료")

    choice = input("원하는 기능의 번호를 입력하세요: ")

    if choice == '1':
        name,price = map(str,input("추가할 상품명,가격을 입력하세요: ").split())

        data_dict[name] = price
        print(f"상품 '{name}'이(가) 추가되었습니다.")

    elif choice == '2':
        old_name = input("수정할 상품명을 입력하세요: ")
        if old_name in data_dict:
            new_name = input("새로운 상품명을 입력하세요: ")
            new_price = input("새로운 가격을 입력하세요: ")
            del data_dict[old_name]
            data_dict[new_name] = new_price
            print(f"상품 '{old_name}'이(가) '{new_name}'(으)로 수정되었습니다.")
        else:
            print(f"상품 '{old_name}'이(가) 존재하지 않습니다.")

    elif choice == '3':
        name = input("삭제할 상품명을 입력하세요: ")
        if name in data_dict:
            del data_dict[name]
            print(f"상품 '{name}'이(가) 삭제되었습니다.")
        else:
            print(f"상품 '{name}'이(가) 존재하지 않습니다.")

    elif choice == '4':
        search_type = input("검색할 유형을 선택하세요 (1. 상품명 / 2. 가격): ")
        if search_type == '1':
            name = input("검색할 상품명을 입력하세요: ")
            result = [(product_name, product_price) for product_name, product_price in data_dict.items() if name.lower() in product_name.lower()]
        elif search_type == '2':
            price = float(input("검색할 가격을 입력하세요: "))
            result = [(product_name, product_price) for product_name, product_price in data_dict.items() if 0.5 * float(product_price) <= price <= 1.5 * float(product_price)]
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")
            continue

        if result:
            print("검색 결과:")
            for product_name, product_price in result:
                print(f"{product_name}: {product_price}원")
        else:
            print("검색 결과가 없습니다.")

    elif choice == '5':
        print("\n상품 목록:")
        for product_name, product_price in data_dict.items():
            print(f"{product_name}: {product_price}원")

    elif choice == '6':
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못된 입력입니다. 다시 선택해주세요.")


