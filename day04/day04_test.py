import random as rd

rand_num=rd.randint(1,100)

counter=1

while True:
    try:
        my_num=int(input("숫자 입력 : "))

        if(rand_num == my_num):
            print("축하합니다. 맞췄습니다.")
            print(f"당신은 {counter}번째 만에 맞췄습니다.")
            break
        elif(rand_num < my_num):
            print("작음.")
        elif(rand_num > my_num):
            print("크다.")

        counter += 1
    except:
        print("숫자만 입력할 수 있습니다")

