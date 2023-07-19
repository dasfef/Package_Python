import random
cnt = 0

while True:
    dice1 = random.randrange(1, 7)
    dice2 = random.randrange(1, 7)
    dice3 = random.randrange(1, 7)
    print(f"dice1: {dice1} / dice2: {dice2} / dice3: {dice3}")
    cnt += 1

    if(dice1 == dice2 == dice3):
        print("던진횟수: %d" %cnt)
        break