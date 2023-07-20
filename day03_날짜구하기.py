'''
작성자: 최연웅
작성일: 23.07.20                파일명: day03_날짜구하기.py
목적: 100일 기념 + 기념일로부터 오늘이 며칠 지났는지 확인
'''
from datetime import datetime, timedelta

def getCurrent():                                       # now() 함수로 현재 날짜와 시간 구하기
    curDate = datetime.now()                
    return curDate

def getAfterDate(now, day):                             # ~ 일 후 기념일 구하기
    retDate = now + timedelta(days=day)
    return retDate

def func_3(now, day):                                   # 오늘이 기념일로부터 며칠 지났는지 구함
    aniDate = datetime(year=int(day[0]), month=int(day[1]), day=int(day[2]))
    retDate = now - aniDate
    return retDate

while True:
    print("[ 1. 며칠 후가 며칠인지 알고싶다. ]")
    print("[ 2. 기념일로부터 오늘이 며칠째인지 알고싶다. ]")
    choice = input("선택(1 or 2) 종료(q) ==> ")
    if (choice == "1"):
        inputDate = int(input("현재 시간으로부터 며칠 지났을 때를 알고싶은가요? "))

        nowDate = getCurrent()
        afterDate = getAfterDate(nowDate, inputDate)
        print(f"현재 날짜는 {nowDate}, {inputDate}일 지난 후는 {afterDate}입니다.\n")
        continue

    elif (choice == "2"):
        anniDate = list(input("오늘은 기념일로부터 며칠 지났나요?(YYYY MM DD) ").split(" "))
        howDate = func_3(nowDate, anniDate)
        print(f"현재 날짜는 {nowDate}, 기념일로부터 {howDate}일 지났습니다.\n")
        continue

    elif(choice == 'q' or choice=='ㅂ' or choice=='Q') : 
        print("== 프로그램 종료 ==")
        break