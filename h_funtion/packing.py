# unpacking : 값을 풀어서 적는것
# def get_total(number1,number2,number3) :
#     return number1 + number2 + number3


# packing : 값을 묶어서 적는것
# def get_total(*numbers):
#     # 외부에서 전달 받은 값들이 numbers(튜플)에 저장된다.
#     print(type(numbers))
#     total = 0
#     for number in numbers :
#         total += number
#
#     return total
# 여러개의 값을 콤마로 구분하여 전달한다.
# total = get_total(1,2,3,4,5,6)
# print(total)

# 여러개의 값을 하나로 묶어서 전달하게 되면, packing으로 인해 첫 번째 방에 통째로 들어가게 된다.
# 즉 결과는 다음과 같다. ([1,2,3,4,5])
# 따라서 내부의 요소를 각각 전달하고 싶다면, 앞에 *을 작성해야 한다.
# numbers = [1,2,3,4,5]
# total = get_total(*numbers)
# print(total)

# 국,영,수 전달받고 총점 출력
# packing!
# 문자열에서 'A'가 몇 개 있는지 검사하는 함수
# packing

def get_grade( *grade):
    total = 0 # 총점
    for score in grade: # 과목
        total += score
    return total
print(get_grade(50,50,50))

# 내가 푼 방법
# num1 = int(input("국어 : "))
# num2 = int(input("수학 : "))
# num3 = int(input("영어 : "))
#
# grade = {
#     '국어' : num1, '수학' :num2,'영어':num3
# }
# total = get_grade(*grade.values())
# print(total)

 # 문자열을 입력받고 원하는 문자의 개수를 구해주는 함수 - 1
def count_words(*strings) :
    return [str.count(word) for str in strings]
word = input('영단어 입력 : ')
print(count_words('adc', 'ddf', 'ddd', 'dddd', 'ddddd'))

# 문자열을 입력받고 원하는 문자의 개수를 구해주는 함수 - 2
# def count_words(*strings):
#     count = 0
#     for word in strings:
#         if word == target_word:
#             count += 1
#     return count
#
# target_word = input("찾을 문자 입력: ")
# result = count_words("apple", "apple", "melon", "grape", "orange")
# print(result)


