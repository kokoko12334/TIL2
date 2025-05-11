

n = 20 
arr = [i+1 for i in range(n)]
print(arr)

tree = [0] * 4 * n
def init(node, start, end):
    
    if start == end:
        tree[node] = arr[start]
        return
    
    mid = (start + end) // 2
    
    init(2 * node, start, mid)
    init(2 * node + 1, mid + 1, end)
    
    tree[node] = tree[2 * node] + tree[2 * node + 1]
    

init(1, 0, n - 1)


def query(node, start, end, left, right):
    
    if start > right or end < left:
        return 0
    
    if start >= left and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    
    q1 = query(2 * node, start, mid, left, right)
    q2 = query(2 * node + 1, mid + 1, end, left, right)
    
    return q1 + q2


def update(node, start, end, idx, new_var):
    diff = new_var - arr[idx]
    arr[idx] = new_var
    recur_update(node, start, end, idx, diff)

def recur_update(node, start, end, idx, diff):
    
    if idx < start or idx > end:
        return
    
    tree[node] += diff
    
    if start != end:
        mid = (start + end) // 2
        recur_update(2 * node, start, mid, idx, diff)
        recur_update(2 * node + 1, mid + 1, end, idx, diff)



print(query(1, 0, n - 1, 3, 11))

print(sum(arr[3:12]))


update(1, 0, n - 1, 3, 10)
print(query(1, 0, n - 1, 3, 11))
print(sum(arr[3:12]))

