class A :
    @classmethod
    def __new__(cls, *args, **kwargs):
        print("__new__")
        obj = object.__new__(cls)
        return obj
    def __init__(self,data1,data2,name=""):
        print("__init__")
        print(self)
        self.data1 = data1
        self.data2 = data2
        self.name = name
    # def print_name(self,name):
    #   print(name)
    def print_name(self):
        print(self.name)
a = A(10,20,'a')
print(a)