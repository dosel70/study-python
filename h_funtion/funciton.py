# # f(x) = 2x + 1
#
# # f(x) = 2x+1
# # def f(x):
# #     return 2 * x + 1
# #
# # result = f(2)
# # print(result)
#
# # 두 정수의 곱셈 함수
# # def get_sum(x,y) :
# #     return x*y
# # result = get_sum(5,3)
# # print(result)
#
# # 두 정수의 나눗셈 후 몫과 나머지 구하는 함수
# # def get_sub(a,b) :
# #     if b != 0 :
# #         return a//b, a%b
# #     return None
# # print(get_sub(5,3))
# #
# #
# # # 1~10까지 print()로 출력하는 함수
# # def get_sub() :
# #     for i in range(1,10) :
# #         print(i+1)
# # print(get_sub())
#
# # 이름을 n번 print()로 출력하는 함수
# # def print_name_multiple_times(name, count_name):
# #     for count in range(count_name):
# #         print(name)
# #
# # name_value = '이름'
# # print_name_multiple_times(name_value, 5)
#
#
# # for i in range(10):
# #     print(f'{i+1}.jsh')
# #
# # for i in range(10) :
# #     print(f'{10-i}')
# # def get_print(n) :
# #     for i in range(n) :
# #         print(i+1)
# #
# # n = int(input("몇번 출력 : "))
# # print(get_print(n))
# # name = input("이름 입력 : ")
# #1~n까지의 합을 구해주는 함수
# # def get_sum(n) :
# #     total_sum = 0
# #     for i in range(n) :
# #         total_sum += i+1
# #     return total_sum
# #
# # n = int(input("숫자를 입력: "))
# # print(get_sum(n))
#
#
#
# # for i in range(10) :
# #     if i == 3 :
# #         continue
# #     print(i+1)
#
# # def print_multiples(n):
# #     for i in range(1, 101):
# #         if i % n == 0:
# #             print(i)
# #
# # n_value = 1
# # print_multiples(n_value)
#
# # n = int(input("숫자를 입력하세요 : "))
# # for j in range(1,n):
# #      total_sum1 += j
# #      print(total_sum1)
#
#
# # 1~100까지 중 n의 배수를 print()로 출력하는 함수
# # def print_multiples1(n):
# #     for i in range(1,101) :
# #         if i % n == 0:
# #             print(i,end=' , ')
# #
# # n_value1 = 3
# # print_multiples1(n_value1)
#
# # A~Z까지 중 n개의 대문자들만 빼고 print()로 출력
# # def print_multiples2(s)  :
# #     list = ([chr(ord('A')+i) for i in range(26)])
# #     if s in list :
# #         print(f'{s}는 존재합니다.')
# #         return
# #     else :
# #         print('없음')
# # s = input("알파벳 입력")
# # print(print_multiples2(s))
#
#
#
# # 세 정수의 뺄셈 함수
# # def st_three_numbers(a, b, c):
# #     result = a - b - c
# #     return result
# # print(st_three_numbers(50,7,8))
# #
#
#
# # # 문자열을 입력받고 원하는 문자의 개수를 구해주는 함수
#
# def count_characters(string,target_charcter):
#     count = 0
#     for char in string:
#         if char == target_charcter:
#             count +=1
#     return count
#
# string = input("문자열 입력 : ")
# target_charcter = input("원하는 문자 입력 : ")
# occ = count_characters(string,target_charcter)
# print(f'{target_charcter}는 {occ}번 나왔습니다.')
#
#
#
# # def count_number(number,target_number):
# #     count1 = 0
# #     for score in range(number) :
# #         if score == target_number :
# #             count1 += 1
# #     return count1
# # number = int(input("숫자를 입력 : "))
# # target_number = int(input("원하는 숫자를 입력 : "))
# # occurrence = count_number(number,target_number)
# # print(f'{target_number}는 {number}에서 {occurrence}번 나왔습니다!')
#
#
#
#
# # f(x) = 2x+1
# # def f(x):
# #     return 2 * x + 1
# #
# # result = f(2)
# # print(result)
#
# # 두 정수의 곱셈 함수
# def multiple(number1, number2):
#     return number1 * number2
#
#
# # 두 정수의 나눗셈 후 몫과 나머지 구하는 함수
# def divide(number1, number2):
#     if number2 != 0:
#         return number1 // number2, number1 % number2
#     return None
#
#
# # 1~10까지 print()로 출력하는 함수
# def print_from1_to10():
#     for i in range(10):
#         print(i + 1, end=' ')
#
#
# # 이름을 n번 print()로 출력하는 함수
# def print_name(name, count):
#     for i in range(count):
#         print(name)
#
#
# # 1~n까지의 합을 구해주는 함수
# def get_total_from1(end):
#     total = 0
#     for i in range(end):
#         total += i + 1
#
#     return total
#
#
# # 1~100까지 중 n의 배수를 print()로 출력하는 함수
# def print_time_from1_to100(time):
#     for i in range(100):
#         if (i + 1) % time == 0:
#             print(i + 1)
#
#
# # 세 정수의 뺄셈 함수
# def sub(number1, number2, number3):
#     return number1 - number2 - number3
#
#
# # 문자열을 입력받고 원하는 문자의 개수를 구해주는 함수

# def get_count_of_result(target, keyword):
#     # return len([i for i in target if i == keyword])
#     count = 0
#     for i in target:
#         if i == keyword:
#             count += 1
#     return count
#
#
# '''
#     문자열과 문자를 입력받은 뒤 해당 문자가 몇 번째 인덱스에 있는 지 검사하고,
#     만약 해당 문자가 없으면 -1을 리턴하는 함수
# '''
# def find(target, keyword):
#     # for i in range(len(target)):
#     #     if target[i] == keyword:
#     #         return i
#     #         break
#     # return -1
#
#     # result = -1
#     # for i in range(len(target)):
#     #     if target[i] == keyword:
#     #         result = i
#     #         break
#     #
#     # return result
#
#     # 초보자용(참고용)
#     result = 0
#     for i in range(len(target)):
#         if target[i] == keyword:
#             result = i
#             break
#         else:
#             result = -1
#
#     return result
#
# # result = divide(10, 3)
# # if result:
# #     value, rest = result
# #     print(f'몫: {value}, 나머지: {rest}')
# # else:
# #     print('0으로 나눌 수 없습니다.')
# #
# # print_from1_to10()
#
# # print_time_from1_to100(7)
#
# print(find('apple', 'z'))


