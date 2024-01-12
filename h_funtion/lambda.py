# lambda x #매개변수 : x + 2 #리턴값 # 익명함수

# lambda (람다) : 이름이 없는 함수, 일회성
# lambda 매개변수 , .... 리턴 값
#
# 일반 함수
def add(**kwargs) :
    def order(pay,login) :

#     return num1+num2
#
# 익명 함수
# lambda number1,number2 : number1 + number2

# 사용예시
# def change(number) :
#     return number + 2
#
# print(list(map(lambda x : x + 2,[1,2,3,4])))

#아래의 리스트의 각 요소에 2를 곱하여 변경

datas = [2,4,6,8]
print(list(map(lambda x : x*2,[2,4,6,8])))


# '/app/game', '/app/news', '/app/fashion', '/app/ranking'
urls = ['/game', '/news', '/fashion', '/ranking']


# print(list(map(lambda url : '/app' + url , urls)))
list2 = ['a','b','c','d']
#Aa Bb Cc Dd
# filter(functuon,iterator)
# 1 ~ 10 까지 짝수만 출력
# filter(function, iterator)
# 1~10까지 중 짝수만 출력
# print(list(filter(lambda number: number % 2 == 0, [i + 1 for i in range(10)])))

# ['/app/game', '/app/news', '/app/fashion', '/app/ranking']
# 'game' 서비스를 제공하는 경로 찾기
urls = ['/app/game', '/app/news', '/app/fashion', '/app/ranking']

# print(list(filter(lambda number : number for i in range(len(urls).split('/game') + [len(urls)])
print(list(filter(lambda url: url.split('/')[-1] == 'game' , urls)))
 # 입력받은 한글을 정수로 변경
# # 입력 예: 삼오일구
# # 출력 예: 3519
hangul = "공일이삼사오육칠팔구"
data = "삼오일구"

print(int("".join(list(map(lambda s: str(hangul.index(s)), data)))))


'''


hangul.index(s)는 s가 hangul 문자열에서 처음으로 나타나는 인덱스를 반환합니다. 그러나 이 값은 정수형이 아닌 문자열이기 때문에, str() 함수를 사용하여 정수를 문자열로 변환합니다.

따라서 str(hangul.index(s))는 hangul에서 s가 나타나는 인덱스를 문자열로 변환한 것입니다. 이렇게 하는 이유는 map 함수를 사용할 때 모든 값이 동일한 형식을 가져야 하기 때문입니다. 만약 변환하지 않는다면, map 함수가 반환하는 결과는 정수와 문자열이 혼합된 리스트가 되어버립니다.

쉽게 말해, map 함수가 생성하는 각 아이템은 문자열 형태의 숫자입니다. 그래서 모든 값이 동일한 데이터 타입을 가지도록 하기 위해 str() 함수를 사용합니다.








'''