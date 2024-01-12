# 내가 푼 문제
from h_funtion import kwargs

post_info = [
    {'number': 1, 'title': '테스트 제목1', 'content': '테스트 내용1', 'file': '/usr/post/file/img001.png', 'read_count': 0},
    {'number': 2, 'title': '테스트 제목2', 'content': '테스트 내용2', 'file': '/usr/post/file/img002.png', 'read_count': 0},
    {'number': 3, 'title': '테스트 제목3', 'content': '테스트 내용3', 'file': '/usr/post/file/img003.png', 'read_count': 0},
    {'number': 4, 'title': '테스트 제목4', 'content': '테스트 내용4', 'file': '/usr/post/file/img004.png', 'read_count': 0},
    {'number': 5, 'title': '테스트 제목5', 'content': '테스트 내용5', 'file': '/usr/post/file/img005.png', 'read_count': 0}
]

#1. 추가하기(다) 2. 수정하기(다) 3. 검색하기(이름) 4. 삭제하기(이름) 5. 목록보기(이름)
def product():
    number = 5

    def insert(**kwargs):
        post_info.append({'number': number, 'title': kwargs.get('title'), 'content': kwargs.get('content'), 'file': kwargs.get('file')})
    def update(**kwargs):
        pass
    def select():
        pass
    def delete():
        pass
    def show():
        pass

    insert(number=5, title="HI", content="알아서 뭐하게?", file="/usr/post")
    return {insert()}

print(post_info)


#
# def practice(*args,**kwargs) :
#     print(args)
#     print(kwargs)
#
# practice("non","is","full" , a=5,b=6,c=7,d=8)