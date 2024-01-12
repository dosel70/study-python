class Student:
    def __init__(self,number,score):
        self.number = number
        self.score = score

    def __add__(self,other): # 합
        return self.score + other.score

    def __eq__(self,other): # 주소 비교하는 매직 메소드
        if self.__repr__() == other.__repr__(): # str 메소드가 없을 때 대신 써줌 (문자열 메소드)
            print("돌아옴")
            return True
        if isinstance(other,Student): # 타입을 비교하며, isinstance(객체, 타입) : 전달한 객체가 전달한 타입일 경우, True, 아니면 False
            return self.number == other.number
        return False
std1 = Student(1,30)
std2 = Student(2,80)

total = std1 + std2
print(total)
print(std1.__dict__.__getitem__('score')) # >> __dict__.__getitem__('score') 의 의미 __dict__는 딕셔너리 연산자, getitem은 인덱스 연산자
print(std1 == std1)
