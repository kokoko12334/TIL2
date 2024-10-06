import sys


n = int(sys.stdin.readline())

arr = [int(i) for i in sys.stdin.readline().split()]

stack = []

answer = [0]*n
i = n-1
stack.append([arr[i], i])
i -= 1

while i>=0:
    if stack[-1][0] > arr[i]:
        stack.append([arr[i],i])
        i -= 1
    else:
        while stack and stack[-1][0] < arr[i]:
            info = stack.pop()
            answer[info[1]] = i+1
        stack.append([arr[i],i])
        i -= 1       


print(*answer)



