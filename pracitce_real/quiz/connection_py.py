from word_quiz_module import *
# book_dict = {}
# # 책 이름 - 작가
#
# library_list = [[] for i in range(3)]
# print(library_list)
# def check(*, key: str, value: str) -> dict:
#     # 저장소(DB)에서 각 도서관 들의 정보를 가져온 뒤
#     for bank in book_dict:
#         # 각 도서관 에서 회원의 정보를 가져온다.
#         for user in bank:
#             # 전달 받은 키워드(key)로 회원의 정보가 value 와 같은 지 검사한다.
#             if user[key] == value:
#                 # 만약 해당 회원을 찾았다면, 회원의 전체 정보를 리턴한다.
#                 return user
#     # 해당 회원을 찾지 못했다면, None을 리턴한다.
#     return None # JAVA 에서 NULL 과 동일