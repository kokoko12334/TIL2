from collections import defaultdict,deque
from typing import List
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        dic = defaultdict(list)
        n = len(wordList)
        s_n = len(beginWord)

        for i in range(s_n):
            for j in range(n):
                arr = list(wordList[j])
                arr[i] = "*"
                ns = "".join(arr)
                dic[ns].append(wordList[j])
        
        
        q = deque()
        q.append((beginWord,1))
        seen = set()
        seen.add(beginWord)
        while q:
            s, answer = q.popleft()

            if s == endWord:
                break
            
            for i in range(s_n):
                arr = list(s)
                arr[i] = "*"
                ns = "".join(arr)
                for j in dic[ns]:
                    if j not in seen:
                        seen.add(j)
                        q.append((j,answer+1))
        
        if endWord not in seen:
            return 0

        return answer