# set = 중복이 없고, 순서가 없다.
# 값이 있는지 없는지 검사 >> 혈액형 검사, mbti 검사 ...

set_one = {1, 3, 3, 4, 5, 6, 7, 8, 9} # 3이 중복되었는데 3의 값은 나오지 않는다(오류는 없음)
set_two = {34, 45, 5, 6, 7, 8, 9}
# print(id(set_one))
# union = set_one.union(set_two) # 합집합
# intersection = set_one.intersection(set_two) # 교집합
# difference = set_one.difference(set_two) # 차집합
# print(difference)
# print(union)
# print(intersection)
# print(type(set_one)) # 세트 타입
# print(len(set_one)) # 길이
change = set_one.add('korea') # set의 값 추가
print(id(change))
print(id(set_one))
datas = [1,2,3,3,4,5]
maraton = [4,5,6,6,8,1,0]
nop = list(set(maraton)) # 아스키코드(문자 >> 숫자 or 숫자 >> 문자)로 알아서 정리가 된다. 리스트로 감싸주면,,,,
print(nop)
# sort_maraton = sorted(maraton)
# print(sort_maraton)
# nop_set = list(set(sort_maraton))
# print(nop_set)
# nop = list(set(datas)) # list 에서 중복을 제거하려면 set으로 형변환 다음 리스트로 다시 형변환
# print(datas)
# print(nop)
# print(set_one)
# print(change)
# set_three = list(set_one)
# set_three[5] = 10
# print(set_three)