class Solution:
    def minReorder(self, n: int, connections) -> int:

        g = {}
        #나가는거 - , 들어오는거 +
        for i in connections:
            f, t = [j+1 for j in i]
            if f not in g:
                g[f] = [-t]
            else:
                g[f].append(-t)
            
            if t not in g:
                g[t] = [f]
            else:
                g[t].append(f)

        stack = [1]
        answer = 0
        seen = [0]*(n+1)
        while stack:
            
            node = stack.pop()
            seen[node] = 1
            for i in g[node]:
                

                if seen[abs(i)] == 0:
                    if i < 0:
                        answer += 1
                        i = -i
                    stack.append(i)


        return answer