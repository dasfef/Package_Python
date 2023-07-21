#1
## 함수 정의 부분
def checkPassword(pwd) :
    if len(pwd) < 8 :
        return False

#2
    if pwd.isalnum() :
        return True
    else :
        return False

#3
## 전역 변수 선언 부분
password = ""

#4
## 메인 코드 부분
password = input("새로운 비밀번호를 입력하세요 :")

if checkPassword(password) :
    print("Good~ 비밀번호가 올바르게 생성되었어요")
else :
    print("오류! 비밀번호가 규칙에 맞지 않습니다")
