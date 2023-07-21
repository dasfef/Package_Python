'''
작성자: 최연웅
작성일: 23.07.20                파일명: day03_복호화.py
목적: 입력된 문자열 복호화 후 파일 저장
'''
secureFile = None
inStr = ""; result = "";

secureFile = open("C:/users/user/desktop/work/python/secure.txt", "r", encoding="UTF-8")
decryptFile = open("C:/users/user/desktop/work/python/decrypt.txt", "w", encoding="UTF-8")

while True:
    s = secureFile.readline()
    for char in s:
        ch = ord(char)
        ch = ch - 114
        result += chr(ch)
        print(result, end="")
    
    break

decryptFile.writelines(result)
print("복호화 및 파일로 저장 성공!")
secureFile.close()