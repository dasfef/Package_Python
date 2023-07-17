num1 = int(input("A수를 입력: "))
num2 = int(input("B수를 입력: "))

print("num1's type: ", type(num1))
print("num2's type: ", type(num2))

out1 = out2 = out3 = out4 = 0

out1 = num1 + num2
print(f"{num1} + {num2} = {out1}")

out2 = num1 - num2
print(f"{num1} - {num2} = {out2}")

out3 = num1 * num2
print(f"{num1} * {num2} = {out3}")

out4 = num1 / num2
print(f"{num1} / {num2} = {out4}")

# ====================================

userName = input("이름 입력: ")
userAge = int(input("나이 입력: "))
userTel = input("전화번호 입력: ")

print("내 이름은 %s이고, 나이는 %d세 입니다." %(userName, userAge))
print("내 전화번호는 %s입니다." %(userTel))
print("프로그램 종료\n")