#1
from datetime import datetime, timedelta

#2
## 함수 정의 부분
def getCurrent() :
    curDate = datetime.now()
    return curDate

#3
def getAfterDate(now, day) :
    retDate = now + timedelta(days=day)
    return retDate

#4
## 전역 변수 선언 부분
nowDate, afterDate = None, None

#5
## 메인 코드 부분
nowDate = getCurrent()
print("현재 날짜와 시간 ==>", nowDate)
afterDate = getAfterDate(nowDate, 100)
print("100일후 날짜와 시간  ==>", afterDate)
