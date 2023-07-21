#1
ss = "Python"
print("원본 문자열 ==>",ss)

ss2 = ""

#2
ss2 += ss[0].lower()

#3
ss2 += ss[1].upper()
ss2 += ss[2].upper()
ss2 += ss[3].upper()
ss2 += ss[4].upper()
ss2 += ss[5].upper()

#4
print("변환 문자열 ==> ", end='')
print(ss2)
