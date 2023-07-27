import random

lotto_num = range(1,46)

lotto_pic = random.sample(lotto_num,6)

lotto_pic.sort()

print(lotto_pic)