import random

count = 0
for cnt in range(11):
    com = random.randint(1, 5)
    user = int(input("숫자입력: "))
    count += 1
    if(com == user):
        print("정답입니다!")
        print("정답횟수: %d" %count)
        break
    else:
        print("틀렸습니다..")
        continue