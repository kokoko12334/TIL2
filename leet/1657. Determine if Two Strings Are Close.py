class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        

        set1 = {}
        set2 = {}

        for i in word1:
            if i not in set1:
                set1[i] = 1
            else:
                set1[i] += 1

        for i in word2:
            if i not in set2:
                set2[i] = 1
            else:
                set2[i] += 1
        
        answer = True


        s1 = [i for i in set1.keys()]
        s1.sort()
        s2 = [i for i in set2.keys()]        
        s2.sort()

        if str(s1) != str(s2):
            answer = False
        else:
            s1 = [i for i in set1.values()]
            s1.sort()
            s2 = [i for i in set2.values()]        
            s2.sort()
            if str(s1) != str(s2):
                answer = False
            
        return answer
    

a = Solution()

a.closeStrings(word1 = "abc", word2 = "bca")
