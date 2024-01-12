# # Comprehension(컴프리헨션 : 어떤 뜻을 내포하고 있다.)
#
# # 반복하거나 특정 조건을 만족하는 list를 보다 쉽게 만들어 내기 위한 방법으로 쓰인다.
#
# #List Comprehension
# # [표현식(ex:항목 * 5) for 항목 in iterateor (if 조건)]
#
# # number_list = [1,2,3,4]
# # result_list = [num * 3 for num in number_list ]
# # print(result_list)
#
# number_list = [1,2,3,4]
# # [6,12]
#
# result_list = [number * 3 for number in number_list if number % 2 == 0]
# print(result_list)
#
# # [표현식 if 조건 else 표현식 for 항목 in iterator]
#
# # 참 = [1,6,3,12]
# num_list = [1,2,3,4]
# result_list = [num * 3 if num % 2 == 0 else num * 5 for num in num_list]
# print(result_list)
#
# 아래의 리스트에서 양수만 추출한 뒤 새로운 list에 담기
number_list = [10,20,30,-20,-3,50,-70]
result_list = [num for num in number_list if num > 0]

new_list = result_list

print(new_list)
# n개의 0으로만 채워진 리승트
# 제곱의 결과가 10보다 큰 결과담은 리스트
# 0~9까지 중 3의 배수만 담은 리스트
number_list = [1,-2,3,-4,5]