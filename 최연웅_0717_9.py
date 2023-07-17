import time

presentTime = time.localtime()
print("[현재시각] %02d : %02d" %(presentTime.tm_hour, presentTime.tm_min))

age = int(input("나이를 입력하세요: "))
tTime = int(input("현재 시각 입력: "))

# if(presentTime.tm_hour >= 22 or presentTime.tm_hour < 8):
#     if(age <= 18 and age >=14):
#         print("PC방에 출입할 수 없습니다.")

if(tTime >= 25):
    tTime = tTime % 24
    if(tTime >= 22 or tTime < 8):
        if(age <= 18 and age >= 14):
            print("청소년은 해당 시간에 출입할 수 없습니다.")

    else:
        print("")
        print(f"{age}세로 입력되었습니다.")
        print("출입이 가능한 나이입니다.")
        print("※ 청소년은 22시 ~ 08시에는 출입이 불가합니다 ※")

else:
    if(tTime >= 22 or tTime < 8):
        if(age <= 18 and age >= 14):
            print("청소년은 해당 시간에 출입할 수 없습니다.")

    else:
        print("")
        print(f"{age}세로 입력되었습니다.")
        print("출입이 가능한 나이입니다.")
        print("※ 청소년은 22시 ~ 08시에는 출입이 불가합니다 ※")
