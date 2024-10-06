
n = int(input())

change = 1000 - n

coins = [500,100,50,10,5,1]
idx = 0
answer = 0
while change > 0:
    answer += change//coins[idx]
    change = change%coins[idx]
    idx += 1


print(answer)