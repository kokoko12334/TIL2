n = int(input())

starts = []
for _ in range(n):
    y, x = [float(i) for i in input().split()]
    starts.append([y, x])


g = [[0] * n for _ in range(n)]


def initialize(n):
    parent = [i for i in range(n)]
    rank = [0] * n
    return parent, rank
 
def find(x, parent):
    if x != parent[x]:
        parent[x] = find(parent[x], parent)
    return parent[x]
    
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











def search(idx):
    total = 0
    y, x = starts[idx][0], starts[idx][1]
    seen = {i for i in range(n)}
    seen.remove(idx)

    stack = [(y, x)]
    while stack:
        y, x = stack.pop()

        current = [float("inf"), -1]
        for i in seen:
            ny, nx = starts[i]

            dis = ((ny - y)**2 + (nx - x)**2)**(1/2)

            if current[0] > dis:
                current = [dis, i]
        
        next_idx = current[1]
        total += current[0]

        seen.remove(next_idx)
        stack.append((starts[next_idx][0], starts[next_idx][1]))
        if not seen:
            break

    return total

answer = float("inf")
for i in range(n):
    answer = min(answer, search(i))

print(format(answer, ".2f"))