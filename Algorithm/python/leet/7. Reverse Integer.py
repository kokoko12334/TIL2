class Solution:
    def reverse(self, x: int) -> int:
        
        # x = n - 1 - i
        
        string = str(x)
        minus = False
        if string[0] == '-':
            minus = True
            string = string[1:]

        n = len(string)
        answer = 0
        for i in range(n):
            num = int(string[i]) * (10**i)
            # print(f"i:{i}, num:{num}")
            answer += num

        if minus:
            answer = -answer
        
        if -(2**(31)) <= answer <= (2**(31)) - 1:
            return answer
        return 0