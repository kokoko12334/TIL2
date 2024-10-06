import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,s = [int(i) for i in input().split()]
arr = [int(i) for i in input().split()]

answer = 0
def back(idx, summ):
    
    global answer

    summ += arr[idx]
    if summ == s:
        answer += 1

    
    for i in range(idx+1, n):
        
        back(i, summ)


for i in range(n):
    back(i,0)

print(answer)


