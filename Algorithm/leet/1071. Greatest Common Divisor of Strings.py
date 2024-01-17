class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        idx = 0
        answer = ""
        prefix = ""
        n = max(len(str1),len(str2))
        while idx < n:

            if idx < len(str1):
                s1 = str1[idx]
            else:
                s1 = ""

            if idx < len(str2):
                s2 = str2[idx]
            else:
                s2 = ""

            if s1 == s2:
                prefix += s1
                try_s1 = prefix*(len(str1)//len(prefix))
                try_s2 = prefix*(len(str2)//len(prefix))
                if try_s1 == str1 and try_s2 == str2:
                    answer = prefix

                idx += 1
            else:
                break
        
        return answer
        