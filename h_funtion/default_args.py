# 만약 값을 매개변수로 전달하지 않았을 경우
# 기본 값을 설정 할 수 있고, arg = value로 작성한다.
# 매개변수에 직접 값을 할당 할 수 있음!!!!!
# def sub(number1,number2,number3,number4=0) :
#     return number1-number2-number3-number4
#
# result = sub(1,2,3)
# print(result)

# def get_info(name="이름",age=0) :
#     return{name:'age',age:'jo'}
# result = get_info()
# print(get_info(name='andy'))
# print(get_info(age='성적'))

#
# packing!

# packing

#국,영,수 전달받고 총점 출력
# kor,eng,math = map(int,(input("국어,영어,수학 점수를 입력하시오 : ").split()))
# def grade(*args) :
#     total = 0
#     avg = 0
#     for i in args :
#         total += i
#         avg = total / len(args)
#     return round(avg,0)
#
# print(grade(kor,eng,math))

# 문자열에서 'A'가 몇 개 있는지 검사하는 함수
# def count_occurrences(text, word):
#     words = text.split()
#     count = 0
#     for w in words:
#         if w == word:
#             count += 1
#     return count
#
# text = "hello world A B C A A A H A H A"
# word_to_find = input("찾을 문자를 입력하세요: ")
# result = count_occurrences(text, word_to_find)
# print(result)

# 최대값 최소값 구하기
# def MaxAndMin(num_list) :
#     max = num_list[0]
#     min = num_list[0]
#
#     for i in range(1,len(num_list)):
#         if max < num_list[i]:
#             max = num_list[i]
#             num_list.append(max)
#         if min > num_list[i]:
#             min = num_list[i]
#             num_list.append(min)
#         else :
#             pass
#     return max,min
#
# numlist = [5,39,2,500,29]
# result = MaxAndMin(numlist)
# print(f'최대값 = {result[0]}\n최소값 = {result[1]}')

#소문자를 대문자로 바꿔주기

# def change(str):
#    result = " "
#    for i in str :
#        if ord(i) >= 97 and ord(i) <= 122 : # 아스키코드로 변환하여 소문자에서 대문자로 바꿈 와 역시..
#            result +=  chr(ord(i) - 32) # 대문자로 바꿔준다.
#        else :
#            result += i
#    return result
#
# alpha = "Abdjeidk"
# print(change(alpha))

# 한글을 정수로 바꿔주기

#
# num1 = input("입력할 한글 : ")
# def translate(num1):
#     result = ""
#     for i in num1:
#         result += str(kor.index(i))
#     return int(result)
# print(translate(num1))

kor = ["공","일","이","삼","사","오","육","칠","팔","구"]
num = [0,1,2,3,4,5,6,7,8,9]
# 정수를 한글로
num2 = int(input("입력할 정수를 입력하세요 : "))
num1 = input("입력할 한글을 입력하세요 : ")

print(list(map(lambda s: kor[int(s)],str(num2))))
print(list(map(lambda s : str(kor.index(s)), num1)))