class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        

        lst1 = list(word1[::-1])
        lst2 = list(word2[::-1])

        answer = ""
        while lst1 or lst2:
            if lst1:
                string = lst1.pop()
                answer += string
            if lst2:
                string = lst2.pop()
                answer += string

        return answer
    


