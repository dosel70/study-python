#
#                               # 캐릭터 1:1 PVP
#
#           이즈리얼                                         다리우스
# #    q (원거리 공격 데미지 + 5)                       q (근거리 공격 데미지 + 7)
# #    w (보조 공격 데미지+3)                           w (보조 공격 데미지 + 1)
# #    e (이동속도 증가 + 5)                            e ( 이동속도 증가 + 3)
# #    r (궁극기 공격 데미지 + 10)                       r ( 궁극기 공격 데미지 + 8)
# #    hp = 30                                       hp = 40
# #    기본 이동속도 = 20                              기본 이동속도 = 10
#
#
#
# #이렇게 이즈리얼, 다리우스 라는 캐릭터의 정보가 있다.
# #(q,w,e,r은 스킬을 사용할 수 있는 단축키) 이고, hp, 기본 이동속도 등은 캐릭터 속성 값이다.
# #이를 토대로 오늘 배운 내용들을 활용하여 이즈리얼, 다리우스 라는 캐릭터가 서로 q,w,e,r이라는 스킬들을 랜덤으로 사용하여 싸우게 해서
# 먼저 hp가 0이 되는 캐릭터가 지는 게임을 만들어 보았다.

#-----------------------------------------------------------------------------------------------------------------------
import random

class Champion: # 캐릭터 명,hp,이동속도 속성을 정의
    def __init__(self,name,hp,move_speed):
        self.name = name
        self.hp = hp
        self.move_speed = move_speed

    def attack(self, skill_damage): # 공격 메서드
        return skill_damage

    def take_damage(self,damage): # 피해량 메서드
        self.hp -= damage
        self.move_speed -= damage


    def is_alive(self): # hp(+ 이동속도) 기능 정의
        return self.hp + self.move_speed > 0

    def use_skill(self, skill_name): # 게임 실행시 스킬을 썼을때 나타나는 출력
        return f"{self.name} {skill_name}"


class Ezreal(Champion): # 이즈리얼
    def __init__(self):
        super().__init__("Ezreal",33,20)

    def q_skill(self):
        return self.attack(5)

    def w_skill(self):
        return self.attack(3)

    def e_skill(self):
        self.move_speed += 5
        return self.attack(0)

    def r_skill(self):
        return self.attack(10)

class Darius(Champion):
    def __init__(self):
        super().__init__("Darius",40,10)

    def q_skill(self):
        return self.attack(7)

    def w_skill(self):
        return self.attack(1)

    def e_skill(self):
        self.move_speed += 3
        return self.attack(0)

    def r_skill(self):
        return self.attack(8)

def simulate_battle(champion1, champion2):
    while champion1.is_alive() and champion2.is_alive():
        skill1 = random.choice(["q_skill","w_skill","e_skill","r_skill"])
        skill2 = random.choice(["q_skill","w_skill","e_skill","r_skill"])

        damage1 = getattr(champion1, skill1)() # getattr (동적으로 객체에 속성을 부여해주는 내장함수)
        # 예를 들어 damage1 이라는 변수에 (champion1의 객체에 위에 랜덤으로 값을 할당받은 skill1을 적용시켜주며, 랜덤으로 값을 할당 받았
        # 기에 정확한 반환값을 받을 수 없기에 뒤에 소괄호를 넣었다.
        damage2 = getattr(champion2, skill2)()

        champion2.take_damage(damage1)
        champion1.take_damage(damage2)

        print(f"{champion1.name} HP: {champion1.hp}, {champion2.name} HP: {champion2.hp}")

    if champion1.is_alive():
        print(f"{champion1.name} WIN")
    else:
        print(f"{champion2.name} WIN")


ezreal = Ezreal()
darius = Darius()

simulate_battle(ezreal, darius)