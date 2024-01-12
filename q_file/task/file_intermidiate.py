# # 파일 읽기
# # try:
# #     file = open('food.txt', 'r', encoding='UTF-8')
# #     # print(file.readlines())
# #     # for i in range(10):
# #     #     # print(file.readline(), end='')
# #     #     print(i + 1)
# #     #     if file.readline() == '':
# #     #         print('다 읽었어요!')
# #     line = None
# #     while line != '':
# #         line = file.readline()
# #         print(line, end='')
# #
# #     file.close()
# # except FileNotFoundError:
# #     print('경로를 다시 확인해주세요.')
#
#
# # with를 사용하면, 자동으로 file이 close된다.
# # with open('food.txt', 'r', encoding='utf-8') as file:
# #     print(file.readlines())
# #
#
#
#
# # 오로지 알파벳만 검사
# # 대소문자 구분 없이 비교
# # 글자수 2개 이상인 단어만 카운트
# # 빈도수 100회 이상인 단어만 카운트
#
#
# # 대소문자 구분 없어서 lower, upper 상관 없음
# # 글자수 2개 이상 .. len 으로 길이값 반환해서 2보다 크거나 같으면 담아야 되는데... 딕셔너리로 담아서
# # key,value 값을 담는다.
# # words 에는 대소문자 구문없이 알파벳이면 True 값을 받아서 소문자로 리스트 형태로 담긴다..
# # print(words)
# # print(len(words))
#
# # word_count = {} # 딕셔너리를 만듬 (알파벳과 횟수를 담기위한..)
# # for word in words:
# #     if len(word) >= 2:
# #         word_count[word] = word_count.get(word,0) + 1 # 잘 모르겠다.. (word,0) + 1 ????
#
#
#
#
# with open('alice.txt','r',encoding='utf-8') as file:
#     # 'alice.txt' 파일을 file로 변환 후  읽기모드로 open
#     content = file.read()
#     # content에 file.read >> 글자 전체를 문자열형태로 보여주게 끔 선언 즉 content에는 alice.txt의 문자들이 담겨져있음

#     words = [word.lower() for word in content.split() if word.isalpha()] # comprehension 사용

#     # comprehension으로 공백이 있는 문자를 단어로 인식하는동안 반복하면서 만약 그게 알파벳 형태면 소문자로 변환

#
#     word_count = {}
#     # word_count 라는 단어들과 단어의 개수를 담는 딕셔너리 생성
#     word_number = 0
#     # 단어의 개수를 나타내는 word_number를 0으로 설정
#     print(len(content.split()))
#     # 문자 전체의 단어들의 개수
#
#
#     for word in words:
#
#         try:
#
#             if len(word) >= 2:
#
#                 word_count[word] = word_count.get(word,word_number)+1
#
#         except:
#
#             print("오류")
#
#
#     for word,word_number in word_count.items():
#
#         if word_number >= 100:
#             print(f"{word} {word_number}\t")
#
#         else :
#             pass
#
#
#
#
# 파일의 단어의 빈도수 구하기

# alice.txt

# 오로지 알파벳만 검사하기
# 대소문자 구문없이 비교
# 글자수 2개 이상인 단어만 카운트 하기
# 빈도수 100회 이상인 단어만 카운트
# 전체 내용을 문자열로 가져오기: file.read()

"""
[출력예]
the 1642
and 872
to 729
it 595
she 553
of 514
said 462
you 411
alice 398
in 369
...
"""

with open('alice.txt', 'r', encoding='utf-8') as file:
    content = file.read().lower()

temp = ""
for character in content:
    if 'a' <= character <= 'z':
        temp += character
        continue
    temp += " "

content = temp

words = [
    word
    for word in content.split()
    if len(word) > 1
]

result = {}
for word in words:
    if result.get(word) is not None:
        result[word] += 1

    else:
        result[word] = 1

result = {
    word: result[word]
    for word in result
    if result[word] >= 100
}

sorted_key = sorted(result, key=result.get, reverse=True)
for key in sorted_key:
    print(key, result[key])

#
#
#
# def change(data):
#     return data * -1
#
# datas = [1, 2, 3, 4]
#
# print(sorted(datas, key=change))

# print(list({"A": 1, "B": 2, "C": 3}))