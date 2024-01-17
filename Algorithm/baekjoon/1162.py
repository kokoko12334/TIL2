from heapq import heappush, heappop
import sys
import math
from collections import deque
input = sys.stdin.readline
n,m,k = [int(i) for i in input().split()]

lst = [[] for _ in range(n)]

for _ in range(m):
    a,b,c = [int(i) for i in input().split()]
    lst[a-1].append([b-1,c])
    lst[b-1].append([a-1,c])

test = [float("inf")]*n
test[0] = 0
for i in lst[0]:
    y,c = i
    test[y] = c
answer = [test[:] for _ in range(k+1)]

hq = []
heappush(hq, [answer[0][0],0,0])
seen = [[0]*n for _ in range(k+1)]
seen[0][0] = 1
while hq:
    c,y,cnt = heappop(hq)
    
    for i in lst[y]:
        ny,nc = i
        new_cost = c + nc
        answer[0][ny] = min(answer[0][ny], new_cost)
        if not seen[0][ny]:
            heappush(hq, [answer[0][ny],ny,0])
            seen[0][ny] = 1
            
        if cnt< k:
            new_cnt = cnt + 1
            new_cost = c
            answer[new_cnt][ny] = min(answer[new_cnt][ny], new_cost)
            if not seen[new_cnt][ny]:
                heappush(hq, [answer[new_cnt][ny],ny,new_cnt])
                seen[new_cnt][ny] = 1


print(min([answer[i][-1] for i in range(k+1)]))




N, M, K = map(int, sys.stdin.readline().split())
gph=[[] for _ in range(N+2)]
while M:
  M-=1
  a,b,c = map(int, sys.stdin.readline().split())
  gph[a].append((b,c))
  gph[b].append((a,c))

# node에서 N까지 K를 사용하는 다익스트라
def dijk(node):
  dist=[[math.inf for _ in range(K+2)] for __ in range(N+2)]
  edges=[]
  cnt=0
  dist[node][cnt]=0 #start:1 , end node: 1, cnt: 0
  # pq: cost, pos, cnt
  heappush(edges,(dist[node][0], 1, cnt))

  while edges:
    cost, pos, cnt = heappop(edges)
    if dist[pos][cnt]<cost:
      continue
    for p,c in gph[pos]:
      c+=cost
      if dist[p][cnt]>c:
        dist[p][cnt]=c
        heappush(edges, (c,p,cnt))
      if dist[p][cnt+1]>cost and cnt<K:
        dist[p][cnt+1]=cost
        heappush(edges,(cost,p,cnt+1))
  return dist

res = dijk(1)
print(min(res[N]))