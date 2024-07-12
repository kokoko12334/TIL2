import sys
sys.setrecursionlimit(10**6)
def solution(a, edges):
    
    if sum(a) != 0:
        return -1
    n = len(a)
    tree = [[] for i in range(n)]
    for e in edges:
        node1, node2 = e
        tree[node1].append(node2)
        tree[node2].append(node1)
    
    def dfs(child,parent):
        nonlocal answer
        for c in tree[child]:
            if c != parent:
                dfs(c, child)
        a[parent] += a[child]
        answer += abs(a[child])
                
    answer = 0
    dfs(0,0)

    return answer