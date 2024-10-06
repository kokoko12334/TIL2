class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        

        s_p = 0
        t_p = 0

        t_n = len(t)
        s_n = len(s)
        
        while t_p < t_n and s_p < s_n:
            
            if s[s_p] == t[t_p]:
                s_p += 1
                t_p += 1
            else:
                t_p += 1


        answer = True
        
        if s_p < s_n:
            
            answer = False



        return answer