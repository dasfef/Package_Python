import random

lotto_994 = [1,3,8,24,27,35]

cnt = 0
while True:
    lotto_pic = random.sample(range(1,46),6)
    lotto_pic.sort()
    
    if lotto_994 == lotto_pic:
        break
    
    cnt = cnt + 1

print(f"{cnt} 회만에 맞췄습니다")

buy_price = cnt * 1000
print(f"구매금액: {buy_price} 원")

gain_price = 1900000000 - buy_price
print(f"이익금: {gain_price} 원")