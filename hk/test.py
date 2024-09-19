from pykis import PyKis, KisOrder

# 실전투자용 PyKis 객체를 생성합니다.
real_kis = PyKis("./real_secret.json", keep_token=True)

# 모의 투자용
fake_kis = PyKis("./real_secret.json", "./fake_secret.json", keep_token=True)

# 종목 객체 생성 및 정보 조회
samsung = fake_kis.stock("005930")
samsung.quote()

# 잔고
account = real_kis.account()
account.balance()

account = fake_kis.account()
account.balance()

# 주문 종목객체로 주문
order: KisOrder = samsung.buy(qty=1) #시장가
order = samsung.buy(price=194700, qty=1)
order = samsung.sell() #시장가
order = samsung.sell(price=194700)


print(order.pending) # 미체결 주문인지 여부
print(order.pending_order.pending_qty) # 미체결 수량

order.cancel() # 주문 취소
# 미체결 주문 전체 취소
for order in account.pending_orders():
    order.cancel()



from pykis import KisRealtimePrice, KisSubscriptionEventArgs, KisWebsocketClient


def on_price(sender: KisWebsocketClient, e: KisSubscriptionEventArgs[KisRealtimePrice]):
    
    
    
    print(e.response)

ticket = samsung.on("price", on_price)


print(fake_kis.websocket.subscriptions) # 현재 구독중인 이벤트 목록
input("Press Enter to exit...")

ticket.unsubscribe()


