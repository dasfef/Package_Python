#1
import random

#2
## 함수 정의 부분
def  lottoFunc() :
    lottoNum = random.randint (1, 45)
    return  lottoNum

#3
## 전역 변수 선언 부분
lottoList = [ ]
num = 0

#4
## 메인(main) 코드 부분
print("** 로또 추첨을 시작합니다. ** \n");

while True :
    num = lottoFunc()

#5    
    if num in lottoList  :
        continue
    else :
        lottoList.append(num)
        
#6
    if len(lottoList) == 6 :
        break 

#7
print("오늘의  로또 번호 ==>  ", end='')
lottoList.sort()
for i in range(0,6) :
    print(lottoList[i], " ", end = '')
