'''
print("========== 택배 요금 계산 프로그램 ==========")
userName = input("이름 입력: ")
userAddr = input("주소 입력: ")
weight = int(input("무게 입력: "))
print("")
print("========== 계산 결과 ==========")

pay = weight * 5
print(f"받는 사람: {userName}")
print(f"주     소: {userAddr}")
print(f"요     금: {pay}원")
print("========== 프로그램 종료 ==========")
'''

age = int(input("나이 입력: "))

if((age <= 13) or (age >= 65)):
    print("30% 할인!")
