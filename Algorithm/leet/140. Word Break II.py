from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        wordDict = set(wordDict)
        def recur(start, arr):

            if start == len(s):
                answer.append(" ".join(arr[:]))
                return
            
            for end in range(start, len(s)):
                word = s[start:end+1]
                if word in wordDict:
                    arr.append(word)
                    recur(end+1, arr)
                    arr.pop()
        
        answer = []
        recur(0,[])

        return answer
