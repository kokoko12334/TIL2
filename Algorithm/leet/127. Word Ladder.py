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
                arr[i] = beginWord[i]
                if beginWord == "".join(arr):
                    dic[beginWord].append(wordList[j])

        for k in range(n):
            for i in range(s_n):
                for j in range(n):
                    if k == j:
                        continue
                    arr = list(wordList[j])
                    arr[i] = wordList[k][i]
                    if wordList[k] == "".join(arr):
                        dic[wordList[k]].append(wordList[j])

        q = deque()
        q.append((beginWord,1))
        seen = set()
        seen.add(beginWord)
        while q:
            s, answer = q.popleft()

            if s == endWord:
                break
            for s2 in dic[s]:
                if s2 not in seen:
                    seen.add(s2)
                    q.append((s2,answer+1)) 
        
        if endWord not in seen:
            return 0

        return answer