## 함수 정의 부분
def func3() :
    result1 = 100
    result2 = 200
    return result1, result2

## 전역 변수 선언 부분
hap1, hap2 = 0, 0

## 메인 코드 부분
hap1, hap2 = func3()
print("func3()에서 돌려준 값 ==> ", hap1, hap2)
