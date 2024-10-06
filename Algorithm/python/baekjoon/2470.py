import sys

N = int(input())
arr = [int(x) for x in sys.stdin.readline().split()]
arr.sort()

start = 0
end = N-1
cstart = start
cend = end

prior_mix = abs(arr[start] + arr[end])

while start < end:
    
    if prior_mix > abs(arr[start] + arr[end]):
        cstart = start
        cend = end
        prior_mix = abs(arr[start] + arr[end])
        if prior_mix == 0:
            break
        
    if arr[start] + arr[end] > 0:
        end -= 1
    else:
        start += 1
    
print(arr[cstart], arr[cend])