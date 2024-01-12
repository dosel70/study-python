from collections import Counter
import re
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
with open("../01_11/practice.txt", 'r', encoding="utf-8") as file:
    content = file.read().lower() # 소문자로 파일을 읽는다.

words = re.findall(r'\b[a-zA-Z]{2,}\b', content.lower())
# 빈도수 100회 이상인 단어만 카운트
# 정규표현식을 사용하여 알파벳만 추출하고 대소문자 구분 없이 소문자로 변환

# 빈도수 100회 이상인 단어만 카운트
word_counts = Counter(words)
result = {word: count for word, count in word_counts.items() if count >= 100}

# 빈도수를 기준으로 오름차순으로 정렬
reversed_result = sorted(result.items(), key=lambda x: x[1],reverse=True)

# 결과 출력
for word, count in reversed_result:
    print(f"{word}: {count}")
# temp = []

# char = [character.lower() for character in content if character.isalpha()]과 아래 반복조건 코드와의 비교

# 이 코드는 character.isalpha()를 사용하여 알파벳 소문자인 문자만을 추출하고 있습니다. 그러나 다른 문자는 그대로 유지됩니다.
# 또한, 추출된 문자는 소문자로 변환됩니다.
#
# 따라서 밑에 있는 코드가 파일에서 영단어로 이루어진 부분만을 남기고 나머지를 공백으로 대체하는 방식이라면,
# 밑에있는 코드가 더 정확한 결과를 제공할 것입니다.
# 하지만 특정 상황에서는 두 번째 코드가 더 유연하게 사용될 수 있습니다. 만약 특수 문자를 제외하고자 한다면,
# 밑에 있는 코드를 사용하는 것이 더 적합할 것입니다.


# # print(char)

# #
# temp = ""
# for character in content:
#     if 'a' <= character <= 'z':
#         temp += character
#         continue
#     temp += " "
# content = temp
# # content 에는 character를 content 내에 반복을 하는동안
# # character가 a~z 까지만 되게 변하게 되고 continue로 다시 반복문으로 돌아와서
# # temp 에 공백인 " "을 추가해주어서 단락을 띄어쓰기 하게 해준다.
# # 결국 알파벳과 공백만 남게 된다.
#
# words = [word for word in content.split() if len(word) > 1]
#
# # words 에 comprehension을 사용하여 앞전에 알파벳과 공백만 남은 content에
# #.split()를 붙혀서 공백까지 검사하게 되고, (반복 하면서) 그리고 단어의 길이 즉
# #단어수가 1이 넘으면 그 값을 word에 전달해주므로 결국 글자수가 2개 이상인것만 남게 된다~!
#
# result = {} # 단어와 단어 빈도수를 key,value값으로 받아야 하기에..dict 사용
# for word in words:
#     if result.get(word) is not None :
#         result[word] += 1
#     else :
#         result[word] = 1
#
# result = {
#     word : result[word]
#     for word in result
#     if result[word] >= 100
# }
#
# # {}: 중괄호는 딕셔너리를 생성하는 문법입니다.
# #
# # word: result[word]: 딕셔너리 컴프리헨션의 키-값 쌍을 정의합니다. 각각의 word는 result 딕셔너리에서 가져온 단어를 나타내며,
# # result[word]는 해당 단어의 빈도수를 나타냅니다.
# #
# # for word in result: result 딕셔너리에서 각각의 단어를 순회합니다.
# # word 변수는 각 순회에서 현재의 단어를 나타냅니다.
# #
# # if result[word] >= 100: 조건문은 해당 단어의 빈도수가 100 이상인지를 확인합니다.
# # 조건이 참일 경우에만 해당 단어를 새로운 딕셔너리에 포함시킵니다.
# #
# # 따라서 이 딕셔너리 컴프리헨션은 result 딕셔너리에서 빈도수가 100 이상인 단어들만을 추려서 새로운 딕셔너리를 생성합니다.
# # 이 새로운 딕셔너리는 해당 단어와 그 빈도수만을 포함하게 됩니다.
# #
# # # print(result)
#
# sorted_key = sorted(result,key=result.get, reverse=True)
# try :
#     for key in sorted_key:
#         print(key,result[key])
# except :
#     print("알 수 없는 오류")
#     # print(key, result[key])
