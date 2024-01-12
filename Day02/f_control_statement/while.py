# 사용자가 입력한 정수가 몇 자리 수인지 출력
# 사용자에ㅔㄱ 정수 입력받는다
# 입력받은 정수의 각 자리수를 샌다
# 자리수를 출력한다.
# 몫과 나머지
# number = int(input('Enter a number: '))
# count = 0
#
# position = "자리수"
#
# while number != 0:
#     number //= 10
#     count+=1
#
# print(str(count) + f'{position}')


# 수열

# number_1 = int(input("몇 번째 수열 인가요 ? : "))
# for i in range(2):
#     if i == 0:
#         number_2 = number_1*2
#     else :
#         number_2 = number_1/2
#     for j in range(2) :
#         if j == 0:
#             number_3 = number_2*2
#     else :
#         number_3 = number_2/2
#         for k in range(2) :
#             if k == 0:
#                 number_4 = number_3*2
#         else :
#             number_4 = number_3/2
#             print(number_4)

count = 0
result = 0
while count < 10 :
    count +=1
    result += count

print(result)