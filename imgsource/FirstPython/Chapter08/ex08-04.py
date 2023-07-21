## 함수 정의 부분
def para2_func(v1, v2) :
    result = 0
    result = v1 + v2
    return result

def para3_func(v1, v2, v3) :
    result = 0
    result = v1 + v2 + v3
    return result

## 전역 변수 선언 부분
hap = 0

## 메인 코드 부분
hap = para2_func(10, 20)
print("매개변수 2개 함수 호출 결과 ==> ", hap)
hap = para3_func(10, 20, 30)
print("매개변수 3개 함수 호출 결과 ==> ", hap)
