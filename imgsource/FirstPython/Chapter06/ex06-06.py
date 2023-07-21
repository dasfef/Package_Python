hap = 0
num1, num2 = 0, 0

while True :
    num1 = int(input("숫자1 ==> "))
    if num1 == 0 : 
        break
    num2 = int(input("숫자2 ==> "))

    hap = num1 + num2
    print(num1, "+", num2, "=", hap)

print("0을 입력해서 계산을 종료합니다.")
