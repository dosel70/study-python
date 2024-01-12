from BookLibrary_module import *
from BookLibrary_message_module import *
from connection_py import *



if __name__ == '__main__':
    while True :
        main_choice = input(f'{menu}메뉴를 선택해주세요 : ')
        if main_choice == 1:
                login_choice= input(owner_message)
                pw_chocice = input(password_message)
                Library.insert(pw_chocice,login_choice)

        elif main_choice == 2:
            pass
        elif main_choice == 3:
            pass
        elif main_choice == 4:
            pass
        elif main_choice == 5 :
            pass
        elif main_choice == 6 :
            print("프로그램 종료")
            break