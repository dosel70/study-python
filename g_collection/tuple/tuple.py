# mutable  = 가변성 >> list,dict
data_list = [1,2,3,4]
# temp = data_list
data_list2 = data_list
#
#
# print(temp) #1,2,3,4
# print(data_list2) # data_list2 == temp == data_list
# data_list2[0] = 10
# print(data_list)
# print(data_list2)
# print(id(temp))
# print(id(data_list))
# print(id(data_list2))

# immutable = 불변성 >> 튜플, set

data_tuple=(1,2,3,4,5)
data_tuple2 = data_tuple
# data_tuple2[2] = 10 # 수정이 안됨


data_tuple2 = data_tuple + (5,6) # 수정이 되는게 아니라 새로운 튜플을 만들어지는것이다.
print(data_tuple) #원본 그대로
print(data_tuple2) #새로운 data_tuple 생성
data_tuple3 = 1,2
sum = data_tuple3 + data_tuple2
print(sum)
# print(data_tuple3)
# # print(data_tuple2)
#
# print(type(data_tuple))
# print(data_tuple[0])

ERROR_CODE = 1, # 대문자로 쓴 이유 >> 상수 이기때문에(협회에서 약속) >> 자바에서는 final의 의미
print(type(ERROR_CODE))
print(ERROR_CODE) # (1,)

test = list(data_tuple2) # 튜플을 수정하고 싶다면 리스트로 감싸서 새로운 변수에 담아라
test[2] = 10
print(test)