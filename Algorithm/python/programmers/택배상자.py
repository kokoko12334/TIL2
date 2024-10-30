from collections import deque
def solution(order):
    n = len(order)
    arr = deque([i for i in range(1,n+1)])
    arr2 = [-1]
    idx = 0
    while idx < n:
        target = order[idx]
        # print(arr, target, idx, arr2)
        if arr2[-1] == target:
            arr2.pop()
            idx += 1
            continue
        
        if target == arr[0]:
            arr.popleft()
            idx += 1
            continue
        elif target < arr[0]:
            break
        else:
            gap = target - arr[0]
            new = []
            for _ in range(gap):
                new.append(arr.popleft())
            arr.popleft()
            arr2 = arr2 + new
            idx += 1
    # print(idx)        
    answer = idx
    return answer