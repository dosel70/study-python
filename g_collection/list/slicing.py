# 인덱스 슬라이싱

# animals = ['cat', 'dog', 'horse', 'monkey', 'rabbit']
#
# # list[inclusive_start = 0 : exclusive_end=len(list) -> list
# print(animals[2:3])
# print(animals[1:4])
# print(animals[:3])
# print(animals[2:])
#
# #list[inclusive_start = 0 . exclusive_end = len(list) : step = 1
# food = ['pizza','bab','noodle','hambuger']
# print(food[:3:2])
# print(food[2::2])
#
# # 역순 출력
# print(food[::-1])

# number_list = list(range(1,11))
# print(number_list)

#[1,3,5,7,9]
#[6,5,4,3,2]
#[2,4,6]
#[2,3,4,5,6,7]

# number_list = list(range(1,11))
# print(number_list[::2])
# print(number_list[5:0:-1])
# print(number_list[1:7:2])
# print(number_list[1:7])

# animals = ['cat', 'dog', 'horse', 'bird']
# zoo = ['panda','giraffe']
#
# # animals[1:2] = zoo
# # print(animals)
#
# animals.insert(animals.index('dog')+1,'giraffe')
# print(animals)
#
# animals.insert(animals.index('dog')+1 , zoo)
# print(animals)

# 슬라이싱,insert,del를 사용하여 아래의 리스트 만들기

# 슬라이싱, insert, del 를 사용하여 아래의 list 만들기
# ['dog', 'hamster', 'fish', 'dog' 'whale', 'bird']
animals = ['dog', 'dog', 'cat', 'bird']
del animals[2]
# # # 값 삽입
animals.insert(2,"whale")
animals.insert(1,"hamster")
animals.insert(animals.index("hamster")+1,"fish")



print(animals)