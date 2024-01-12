class Magic:
    def __init__(self,name):
        self.name = name


    def __str__(self):
        return f'name : {self.name}'
    # def __str__(self):
    #     return f'{self.__repr__()}, __repr__() 사용됨.'

# 객체를 출력하면 항상 __repr__()가 자동으로 뒤에 붙는다.
# print(Magic().__repr__())
# 만약 해당 클래스에서 __str__()을 재정의했다면, __repr__()가 아닌 __str__()이 사용된다.
# print(Magic().__str__())
# 따라서, 생략해서 작성하면 __str__()이 붙게된다.
# Magic('magic')
# print(Magic)

class Student:
    def __init__(self,number,score):
        self.number= number
        self.score = score
    def __mul__(self,other):
        return self.score * other.score

    def __eq__(self,other):
        # 주소 비교
        if self.__str__() == other.__repr__():
            print('들어옴')
            return True
        # 타입 비교
        # isinstance(객체, 타입) : 전달한 객체가 전달한 타입일 경우 True, 아니면 False (타입은 클래스명)
        if isinstance(other,Student):
            # 값 비교
            return self.number == other.number

        return False


std1 = Student(1,30)
# std2 = Student(1,50)
std2 = std1
print(std1.__dict__)
print(std2.__dict__)
total = std1.__mul__(std2)

print(std1.__dict__.__getitem__('score'))
print([1,2,3].__getitem__(2))
print(total)
print([1,2,3].__contains__(0))
print(std1 == std2)
