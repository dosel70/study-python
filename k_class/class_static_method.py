class Student:
    status = '쉬는 중'

    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    @staticmethod
    def print_start_time_of_study():
        print("9시 땡")
        Student.status = '공부 중'


han = Student(0, 0, 0)
hong = Student(0, 0, 0)
print(Student.status)

Student.print_start_time_of_study()
print(Student.status)