import random as r

# randint(시작값, 끝값)
# 1~10 까지 중 랜덤한 값 1 개
rand = r.randint(1,10)
print(r.randint(1,10)) # 1 ~ 10 중 랜덤으로 나온다.

# 확률
# 1. list 선언

# 2. 확률을 계산해서 해당자리에 1 대입

# 1 -> 100
# 10 -> 10
count = 10 # 단위

count_dict = {1:100,10:10}

rating = ["꽝"] * count_dict[count]

percent = 50 # 확률

# 확률을 계산해서 해당 자리에 1 대입
for i in range(percent // 10):
    rating[i] = "당첨"

# 3. 10 개중 당첨은 5개 있기 때문에, 당첨이 나올 확률은 50 %이다.
if print(rating[r.randint(0,len(rating)-1)]) == 1:
    print("강화 성공")

print(rating)
# [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]