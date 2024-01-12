# def solution(code):
#     ret = ''
#     mode = 0
#     for idx in range(len(code)):
#        if mode == 0 :
#            if code[idx] != "1" and idx % 2 == 0 :
#                ret += code[idx]
#            elif code[idx] == "1" :
#                mode = 1
#        elif mode == 1 :
#            if code[idx] != "1" and idx % 2 == 1:
#                ret += code[idx]
#            elif code[idx] == "1" :
#                mode = 0
#     if ret == '':
#         return "EMPTY"
#     return ret
#
# code = "abc1abc1abc"
# print(solution(code))
class Post:
    number = 0
    def __init__(self, name, title, content):
        Post.number += 1
        self.number = Post.number
        self.name = name
        self.title = title
        self.content = content

    def post_info(self):
        print(self.number,self.name, self.title, self.content)
def solution(rank, attendance):
    n = len(rank)
    rank_a = []

    for i in range(n):
        if attendance[i]:
            rank_a.append([rank[i], i])
    rank_a.sort(key=lambda v: v[0])

    return 10000 * rank_a[0][1] + 100 * rank_a[1][1] + rank_a[2][1]

print(solution([3, 7, 2, 5, 4, 6, 1], [True, True, True, False, False, False, False]))
