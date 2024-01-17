from collections import deque
import sys
input = sys.stdin.readline
n,m = [int(i) for i in input().split()]

g_cnt = [0]*(n+1)
g = {i:[] for i in range(1,n+1)}
for _ in range(m):
    a,b = [int(i) for i in input().split()]
    g[a].append(b)
    g_cnt[b] += 1  #진입차수 증가

q = deque()
seen = [0]*(n+1)
for i in range(1,n+1):
    if not g_cnt[i]:
        seen[i] = 1
        q.append(i)

answer = []
while q:
    out = q.popleft()
    
    answer.append(out)
    for i in g[out]:   #방향그래프 확인
        if not seen[i]:  #방문 안했으면
            g_cnt[i] -= 1 #해당 진입차수 제거
            if not g_cnt[i]: #제거하고 진입차수가 0이면
                q.append(i)
                seen[i] = 1

print(*answer)

