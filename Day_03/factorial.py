# message = "정수 입력"
# number = int(input(message))
# digit = 1
#
# while number > 0 :
#     digit *= number
#     number -= 1
# print(digit)

# n = int(input("숫자 입력: "))
#
# # 위쪽 삼각형 출력
# for i in range(n):
#     print(" " * (n - i - 1), end='')
#     print("*" * (2 * i + 1))
#
# # 아래쪽 삼각형 출력
# for j in range(n - 2, -1, -1):
#     print(" " * (n - j - 1), end='')
#     print("*" * (2 * j + 1))
data_list = [1,2,3]

data_list.append(66)
del data_list[2]
print(data_list)
data_list.index(2)
print(data_list)
data_list.clear()
print(data_list)

subway = ["리신","이즈리얼",505,506]
print(subway.index("이즈리얼"))
subway[2] = "안녕"
print(subway)