from collections import defaultdict, deque

n, m = [int(i) for i in input().split()]
nums = [0 for _ in range(n + 1)]
maps = defaultdict(list)
for _ in range(m):
    arr = [int(i) for i in input().split()]
    pre = 0
    post = 0
    for i in range(1, len(arr) - 1):
        pre = arr[i]
        post = arr[i+1]
        if post not in maps[pre]:
            nums[post] += 1
            maps[pre].append(post)

q = deque()
visited = [0] * (n + 1)
for i in range(1, n+1):
    if not nums[i]:
        q.append(i)
        visited[i] = 1

answer = []
while q:
    num = q.popleft()
    answer.append(num)

    for next_num in maps[num]:

        if visited[next_num]:
            continue
        nums[next_num] -= 1
        if nums[next_num] == 0:
            q.append(next_num)
            visited[next_num] = 1

if len(answer) != n:
    print(0)
else:
    for num in answer:
        print(num)