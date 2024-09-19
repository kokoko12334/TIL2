#https://github.com/Soju06/python-kis/wiki/Tutorial/d6aaf207dc523b92b52e734908dd6b8084cd36ff
from pykis import PyKis
from pykis import KisRealtimePrice, KisSubscriptionEventArgs, KisWebsocketClient

# 모의 투자용
kis = PyKis("./real_secret.json", "./fake_secret.json", keep_token=True)

def on_price(sender: KisWebsocketClient, e: KisSubscriptionEventArgs[KisRealtimePrice]):
    
    print(e.response)
    price = e.response.price
    if price >= 679730:
        order = stock.sell()
        print(order)

account = kis.account()
account.balance()
amount = account.balance().deposits['KRW'].amount

stock = kis.stock("006740")

ticket = stock.on("price", on_price)


print(kis.websocket.subscriptions) # 현재 구독중인 이벤트 목록
input("Press Enter to exit...")

ticket.unsubscribe()



