
w = input()

n = len(w)

al = set()
dic = {}
for i in w:
    if i not in al:
        al.add(i)
        dic[i] = 1
    else:
        dic[i] += 1

dic = dict(sorted(dic.items()))

dic1 = {}
dic2 = {}
for k in dic.keys():
    dic1[k] = dic[k]//2
    dic2[k] = dic[k]%2 


answer = ""
for k,v in dic1.items():
    if v:
        answer += k*v
right = answer[::-1]

check = 0
for k,v in dic2.items():
    if v:
        answer += k
        check += 1
answer += right
#홀수
if n%2:
    if check == 1:
        print(answer)
    else:
        print("I'm Sorry Hansoo")
else:
    if check:
        print("I'm Sorry Hansoo")
    else:
        print(answer)

