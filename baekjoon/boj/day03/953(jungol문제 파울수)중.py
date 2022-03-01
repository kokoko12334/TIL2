

players = input().split()

fouls = {}

for player in players:
    if player in fouls:
        fouls[player] +=1
    else:
        fouls[player] = 1   #처음에는 아무도 없으므로 foul은 빈공간임 따라서 이거는 초기공간


min_foul = min(fouls.values())

######################컴프리헨션
k=[k for k,v in fouls.items() if v == min_foul]
print(*k, min_foul, sep = '\n')

#########################for문
for player, foul in fouls.items():
    if foul ==min_foul:
        print(player)
print(min_foul)