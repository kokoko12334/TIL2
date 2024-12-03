import sys
input = sys.stdin.readline

n, m = [int(i) for i in input().split()]

lessons = [int(i) for i in input().split()]

r = sum(lessons)
l = max(lessons)

# 2 2
# 1 11 에서 반례생깅 l = 1인경우

def check(mid):
    summ = 0
    cnt = 0
    for i in range(n):
        lesson = lessons[i]
        if summ + lesson > mid:
            cnt += 1
            summ = 0
        summ += lesson
    
    if summ:
        if summ <= mid:    
            cnt += 1
        else:
            return False
    if cnt > m:
        return False
    return True

answer = 0
while l <= r:
    mid = (l + r) // 2
    if check(mid):
        r = mid - 1
        answer = mid
    else:
        l = mid + 1
        
print(answer)
