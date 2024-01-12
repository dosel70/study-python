
    # user_info = [
    #     {'number': 1, 'name': 'john'},
    #     {'number': 2, 'name': 'mike'},
    #     {'number': 3, 'name': 'ted'},
    #     {'number': 4, 'name': 'lindy'},
    #     {'number': 5, 'name': 'adam'},
    # ]
    #
    # #
    # # 추가(초보자용)
    # def insert(*, number, name):
    #     '''
    #
    #     :param number: 회원 번호
    #     :param name: 회원 이름
    #     '''
    #     user_info.append({'number': number, 'name': name})
    #
    # #
    # # # 추가
    # # # 회원 번호는 자동 증가한다.
    # # number = 5
    # # def insert(name):
    # #     global number
    # #     number += 1
    # #     user_info.append({'number': number, 'name': name})
    # #
    # #
    # # # 목록
    # # def select_all():
    # #     return user_info
    # #
    # #
    # # # 조회(번호로 조회)
    # def select(number):
    #     for user in user_info:
    #         if user['number'] == number:
    #             return user
    #     return {}
    # #
    # #
    # # # 수정(번호로 이름 수정)
    # def update(**kwargs):
    #     '''
    #
    #     :param kwargs: {'number': 기존 회원번호, 'name': '새로운 회원이름'}
    #     '''
    #     select(kwargs.get('number'))['name'] = kwargs.get('name')
    #
    # #
    # # 삭제(번호로 삭제)
    # def delete(number):
    #     del user_info[user_info.index(select(number))
    #
    # # # 삭제(번호로 삭제)
    # # def delete(number):
    # #     del user_info[user_info.index(select(number))]
    # # print(select_all())