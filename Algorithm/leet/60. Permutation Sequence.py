from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        arr = [i for i in range(1, n+1)]
        
        per = permutations(arr, n)
        cnt = 1
        for i in per:
            if cnt == k:
                answer = i
            cnt += 1
        
        return "".join([str(i) for i in answer])
    


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        arr = [str(i) for i in range(1, n+1)]
        seen = [0] * n
        answer = []
        cnt = 1
        def recur(idx, level, sub):
            # print(idx, level,sub)
            nonlocal cnt
            if level == n+1:
                answer.append("".join(sub[:]))
                if cnt == k:
                    return True
                cnt += 1
                return False

            for i in range(n):
                if not seen[i]:
                    sub.append(arr[i])
                    seen[i] = 1
                    result = recur(idx+1, level+1, sub)
                    if result:
                        return True
                    sub.pop()
                    seen[i] = 0
        
        recur(0,1,[])
        # print(answer)
        return answer[k-1]