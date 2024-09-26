def solution(n, costs):
    
    rank = [0] * n
    parent = [i for i in range(n)]
    
    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x,y):
        xroot = find(x)
        yroot = find(y)
        
        if xroot == yroot:
            return
        
        if rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        elif rank[yroot] > rank[xroot]:
            parent[xroot] = yroot
        else:
            parent[xroot] = yroot
            rank[yroot] += 1
    
    cnt = 0
    costs.sort(key = lambda x: -x[2])
    answer = 0
    while cnt < n-1:
        a, b, c = costs.pop()
        aroot = find(a)
        broot = find(b)
        
        if aroot == broot:
            continue
            
        union(a,b)
        cnt += 1
        answer += c
        
    return answer