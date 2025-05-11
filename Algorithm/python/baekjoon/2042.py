import sys

input = sys.stdin.readline

N, M, K = [int(i) for i in input().split()]

arr = []
for _ in range(N):
    arr.append(int(input()))
    
tree = [0] * (4 * N)


def init(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return
    
    mid = (start + end) // 2
    init(2 * node, start, mid)
    init(2 * node + 1, mid + 1, end)
    
    tree[node] = tree[2 * node] + tree[2 * node +1]
    

init(1, 0, N-1)


# node: 현대 노드
# start ~ end: 현재 범위
# left ~ right: 구하고자 하는 범위
def query(node, start, end, left, right):
    
    # 구하고자 하는 범위를 넘는 경우 즉, 겹치는 부분이 벗음
    if end < left or right < start:
        return 0
    
    # 현재 범위가 구하고자 하는 범위에 포함되는 경우(완전 포함도 포함)
    if left <= start and end <= right:
        return tree[node]
    
    # 그 외에 양쪽으로 나뉘어 지는 경우, 나누어서 탐색 후 결과를 합침
    mid = (start + end) // 2
    
    q1 = query(2 * node, start, mid, left, right) # 왼쪽 자식
    q2 = query(2 * node + 1, mid + 1, end, left, right) #오른쪽 자식
    
    return q1 + q2

def update(node, start, end, idx, diff):
    
    if idx < start or idx > end:
        return
    
    tree[node] += diff
    
    if start != end:
        mid = (start + end) // 2
        update(2 * node, start, mid, idx, diff)
        update(2 * node + 1, mid + 1, end, idx, diff)
    
    

for _ in range(M + K):
    a, b, c = [int(i) for i in input().split()]
    b -= 1
    if a == 1:
        diff = c - arr[b]
        arr[b] = c
        update(1, 0, N-1, b, diff)
    else:
        c -= 1
        print(query(1, 0, N-1, b, c))
        
