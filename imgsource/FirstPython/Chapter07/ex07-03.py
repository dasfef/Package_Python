numList = []
for i in range(0, 4) :
    numList.append(0)
hap = 0

for i in range(0, 4) :
    numList[i] = int(input( "숫자 : " ))

hap = numList[0] + numList[1] + numList[2] + numList[3]

print("합계 ==> ", hap)
