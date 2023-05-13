import sys
input = sys.stdin.readline
t = int(input())


coins = [25,10,5,1]
for _ in range(t):
    answer = [0,0,0,0]
    change = int(input())

    for i in range(4):
        cnt = change//coins[i]
        answer[i] = cnt    
        change = change%coins[i]
    print(*answer)


