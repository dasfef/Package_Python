## 함수 정의 부분
def func1() :
    global a 
    a = 10
    print("func1()에서 a의 값 ", a)

def func2() :
    print("func2()에서 a의 값 ", a)

## 함수 변수 선언 부분
a = 20    # 전역변수

## 메인 코드 부분
func1()
func2()
