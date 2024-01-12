# 인간 ( 부모 )
# 이름, 나이
# 걷기 (walk)
#: 두 발로 걷습니다! 출력

class Human :
    def __init__(self,name : str,age : int):
        self.name = name
        self.age = age
    def walk(self):
        print("두발로 걷습니다.")

class Monkey(Human):
    def __init__(self,name,age,zoo):
        super().__init__(name,age)
        self.name = name
        self.age = age
        self.zoo = zoo
        print(age,name,zoo)

    def walk(self):
        super().walk()
        print("네발로 걷습니다.")

kingkong = Monkey('콩순이',20,'에버랜드')
kingkong.walk()






