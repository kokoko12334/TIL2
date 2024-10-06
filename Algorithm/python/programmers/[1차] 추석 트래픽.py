from collections import defaultdict

def trans(time):
    arr = time.split(":")
    num = 0
    trans_second = [3600000, 60000, 1000]
    for i in range(3):
        num += float(arr[i]) * trans_second[i]
    return num

def solution(lines):
    n = len(lines)
    dic = defaultdict(int)
    
    for i in range(n):
        _, time, comple = lines[i].split(" ")
        e = trans(time)
        s = e + 1 - (float(comple[:-1])*1000)
        s = int(s)
        e = int(e)
        for j in range(s, e+1):
            dic[j] += 1
        for j in range(e+1, e+1000):
            dic[j] += 1

    return max(dic.values())