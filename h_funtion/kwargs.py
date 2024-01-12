# keyword arguments
# packing : 값을 묶어서 적는것
# def get_total(*numbers):
#     # 외부에서 전달 받은 값들이 numbers(튜플)에 저장된다.
#     print(type(numbers))
#     total = 0
#     for number in numbers :
#         total += number
#
#     return total
# 여러개의 값을 콤마로 구분하여 전달한다.
# total = get_total(1,2,3,4,5,6)
# print(total)
# def introduce(**intro):
#     print(type(intro))
#     print(f'name : {intro["name"]}')
#
# info_dict = {
#     "name": "Jo"
# }
# introduce(name="조성현")
# introduce(**info_dict)

# keyword arguments

# def introduce(**intro):
#     print(intro)
#     print(type(intro))
#     print(f'name: {intro["name"]}')
#
#
# info_dict = {
#     'name': '한동석'
# }
#
# introduce(name='한동석')
# introduce(**info_dict)

# 주문 가격과 주문한 회원의 정보 출력

# def get_price(*price,**kwargs) :
#     total = 0
#     for i in price :
#         total += i
#
#     print(f'{kwargs["name"]}님의 총 주문 가격 : {total}원')
# get_price(3000,2000,1000,name ='andy')

#국 영 수 점수 평균 구하기 kwargs를 사용

# def get_score(*score,**kwargs):
#     total = 0
#     for i in score :
#         total += i/len(score)
#
#     print(f'{kwargs["name"]} 총점수 : {total} ')
# get_score(50,60,70,name='국어,영어,수학의')


# def average(**score1) :
#     kor = score1['kor']
#     eng = score1['eng']
#     math = score1['math']
#     return (kor+eng+math) / 3
# print(average(kor=60,eng=60,math=100))

# 사용자 원하는 자리수(round) 반올림
# 자리수 받지 않으면 기본값 리턴

# def calculate_average(**score2) :
#     kor = score2['kor']
#     eng = score2['eng']
#     math = score2['math']
#
#     decimal_places = score2.get('decimal_places',2)
#     rounded_math = round(math,decimal_places)
#     return (kor+eng+math) / 3
#
# result_rounded = calculate_average(kor=60, eng=98.548, math=85.45, decimal_places=2)
# print(result_rounded)



# def average(**kwargs) :
#     kor,eng,math = kwargs['kor'],kwargs['eng'],kwargs['math']
#     total = kor+eng+math
#     avg = total / 3
#
#     if "round" in kwargs:
#         return round(avg,kwargs['round'])
#
#     return avg
# print(average(kor=60, eng=98, math=22,round=3))


# 반드시 Key 와 함께 사용하고자 할 때에는 매개변수의 시작을 *로 한다.
# def average(*,kor, eng, math):
#     '''
#     각 과목의 점수를 출력
#     :param kor:100
#     :param eng:97
#     :param math:22
#     :return:
#     '''
#     return (kor + eng + math)/3
#
# print(average(kor=100,eng=97,math=22))
#
# def get_price(*price,**kwargs) :
#     total = 0
#     for i in price :
#         total += i
#
#     print(f'{kwargs["name"]}님의 총 주문 가격 : {total}원')
# get_price(3000,2000,1000,name ='andy')
