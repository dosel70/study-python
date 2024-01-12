def check(*, key: str, value: str) -> dict:
    # 키와 value 값을 스트링 계열로 변환해서 딕셔너리로 변환
    for bank in Bank.banks:
        # Bank 클래스 내에서 반복
        for user in bank:
            # bank 객체 내의 user를 반복하여
            if user[key] == value:
                # 유저의 [key] 값이 value와 같으면
                return user
                # user를 리턴한다.

    return None
# user가 bank 에 없을 때 None을 리턴한다.


class Bank:
    # Bank 클래스 : 은행 정보들을 담아 놓은 클래스이다. (개설,입금,출금,계좌열람,계좌변경)
    total_count = 3 # 은행의 개수
    # 반복할 횟수 = 3
    banks = [[] for i in range(total_count)]
    #각 3개의 은행들을 담을 리스트를 만들기 때문에, comprehension으로 [[][][]] 형태로만듬

    def __init__(self, owner: str, account_number: str, phone: str, password: str, money: int):
        # 생성자 ( 이름,계좌번호,폰번호,패스워드,예치금 )
        self.object = self
        # 각 회원의 object 필드에는 필드의 주소값이 담긴다.
        self.owner = owner
        self.account_number = account_number
        self.phone = phone
        self.password = password
        self.money = money

    # 어떤 은행에서 개설하는 지를 bank_choice로 전달 받는다.
    # 개설에 필요한 모든 회원정보는 **kwargs로 받는다.
    @classmethod
    def open_account(cls, bank_choice, **kwargs):
        user = [ShinHan, KookMin, KaKao][bank_choice - 1](**kwargs) # 생성자를 호출해야 하기 때문에 키워드 인자를 씀
        # 은행 db에 고객의 정보를 담을 때 딕셔너리 형태로 받는다.
        # check 함수에서 원하는 key로 회원의 정보를 찾기 위해서
        cls.banks[bank_choice - 1].append(user.__dict__)
        # 개설된 회원 정보를 리턴한다.
        return user

    # 클래스 메소드 (리스트 내의 은행의 인덱스 추출을 은행을 고르는 bank_choice을 활용하여 이동 할 수 있게끔 하였다.)
    # ex) 위에 보이는 변수 bank에는 리스트들이 들어가있는데 그 중에서 맨 앞에 있는 신한 은행에 접근하기 위해서는 인덱스 0번으로 가야한다.
    # 그러나 메뉴 화면에서 우리가 신한은행으로 이동하려면 bank_choice 1을 입력해야 하기 때문에, 1-1 = 0번 인덱스로 이동하기 때문에 !!
    # bank_choice - 1을 한 것이다.


    @classmethod
    def change_account_number(cls, new_account_number, **kwargs):
        # 여기에 실제 계좌번호 변경 로직을 구현
        # kwargs에는 필요한 다양한 인자가 들어갈 수 있음 (예: phone, password 등)

        # 예시로 인자가 유효한지 확인하는 부분 추가
        phone = kwargs.get('phone')
        password = kwargs.get('password')

        if phone is not None and password is not None:
            # 계좌번호를 변경하는 로직을 수행하고, 변경이 성공하면 결과를 리턴
            # 예시로 변경이 성공했다고 가정
            Bank.account_number = new_account_number
            return f"계좌번호 {new_account_number}로 성공적으로 변경되었습니다."

        else:
            # 필요한 입력값이 부족한 경우 None을 리턴하거나, 적절한 에러 메시지를 출력
            return None
    # def change_account_number(self, new_account_number, phone, password):
    #     # Validate inputs
    #     if phone is not None and password is not None:
    #         # Check if the provided phone and password match the user's actual credentials
    #         if self.authenticate(phone, password):
    #             # Change the account number
    #             self.account_number = new_account_number
    #             return f"계좌번호 {new_account_number}로 성공적으로 변경되었습니다."
    #         else:
    #             return "인증 실패: 올바른 핸드폰 번호와 비밀번호를 입력하세요."
    #     else:
    #         return "핸드폰 번호와 비밀번호를 입력하세요."

    # self에 접근하는 메소드가 아니기 때문에,
    # staticmethod 데코레이터를 붙혀서 사용
    @staticmethod
    def check_account_number(account_number: str) -> dict:
        # check 함수에서 검사할 key와 value를 전달한다.
        # 계좌번호 확인 메서드
        return check(key='account_number', value=account_number)
        # 중복성 or 존재 유무를 판단하는 기능을 가진 check 함수에서 계좌번호의 키 갑소가 value 값을 추출하여
        # 중복된다면, 계좌번호를 바꿀 수 있게끔 한다.



    @staticmethod
    def check_phone(phone: str) -> dict:
        return check(key='phone', value=phone)
    # check_function -> 휴대폰 번호 중복성 검사

    def deposit(self, money: int):
        self.money += money
    # 입금 시에 money(돈이 추가됨)
    def withdraw(self, money: int):
        self.money -= money
    # 출금 시에 money가 감소됨(돈이 감소됨)
    def balance(self):
        return self.money
    # 잔액을 보여줌 return self.money

    # 객체를 출력해도 __str__() 가 실행되기 때문에,
    # 편하고 빠르게 회원 정보를 확인 할 수 있다.
    def __str__(self):
        return f'{self.owner}, {self.account_number}, {self.phone}, {self.password}, {self.money}'
    # 주소값을 받아옴 ( 사용자, 계좌번호,폰 번호,패스워드, 잔액 )


class ShinHan(Bank):
    # 신한은행 클래스 (Bank 클래스 상속)
    def deposit(self, money: int):
        money //= 2
        super().deposit(money)
    # 신한은행은 입금을 할 시에 수수료가 50% 이기에 Bank클래스의 deposit 인스턴스 메서드의 값을
    # 오버라이딩 하여, 나누었을때 몫이 2가 나오면 50이므로 저렇게 해주었다.

class KookMin(Bank):
    # 국민은행 클래스 (Bank 클래스 상속)
    def withdraw(self, money: int):
        money *= 1.5
        super().withdraw(int(money))
    # 출금 시, 50% 차감이기 때문에, 0.5 라 생각할 수 있지만,
    # 은행의 구조 상, 출금을 할 때 수수료를 포함한 금액이 같이 차감
    # 따라서, *= 1.5 한 만큼 금액이 차감된다고 보면 된다.
    # 예를들면, 40000 원을 출금하면, 총 60000 원이 출금되는 것이다.

class KaKao(Bank):
    # 카카오 뱅크 클래스 (Bank)상속
    def balance(self):
        self.money //= 2
        return super().balance()
    # 카카오뱅크는 불쌍하게도 잔액 조회만 해도 재산이 반토막난다...
    # 잔액조회 메서드인 balance 메서드를 호출하여 money에 // 2를 해버림으로써, 50%가 날라간다.


# 메인 스크립트 시작
# 이 파일이 실행하는 파일이다.
if __name__ == '__main__':
    # 은행 메뉴 옵션 정의
    bank_menu = "1. 신한 은행\n" \
                "2. 국민 은행\n" \
                "3. 카카오 뱅크\n" \
                "4. 나가기\n"

    # 거래 메뉴 옵션 정의
    menu = "1. 개설\n" \
           "2. 입금\n" \
           "3. 출금\n" \
           "4. 잔액\n" \
           "5. 계좌번호 변경\n"

    # 사용자 입력 메시지
    owner_message = "예금주: "
    account_number_message = "계좌번호: "
    phone_message = "핸드폰 번호: "
    password_message = "비밀번호(4자리): "
    money_message = "예치금: "
    deposit_message = "입금액: "
    withdraw_message = "출금액: "
    error_message = "다시 시도해주세요"

    # 은행 선택을 위한 메인 루프
    while True:
        # 은행 선택
        bank_choice = int(input(bank_menu))
        if bank_choice == 4:
            break
        # 여기서 약간 이상했던 점. open_account 메서드에서 은행의 인덱스들은 bank_choice -1 을 해줌으로써
        # 각각 0,1,2 자신들의 순번으로 들어가는데 이럴려면 bank_choice의 값은 적어도 (1~3)이다. but 4는 종료 한다고 명시를 해놨으니 무시
        # 고로 bank_choice 는 5가 넘어가는 순간부터는 종료 or 오류 메시지가 떠야 하므로
        # 메뉴의 번호 이외의 번호를 입력시 밑으로 내려가지 못하게 막아준다.
        elif bank_choice >= len(Bank.banks) or bank_choice < 1:
            print("다시 입력해주세요")
            continue
        # bank_choice가 5 이상이 되서부터는 탈출을 해야한다!!!


        # 거래를 위한 내부 루프
        while True:
            # 서비스 메뉴
            menu_choice = int(input(menu))
            if menu_choice == 6:
                break

            # 계좌 개설
            if menu_choice == 1:
                owner = input(owner_message)

                # 고유한 계좌번호 보장
                while True:
                    account_number = input(account_number_message)
                    # None 은 False 값이지만 가독성과 직관성을 높이기 위해 is 연산자로 검사한다.
                    if Bank.check_account_number(account_number) is None:
                        break #  Bank.check_account_number 내의 계좌 번호가 없으면 성공!
                            # 없으면 실패


                while True:
                    phone = input(phone_message)
                    if Bank.check_phone(phone) is None:
                        break # 휴대폰도 계좌번호와 동일

                while True:
                    password = input(password_message)
                    if len(password) == 4: # 패스워드 길이가 4가 되지 않으면 다시 입력해야함
                        break

                money = int(input(money_message))
                # 계좌가
                # 개설된다.
                # 어떤 은행에서 개설했는 지를 bank_choice에 담아서 전달한다 .
                user = Bank.open_account(bank_choice, owner=owner, account_number=account_number, phone=phone,
                                         password=password, money=money)
                # 재정의한 __str__()이 사용되고,
                print(user)

            # 입금
            # 개설한 은행에서만 입금 가능(신한 은행)
            elif menu_choice == 2:
                account_number = input(account_number_message)

                #
                user = Bank.check_account_number(account_number)
                if bank_choice != 1:
                    print("개설한 은행에서만 입금 서비스 사용 가능")
                    continue


                if user is not None:
                        # 회원정보가 있으면
                    if user['password'] == input(password_message):
                        deposit_money = int(input(deposit_message))
                        # 계좌 개설 시 담아놓은 self(객체)를 통해 메소드를 접근한다.
                        user['object'].deposit(deposit_money)

                else:
                    print(error_message)
                    # 회원정보가 없으면 오류메세지 출력

            # 출금
            elif menu_choice == 3:
                account_number = input(account_number_message)
                # 계좌번호 입력
                user = Bank.check_account_number(account_number)
                # 계좌 확인 메서드를 user에 선언
                if user is not None:
                    # user가 즉 계좌 정보가 있다면
                    if user['password'] == input(password_message):
                        # 패스워드가 일치하면
                        withdraw_money = int(input(withdraw_message))
                        # 출금 가능
                        if withdraw_money * (1.5 if isinstance(user['object'], KookMin) else 1) <= user['money']:
                            # 만약 국민은행클래스 값과 user의 object 값이 같다면(isinstance 내장함수 기능을 활용!!)
                            user['object'].withdraw(withdraw_money)
                            # 출금 실행
                        else:
                            print(error_message)
                            # 오류메세지 >> 패스워드 불일치
                else:
                    print(error_message)
                    # 유저 정보가 없다면

            # 잔액 조회 선택
            elif menu_choice == 4:
                # 계좌번호 입력
                account_number = input(account_number_message)
                # 해당 계좌 확인
                user = Bank.check_account_number(account_number)
                if user is not None:
                    # 비밀번호 확인
                    if user['password'] == input(password_message):
                        # 현재 잔액 출력
                        print(f'현재 잔액: {user["object"].balance()}')
                        continue
                else:
                    # 계좌가 존재하지 않거나 비밀번호가 일치하지 않을 때 오류 메시지 출력
                    print(error_message)

            # 계좌 번호 변경 선택
            elif menu_choice == 5:
                # 핸드폰 번호와 비밀번호 입력
                phone = input("핸드폰 번호 입력 : ")
                password = input("비밀번호 입력 : ")

                if phone is not None and password is not None:
                    # 새로운 계좌번호 입력
                    account_number = input("새 계좌번호를 입력하세요 : ")
                    # 계좌번호 변경 시도
                    user = Bank.change_account_number(Bank, account_number=account_number, phone=phone,
                                                      password=password)

                    if user is not None:
                        # 성공적으로 변경되었을 경우 메시지 출력
                        print("계좌번호가 성공적으로 변경되었습니다.")
                    else:
                        # 실패했을 경우 오류 메시지 출력
                        print("핸드폰 번호 또는 비밀번호가 잘못되었습니다.")
                else:
                    # 핸드폰 번호와 비밀번호를 모두 입력하지 않았을 때 오류 메시지 출력
                    print("핸드폰 번호와 비밀번호를 모두 입력해야 합니다.")



            else:
                # 잘못된 메뉴 선택 시 오류 메시지 출력
                print(error_message)

