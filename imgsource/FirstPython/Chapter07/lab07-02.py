#1
print("홍길동 선수 경기 끝났습니다~~ 짝짝짝")

#2
score = []
for i in range(5) :
    jumsu = int(input("평가 점수 ==>"))
    score.append(jumsu)

#3
hap = 0
for i in range(5) :
    hap += score[i]

#4
avg = hap / 5
print("심사위원 평균 점수 :", avg)
