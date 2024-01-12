# # animals = ['dog', 'cat', 'bird','fish']
# #
# # humans = ["철수","영희","광수"]
# #
# # animals.extend(humans) # 리스트 확장
# # print(len(animals))
# # # # 값 추가
# # # animals.append('monkey')
# #
# # # # 값 삭제
# # # # animals.remove('monkey')
# # # del animals[2]
# # # print(animals)
# # # animals.clear()
# # # print(animals)
# # fish = animals.index("fish")
# # print(fish)
# # # # 값 삽입
# # # animals.insert(0,"monkey")
# #
# # # 값 수정
# # animals[animals.index('fish')] = "lion"
# # print(animals)
# #
# #
# # # # 인덱스로 접근
# # # animals.append(100)
# #
# # # # 음수 인덱스 가능 ( 가장 마지막부터 순서대로 앞으로 이동한다.)
# # # print(animals[-4])
# #
# # # print(animals.index("monkey"))
# #
# # # animals.pop(2)
# #
# # # print(animals)
# # #
# # # print(type(animals))
# # animals.insert(1,1500)
# # print(len(animals))
# # print(animals)
# #
# # first = ["a","b","c","d","e"]
# # print(first[0], first[1], first[-1])
# # jack = ['welcome!'] * 3
# # print(jack)
#
# # 그 외
# # animals = ['dog', 'cat', 'bird','fish']
# # print(animals * 2)
# #
# # print("dog" in animals)
# # print("tiger" in animals)
# #
# # for animals in animals:
# #     print(animals)
#
# # 실습
# # 1~90까지 list 에 담고 출력
# # 1 ~ 100 까지 짝수만 list에 담고 출력
# # 1 ~ 10 까지 list에 담고 짝수만 출력
# # 회원정보를 list에 담은 뒤 두 번째 회원의 이름을 변경하고 마지막 회원은 삭제
#
#
# list = [] # list = [0] * 90
# for i in range(len(list)) :
#     list[i] += 1
# for i in range(90) :
#     list.append(i+1)
# print(list)
#
#
# # arr_list = [0] * 50
# # for i in range(len(arr_list)) :
# #     arr_list[i]  = (i+1) * 2
# # print(arr_list)
# # #
# # arr1_list = []
# # for i in range(10) :
# #     arr1_list.append(i + 1)
# # for i in range(len(arr1_list)) :
# #     if arr1_list[i] % 2 == 0:
# #         print(arr1_list[i])
#
#
#
# # user_list = []
# # while True :
# #     choice_one = "1. 이름 입력 \n2. 수정 \n3. 삭제 \n4. 명단 확인"
# #     choice = int(input(choice_one + "\n메뉴 입력 "))
# #
# #
# #
# #     if choice == 1 :
# #         while True:
# #             name = input("이름 입력 : ")
# #             user_list.append(name)
# #             if name == '':
# #                 break
# #
# #
# #
# #     elif choice == 2:
# #         while True:
# #             old_name = input("변경하고 싶은 이름을 입력하시오 (엔터키 누르면 종료): ")
# #             if old_name == '':
# #                 break
# #             if old_name in user_list:
# #                 index = user_list.index(old_name)
# #                 new_name = input("새로운 이름을 입력 : ")
# #                 user_list[index] = new_name
# #             else:
# #                 print("이름 없음")
# #     elif choice == 3:
# #         while True:
# #             del_name = input("삭제할 친구 이름 (엔터키 누르면 종료): ")
# #             if del_name == '':
# #                 break
# #             user_list.remove(del_name)
# #     if choice == 4 :
# #         print(user_list)
#
# # s = "189,000원"
# # s1
# list 안의 list
number_list = [[1,3,5] , [2,4,6]]

for i in range(len(number_list)):
    for j in range(len(number_list[i])):
        print(number_list[i][j])

