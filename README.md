Python - 프로그래밍 언어
컴퓨터와 소통하기 위해 사용하는 언어

소스코드: 명령어를 작성해 놓은 것
         개발자와 컴퓨터가 소통할 것을 글로 작성해 놓은 것
소스파일: 소스코드가 작성되어 있는 파일
컴파일: 사람의 언어를 컴퓨터 언어로 바꿔주는 작업
컴파일러: 컴파일 해주는 프로그램 또는 명령어
인터프리터: 인터프리트를 해주는 프로그램 또는 명령어
    ※ 파이썬은 인터프리터 안에 컴파일러를 내장하고 있다.
    인터프리터는 매번 소스코드를 한 줄 씩 해석해서 실행하므로(개별 처리), 전체 프로그램의 퍼포먼스에 큰 손해를 본다.
    파이썬은 소스코드를 바이트 코드로 컴파일한 뒤 이를 번역기가 돌려주는 방식으로 실행된다.
    따라서 컴파일 언어인지, 인터프리트 언어인지를 구분하는 것이 아니라 어떻게 구현하였는지로 판단해야 한다.
프로그램: 소스코드로 잘 짜여진 틀

1. 일반 프로그램

    프로그램
    OS(운영체제): 하드웨어에 적절한 전기신호를 흘려주는 역할
    하드웨어

    - 일반 프로그램은 이식성이 좋지 않다.

2. Python 프로그램

    프로그램
    PVM: Python 프로그램을 OS에 맞게 번역한다.
    OS(운영체제): 하드웨어에 적절한 전기신호를 흘려주는 역할
    하드웨어

    - Python 프로그램은 이식성이 좋다.

콘솔: 개발자가 내 컴퓨터(로컬)와 직접 소통할 수 있는 입출력장치(입력: 키보드, 출력: 모니터)

터미널: 내 컴퓨터(로컬)뿐만 아니라 다른 컴퓨터에 원격으로 접속 할 수 있는 콘솔을 구현한 프로그램

쉘: 명령어 해석기

정리
    1. 개발자가 터미널에 명령어 입력
    2. 쉘이 명령어를 받은 뒤 해석 및 수행
    3. 터미널은 쉘에게 받은 결과를 화면에 출력

변수 - 저장공간
    변수는 값을 담는 저장공간이다.
    x = 10, x라는 이름의 저장공간이 RAM(메모리)에 만들어지고 10이라는 값이 들어간다.

자료형(Type) - 저장공간의 종류
    동적 바인딩: 값에 따라 자료형이 정해진다.

    자료형(type)       값
    정수(int)       0, 10, -187, ...
    실수(float)       0.0, 10.58, -77.568, ...
    문자열(str)       '0', "0.0", """홍길동""", '''Python''', ...
    리스트(list)       [1, 2, 3], [0], [3,], ...
    튜플(tuple)       (1, 2), (), 1, 2, 3, (1,), ...
    딕셔너리(dict)   {key:value,}, ...
    집합(set)       {1, 2, 3}, {1}, ...
    불린(bool)       True, False

변수명 주의사항
    문자로 시작해야 한다.
    특수문자는 사용할 수 없다. 단, _는 허용한다.
    소문자로 시작한다.
    공백을 사용할 수 없다.
    되도록 한글은 사용하지 않는다.
    명사로 사용한다.
    뜻이 있는 단어를 사용한다.
        - a, b, c, d, e, ... (X)
        - data, number, age, name, ...(O)

변수의 선언과 사용
    1. 선언: 대입연산자가 있다면 선언이다. (값으로 봐서는 안됨)
    2. 사용: 대입연산자가 없다면 사용이다. (반드시 값으로 봐야함)

표기법
    파스칼 표기법(클래스명, 오류)
        대문자로 시작하고 이어지는 단어의 시작은 대문자로 작성한다.
        PascalCase

    카멜 표기법(Java 등에서 사용)
        소문자로 시작하고 이어지는 단어의 시작은 대문자로 작성한다.
        camelCase

    스네이크 표기법(변수, 함수)
        단어 사이에 언더스코어(_)를 작성한다.
        snake_case

    케밥 표기법(HTML, CSS, URL 등에서 사용)
        kebab-case

서식문자 - 따옴표 안에서 변수 또는 값을 사용해야 할 때 작성한다.
    반드시 따옴표 안에서 작성한다.

    ----------------------------------
    서식문자   설명
    ----------------------------------
    %d           10진수 정수 표현
    %f           실수 표현
    %s           문자열 표현
    ----------------------------------

변수를 사용하는 이유
    1. 반복되는 값을 쉽게 관리하고자 할 때
    2. 값에 의미 부여를 할 때(자료구조)



  제어문
    컴파일러의 방향을 제어할 수 있는 문법이며,
    건너뛰기, 되돌아가기 등이 있다.


조건문
    if문

    1.
        if 조건식 :
            실행할 문장
        if 조건식 :
            실행할 문장
        if 조건식 :
            실행할 문장

         ...

    2.
        if 조건식 :
            실행할 문장
        elif 조건식 :
            실행할 문장

          ...
        else :
            실행할 문장



반복문
    for : in 절 뒤의 요소를 순서대로 변수에 담고 다음 값이 더 이상 없을 경우 종료


        for 변수명 in range(inclusive_start, exclusive_end, step):
            실행할 문장
            디폴트

    while : 조건식이  True 일때, 반복, False 일 때 종료

        while 조건식 :
            실행할 문장




# -*- coding: utf-8 -*-
"""
2차원 리스트

"""
# 2차원 리스트
# s =  [
#      [1,2,3,4,5],
#      [6,7,8,9,10],
#      [11,12,13,14,15]
#      ]
# print(s)

# score = [
#         ["김철수",1,2,3,4,5],
#         ["김영희",6,7,8,9,10],
#         ["최지영",11,12,13,14,15]
#         ]

# print(score)

# 동적 2차원 리스트
rows = 3
cols = 5
s=[]
for row in range(rows) :
    s += [[0]*cols]

print("s=",s)

# # rows = 3
# # cols = 5
# # s = [ ([0] * cols) for row in range(rows)]


# # print("s = ",s)

# a = [
#     [1,2,3,4,5],
#     [6,7,8,9,10],
#     [11,12,13,14,15]
#     ]

# rows = len(a)
# cols = len(a[0])

# for r in range(rows) :
#     for c in range(cols):
#         print(a[r][c], end =",")
#     print()


rows = 6
cols = 6



# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 16:34:24 2024

@author: user
"""

# 친구 리스트 설정 (친구 추가를 통해 계속 업데이트)
choice = 0
addList = []
while choice != 5 :
    print("----------------------------")
    num1 = "\n1. 친구 리스트 출력"
    num2 = "\n2. 친구추가"
    num3 = "\n3. 친구 삭제"
    num4 = "\n4. 이름 변경"
    num5 = "\n5. 종료"
    print(num1,num2,num3,num4,num5)
    choice = int(input("원하는 메뉴의 버튼을 클릭하세요 : "))
    print("----------------------------")


    if choice == 1 :
        print(addList)

    elif choice == 2:
        while True :
            name = input("친구 추가 (엔터키 누르면 종료): ")
            if name == '':
                break
            addList.append(name) # 친구 리스트에 친구 이름들을 계속 추가


    elif choice == 3:
        while True :
            del_name = input("삭제할 친구 이름 (엔터키 누르면 종료): ")
            if del_name == '':
                break
            addList.remove(del_name)

    elif choice == 4:
        while True :
            old_name = input("변경하고 싶은 이름을 입력하시오 (엔터키 누르면 종료): ")
            if old_name == '':
                break
            if old_name in addList:
                index = addList.index(old_name)
                new_name = input("새로운 이름을 입력 : ")
                addList[index] = new_name
            else :
                print("이름 없음")
    elif choice == 5:
        print("프로그램을 종료합니다.")
        break
    else :
        print("정확한 번호를 입력해주세요")
        continue




        # -*- coding: utf-8 -*-
"""
함수는 특정 작업을 수행하는 명령어들의 모음에 이름을 붙인 것
함수의 장점 : 1. 프로그램 안에서 중복된 코드를 제거
2. 복잡한 프로그래밍 작업을 더 간단한 작업들로 분해할 수 있다. 각 함수들은 레고의 블록 처럼 다른 함수들과 연결되어서
하나의 프로그램을 구성한다. 3. 함수는 한번 만들어지면 다른 프로그램에서도 재사용 될 수 있다.
4. 함수를 사용하면 가독성이 증대되고, 유저 관리도 쉬워진다.
"""


# name = "철수"
# msg = "어서 집에 오너라"
# def say_hello(name,msg):
#     print("안녕",name,"야, " ,msg)
# print(say_hello(name, msg))


# def get_sum(start,end) :
#     sum = 0
#     for i in range(start,end+1):
#         sum+=i
#     return sum
# print(get_sum(1, 20))
# print(get_sum(1, 100))

# def square(n):
#     return n*n
# print(square(5))


# def power(x,y) :
#     result = 1
#     for i in range(y):
#         result = result * x
#     return result
# print(power(10, 2))

# x =int(input("정수 입력 : "))
# def fac(x):
#     digit = 1
#     while x > 0 : # x가 0이 되야 반복문 종료 >> x // 10 == 0
#         digit = digit * x
#         x -= 1

#     return digit
# value = fac(x)
# print(value)


celebration = "\n생일 축하 합니다!"
celefriend = "\n사랑하는 친구의 생일축하 합니다!"

def birthday(celebration):
    result = ""  # 결과 문자열을 초기화
    for i in range(2):
        result += celebration  # 결과 문자열에 celebration을 추가
    return result

print(birthday(celebration), celefriend)




# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 14:20:46 2023

@author: user
"""

# subway = [10,20,30]

# subway = ["리신","이즈리얼",505,506]
# print(subway.index("이즈리얼"))
# print(subway.append("라이즈"))
# print(subway)

# subway.insert(0,"티모")
# '''
# print(subway.pop())
# print(subway)
# print(subway.pop())
# print(subway)
# print(subway.pop())
# print(subway)

# '''

# print(subway.count(505)) # 몇번들어갔는지 확인

# num_list = [5,2,4,3,1]
# num_list.sort() # 정렬
# print(num_list)

# kist = [1,2,3,4,5]
# kist.reverse() # 뒤집기
# print(kist)

# # num_list.clear() # 모두 지우기


# # 리스트 확장
# num_list.extend(kist)
# print(num_list)
# total_scores = 0
# scores = []
# for i in range(10) :
#     value = int(input("성적을 입력하세요 : "))
#     scores.append(value)
#     total_scores += value
# avg = total_scores / 10

# highscores = 0
# for i in range(len(scores)) :
#     if scores[i] >= 80 :
#         highscores += 1
# print(f'성적 평균은 {avg}점 입니다. ')
# print(f'80점 이상 학생은 {highscores}명 입니다.')

# puppy = []
# total_puppy = " "
# while True:
#     name = input("강아지의 이름을 입력하시오(종료시에는 엔터키) : ")
#     if name == '' :
#         break
#     puppy.append(name)
#     total_puppy += name

# print(f'강아지들의 이름 :')
# for name in puppy:
#     print(name,end=', ')

first = ["a","b","c","d","e"]
print(first[0], first[1], first[-1])
jack = ['welcome!'] * 3
print(jack)
for x in [1,2,3]: print(x)
# print(first[2:4]) # 슬라이싱
# print(first[3])
# print(len(first))
squares = [0,1,2,3,4,5,6,7,8,9]
squares[7] = 49
print(squares)
squares[2:7] = ["a","b","c","d","e"]
print(squares)

for x in [1,2,3] : print(x)

# for squares in ["안녕하세요"] : squares
# print(squares)
# squares.insert(1,"하이")
# print(squares)

# 얕은 복사 shallow copy (리스트는 실질적으로 복사 x)
# scores = [1,2,3,4,5,6]
# values = scores
# scores[2] = 99

# for scores[2] in scores :
#     print(scores,end='')

# 깊은 복사
level = [100,200,300,400,600,900]
value = list(level)
value[5] = 9900
print(value)
print(level)

dict
    한 쌍으로 저장되어 관리한다. {key1:value1 , key2:value2}... (각각의 키와 value값으로 한쌍 이 맺어져서 저장된다.)
    (ex : 사이트 회원 리스트 , 서버와 데이터를 공유할 때 json 형태)
    len()를 사용하면 한 쌍을 1로 카운트 한다.
    키 값은 중복이 될 수 없지만, 값은 중복이 가능하다.
    키 값을 주면 그 키의 값을 가지고 온다. (key(set 처럼 순서 x) : value(value 값에 리스트를 추가 할 수 있다.) )

    딕셔너리 선언

        dict 명 = {키 : 값, 키 : 값 , 키 : 값 ...}

    딕셔너리 사용
        -추가, -수정
            dict명[키] = 값
            키 값이 기존에 있으면 수정이고, 기존에 없으면 추가이다.

        -검사
            키 in dict 명 : 키가 있으면 참
            키 not in dict 명 : 키가 없으면 참


        -삭제



list
    여러개의 저장공간이 나열되어 있는 것.

    사용 목적
    1. 여러 번 선언하지 않고 한 번만 선언하기 위해서 사용
    2. 규칙성 없는 값에 규칙성을 부여하기 위해서 사용

 list 선언
    - 어떤 값을 넣을 지 알때
        list 명 = [값1,값2]...
    - 어떤  값인지는 모르지만 칸 수는 알때
        list명 = [값] * 칸 수
    - 어떤 값인지도 모르고 칸 수도 모를 때
        list명 = []

    list명 = list(range(start,end,step))

 list 길이
    len(list명)
 list 사용
    data_list = [1,2,3]
    - 값 넣기
    (추가)
        data_list.append(값) >> 뒤에 추가됨
        data_list.append(4) >> [1,2,3,4]
    (삽입)
        data_list.insert(인덱스 번호,값)
        data_list.insert(0,5.5) >> [5.5,1,2,3,4,5]
    (삭제)
       data_list.remove(값)
       del(data_list[인덱스 번호])
       del data_list[인덱스 번호]

       data_list.clear() >> 모두 삭제
    - 값 검색
        list = [1,2,3,3,4,5]
        list.index(3)
        print(list.index(3)) >> 2
        값이 들어 있는 저장공간의 인덱스 번호
        중복 시 먼저 나온 값의 인덱스 번호
    - 값 수정
        list[2] = 새로운 값

# subway = ["리신","이즈리얼",505,506]
# print(subway.index("이즈리얼"))
# subway[3] = "안녕"



함수 - 이름 뒤에 소괄호, 작성된 코드의 주소값을 담고 있는 저장공간
    f   (x)     =   2x+1
    함수명(매개변수) = 값(return)

함수 선언
    def 함수명(매개변수,....)
        실행할 문장
        return 리턴값

함수 사용
    함수명(값1, ...)

함수를 사용하는 목적
    1. 재사용
    * 특정성을 부여해서는 안된다 절대

    2. 간결화

함수 선언 순서
    문제) 두 정수의 덧셈을 해주는 함수 구현
    1. 함수 명을 생각한다.
        add() :
    2. 매개변수를 생각한다.
        def add(x,y):
    3. 실행할 문장을 생각한다.
    4. 리턴 값을 생각한다.
    def add(x,y) :
          sum = x + y
          return sum
    sol1 = add(1,5)
    print(sol1)

    def add(x,y):
        sum = x+y
        return sum


    sol2 = add(2,4)

    print(sol2)

매개변수 선언 방법

1.packing(args)
    여러 개의 값을 마구잡이로 받을 때 사용.
2.kwags
    여러 개의 값을 key=value(딕셔너리) 형식으로 받는다.
3.unpacking
    매개 변수에 *로 시작하면 kwargs 형식과 동일하게 받아야 하고,
    그냥 매개변수가 나열 되어 있으면 , 값만 전달해도 된다.

packing(args) 함수 사용 방법
    1. 여러 개의 값을 콤마로 구분하여 전달
    2. 여러 개의 값을 묶은 뒤 앞에 *을 작성하여 전달

kwargs 함수 사용방법
    1. 여러개의 값을 콤마로 구분하여 , key:value 형태로 전달
    2. dict에 정보를 담은 뒤 **을 앞에 붙여서 전달



클로저(closure, 폐쇄) : 함수 안에 함수 , 모듈화
    함수가 정의된 시점의 변수를 기억하고, 이 변수를 나중에 참조 혹은 변경이 가능하도록 해준다.
    내부 영역에 선언된 변수는 외부에서 접근이 불가능하기 때문에 데이터 은닉을 할 수 있으며,
    함수가 종료된 이후에도 지역변수에 접근 할 수 있기 때문에 데이터 지속성을 가지고 있다.
    또한 다른 함수를 인자로 받거나 리턴할 수 있는 함수형 프로그래밍이 가능해진다.
    하지만 코드 복잡성이 증가하고 지역변수를 메모리에 유지하기 때문에 메모리 사용량이 증가 될 수 있다.


클로저 구현 코드
  def out(arg) :
    local_variable = value

    def in(arg) :
        #read local_variable
        value = oprate something

        return value

    return in


데코레이터(장식)
    좋은 개발 환경에서는 개발자가 메인 로직(비즈니스 로직)에만 집중 할 수 있게 한다.
    보안이나 로그, 트랜잭션, 예외처리 같이 비즈니스 로직은 아니지만,
    반드시 처리가 필요한 부분을 주변 로직이라고 한다.
    주변 로직을 다른 함수에 분리 시킨 뒤 메인 로직이 실행 될 때 함께 실행 되도록 할 수 있다.

데코레이터 동작 코드

1.
    def 데코레이터 이름(원래 함수) :
        def 주변 로직 함수(원래 함수의 매개 변수) :
            완성 코드 = 주변 로직
            원래 함수(완성 코드)

        return 주변 로직 함수


2.
    def 데코레이터 이름(원래 함수) :
        def 주변 로직 함수(원래 함수의 매개 변수) :
            주변 로직
            원래 함수(원래 함수의 매개 변수)

        return 주변 로직 함수



클래스 - 반
    공통 요소를 딱 한번만 선언하자!

    1. 타입이다.
        클래스 안에 선언된 변수와 메소드를 사용하고 싶다면
        해당 클래스 타입으로 변수를 선언해야 한다.

    2. 주어이다.
         원숭이가 바나나를 먹는다.
         Monkey.eat("바나나")

클래스 선언
    class 클래스명:
        필드(변수,메소드)

클래스의 필드 사용
    1. 객체화(instance)
        객체(instance variable)를 만드는 작업,
        추상적인 개념을 구체화 시키는 작업.

    2.생성자
    클래스 이름 뒤에 소괄호가 있는 형태, 메소드와 기능이 똑같지만 메소드라고 부르지않는다.
    생성자는 할당한 필드의 주소를 자동으로 리턴하기 때문에,
    선언 시, 리턴이라는 기능을 사용 할 수 없다.

기본 생성자
    매개변수가 없는 생성자를 뜻하며, 클래스 선언 시 자동으로 선언된다.
    사용자가 직접 생성자를 선언하게 되면 자동으로 선언되지 않는다.


self
    필드에 접근한 객체가 누구 인지 알아야 해당 필드에 접근 할 수 있다.
    이 때 접근한 객체가 가지고 있는 필드의 주소 값이 self 라는 변수에 자동을 담긴다.



클래스 - 반
    공통 요소를 한 번만 선언하자!

    1. 타입이다.
        클래스 안에 선언된 변수와 메소드를 사용하고 싶다면,
        해당 클래스 타입으로 변수를 선언해야 한다.

    2. 주어이다.
        원숭이가 바나나를 먹는다.
        Monkey.eat("바나나")

클래스 선언
    class 클래스명:
        필드(변수, 메소드)

클래스의 필드 사용
    1. 객체화(instance)
        객체(instance variable)를 만드는 작업.
        추상적인 개념을 구체화시키는 작업.
    2.

생성자
    클래스 이름 뒤에 소괄호가 있는 형태, 메소드와 기능이 똑같지만 메소드라고 부르지 않는다.
    생성자는 할당한 필드의 주소를 자동으로 리턴하기 때문에,
    선언 시, 리턴이라는 기능을 사용할 수 없다.

기본 생성자
    매개변수가 없는 생성자를 뜻하며, 클래스 선언 시 자동으로 선언된다.
    사용자가 직접 생성자를 선언하게 되면 자동으로 선언되지 않는다.

self
    필드에 접근한 객체가 누구인지 알아야 해당 필드에 접근할 수 있다.
    이 때 접근한 객체가 가지고 있는 필드의 주소값이 self라는 변수에 자동으로 담긴다.





# 상속
부모 클래스의 내용을 자식 클래스가 물려 받는다 (내 지식)
    1. 기존에 선언된 클래스의 필드를, 새롭게 만들 클래스의 필드로 사용하고자 할 때
    2. 여러 클래스를 선언하면서, 겹치는 필드가 있을 경우 부모 클래스를 선언한 뒤
       겹치는 필드를 구성하고 각 자식 클래스에 상속해준다.(추상화)
상속 문법
    class A:
        A필드

    class B(A): # 상속
        A,B필드

    A : 부모 클래스, 상위 클래스, 슈퍼 클래스, 기반 클래스
    B : 자식 클래스, 하위 클래스, 서브 클래스, 파생 클래스

super().__init__ : 부모 생성자
    자식 객체로 부모 필드에 접근 할 수 있다.
    하지만 자식 생성자만 호출 하기 때문에, 자식 필드만 메모리에 할당된다고 생각할 수 있다.
    사실, 자식 생성자에는 항상 부모 생성자를 호출하기 때문에, 자식 생성자 호출 시 부모와 자식 필드 모두 메모리에 할당된다.
    이 때 부모 생성자를 호출 하는 방법은 super().__init__()를 사용하는 것이다.
    만약, super().__init__()을 직접 작성하지 않더라도 컴파일러가 자동으로 작성해준다.

메소드 = 저장공간
오버라이딩(재정의, 무시하기)
    부모 필드에서 선언한 메소드를 자식 필드에서 수정하고자 할 때 재 정의를 해야 한다.
    이는 자식에서 부모 필드의 메소드와 동일한 이름으로 선언하는 문법을 의미한다.
    접근한 객체와 가까운 곳 부터 찾기 때문에, 자식 필드에 해당 메소드가 있다면, 재정의된 메소드가 실행된다.


[종합 실습]
은행
   예금주
   계좌번호(중복 없음)
   핸드폰번호(중복 없음)
   비밀번호
   통장잔고


은행은 3개를 선언한다.
모든 은행 고객을 관리하는 DB를 2차원 list로 선언한다.
모든 은행은 출금, 입금, 잔액조회, 계좌개설, 계좌번호 중복검사, 로그인, 핸드폰 번호 중복검사 서비스가 있다.
화면쪽 메뉴는 "계좌개설, 입금하기, 출금하기, 잔액조회, 계좌번호 찾기(새로운 계좌 설정, 핸드폰 번호로 서비스 이용가능),
나가기"로 구성되어 있다.



매직 메소드
    클래스 안에 정의할 수 있는 스페셜 메소드이다.

연산자     메소드                         설명
───────────────────────────────────────────────────────
 +      __add__(self, other)            덧셈
 *      __mul__(self, other)            곱셈
 -      __sub__(self, other)            뺄셈
 /      __truediv__(self, other)        나눗셈
 //     __floordiv__(self, other)       몫
 %       __mod__(self, other)           나머지
 **      __pow__(self, other[, modulo]) 제곱
 >>      __lshift__(self, other)        우쉬프트
 <<      __rshift__(self, other)        좌쉬프트
 &       __and__(self, other)           논리곱
 ^      __xor__(self, other)            배타논리합
 |      __or__(self, other)             논리합
+=      __iadd__(self, other)           누적 더하기
-=      __isub__(self, other)           누적 빼기
*=      __imul__(self, other)           누적 곱하기
/=      __idiv__(self, other)           누적 나누기
//=     __ifloordiv__(self, other)      누적 몫
%=      __imod__(self, other)           누적 나머지
**=     __ipow__(self, other)           누적 제곱
>>=     __irshift__(self, other)        누적 우쉬프트
<<=     __ilshift__(self, other)        누적 좌쉬프트
&=      __iand__(self, other)           누적 논리합
^=      __ixor__(self, other)           누적 배타논리합
|=      __ior__(self, other)            누적 논리합
 <      __lt__(self, other)             작다(미만)
 <=     __le__(self, other)             작거나 같다(이하)
 ==     __eq__(self, other)             같다
 !=     __ne__(self, other)             같지 않다
 >      __gt__(self, other)             크다(초과)
 >=     __ge__(self, other)             크거나 같다(이상)
 [i]    __getitem__(self, index)        인덱스 연산자
 in     __contains__(self, value)       멤버 확인
 len    __len__(self)                   요소 길이
 str    __str__(self)                   문자열 표현

        __init__                       생성자(초기화)
        __del__                        소멸자
        __new__                        할당자
        __repr__(self)              __str__을 정의하지 않을 경우, __repr__이 대신 쓰인다, 객체를 표현(객체의 주소)하는 목적 으로 사용


        API = (Application Programming Interface)
    선배 개발자들이 미리 작성해놓은 틀 (소스코드)

    1. 내부 API (기본 API)
        python 설치 시 다운로드 되었던 모듈.
        바로 사용 할 수 있는 API

    2. 외부 API
        해당 기업에서 배포한 코드를 다운로드 받은 뒤, 사용 할 수 있는 모듈
        기본으로 제공되지 않는 API.

    ※ 주의 사항
        모듈을 사용할 파일의 이름이 모듈과 같으면 절대 못 쓴다!!!!


예외 처리
    프로그램 실행 중 오류 발생 시 강제 종료되기 때문에 이를 막기 위하여 예외 처리를 작성한다.
    제어문으로 오류를 막을 수 없는 상황에서는 반드시 예외처리를 작성해야 한다.

try, except 문

    1.
        try:
            오류가 발생할 수 있는 문장

        except 발생오류 as 오류객체:
            오류 발생 시 실행할 문장

        ...
    2.
        try:
            오류가 발생할 수 있는 문장

        except 발생오류:
            오류 발생 시 실행할 문장

        ...

    3.
        try:
            오류가 발생할 수 있는 문장

        except:
            오류 발생 시 실행할 문장

        ...

        finally:
            오류 발생 여부와 상관없이 실행


예외 발생시키기
    심각한 문제가 발생하기 전에 일부러 프로그램을 강제 종료할 때 사용한다.
    예외를 한 곳에서 묶어서 처리하기 위해 사용한다(상위 과정에서 다룰 예정)

    raise 발생오류

예외 만들기
    class 오류명(Exception):
        def __str__(self):
            return "오류 메세지"




파일
    외부에 파일을 생성하거나 내용을 작성할 수 있으며, 기존의 내용도 읽어올 수 있다.

파일 생성하기
    파일을 열고 작성할 때 사용한다.
    'w'를 작성해서 운영체제에게 파일을 여는 목적을 알려줘야 하며, 이 때 'w'를 작성한다.
    open(path, 'w')

내용 추가하기
    기존의 내용을 없애지 않고, 아래에 내용을 추가한다. 이 때에는 추가 모드인 'a'를 작성한다.
    open(path, 'a')

파일 읽기
    기존 내용을 한 줄씩 읽어올 때 'r'를 작성하여 읽기 모드로 파일을 열어준다.
    open(path, 'r')


