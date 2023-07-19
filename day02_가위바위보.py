import random

process = [0, 1, 2]
comA = []
comB = []

winRateA = 0
winRateB = 0
draw = 0
num = 0

for num in range(10000):
    comA.append(random.randint(0, 2))
    comB.append(random.randint(0, 2))

for i in range(10000):
    if (comA == 0 and comB == 2):
        winRateA += 1
    elif(comA == 1 and comB == 0):
        winRateA += 1
    elif(comA == 2 and comB == 1):
        winRateA += 1
    elif(comB == 0 and comA == 2):
        winRateB += 1
    elif(comB == 1 and comA == 0):
        winRateB += 1
    elif(comB == 2 and comA == 1):
        winRateB += 1
    else:
        draw += 1


print("컴퓨터 A의 승리: %d" %winRateA)
print("컴퓨터 B의 승리: %d" %winRateB)
print("비김: %d" %draw)