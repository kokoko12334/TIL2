import sys
sys.setrecursionlimit(10**6)
n, m = [int(i) for i in sys.stdin.readline().split()]

graph = {}
for i in range(1,n+1):
    graph[i] = []


for _ in range(m):
    node1, node2 = [int(i) for i in sys.stdin.readline().split()]
    graph[node1].append(node2)
    graph[node2].append(node1)



#dfs

seen = set()
stack = []
first = list(graph.keys())[0]

stack.append(first)
seen.add(first)
answer = 0
def dfs():
    global answer
    if stack:
        out = stack.pop()
        
        for i in graph[out]:
            if i not in seen:
                stack.append(i)
                seen.add(i)
        dfs()
    else:
        
        answer += 1
        all_ = set(graph.keys())
        remain = list(all_ - seen)
        if remain:
            stack.append(remain[0])
            seen.add(remain[0])
            dfs()
        

dfs()

print(answer)













