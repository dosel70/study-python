from word_quiz_module import *
from word_quiz_message import *

# --------------------------
# 1. 단어 추가
# 2. 단어 삭제
# 3. 문제 풀기
# --------------------------
# 메뉴 선택 : (번호 입력)


while True:

    choice = input(f'{menu}{menu1}')
    if choice == '1':

            word = input("단어를 입력하세요 : ")
            word1 = input("뜻을 입력하세요 : ")
            insert(word,word1)
            print(word_dict)


    elif choice == '2':

        word = input("삭제할 단어를 입력하세요 : ")
        delete(word)
        print(word_dict)




    elif choice == '3':
        result = solution()
        print(result)

    elif choice == '4':
        print("프로그램을 종료합니다.")
        pass

