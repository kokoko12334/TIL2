word = input().upper()
al = [  ['A','B','C'],
        ['D','E','F'],
        ['G','H','I'],
        ['J','K','L'],
        ['M','N','O'],
        ['P','Q','R','S'],
        ['T','U','V'],
        ['W','X','Y','Z']
    ]
num = list(range(2,10))
phone = dict(zip(num,al))
phone
cnt=0
for i in word:
    r=[k for k,v in phone.items() if i in v][0]+1
    
    cnt += r
print(cnt)



######

word = list(input())

numbers = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
result = 0
for w in word:
    for n in range(len(numbers)):      
        if(numbers[n].find(w) != -1):
            result = result + n + 3

print(result)













