# student = {
#     "name": "한동석",
#     "email": "tedhan1204@gmail.com"
# }
#
# print(student['name'])
# print(student.get('name'))
#
# # get()을 사용하면 key를 찾지 못했을 때 원하는 default 값으로 설정이 가능하며,
# # default 값이 없을 때에는 None을 가져온다.
# # print(student['phone']) # 오류
# print(student.get('phone', '01012341234'))
#
# # 'name' key 값이 이미 있기 때문에, 아래의 코드는 '수정'이다.
# student['name'] = '홍길동'
# print(student)

# student = {
#     "name": "<NAME>",
#     "email": "dosel45@nacver"
# }
# # key 분리
# print(list(student.keys()))
# # value 분리
# print(list(student.values()))
# # item 분리
# print(list(student.items()))
#
#
# for key,value in student.items() :
#     print(key,value)




#
# # 'phone' key 값이 없기 때문에, 아래의 코드는 '추가'이다.
# student['phone'] = '01012341234'
# print(student)
#
# if 'email' in student: # 수정
#     student['email'] = 'hgd1234@gmail.com'
# else: # 추가
#     student['email'] = 'hgd1234@gmail.com'
#
# print(student)

my_dict = {
    1: "한동석",
    "two": "20살",
    False: [10, 20, 30],
    "row": [
        {"name": "ted", "age": 40},
        {"name": "jack", "age": 30},
        {"name": "john", "age": 20}
    ]
}
# # # row에 있는 회원 3명의 정보를 모두 출력

# def find() :
#     if 'row' in my_dict :
#         print(my_dict['row'])
#     return
#
# result = find()
# print(result)

# if 'row' in my_dict:
#     for data in my_dict['row']:
#         print(f'{data["name"]}: {data["age"]} ',end='')


# 1~10까지 중 홀수와 짝수가 있다.
# #  사용자가 '짝수'를 입력하면, 짝수만 출력하고
# # '홀수'를 입력하면, 홀수만 출력한다.
# # dict를 사용한다. 아니면 클래스도 사용, 함수도 사용


number_dict = {


               }




















# # row에 있는 회원 3명의 정보를 모두 출력
# # if 'row' in my_dict:
# #     # print(type(my_dict['row']))
# #     for data in my_dict['row']:
# #         print(f'{data["name"]}, {data["age"]}')
#
# # 1~10까지 중 홀수와 짝수가 있다.
# #  사용자가 '짝수'를 입력하면, 짝수만 출력하고
# # '홀수'를 입력하면, 홀수만 출력한다.
# # dict를 사용한다.

# number_dict = { # dict에 comprehension를 이용하여서 홀수와 짝수 값에 홀수, 짝수를 각각 집어넣고 1~10까지 각각 출력
#     '홀수': [i * 2 + 1 for i in range(5)],# 홀수 = 2n +1
#     '짝수': [i * 2 + 2 for i in range(5)] # 짝수 = 2n+2
# }
# print(", ".join(map(str, number_dict[input('짝수 혹은 홀수: ')]))) # "짝수" 혹은 "홀수"로 입력을 해야 하기 때문에,


# # number_dict = {
# #     True: [i * 2 + 1 for i in range(5)],
# #     False: [(i + 1) * 2 for i in range(5)]
# # }
# #

# alpha_dict = {
#     '대문자': ([chr(ord('A')+i) for i in range(26)]),
#     '소문자': ([chr(ord('a')+i) for i in range(26)])
# }
# print(",".join(map(str,alpha_dict[input('대문자 혹은 소문자: ' )])))
#
#
# # alpha = ([chr(ord('A')+i) for i in range(26)])
# # print(alpha)
# # print(", ".join(map(str, number_dict[input('짝수 혹은 홀수: ') == '홀수'])))