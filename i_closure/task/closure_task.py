# user_info = [ # 회원 정보 목록
#     {'number': 1, 'name': 'john'},
#     {'number': 2, 'name': 'mike'},
#     {'number': 3, 'name': 'ted'},
#     {'number': 4, 'name': 'lindy'},
#     {'number': 5, 'name': 'adam'},
# ]
#
#
# # 추가(초보자용)
# # def insert(*, number, name):
# #     '''
# #
# #     :param number: 회원 번호
# #     :param name: 회원 이름
# #     '''
# #     user_info.append({'number': number, 'name': name})
#
#
# # 추가
# # 회원 번호는 자동 증가한다.
# number = 5
# def set_user() :
#
#     def insert(name):
#         global number
#         number += 1
#         user_info.append({'number': number, 'name': name})
#
#
#     # 목록
#     def select_all():
#         return user_info
#
#
#     # 조회(번호로 조회)
#     def select(number):
#         for user in user_info:
#             if user['number'] == number:
#                 return user
#         return {}
#
#
#     # 수정(번호로 이름 수정)
#     def update(**kwargs):
#         '''
#
#         :param kwargs: {'number': 기존 회원번호, 'name': '새로운 회원이름'}
#         '''
#         select(kwargs.get('number'))['name'] = kwargs.get('name')
#
#
#     # 삭제(번호로 삭제)
#     def delete(number):
#         del user_info[user_info.index(select(number))]
#
#     return {'insert': insert,'select_all': select_all,'select': select, 'update':update, 'delete': delete}
# user_service = set_user()
# user_service.get('insert')('jo')
# print(user_service.get('select')(6))


post_info = [
    {'number': 1, 'title': '테스트 제목1', 'content': '테스트 내용1', 'file': '/usr/post/file/img001.png', 'read_count': 0},
    {'number': 2, 'title': '테스트 제목2', 'content': '테스트 내용2', 'file': '/usr/post/file/img002.png', 'read_count': 0},
    {'number': 3, 'title': '테스트 제목3', 'content': '테스트 내용3', 'file': '/usr/post/file/img003.png', 'read_count': 0},
    {'number': 4, 'title': '테스트 제목4', 'content': '테스트 내용4', 'file': '/usr/post/file/img004.png', 'read_count': 0},
    {'number': 5, 'title': '테스트 제목5', 'content': '테스트 내용5', 'file': '/usr/post/file/img005.png', 'read_count': 0}
] # 텍스트 정보 리스트

# 추가, 목록, 수정, 삭제 , 검색
number = 5 # 초기에 등록되어 있는 회원 수가 5명이므로 초기값을 5로 설정
def set_user(): # 추가(회원정보)
    def insert(**kwargs):
        '''
        title = 테스트 제목 , content = 테스트 내용, file = 파일 경로
        :param kwargs:
        :return:
        '''
        global number # 전역변수 5
        number += 1
        post = {
            'number': number ,
            'title': kwargs.get('title'),
            'content': kwargs.get('content'),
            'file': kwargs.get('file'),
            'read_count': 0
        }
        post_info.append(post)


    def select(number): # 번호로 검색
        for post in post_info:
            if post['number'] == number:
                return post

        return{}


    def select_all() : # 총 목록을 보여줌 (최신순)
        return post_info[::-1]



    def update(**kwargs) : # 수정, 삭제는 검색 다음에 만드는게 편하다. 왜냐하면 번호를 받아서 각각 역할의 함수들에 전달할 수 있기 때문에
        post = select(kwargs.get('number'))
        post['title'] = kwargs.get('title')
        post['content'] = kwargs.get('content')
        post['file'] = kwargs.get('file')


    def delete():
        pass
    return {'insert': insert,'select': select,'selectAll': select_all,'update': update,'delete': delete}

user_service = set_user()
user_service.get('insert')(number=1,title='nana',content='nana',file='nana')
print(user_service.get('selectAll')())






















# # 전역변수
# number = 5
# # 추가(조회수는 전달받지 않고 기본값 0으로 설정)
# def user_set() :
#     def insert(**kwargs):
#         '''
#
#         :param kwargs: {'title': '게시글 제목', 'content': '게시글 내용', 'file': '파일의 경로'},
#         :return:
#         '''
#         global number
#         number += 1
#         post = {
#             'number': number,
#             'title': kwargs.get('title'),
#             'content': kwargs.get('content'),
#             'file': kwargs.get('file'),
#             'read_count': 0
#         }
#         post_info.append(post)
#
#
#     # 목록(최신순으로 조회)
#     def select_all():
#         return post_info[::-1]
#
#
#     # 조회(번호로 조회, 조회수 1 증가)
#     def read(number):
#         post = select(number)
#         post['read_count'] += 1
#         return post
#
#
#     def select(number):
#         for post in post_info:
#             if post['number'] == number:
#                 return post
#
#         return {}
#
#
#     # 수정(번호로 정보 수정)
#     def update(**kwargs):
#         post = select(kwargs.get('number'))
#         post['title'] = kwargs.get('title')
#         post['content'] = kwargs['content']
#         post['file'] = kwargs.get('file')
#
#
#     # 삭제(번호로 삭제)
#     def delete(number):
#         del post_info[post_info.index(select(number))]
#
#     return {'insert':insert, 'update':update, 'delete':delete, 'read':read, 'select':select,'select_all':select_all}
#
# user_service = user_set()
# user_service.get('insert')(number= 0,title="새 프로젝트",content="수학문제",file="http://www.naver.com",read_count=1)
# user_service.get('insert')(title="CRUD",content="closure 함수 활용",file="/usr/post/file/new.png",read_count=1)
#
# # print(user_service.get('select')(6))
# print(user_service.get('select_all')())
# # user_service = set_user()
# # user_service.get('insert')('jo')
# # print(user_service.get('select')(6))



