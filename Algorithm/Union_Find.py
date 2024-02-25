def initialize(n):
    parent = [i for i in range(n)]
    rank = [0] * n
    return parent, rank

def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]

# def find(x,parent):
    
#     if x == parent[x]:
#         return parent[x]
#     parent[x] = find(parent[x],parent)
    
def union(x, y, parent, rank):
    xroot = find(x, parent)
    yroot = find(y, parent)

    if xroot == yroot:
        return

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1


#길이가 긴것이 부모모드가 된다
        
parent,rank = initialize(10)


union(0,1,parent,rank)
union(1,2,parent,rank)

find(2,parent)




def find(arent, a) -> int:
        if parent[a] == a:
            return a
        parent[a] = self.find(parent, parent[a])
        return parent[a]

def union(parent, rank, a: int, b: int) -> None:
    a = find(parent, a)
    b = find(parent, b)
    if a == b:
        return
    if rank[a] < rank[b]:
        a, b = b, a
    parent[b] = a
    rank[a] += rank[b]





