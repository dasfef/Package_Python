score = []
nums = 0

for i in range(5):
    result = int(input("평가 점수: "))
    score.append(result)

for res in score:
    nums += res
print("심사위원 평균 점수: %1.2f" %(nums / 5))