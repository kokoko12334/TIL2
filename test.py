
구매 = 9
promotion_stock = 10
original_stock = 100
buy = 1
get = 4

추가수량여부 = 0
정가결제여부 = 0
증정 = 0
정가구매 = 0
# 행사상품 나누고 남은건 무조건 정가결제여부로
while 구매 > 0:
    
    if promotion_stock - (정가구매 + 증정) > buy:

        if 구매 >= buy:
            구매 -= buy
            정가구매 += buy

        else:
            구매 -= 구매
            정가구매 += 구매

        if promotion_stock - (정가구매 + 증정) >= get and 구매 >= get: #프로모션 재고가 남고 구매한만큼 증정한다.
            증정 += get
            구매 -= get

        elif promotion_stock - (정가구매 + 증정) < get and 구매 >= get: 
            증정 += promotion_stock - (정가구매 + 증정)
            구매 -= promotion_stock - (정가구매 + 증정)

        elif promotion_stock - (정가구매 + 증정) >= get and 구매 < get: #프로모션 재고가 남고 구매한것보다 더 받아갈수 있다.
            # if 구매 == 0:
            #     추가수량여부 = get - 구매
            # else:
            증정 += min(get, 구매)
            구매 -= min(get, 구매)
            if 구매 == 0:
                추가수량여부 = get - 구매      

        elif promotion_stock - (정가구매 + 증정) < get and 구매 < get:
            if 구매 == 0:
                추가수량여부 = promotion_stock - (정가구매 + 증정) - 구매
            else:
                증정 += min(promotion_stock - (정가구매 + 증정), 구매)
                구매 -= min(promotion_stock - (정가구매 + 증정), 구매)
    else:
        정가결제여부 += 구매
        구매 -= 구매

def 재고_차감(차감할_재고):
    global promotion_stock, original_stock

    if promotion_stock >= 차감할_재고:
        promotion_stock -= 차감할_재고
    else:
        promotion_stock -= promotion_stock
        차감할_재고 -= promotion_stock
        original_stock -= 차감할_재고

우선_차감될_재고 = 증정 + 정가구매
재고_차감(우선_차감될_재고)
print(f"구매:{구매}")
print(f"추가수량여부:{추가수량여부}, 정가결제여부:{정가결제여부}, 증정:{증정}, 정가구매:{정가구매}, 남은 프로모션 재고:{promotion_stock}, 기본재고:{original_stock}")
print(f"{추가수량여부},{정가결제여부},{증정},{정가구매},{promotion_stock}\n")


print(f"만약 정가결제 yes라면 정가 결제 만큼 다시 promotion_stock, original_stock 차감")
정가구매 += 정가결제여부
재고_차감(정가결제여부)
정가결제여부 -= 정가결제여부
print(f"구매:{구매}")
print(f"추가수량여부:{추가수량여부}, 정가결제여부:{정가결제여부}, 증정:{증정}, 정가구매:{정가구매}, 남은 프로모션 재고:{promotion_stock}, 기본재고:{original_stock}")
print(f"{추가수량여부},{정가결제여부},{증정},{정가구매},{promotion_stock}\n")


print(f"만약 추가수량 여부를 받는다면 증정에 +추가수량을 하고 stock 차감")
증정 += 추가수량여부
재고_차감(추가수량여부)
추가수량여부 -= 추가수량여부
print(f"구매:{구매}")
print(f"추가수량여부:{추가수량여부}, 정가결제여부:{정가결제여부}, 증정:{증정}, 정가구매:{정가구매}, 남은 프로모션 재고:{promotion_stock}, 기본재고:{original_stock}")
print(f"{추가수량여부},{정가결제여부},{증정},{정가구매},{promotion_stock}\n")

