class Solution:
    def thousandSeparator(self, n: int) -> str:

        num_string = str(n)
        nn = len(num_string)

        몫 = nn//3

        answer = ["0"] * (nn+몫)

        for i in range(1, 몫+1):
            dot = (nn+몫) - (4*i)
            answer[dot] = "."

        answer_idx = 0
        num_string_idx = 0
        while answer_idx < (nn+몫):

            if answer[answer_idx] == ".":
                answer_idx += 1
                continue
            
            answer[answer_idx] = num_string[num_string_idx]
            answer_idx += 1
            num_string_idx += 1

        if answer[0] == ".":
            return "".join(answer[1:])
        
        return "".join(answer)
    

