
def choice_1():
    return addList

def choice_2(name):
    if name not in addList:
        addList.append(name) # 친구 리스트에 친구 이름, 나이들을 계속 추가

def choice_3(name):
    if name in addList :
        addList.remove(name)
    else :
        print("해당 이름이 없습니다.")
def choice_4(**kwargs):
    name = kwargs.get('name')
    new_name= kwargs.get('new_name')
    if name in addList :
        position = addList.index(name)
        del addList[position]
        addList.append(new_name)
    else :
        print("해당 이름이 없습니다.")
def choice_5():
    pass

choice = 0
addList = []
while choice != 5 :
    print("----------------------------")
    num1 = "\n1. 친구 리스트 출력"
    num2 = "\n2. 친구추가"
    num3 = "\n3. 친구 삭제"
    num4 = "\n4. 이름 변경"
    num5 = "\n5. 종료"
    print(num1,num2,num3,num4,num5)
    choice = int(input("원하는 메뉴의 버튼을 클릭하세요 : "))
    print("----------------------------")


    if choice == 1 :
        if len(choice_1()) == 0:
            result_message = "이름이 없습니다."
        else:
            for name in addList:
                print(f'{name}')
                continue
        print(addList)


    elif choice == 2:
        while True :
            name = input("친구 추가  (엔터키 누르면 종료): ")

            if name == '':
                break
            choice_2(name)


    elif choice == 3:
        while True :
            del_name = input("삭제할 친구 이름 (엔터키 누르면 종료): ")
            if del_name == '':
                break
            choice_3(del_name)

    elif choice == 4:
        while True :
            old_name = input("변경하고 싶은 이름을 입력하시오 (엔터키 누르면 종료): ")
            new_name = input("변경할 이름을 입력하세요 : ")

            if old_name == '':
                break
            choice_4(name=old_name,new_name=new_name)

    elif choice == 5:
        print("프로그램을 종료합니다.")
        break
    else :
        print("정확한 번호를 입력해주세요")
        continue