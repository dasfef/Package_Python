#1
import random

toss = []

#2
for i in range(10000) :
    comA = random.choice(["가위", "바위", "보"])
    comB = random.choice(["가위", "바위", "보"])

#3
    if comA == "가위" :
        if comB == "가위" :
            toss.append("없음")
        elif comB == "바위" :
            toss.append("B")
        elif comB == "보" :
            toss.append("A")
    elif comA == "바위" :
        if comB == "가위" :
            toss.append("A")
        elif comB == "바위" :
            toss.append("없음")
        elif comB == "보" :
            toss.append("B")
    elif comA == "보" :
        if comB == "가위" :
            toss.append("B")
        elif comB == "바위" :
            toss.append("A")
        elif comB == "보" :
            toss.append("없음")

#4
aWin = toss.count("A")
bWin = toss.count("B")
noWin = toss.count("없음")

print("10000번 중 컴퓨터A의 승리 : ", aWin)
print("10000번 중 컴퓨터B의 승리 : ", bWin)
print("10000번 중 비긴 경기 : ", noWin)

            
