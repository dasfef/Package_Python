'''
작성자: 최연웅
작성일: 23.07.21                파일명: day04_class.py
목적: 클래스 연습
'''

class Rabbit:
    shape = ""
    xPos = 0
    yPos = 0

    def goto(self, x, y):
        self.xPos = x
        self.yPos = y

    def __add__(self, other):
        print(f"객체 {self.shape}와 {other.shape}가 친구가 됨")

rabbit = None
userX = 0
userY = 0

rabbit = Rabbit()
rabbit.shape = "토끼"

rabbit1 = Rabbit()
rabbit1.shape = "엽기토끼"

rabbit2 = Rabbit()
rabbit2.shape = "도비"

rabbit1 + rabbit2

print("프로그램 종료")

# while True:
#     print("좌표 입력(종료:Q)")
#     userX = int(input("x좌표 입력: "))

#     if(userX == "Q" or userX == "q"): break

#     userY = int(input("y좌표 입력: "))
#     rabbit.goto(userX, userY)
#     print(f"토끼의 현재위치: {str(userX)}, {str(userY)}\n")