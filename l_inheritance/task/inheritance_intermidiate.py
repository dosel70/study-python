# 은행은 3개를 선언한다.
# 모든 은행 고객을 관리하는 DB를 2차원 list로 선언한다.
# 모든 은행은 출금, 입금, 잔액조회, 계좌개설, 계좌번호 중복검사, 로그인, 핸드폰 번호 중복검사 서비스가 있다.
# 화면쪽 메뉴는 "계좌개설, 입금하기, 출금하기, 잔액조회, 계좌번호 찾기(새로운 계좌 설정, 핸드폰 번호로 서비스 이용가능), 나가기"로 구성되어 있다.
#신한은행 = 입금 시 수수료 50%

#국민은행 = 출금 시 수수료 50%

#카카오 = 잔액조회 시 재산 반토막


def check():
    pass


class Bank:
    total_count = 3
    banks = []
    bank_list = [[x ** total_count for x in row] for row in banks]


    def __init__(self,name,account,number,password):
        self.name = name
        self.account = account
        self.number = number
        self.password = password

    @classmethod
    def open_account(cls,name):
        if name not in cls.bank_list:
            cls.bank_list.append(name)
        else :
            print("Invalid")

    @staticmethod
    def money_in_account(money):
        Bank.bank_list.append(money)

    @staticmethod
    def check_account_number(account_number):

        if account_number not in Bank.bank_list:
            Bank.bank_list.append(account_number)
        else :
            print("Invalid")

    @staticmethod
    def check_phone(phone_number):

        if phone_number not in Bank.bank_list:
            Bank.bank_list.append(phone_number)
        else :
            print("Invalid")
    @classmethod
    def check_password(cls,password):
        if password not in Bank.bank_list:
            print("계좌 개설 완료!")
            cls.bank_list.append(password)
        else :
            print("Invalid")

    def deposit(self,input_money,account_number):
        if account_number in self.bank_list:
            Bank.money_in_account(input_money)
            print("입금 완료!")
        else :
            print("Insufficient money")


    def withdraw(self,withdraw_money,account_number): # 수수료 있는 출금 ( 국민은행)
        if account_number in self.bank_list:
            Bank.money_in_account(withdraw_money)
            print("출금 완료!")
        else :
            print("Insufficient money")

    def withdraw1(self,withdraw_money): # 수수료 없는 출금 ( 신한, 카카오 )
        self.withdraw_money = withdraw_money
        if withdraw_money > 0 :
            Bank.bank_list.append(withdraw_money)
            print("출금 완료 !")
        else :
            print("Insufficient money")


    def balance(self):
        print(Bank.bank_list)

    def __str__(self):
        pass


class ShinHan(Bank):
    def __init__(self,input_money,account_number):
        super().deposit()
        Bank.money_in_account(input_money-(1-(input_money*0.5)))
        print("입금 완료!")




class KookMin(Bank):
    def __init__(self, name, account, number, password):
        super().__init__(name, account, number, password)


class KaKao(Bank):
    def __init__(self, name, account, number, password):
        super().__init__(name, account, number, password)




if __name__ == '__main__':
    bank_menu = "1. 신한 은행\n" \
                "2. 국민 은행\n" \
                "3. 카카오 뱅크\n" \
                "4. 나가기\n"

    menu = "1. 개설\n" \
           "2. 입금\n" \
           "3. 출금\n" \
           "4. 잔액\n" \
           "5. 은행 선택 메뉴로 돌아가기\n"

    owner_message = "예금주: "
    account_number_message = "계좌번호: "
    phone_message = "핸드폰 번호: "
    password_message = "비밀번호(4자리): "
    money_message = "예치금: "
    deposit_message = "입금액: "
    withdraw_message = "출금액: "
    error_message = "다시 시도해주세요(중복된 값)"

    while True:
        # 은행 메뉴
        choice = int(input(bank_menu))
        if choice == 1 :

                # 서비스 메뉴(신한은행 서비스)
                s_choice = int(input(menu))
                while True :
                    if s_choice == 1: # 개설
                        name = input(owner_message)
                        account = input(account_number_message)
                        number = input(phone_message)
                        password = input(password_message)
                        money = (input(money_message))
                        if password == "" or name =="" or number == "" or account == "" or money == "":
                            break
                        if len(password) < 4 :
                            print(error_message)
                            break
                        create = Bank.open_account(name), Bank.check_account_number(account),Bank.check_phone(number),
                        Bank.check_password(password),Bank.money_in_account(money)

                    elif s_choice == 2: # 입금
                        selelct_account = (input("보내실 계좌를 입력 : "))
                        input_money = (input(deposit_message))
                        Bank.deposit("신한은행", selelct_account, input_money)
                        shinhan_bank = ShinHan(input_money=input_money, account_number=account_number)



                    elif s_choice == 3:
                        account_number = int(input(account_number_message))
                        withdraw_money = int(input(withdraw_message))

                        if withdraw_money == "" :
                            break

                        withdraw = Bank.withdraw("신한은행",account_number,withdraw_money)

                    elif s_choice == 4:
                        shinhan_bank.balance()

                    elif s_choice == 5:
                        break


        elif choice == 2:

                # 국민 은행 서비스
                kb_choice = int(input(menu))
                while True:
                    if kb_choice == 1: # 개설
                        name = input(owner_message)
                        account = input(account_number_message)
                        number = input(phone_message)
                        password = input(password_message)
                        money = int(input(money_message))
                        if password == "" or name == "" or number == "" or account == "":
                            break
                        if len(password) < 4:
                            print(error_message)
                            break
                        create = Bank.open_account(name), Bank.check_account_number(account), Bank.check_phone(number),
                        Bank.check_password(password), Bank.money_in_account(money)

                    elif kb_choice == 2:
                        selelct_account = (input("보내실 계좌를 입력 : "))
                        input_money = int(input(deposit_message))
                        if input_money == "":
                            break

                        Bank.deposit("국민은행", selelct_account, input_money)

                    elif kb_choice == 3:
                        account_number = int(input(account_number_message))
                        withdraw_money = int(input(withdraw_message))

                        if withdraw_money == "":
                            break

                        withdraw = Bank.withdraw("국민은행", account_number, withdraw_money)

                    elif kb_choice == 4:
                        Bank.balance()

                    elif kb_choice == 5:
                        break

        elif choice == 3:

                # 카카오 뱅크 서비스
                k_choice = int(input(menu))
                while True:
                    if k_choice == 1:
                        name = input(owner_message)
                        account = input(account_number_message)
                        number = input(phone_message)
                        password = input(password_message)
                        money = int(input(money_message))

                        if password == "" or name == "" or number == "" or account == "":
                            break
                        if len(password) < 4:
                            print(error_message)
                            break
                        create = Bank.open_account(name), Bank.check_account_number(account), Bank.check_phone(number),
                        Bank.check_password(password),Bank.money_in_account(money)

                    elif k_choice == 2:
                        selelct_account = (input("보내실 계좌를 입력 : "))
                        input_money = int(input(deposit_message))
                        if input_money == "":
                            break

                        Bank.deposit("카카오뱅크",selelct_account,input_money)

                    elif k_choice == 3:
                        account_number = int(input(account_number_message))
                        withdraw_money = int(input(withdraw_message))

                        if withdraw_money == "":
                            break

                        withdraw = Bank.withdraw("카카오뱅크", account_number, withdraw_money)

                    elif k_choice == 4:
                        Bank.balance()

                    elif k_choice == 5:
                        break
        elif choice == 4 :
            print("어플리케이션 종료")
            break