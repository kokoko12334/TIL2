import sys
from collections import defaultdict
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
n = int(input())
m = int(input())

graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    from_, to_, cost = [int(i) for i in input().split()]
    graph[from_][to_] = cost

s, e = [int(i) for i in input().split()]



def dfs(node, cost):
    global answer

    if cost < answer:
        return

    if node == e:
        answer = max(answer, cost)
        result[cost].append(arr[:])
        return
    
    for i in range(1, n+1):
        next_cost = graph[node][i]
        if next_cost != 0 and not seen[i]:
            seen[i] = 1
            arr.append(i)
            dfs(i, cost + next_cost)
            seen[i] = 0
            arr.pop()

seen = [0] * (n + 1)
arr = [s]
seen[s] = 1
answer = 0
result = defaultdict(list)
dfs(1, 0)

sett = set()
for arr in result[answer]:
    for i in range(len(arr)-1):
        key = (arr[i], arr[i+1])
        sett.add(key)
print(answer)
print(len(sett))
print(result)



arr = [[0] * 10000 for _ in range(10000)]
