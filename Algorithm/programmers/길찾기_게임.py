from collections import deque, defaultdict
import sys
sys.setrecursionlimit(10**6)
def solution(nodeinfo):
    n = len(nodeinfo)
    nodeinfo = [nodeinfo[i] + [i+1] for i in range(n)]
    nodeinfo.sort(key=lambda x: (-x[1],x[0]))
    g = defaultdict(deque)
    pre_y = -1
    level = 0
    for i in range(n):
        x, y, num = nodeinfo[i]
        if y != pre_y:
            level += 1
            g[level].append((x,y,num))
        else:
            g[level].append((x,y,num))
        pre_y = y
    
    arr = [[None, None] for _ in range(n+1)]
    arr[0][0] = 1
    deapth = len(g.keys())
    def dfs(p, level, minn, maxx):
        if level > deapth:
            return
        px, py, pnum = p
        # print("############")
        # print(f"p:{p}, minn:{minn}, maxx:{maxx}")
        
        for i in range(len(g[level+1])): 
            x, y, num = g[level+1][i]
            if minn < x and x < px:
                arr[pnum][0] = num
                c = g[level+1].popleft()
                # print(f"왼족자식:{c}")
                dfs(c, level+1, minn, px)
                break
                
        for i in range(len(g[level+1])): 
            x, y, num = g[level+1][i]
            # print(px, x, maxx)
            if px < x and x < maxx:
                arr[pnum][1] = num
                c = g[level+1].popleft()
                # print(f"오른쪽자식:{c}")
                dfs(c, level+1, px, maxx)
                break
        
        return
    p = g[1][0]
    level = 1
    minn = -1
    maxx = float('inf')
    dfs(p, level, minn, maxx)
    # print(arr)
    # print(p)
    
    def pre_order(node):
        if node is None:
            return []
        left, right = arr[1:][node-1]
        return [node] + pre_order(left) + pre_order(right)
    def post_order(node):
        if node is None:
            return []
        left, right = arr[1:][node-1]
        return post_order(left) + post_order(right) + [node]
    answer = []
    # print(p[-1])
    answer.append(pre_order(p[-1]))
    answer.append(post_order(p[-1]))
    
    return answer