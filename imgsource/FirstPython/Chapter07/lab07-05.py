#1
store = {}

#2
print("*** 물품과 재고량 입력 ***")
while True :
    item = input("입력 물품 ==>")
    if item == "z" :
        break

#3
    count = int(input("재고량 ==>"))
    store[item] = count

#4
print("*** 물품의 재고량 확인 ***")
while True :
    item = input("찾을 물품 ==>")
    if item== "" :
        break

#5
    if item in store :
        print(store[item], " 개 남았어요")
    else :
        print("그 물품은 없어요.")
