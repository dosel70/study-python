"""
while 문을 활용하여 이름을 입력 받고 다음과 같이 출력을 반복하시오.
단 입력 받은 이름이 "최성우"라면 '멋지다'를 출력하고
반복을 종료한다.
"""

# list = ["최성우"]
# while True:
#     name = input("Enter your name >> :")
#     if name in list:
#         print(f"{name}님 안녕하세요 회원이 되셨습니다! " )
#         break
#     else :
#         print(f'{name}님 안녕하세요')
#
#
# count = 0
# result = 0
# while count < 10 :
#     count +=1
#     result += count
#
# print(result)
#


"""
n회차 로또가 시작되었다. 만약 "당첨자 목록" 리스트 내에 josh라는 이름이 입력되면 n회차의 n값을 1~n까지의 합 * 
10 만원을 지급하도록 한다. (단 이름은 영소문자로 입력해야 한다!)

"""

n = 0
result = 0
message = f'안녕하세요 {n}회차 로또가 시작 되었습니다! 모두 준비하시기 바랍니다.'
list=["josh","lisa","jack","harry","paul"]
name = input(f'{message}\n 이름을 입력해주세요 :  ')
while n == 50:
    n=+1
    result += n