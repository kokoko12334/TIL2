from collections import deque
import sys
input = sys.stdin.readline
n,m = [int(i) for i in input().split()]


arr = []
for _ in range(m):
    arr.append([int(i) for i in input().split()])

#1111 => 남동북서 

graph = {}
for y in range(m):
    for x in range(n):
        graph[(y,x)] = set()

dx = [0,1,0,-1]
dy = [1,0,-1,0]

for y in range(m):
    for x in range(n):
        num = arr[y][x]
        num_str = format(num,"04b")
        
        for i in range(4):
            if num_str[i] == "1":
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    
                    graph[(y,x)].add((ny,nx))
                    
seen = set()
for y in range(m):
    for x in range(n):
        seen.add((y,x))

rooms = {}
room = 0
q = deque()
where_in_room = {}
while seen:
    
    size = 0
    y,x = iter(seen).__next__()
    q.append([y,x])
    seen.remove((y,x))
    
    while q:
        size += 1
        y,x = q.popleft()
        where_in_room[(y,x)] = room
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (ny,nx) in seen and not (ny,nx)in graph[(y,x)]:
                seen.remove((ny,nx))
                q.append([ny,nx])
    rooms[room] = size
    room += 1
    
no_wall = 0
for k,v in where_in_room.items():
    room1 = rooms[v]
    for k2 in graph[k]:
        room_num = where_in_room[k2]
        if room_num != v:
            room2 = rooms[room_num]
            result = room1 + room2
            if no_wall < result:
                no_wall = result

lst = rooms.values()

print(len(lst))
print(max(lst))
print(no_wall)