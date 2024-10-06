t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    #h는 높이 w는 방 갯수
    rooms = []
    for j in range(1,h+1):
        
        start = int(str(j)+'00')
    
        rooms.append([start+i for i in range(1,w+1)])
    
    
    # for i in range(w):
    #     for j in range(h):
    #         print(rooms[j][i])
    
    result = [rooms[j][i] for i in range(w) for j in range(h)]
    
    print(result[n-1])




















