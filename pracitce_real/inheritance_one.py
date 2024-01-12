class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def walk(self):
        print("두발로 걷습니다.")
class Monkey(Person):
    def __init__(self,name,age,zoo):
        super().__init__(name,age)
        self.zoo = zoo

    def walk(self):
        print("네발로 걷습니다.")

name = Monkey("콩순이",12,"서울시 동물원")
name.walk()
print(name.__dict__) # 딕셔너리 형태로 받아오게 함

