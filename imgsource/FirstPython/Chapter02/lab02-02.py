#1
print("## 택배를 보내기 위한 정보를 입력하세요. ##")

personName = input("받는 사람 : ")
personAddr = input("주소 : ")
weight = int(input("무게(g) : "))

#2
print("** 받는 사람 ==>", personName)
print("** 주소 =>", personAddr)

#3
print("** 배송비 ==>", weight*5, "원")
