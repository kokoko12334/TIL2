import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

dic = {i:[] for i in range(1,n+1)}

for _ in range(m):
    input_ = [int(i) for i in sys.stdin.readline().split()]
    dic[input_[0]].append(input_[1])
    dic[input_[1]].append(input_[0])

stack = []
seen = set()

stack.append(1)
seen.add(1)
answer = -1
while stack:
    a = stack.pop()
    
    answer += 1
    for i in dic[a]:
        if i not in seen:
            stack.append(i)
            seen.add(i) 
print(answer)

