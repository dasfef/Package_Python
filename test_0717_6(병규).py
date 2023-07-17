# 물품 리스트 , 개별 가격

buy_lst = {"캔 커피" : 500 , "삼각김밥" : 900,
            "바나나 우유" : 800 , "도시락" : 3500,
            "콜라" : 700, "새우깡" : 1000 }

sell_lst = {"캔 커피" : 1800 , "삼각김밥" : 1400,
            "바나나 우유" : 1800 , "도시락" : 4000,
            "콜라" : 1500, "새우깡" : 2000 }


buy_total = 0 # 총 구매금액
 
sell_total = 0 # 총 판매금액

while True :
    print("===============" * 5 )
    print(f' 1.구매 2.판매 3.조회 4.종료')
    x = int(input("선택 >>> "))

    if x == 1 :
        buy_this = input("구매 상품 : ")
        buy_this_cnt = int(input("구매 개수 : "))

        if buy_this in buy_lst :
            buy_pay = buy_lst[buy_this] * buy_this_cnt
            buy_total += buy_pay
            #print(buy_total)
    
    elif x == 2 :
        sell_this = input("판매 상품 : ")
        sell_this_cnt = int(input("판매 개수 : "))

        if sell_this in sell_lst :
            sell_pay = sell_lst[sell_this] * sell_this_cnt
            sell_total += sell_pay

    elif x == 3 :
        print("===============" * 5 )
        print(f'총 구매금액    || 총 판매금액     || 차액    ')
        print("===============" * 5 )
        print(f'{buy_total}              || {sell_total}               || {buy_total - sell_total}')
        
        

    elif x == 4 :
        print("===============" * 5 )
        print("종료합니다")
        break

    else :
        print("1,2,3,4번 중 선택하세요 ")
        continue

    
    
            
        

