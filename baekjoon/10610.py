
n = int(input())

lst = [int(i) for i in list(str(n))]

if sum(lst)%3 != 0:
    answer = -1
else:
    lst.sort(reverse= True)
    if lst[-1] != 0:
        answer = -1
    else:
        answer = ""
        for i in lst:
            answer += str(i)
        answer = int(answer)
    
print(answer)