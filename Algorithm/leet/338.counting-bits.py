class Solution:
    def countBits(self, n: int):

        answer = []
        for i in range(n+1):
            cnt = bin(i).count("1")
            answer.append(cnt)
        
        return answer
