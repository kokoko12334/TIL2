N, M = [int(i) for i in input().split()]

t = [int(i) for i in input().split()]

know = set()
for i in range(1, t[0]+1):
    know.add(t[i])

parent = [i for i in range(N)]
rank = [0 for _ in range(N)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])    
    return parent[x]

def union(x, y):
    xroot = find(x)
    yroot = find(y)
    
    if (xroot == yroot):
        return
    if (xroot+1 in know):
        parent[yroot] = xroot
        rank[xroot] = max(rank[xroot], rank[yroot])
        return
    if (yroot+1 in know):
        parent[xroot] = yroot
        rank[yroot] = max(rank[xroot], rank[yroot])
        return
    
    if rank[xroot] > rank[yroot]:
        parent[yroot] = xroot 
    elif rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    else:
        parent[xroot] = yroot
        rank[yroot] += 1
    return

party_list = []
for _ in range(M):
    party = [int(i) for i in input().split()]

    for i in range(1, party[0]+1):
        for j in range(i+1, party[0]+1):
            union(party[i]-1, party[j]-1)
    
    party_list.append(party)

cnt = 0
for party in party_list:
    flag = False
    for j in range(1, party[0]+1):
        root = find(party[j]-1)
        if (root+1) in know:
            flag = True
            break

    if flag:
        cnt += 1
    
print(M - cnt)
            