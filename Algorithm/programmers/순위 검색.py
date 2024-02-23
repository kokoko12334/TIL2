from bisect import bisect_left
from itertools import combinations
from collections import deque
def solution(info, query):
    table = {}

    
    for i in info:
        arr = i.split()
        for j in range(5):
        
            cases = list(combinations([0,1,2,3],j))
            for c in cases:
                key = ""
                for idx in range(4):
                    if idx in c:
                        key += "-"
                    else:
                        key += arr[idx]
            
        
                if key not in table:
                    table[key] = deque([[int(arr[-1])],1])
                else:
                    idxx = bisect_left(table[key][0],int(arr[-1]))
                    table[key][0].insert(idxx,int(arr[-1]))
                    table[key][1] += 1
                    
    # print(table)
    
    answer = []
    for q in query:
        string = ""
        arr = q.split("and")
        for i in range(3):
            string += arr[i].strip()
        
        last, score = arr[-1].split()
        string += last.strip()
        score = int(score.strip())
        # print(f"{string},{score}: {table[string]}")
        # print(string)
        if string in table:
            idx = bisect_left(table[string][0],score)
            result = table[string][1]-idx
            answer.append(result)
        else:
            answer.append(0)
    
    return answer