
class A :
    def __init__(self,name):
        # super().__init__() 파이썬 2.* 버전에서는 항상 상위클래스에 super()>__init__을 사용해야 했다.
        # 상위 클래스의 부모 클래스는 object이다. 그러나 파이썬 3.10 버전에서는 쓰지 않는다. super().__init__ (x)
        self.name = name
        print('부모 생성자')
    def print_intro(self):
        print('A')
class B(A) : # 자식 생성자는 무조건 부모 생성자 부터 호출을 한다. 그러므로 자식 생성자는 무조건 부모 생성자 필드에 접근할 수 있다.
    def __init__(self,name):
        super().__init__(name) # super : 부모 생성자를 호출 (슈퍼 클래스를 호풀)
        print('자식 생성자') # 무조건 출력도 부모 생성자가 자식 생성자 보다 먼저 출력 된다.

    def add(self, number1, number2):
        return number1 + number2

    def print_intro(self): # 오버라이딩(Over ride) =  부모 클래스의 메소드를 무시하고 , 자식의 객체로 사용하게 된다.
        # 부모의 메소드를 그대로 사용하고자 할 때 (선택 사항)
        super().print_intro()
        # 자식의 메소드에서 추가할 내용 작성
        print('B')


b = B('조성현')
print(b.name)
print(b.print_intro())
print(b.add(5,7))

banks = []
bank_list = banks * 3
print(bank_list)


