store = {}
item = ""
cnt = 0

while True:
    item = input("제품 입력: ")
    if((item == "z") or (item == "Z")):
        break
    else:
        cnt = int(input("재고량 입력: "))
        store[item] = cnt

print("=== 재고량 출력 ===")
while True :
    item = input("찾을 제품 이름: ")
    if(item ==""):
        print("찾는 물품이 없음")
        break
    else:
        print(f"{item}은 {store[item]}개 남았습니다")