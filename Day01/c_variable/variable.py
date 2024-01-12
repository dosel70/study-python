# 여러 개의 변수를 한 줄에 선언
a = 10; b = 20; c = 30
print(a, b, c, sep=', ')

a, b, c = 100, 200, 300
print(a, b, c)

# 변수의 값을 서로 바꾸기
a = 11
b = 33
print(a, b)
print(a,b)

# temp = a
# a = b
# b = temp
# print(a, b)

a, b = b, a
print(a, b)

# 동적 바인딩
a = 10
print(type(a))
a = 10.5
print(type(a))
a = 'A'
print(type(a))
a = 'ABC'
print(type(a))
a = ['A', 'B', 'C']
print(type(a))
a = {'A':1, 'B':2, 'C':3}
print(type(a))
a = True
print(type(a))

# 변수명 주의사항
num = 10
print(type(num))
num2 = 10.5
print(type(num2))
text = 'A'
print(type(text))
text2 = 'ABC'
print(type(text))
list = ['A', 'B', 'C']
print(type(text2))
score = {'A':1, 'B':2, 'C':3}
print(type(score))
condition = True
print(type(a))

# 서식문자
name = '홍길동'
age = 20
height = 157.45
height2 = 157.55
# 5의 경우네는 5의 앞자리가 홀수인 경우에 올림을 하고 짝수인 경우에 버림을 하여 짝수로 만들어준다.
# 예를 들어 157.45는 157.4로, 157.55는 157.6으로 반올림한다.
# 이를 "오사오입"이라고 한다.
print('이름: %s' % name)
print('나이: %d' % age)
print('키: %.1f' % height)
print('키: %.1f' % height2)

# 실습
# 정수 2개를 변수에 담기
# 두 정수의 합을 아래 형식으로 출력하기
# 1 + 3 = 4

# format 함수
name = '홍길동'
age = 80
height = 156.26
print('이름: {}\n나이: {}\n키: {:.2f}'.format(name, age, height))

# 실습 (format)
# Hello 파이썬, Python is fantastic
# Hello 장고, Django is fantastic
# hello 리액트, React is fantastic

# f-string
name = '홍길동'
age = 80
height = 156.26

print(f'이름: {name}')
print(f'나이: {age}살')
# round(실수값, 반올림 자리수
print(f'키: {round(height, 1)}')

# 실습(f-string)
# Hello 파이썬, Python is fantastic
# Hello 장고, Django is fantastic
# hello 리액트, React is fantastic