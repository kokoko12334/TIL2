
#dfs 풀이법 (시초)
from collections import defaultdict
from bisect import bisect_right
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        dic = defaultdict(list)
        for i in range(len(s)):
            dic[s[i]].append(i)
        
        n = len(t)
        stack = [(i,0) for i in dic[t[0]]]
        answer = 0
        while stack:
            idx, level = stack.pop()
            if level+1 == n:
                if s[idx] == t[level]:
                    answer += 1
                continue
            # print(f"idx:{idx}, level:{level},s:{t[level]}, next:{t[level+1]}, next_arr:{dic[s[level+1]]}")
            arr = dic[t[level+1]]
            arr_n = bisect_right(arr, idx)
    
            next_node = arr[arr_n:]
            # print(f"n: {arr_n} next:{next_node}")
            # print("##########")
            for node in next_node:
                stack.append((node,level+1))


        return answer