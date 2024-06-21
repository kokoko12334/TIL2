from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        def init():
            return defaultdict(int)

        g = defaultdict(init)

        n = len(tickets)
        for i in range(n):
            f, t = tickets[i]
            g[f][t] += 1
        
        for k, v in g.items():
            g[k] = {f: t for f, t in sorted(v.items())}
        
        # print(g)

        arr = ['JFK']
        def dfs(node, cnt):
            # print("#########################")
            # print(g[node])
            flag = True
            for v in g[node].values():
                if v > 0:
                    flag = False
                    break

            if flag:
                if cnt == n + 1:
                    # print(f"결과:{arr}")
                    return 1
                return

            # print(node, cnt, arr)
            for next_node, avail in g[node].items():
                
                if avail:
                    arr.append(next_node)
                    g[node][next_node] -= 1
                    result = dfs(next_node, cnt + 1)
                    if not result:
                        arr.pop()
                        g[node][next_node] += 1
                    else:
                        return 1
                
        dfs('JFK', 1)
        return arr