
N, S =[int(i) for i in input().split()]

arr = [int(i) for i in input().split()]
prefix_sum = [0] * (N + 1)

for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i-1]
# print(prefix_sum)

l = 0
r = 0

answer = float("inf")
while l <= r:
    summ = prefix_sum[r + 1] - prefix_sum[l]    
    
    if summ < S:
        r += 1
    else:
        answer = min(answer, r - l + 1)
        l += 1
        
    if r >= N:
        break        
    
if answer == float("inf"):
    print(0)
else:
    print(answer)