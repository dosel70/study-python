# def solution(flo):
#     return int(flo)
# result = solution(34.54)
# print(result)

# 대소문자 바꾸기
# str = "aBcDeFg"
# print(str.swapcase())

#특수문자 출력하기
#!@#$%^&*(\'"<>?:;
# print('"!@#$%^&*(\\\'\'''"<>?:;"')
# print(r'!@#$%^&*(\'"<>?:;')

# 슬라이싱 하기
# def solution(num_list, n):
#     return num_list[n-1:]
# num_list = [2,1,6]
# n = 3
# print(solution(num_list, n))

# def solution(start_num, end_num):
#     return [i for i in range(start_num, end_num )]
# print(solution(10,1))

# def solution2(start_num, end_num):
#     result = []
#     while start_num >= end_num:
#         result.append(start_num)
#         start_num -= 1
#     return result
# print(solution2(10,3))
#
# # def solution(n):
#     return str(n)

# print(solution(123))
# str = input("Enter a string: ")

# while True :
#     if len(str) <= 1 and len(str) <= 100000 and str != ' ':
#
#         print(str)
#         break
#     else :
#         continue
#
# def solution(rank, attendance):
#     n = len(rank)
#     answer =0
#     r_a = []
#
#     for i in range(n):
#         if attendance[i]:
#             r_a.append([rank[i], i])
#
#     r_a.sort(key = lambda v : v[0])
#
#     return 10000 * r_a[0][1] + 100 * r_a[1][1] + r_a[2][1]
