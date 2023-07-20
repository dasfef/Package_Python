from datetime import datetime, timedelta

nowDate, afterDate = None,None

#현재 날짜와 시간
def getCurrent():
    curDate=datetime.now()
    return curDate

#기념일로부터 며칠 지났는지 구하기
def getDay(day,now):
    return now-day

Day = input("날짜 입력 >> ")

nowDate=getCurrent()
print(f"현재 날짜와 시간 = {nowDate}")

Inday = datetime.strptime(Day, "%Y%m%d")
afterDay=getDay(Inday,nowDate)
print(f"    지난 일      = {afterDay}")
