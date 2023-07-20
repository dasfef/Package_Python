'''
작성자: 최연웅
작성일: 23.07.20                파일명: day03_암호화.py
목적: 입력된 문자열 암호화 후 파일로 저장
'''
secureFile = None
inStr = ""; secure = "";

secureFile = open("C:/users/user/desktop/work/python/secure.txt", "w", encoding="UTF-8")

while True:
    inStr = input("암호화하고 싶은 문자열: ")
    if(inStr == ""):
        break

    for ch in inStr:
        num = ord(ch)
        num = (num + 100) + 14
        secure += chr(num)

secureFile.writelines(secure)
secureFile.close()
print("암호화 성공 후 secure.txt로 변환 완료!")