# 문자열끼리만 연결(+)이 가능하다!
# data = 3
# print('안' + str(data))
# name = input("이름: ")
# formatting = f'{name}님 환영합니다.'
# print(formatting)

# 제 이름은 ???, 키는 ???cm입니다.
# name = input('이름: ')
# height = input('키: ')
# formatting = f'제 이름은 {name}, 키는 {height}cm입니다.'
# print(formatting)

# 두 정수를 입력받은 후 곱셈 결과 출력
# message1 = '첫 번째 정수: '
# message2 = '두 번째 정수: '
# number1 = int(input(message1))
# number2 = int(input(message2))
# result = number1 * number2
# formatting = f'{number1} * {number2} = {result}'
#
# print(formatting)

# map(각각 어떻게 바꿀 것인가, [])
# message = '두 정수를 입력하세요.'
# example_message = '예)1, 3'
# number1, number2 = map(int, input(message + '\n' + example_message + '\n').split(', '))
# result = number1 * number2
# formatting = f'{number1} * {number2} = {result}'
#
# print(formatting)

# 현재 시간을 입력하고 시와 분으로 분리하여 출력
# message = '현재 시간: '
# time = input(message)
# hours, minutes = time.split(':')
# formatting = f'{hours}시 {minutes}분'
#
# print(formatting)

# 핸드폰 번호를 -(하이폰)과 함께 입력받은 뒤 각 자리의 번호를 분리해서 출력
# message = '핸드폰 번호: '
# number1, number2, number3 = input(message).split('-')
# formatting = f'통신사: {number1}\n앞번호: {number2}\n뒷번호: {number3}\n'
# print(formatting)

# name = '이름과 나이를 입력하세요 : '
# name1, age1 = input(name).split(' ')
# formatting1 = f'{name1} 님의 나이는 {age1}살 입니다.'
# print(formatting1)

# 이름과 나이를 한 번에 입력받은 뒤 "000님의 나이는 000살" 형식으로 출력
# message = '이름과 나이를 입력하세요'
# example_message = '예)홍길동 20'
#
# name, age = input(message + '\n' + example_message + '\n').split()

# 3개의 정수를 입력받은 뒤 덧셈 결과 출력
# message = '3개의 정수를 입력해주세요.'
# example_message = '예/ 1/2/3'
# num1, num2, num3 =map(int,input(message + '\n' + example_message + '\n').split('/'))
# result = num1 * num2 * num3
# formatting1 = f'{num1}x{num2}x{num3} = {result}'
# print(formatting1)