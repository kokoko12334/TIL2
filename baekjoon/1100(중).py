
board = [list(input()) for _ in range(8)]  
#list하면 자동으로 하나하나씩 나누어짐
#만약 list(map(int, input().split()))으로 하면 'ffffff'이렇게 하나씩 묶임.
cnt = 0
for i in range(8):
    if i%2 == 0:
        check=board[i][::2]
        
    else:
        check =board[i][1::2]
    
    cnt += check.count('F')

print(cnt)

########간편함 식
board = [list(input()) for _ in range(8)]
cnt = 0
for i, row in enumerate(board):
    if i % 2 ==0:
        row = row[::2]        #짝수만 받는다.
    else:
        row = row[1::2]    #홀수만 받는다.
    cnt += row.count('F')
print(cnt)


