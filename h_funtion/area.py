# 전역 변수(global variable)
# 지역 밖에 선언된 변수

# 지역 변수(local variable)
# 지역 안에 선언된 변수
# 어떤 지역 안에 선언된 변수
# 전역변수
count = 0

def increase():
    # print(count)

    # 지역변수
    global count # 전역변수를 수정하려면 global 키워드를 사용한다.
    count += 100

increase()
print(count)

