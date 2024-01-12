# upper(), lower()
# jack = "AbcDefQWEf"
# print(jack.lower())
# print(jack.upper())
#
jack = "dosel70@naver.com"
print(jack.split("@"))

# #split()
# data = "사과,바나나,파인애플,포도,복숭아"
# data = data.split(",",2)
# print(data)

# jol = ("a b c d e f g h i j k l")
# print("a      \n        b".split(" "))
# print(jol.split())
#

# # join()
# print(":".join(jol.split()))
# print(":".join(["a","b","c","d"]))
#

# # replace('기존 값, '새로운 값')
# print("A b C d".replace(" ",""))
# print("안녕! 반가워".replace("!", "?"))
#

# # strip(), lstrip(), rstrip() : 앞 뒤 공백을 제거 할 때 보통 사용한다.
# print("a    b      c".strip())
# print("a    b      c".strip(" "))
# print("apple".lstrip("p"))
# print("apple".strip("a"))
# print("apple".strip("e"))
# print("apple".strip("l"))
#

# # index()  : 찾고자 하는 값이 없으면 오류가 발생
# print("ABC".index("A"))
# # print("abc".index("z")) # 오류
#

# # find() : 찾고자 하는 값이 없으면 -1을 가져온다.
# print("ABC".find("A"))
# print("ABC".find("Z"))
#

# # in : 값의 유무 검사
# print("A" in "ABC")
#
# # count() : 전달한 값이 몇 개 있는지 검사

s = "189,000원"
# s_list = [i for i in s if '0' <= i <= '9']
print("".join(i for i in s if '0' <= i <= '9'))

# for i in s:
#     if '0' <= i <= '9':
#         print(i)

# # join()
# print(":".join(jol.split()))
# print(":".join(["a","b","c","d"]))