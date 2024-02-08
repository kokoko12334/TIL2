class Solution:
    def letterCombinations(self, digits: str):
        phone = {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }
        
        answer = []
        if not digits:
            return answer
        rank = 0
        
        stack = [[i,rank] for i in phone[digits[rank]]]
        answer = []
        n = len(digits)
        while stack:
            string,rank = stack.pop()
        
            if rank == n-1:
                answer.append(string)
            else:
                for i in phone[digits[rank+1]]:
                    stack.append([string+i,rank+1])
        
        return answer