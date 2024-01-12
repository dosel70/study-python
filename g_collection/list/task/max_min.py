# 5개 정수의 최소값과 최대값을 각각 출력

def get_maxmin(num_list) :
    max_list = num_list[0]
    min_list = num_list[0]

    # for i in range(1,len(num_list)) :
    #     if max_list < num_list[i] :
    #         max_list = num_list[i]
    #     if min_list > num_list[i] :
    #         min_list = num_list[i]
    # return max_list, min_list

    # result = [max_list = num_list[i] for i in range(1, len(num_list)) if max_list < num_list[i]]
    #
    #     return max_result, min_result



# num_list = [1,5,7,3,2]
# result = get_maxmin(num_list)
# print("최대값은",result[0] ,"최소값은", result[1])
#
#
# def get_max(num_list):
#     max_result = num_list[0]
#     min_result = num_list[0]
#     max_reuslt1 = [max_result = num_list[i]
#     for i in range(1, len(num_list) if max_result < num_list[i])]
#     return max_result, min_result
#
#
# num_list = [5, 9, 2, 8, 3]
# result1 = get_max(num_list)
# print(f"최대값은 {result1[0]} 최소값은 {result1[1]}")