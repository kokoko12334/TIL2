

class Solution:
    def calcEquation(self, equations, values, queries):

        n = len(equations)

        dic = {}
        sett = {}
        for i in range(n):
            x,y = equations[i]
            sett[x] = 0
            sett[y] = 0
            v = values[i]

            if x not in dic:
                dic[x] = {x:1}
            dic[x][y] = v

            if y not in dic:
                dic[y] = {y:1}
            dic[y][x] = 1/v

        answer = []

        for q in queries:
            
            x,y = q

            stack = [[x,1]]
            seen = {i:0 for i in sett.keys()}
            flag = True

            while stack:

                v,num = stack.pop()

                seen[v] = 1

                if v in dic:

                    for j in dic[v]:

                        num2 = num*dic[v][j]
                            
                        if j == y:
                            result = num2
                            stack = []
                            flag = False
                            break
                        
                        if seen[j] == 0:
                            stack.append([j,num2])
                
                else:

                    result = -1
                    break
            
            if flag:
                result = -1

            answer.append(result)
        
        print(answer)

        return answer



a = Solution()

a.calcEquation(equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]])


