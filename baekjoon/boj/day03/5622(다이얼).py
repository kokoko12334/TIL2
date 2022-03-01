phone = {
    3:['A','B','C'],
    4:['D','E','F'],
    5:['G','H','I'],
    6:['J','K','L'],
    7:['M','N','O'],
    8:['P','Q','R','S'],
    9:['T','U','V'],
    10:['W','X','Y','Z']    
}

cnt =0
for i in input():
    
    num = [k for k, v in phone.items() if i in v] 
    cnt += num[0]

print(cnt)
######정답
dial = {
    "ABC": 3,
    "DEF": 4,
    "GHI": 5,
    "JKL": 6,
    "MNO": 7,
    "PQRS": 8,
    "TUV": 9,
    "WXYZ": 10,
}

total = 0
for char in input():
    for key in dial:
        if char in key:
            total += dial[key]
print(total)



