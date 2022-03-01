n = int(input())

cnt = 0
for i in range(n):
      
    word = input()

    while  True:
        ch = word[0]   # word는 수시로 변해서 여기서 따로 할당함(비교대상을)

        word = word.lstrip(ch)

        if ch in word:
            break

        if len(word) == 0:
            cnt += 1    
            break

print(cnt)
