while True:
    try:
        a,b = map(int, input().split())
        print(a+b)
    except:
        break


#문제가 테스트 케이스 개수가 정해지지않아서 다음과 같이 True로 한ㄷ.
#이때 오류가 발생하면 Except로 빠져나오게 한다.

