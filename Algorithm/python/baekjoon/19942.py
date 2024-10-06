import sys

# 자기 앞번호만 탐색
# 조건1: 이미 탐색했던 경로 일 때
# 조건2: 최소비용보다 높을 때
# 조건3: 최소 영양조건을 모두 만족 했을 때

input = sys.stdin.readline

n = int(input())

condition = [int(i) for i in input().split()]

ingres = []
for _ in range(n):
    ingres.append([int(i) for i in input().split()])

def dfs(idx, arr, cost):
    global min_cost, answer

    # 조건1: 이미 탐색했던 경로 일 때
    key = "".join(map(str, result))
    if key in dp:
        return
    
    for i in range(4):
        arr[i] += ingres[idx][i]
    cost += ingres[idx][4]

    # 조건2: 최소비용보다 높을 때
    if min_cost <= cost:
        return
    
    # 조건3: 최소 영양조건을 모두 만족 했을 때
    flag = True
    for i in range(4):
        if condition[i] > arr[i]:
            flag = False
    if flag:
        dp.add(key)
        min_cost = cost
        answer = result[:]
        return
    
    # 중복방지를 위해 자기 앞번호만 탐색
    for i in range(idx+1, n):
        result.append(i)
        dfs(i, arr[:], cost)
        result.pop()

min_cost = float('inf')
dp = set()
answer = []

for i in range(n):
    result = []
    result.append(i)
    dfs(i, [0,0,0,0], 0)
    result.pop()

if answer:
    print(min_cost)
    print(*[i+1 for i in answer])
else:
    print(-1)