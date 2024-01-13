score = [(100, 50),(90, 86),(77, 69),(98, 92)]


def get_avg(score: list):
    for index, point in enumerate(score):
        print(f'{index + 1}번 , 평균 : {sum(point) / len(point):.1f}')


def need_password(func): #
    def wrapper(*args, **kwargs):
        password = "1234"
        input_pw = input("비밀번호를 입력하세요 : ")
        if input_pw == password:
            result = func(*args, **kwargs)
        else :
            result = "잘못된 비밀번호입니다."
        return result
    return wrapper()

