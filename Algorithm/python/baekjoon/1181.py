
n = int(input())
lst = set()

for _ in range(n):
    word = input()
    if word not in lst:
        lst.add(word)

answer = sorted(lst, key = lambda x : (len(x), x))
for i in answer:
    print(i)
