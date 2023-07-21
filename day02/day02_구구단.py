# 2단 ~ 19단까지 출력

num = 2
for i in range(0, 5):
    print(f"{num}단", end="\t\t")
    num += 1
print()

for j in range(2, 20):
    cnt = j
    for k in range(1, 10):
        for x in range(0, 5):
            print(f"{j} * {k} = {j*k}", end="\t")
            j = j+cnt
        print()
