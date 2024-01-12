
# if number % 3 == 0 and number % 5 == 0:
#     print(f'{number}는 3과 5의 공배수이다.')
# elif number % 3 == 0:
#     print(f'{number}는 3의 배수이다.')
# if number % 3 == 0:
#     print(f'The {number} is 3배수')
#     if number % 5 == 0:
#         print(f'The {number} is 5배수')

#

#number가 양수인지 음수인지 0인지 검사
# number = int(input('Enter a number: '))

# if number > 0 :
#     print(f'입력된 값 {number} 은/는 양수')
# elif number < 0 :
#     print(f'입력된 값 {number} 은/는 음수')
# else :
#     print(f'입력된 값 {number} 은/는 0')
#
# p_condition = number > 0
# n_condition = number < 0
#
#
# if p_condition :
#     print(f'입력된 값 {number} 은/는 양수')
# elif n_condition :
#     print(f'입력된 값 {number} 은/는 음수')
# else :
#     print(f'입력된 값 {number} 은/는 0')

# age= int(input("Enter your age: "))
# error = age <= 0 or age >= 150
# little = 0 < age < 18 # age > 0 and age < 18
#
# if little :
#     print(f"미성년자.")
# elif error:
#     print(f"에러")
# else :
#     print("성인이다.")
#
message = "두 정수를 입력해주세요 : "
example_message = '예/ 1 3'
num1, num2 = map(int,input(message + '\n' + example_message + '\n').split(' '))
num1_win = num1 > num2
num2_win = num1 < num2

# 선언할 때 넣을 값을 모를 경우 초기값을 넣어준다.
# 정수 : 0
# 실수 : 0.0
# 문자열 : '' 또는 ""
# boolean : False

result_message = ''

if num1_win :
    result_message = f'{num1} > {num2}'
elif num2_win :
    result_message = f'{num1} < {num2}'
else :
    result_message = f'{num1} = {num2}'

print(result_message)

