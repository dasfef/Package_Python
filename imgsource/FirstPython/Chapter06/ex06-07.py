i, hap = 0, 0

for i in range(1,101,1) :
    if i % 4 == 0 :
        continue

    hap += i

print("1~100의 합계(4의 배수 제외) : ", hap)
