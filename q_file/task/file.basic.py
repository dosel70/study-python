# # fish.txt를 만든다. 사용자에게 입력받은 물고기를
# # fish.txt에 작성한다.
# # q를 입력하면 fish.txt의 전체 내용삭제
# # r 입력하면 fish.txt의 전체 내용을 콘솔에 출력
#
# filename = 'fish.txt'
#
# # 물고기 목록 파일 생성
# with open('water.txt', 'w', encoding='UTF-8') as file:
#     while True:
#         fish_input = input("물고기 입력(엔터시 종료) : ")
#         file.write(fish_input + '\n')
#         if fish_input == '' :
#             break
#
# # 사용자에게 입력받은 물고기를 fish.txt에 추가
#     while True:
#         user_input = input("(q 입력 시 전체 내용 삭제, r 입력 시 전체 내용 출력): ")
#
#         if user_input == 'q':
#
#             with open('water.txt', 'w', encoding='UTF-8') as file:
#                 pass
#                 try :
#                     with open('water.txt','r',encoding='utf-8')as file:
#                         print(file.readlines())
#                 except FileNotFoundError:
#                     print("오류")
#
#         elif user_input == 'r':
#
#             with open('water.txt', 'r', encoding='UTF-8') as file:
#                 print(file.readlines())
#
#         elif user_input == '':
#            break
#         else :
#             pass
#
# # with open('water.txt', 'r', encoding='UTF-8') as file:
# #     print(file.readlines())
# #
#
#
# fish.txt
# 사용자에게 입력받은 물고기를 fish.txt에 작성한다.
# 사용자가 q를 입력하면, fish.txt의 전체 내용을 삭제한다.
# 사용자가 r을 입력하면, fish.txt의 전체 내용을 콘솔에 출력한다.

# with open('./fish.txt', 'w', encoding='utf-8') as file:
#     pass

# with open('./fish.txt', 'a', encoding='utf-8') as file:
#     fish = input('물고기: ') + '\n'
#     file.write(fish)

# with open('./fish.txt', 'r', encoding='utf-8') as file:
#     for line in file.readlines():
#         print(line, end='')


# title = 'q: 삭제, r: 읽기'
# message = '물고기: '
#
# while True:
#     path = input('경로: ')
#     fish = input(title + '\n' + message)
#
#     if fish == 'q':
#         with open(path, 'w', encoding='utf-8') as file:
#             pass
#
#     elif fish == 'r':
#         try:
#             with open(path, 'r', encoding='utf-8') as file:
#                 for line in file.readlines():
#                     print(line, end='')
#             break
#         except FileNotFoundError:
#             print('경로를 다시 확인해주세요.')
#
#     else:
#         with open(path, 'a', encoding='utf-8') as file:
#             file.write(fish + '\n')

#

# 수정  고등어 >> 참치
# 외부 파일에 있는 내용을 담아줄 변수
# content = ""
# with open('fish.txt','r',encoding='UTF-8')as file:
#     line = None
#     # 전체 내용을 한줄에 읽어오기
#     while line != '':
#         line = file.readline()
#         # 담은 내용이 찾고 있는 햄버거 일 경우
#         if line == '고등어\n':
#             content += '참치\n'
#             continue
#         content += line
    # 수정 완료된 문자열 값 확인
    # print(content)
# 기존의 내용을 수정 완료된 문자열로 덮어쓰기
# with open('food.txt','w',encoding='UTF-8')as file:
#     file.write(content)

content = ""
with open('fish.txt','r',encoding='UTF-8')as file:
    line = None
    while line != '':
        line = file.readline()
        if line == '고등어\n':
            content += '꽁치\n'
        elif line == '상어\n':
            content += '조성현\n'
            continue
        content += line
    print(content)
with open('fish.txt','w',encoding='utf-8') as file:
    file.write(content)

# 원본 파일의 내용 확인
# with open('food.txt','r',encoding='UTF-8')as file:
#     print("".join(file.readlines()))