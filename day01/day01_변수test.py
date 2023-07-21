print("======================== 물품 목록 ========================")
print("| 캔커피 | 삼각김밥 | 바나나우유 | 도시락 | 콜라  | 새우깡 |")
print("======================== 구입 가격 ========================")
print("|  500   |   900    |   800      |  3500  |  700  |  1000  |")
print("======================== 판매 가격 ========================")
print("|  1800  |   1400   |   1800     |  4000  |  1500 |  2000  |")
print("===========================================================")

things = ["캔커피", "삼각김밥", "바나나우유", "도시락", "콜라", "새우깡"]
purchase = [500, 900, 800, 3500, 700, 1000]
sell = [1800, 1400, 1800, 4000, 1500, 2000]

price = 0

while True:
    choice = input("구입 or 판매(종료는 q): ")
    if(choice=="q" or choice=="ㅂ"):
        break
    elif(choice=="구입"):
        num = 0
        pList = input("구입목록: ")
        pNums = int(input("구입개수: "))
        for i in things:
            if(pList==i) :
                price -= purchase[num] * pNums
            num += 1

    elif(choice=="판매"):
        num = 0
        pList = input("판매목록: ")
        sNums = int(input("판매개수: "))
        for i in things:
            if(pList==i):
                price += sell[num] * sNums
            num += 1

print(f"총 매출액: {price}원")
print("== 프로그램 종료 ==")