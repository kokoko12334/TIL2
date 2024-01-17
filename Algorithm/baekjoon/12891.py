
#input
s,p = [int(i) for i in input().split()]
strings = input()
condition = [int(i) for i in input().split()]

#hashmap
hash_map = {"A":0,"C":0,"G":0,"T":0}
idx = 0
for k in hash_map.keys():
    hash_map[k] = condition[idx]
    idx += 1

#check 
answer = 0
def check(answer,hash_map):

    flag = True

    for v in hash_map.values():
        if v > 0:
            flag = False
            break
    if flag:
        answer += 1

    return answer

#sliding window init
l = 0
r = p-1
arr = strings[l:r+1]

for k in arr:
    hash_map[k] -= 1
answer = check(answer,hash_map)

l += 1
r += 1

#sliding window
while r < s:

    front = strings[l-1]
    rear = strings[r]

    hash_map[front] += 1
    hash_map[rear] -= 1
    
    answer = check(answer, hash_map)

    l += 1
    r += 1

print(answer)