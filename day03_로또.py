import random

num_list = []

while True:
    randNum = random.randint(1, 45)
    if (randNum not in num_list):
        num_list.append(randNum)
        cnt = len(num_list)
        if(cnt > 6): break
    else: continue
    
print("오늘의 로또 번호 ==> ")
print(sorted(num_list))