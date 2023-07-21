#1
## 함수 정의 부분
def calc(v1, v2, op) :
    result = 0
    if op == '+' :
        result = v1 + v2
    elif op == '-' :
        result = v1 - v2
    elif op == '*' :
        result = v1 * v2
    elif op == '/' :
        result = v1 / v2

    return result

#2
## 전역 변수 선언 부분
res = 0
var1, var2, oper = 0, 0, ""

## 메인 코드 부분
oper = input("계산 입력 ( +, -, * , / ) : ")
var1 = int(input("첫번째 숫자 입력 : "))
var2 = int(input("두번째 숫자 입력 : "))

#3
res = calc(var1, var2, oper)

print("## 계산기 : ",var1, oper, var2, "=", res)
