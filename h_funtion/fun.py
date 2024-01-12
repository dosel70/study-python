

# def FindMax(num_list) :
#     max_data = num_list[0]
#     min_data = num_list[0]
#     for i in range(1,len(num_list)):
#         if max_data < num_list[i]:
#             max_data = num_list[i]
#         if min_data > num_list[i]:
#             min_data = num_list[i]
#     return max_data,min_data
#
# num_list = [7,3,8,9]
# result = FindMax(num_list)
# print(type(result)) # 타입은 튜플로 나온다.
# print("최대값 : ",result[0])
# print("최소값 : ",result[1])

def FindMAx(data_list):
    max(data_list)
    min(data_list)
    return max(data_list),min(data_list)
data_list = [5,7,2,6,1,8,3,1]
print(f'최대값:{max(data_list)},최소값:{min(data_list)}')





