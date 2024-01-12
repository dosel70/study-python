class A:

    name = 0
    @classmethod
    def __new__(cls,*args, **kwargs):
        print('__new__')# 기본 생성자
        obj = super().__new__(cls)           # __new__ >> 메모리에 할당하는 애 (진짜 생성자)
        return obj

    def __init__(self,data1,data2,name=''): # 메모리를 직접 할당 받아서 저장하는애는 __init__ : __new__와 __init__은 한쌍이다.
        print('__init__')
        print(self) # self에는 무조건 그 객체의 주소가 담긴다.
        self.data1 = data1
        self.data2 = data2
        self.name = name
    # def print_name(self,name):
    #     print(name)

    def print_name(self):
        print(self.name)


# a = A() # 주소값이 된다, 생성자 , A()는 주소값
a=A(10,20)
# a.data1 = 10 # 동적바인딩으로 기존에 없던 data1,data2값이 만들어진다.
# a.data2 = 20 # a >> 객체 .의 필드 주소로 들어가져서 data1,data2의 주소값이 만들어진다.
print(a.data1,a.data2)
# a.print_name('a')


# b = A()
b=A(10,20)
print(b)
print(a)
# b.data1 = 100
# b.data2 = 200

 # a라는 필드에 존재

print(b.data1,b.data2)
b.print_name('b') # b 라는 필드에 존재
# 즉 객체는 계속 생성된다!
