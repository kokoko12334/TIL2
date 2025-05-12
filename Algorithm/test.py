

n = 10

arr = [i+1 for i in range(n)]

tree = [0] * 4 * n

def init(node, start, end):
    
    if start == end:
        tree[node] = arr[start]
        return
    
    mid = (start + end) // 2
    init(2 * node, start, mid)
    init(2 * node + 1, mid + 1, end)
    
    tree[node] = tree[2 * node] + tree[2 * node + 1]


def query(node, start, end, left, right):
    
    if right < start or end < left:
        return 0
    
    
    if left <= start and end <= right:
        return tree[node]
    
    mid = (start + end) // 2
    q1 = query(2 * node, start, mid, left, right)
    q2 = query(2 * node + 1, mid + 1, end, left, right)
    
    return q1 + q2

init(1, 0, n-1)
print(query(1, 0, n-1, 2, 4))


def update(node, start, end, idx, new_val):
    diff = new_val - arr[idx]
    arr[idx] = new_val
    rec_update(node, start, end, idx, diff)


def rec_update(node, start, end, idx, diff):
    
    if idx < start or idx > end:
        return
    
    tree[node] += diff
    
    if start != end:
        mid = (start + end) // 2
        rec_update(2 * node, start, mid, idx, diff)
        rec_update(2 * node + 1, mid + 1, end, idx, diff)


update(1, 0, n - 1, 2, 7)
print(arr)
print(query(1, 0, n-1, 2, 4))
     