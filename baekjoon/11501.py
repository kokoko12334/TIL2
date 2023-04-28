

t = int(input())

for _ in range(t):
    d = int(input())
    stocks = [int(i) for i in input().split()][:: -1]


    s = stocks[0]
    buy = [0,0]
    answer = 0
    for i in range(1,d):
        if stocks[i] <= s:
            buy[0] += 1
            buy[1] += stocks[i]
            
            
        else:
            benefits = s* buy[0]
            answer += benefits - buy[1]
            s = stocks[i]
            buy = [0,0] 
    
    if buy[0]:
             
        benefits = s * buy[0]
        answer += benefits - buy[1]
    
    print(answer)

