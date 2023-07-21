#1
import random

#2
myHand = input("나의 가위/바위/보 ==>")

#3
comHand = random.choice(["가위", "바위", "보"])
print("컴퓨터의 가위/바위/보 ==>", comHand)

#4
if myHand == "가위" :
    if comHand == "가위" :
        print("비겼습니다. ㅡ.ㅡ")
    elif comHand == "바위" :
        print("졌습니다. ㅠㅠ")
    elif comHand == "보" :
        print("이겼습니다. ^^")
#5
elif myHand == "바위" :
    if comHand == "가위" :
        print("이겼습니다. ^^")
    elif comHand == "바위" :
        print("비겼습니다. ㅡ.ㅡ")
    elif comHand == "보" :
        print("졌습니다. ㅠㅠ")

elif myHand == "보" :
    if comHand == "가위" :
        print("졌습니다. ㅠㅠ")
    elif comHand == "바위" :
        print("이겼습니다. ^^")
    elif comHand == "보" :
        print("비겼습니다. ㅡ.ㅡ")

#6        
else :
    print("가위/바위/보 중 하나를 내세요.")
