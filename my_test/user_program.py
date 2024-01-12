from typing import List, Dict, Set, Tuple, Union, Final
number : Final[int] = 10
print(number)
class User:
    def __init__(self, user_id, user_pw):
        self.user_id = user_id  # 유저 아이디 정보
        self.user_pw = user_pw  # 유저 패스워드 정보
        if user_id.startswith("admin_"):
            self.admin = False



class AdminUser(User):  # 어드민 계정으로 접속 하면
    # 유저 아이디에 "admin_" 추가됨
    def __init__(self, user_id, user_pw):
        super().__init__("admin_" + user_id, user_pw)

        if user_id.startswith("admin_"):
            self.admin = True


class Membership:  # 회원 정보를 담은 클래스
    def __init__(self):
        self.users = {}  # 회원 정보 목록 (dict)

    def register_user(self, user_id, user_pw):
        if user_id not in self.users:
            encrypt_pw = ''.join([chr(ord(char) * 66) for char in user_pw])
            self.users[user_id] = User(user_id, encrypt_pw)
            print("회원 가입이 완료 되었습니다!")
            if user_id.startswith("admin_"):
                print("어드민 계정으로 들어오셨습니다!")
        else:
            print("중복된 아이디가 있습니다!")

    def delete_user(self, user_id, user_pw1):
        if user_id in self.users:
            if user_pw1 == user_pw:
                del self.users[user_id]
                print(f"{user_id}님의 회원 정보가 삭제 되었습니다.")
            else:
                print("비밀번호가 일치 하지 않습니다.")
        else:
            print(f"{user_id}님의 회원 정보가 존재 하지 않습니다.")

    def show_all_users(self):
        print("전체 회원 정보 : ")
        for user_id, user in self.users.items():
            print(f"아이디: {user.user_id}, 암호화된 비밀번호 : {user.user_pw}")

    def change(self, **kwargs):
        change_id = kwargs.get("change_id")
        new_id = kwargs.get("new_id")

        if change_id in self.users:
            user_pw2 = input(f"비밀번호를 입력하세요 ({change_id}님의 비밀번호): ")
            if user_pw2 == user_pw:
                self.users[new_id] = self.users.pop(change_id)
                print(f"{change_id}님의 회원 정보가 {new_id}로 변경되었습니다.")
            else:
                print("비밀번호가 일치하지 않습니다.")
        else:
            print(f"{change_id}님의 회원 정보가 존재하지 않습니다.")


# MembershipSystem의 인스턴스를 생성
membership_system = Membership()
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
    print("메뉴: \n1. 회원가입 \n2. 회원 탈퇴 \n3. 목록 조회 \n4. 회원 정보 업데이트 \n5. 프로그램 종료")
    choice = int(input("선택할 메뉴를 입력하세요: "))

    if choice == 1:
        user_id = input("아이디 입력 : ")
        user_pw = input("비밀번호 입력 : ")
        membership_system.register_user(user_id, user_pw)

    elif choice == 2:
        user_id = input("삭제할 아이디 입력 : ")
        user_pw = input("해당 비밀번호 입력 : ")
        membership_system.delete_user(user_id, user_pw)

    elif choice == 3:
        membership_system.show_all_users()

    elif choice == 4:
        change_id = input("수정할 회원 정보 : ")
        new_id = input("새로운 회원 이름을 입력하세용 : ")
        membership_system.change(change_id=change_id,new_id=new_id)


    elif choice == 5:
        print("프로그램 종료")
        break

    else :
        break
