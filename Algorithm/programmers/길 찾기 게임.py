# 전위: root-l-r
#후위: l-r-root
from collections import defaultdict
from bisect import bisect_left
def solution(nodeinfo):
    answer = [[],[]]
    def default_value():
        return [-1, -1]
    def pre(node):
        answer[0].append(node)
        
        for child_node in g[node]:
            if child_node == -1:
                continue
            pre(child_node)
            
    def post(node):
        
        for child_node in g[node]:
            if child_node == -1:
                continue
            post(child_node)
            
        answer[1].append(node)
    
    def check(y_idx,x,l,r):
        node = idx[(x, keys[y_idx])]
        
        
        if y_idx + 1 == n_keys:
            return
        child_node = y_x[keys[y_idx + 1]]
        
        # 왼쪽 찾기
        c = bisect_left(child_node, x)
        l_idx = bisect_left(child_node, l)
        
        if child_node[l_idx:c]:
            l_x = child_node[l_idx:c][0]
            g[node][0] = idx[(l_x, keys[y_idx + 1])]
            # print(y_idx)
            # print(f"왼쪽 범위:{l_idx, c}, 자식노드 후보:{child_node}")
            # print(f"{node}의 왼쪽자식:{g[node]}")
            check(y_idx + 1, l_x, l, x)

        
        # 오른쪽찾기
        r_idx = bisect_left(child_node, r)
        if child_node[c:r_idx]:
            r_x = child_node[c:r_idx][0]
        else:
            return

        g[node][1] = idx[(r_x, keys[y_idx + 1])]
        # print(y_idx)
        # print(f"오른쪽 범위:{c, r_idx}, 자식노드 후보:{child_node}")
        # print(f"{node}의 오른쪽 자식:{g[node]}")
        check(y_idx + 1, r_x, x, r)
    
    
    g = defaultdict(default_value)
    idx = defaultdict(int)
    n = len(nodeinfo)

    for i in range(n):
        x,y = nodeinfo[i]
        idx[(x,y)] = i + 1
    nodeinfo.sort(key = lambda x: (-x[1],x[0]))
    
    y_x = defaultdict(list)
    for i in range(n):
        x,y = nodeinfo[i]
        y_x[y].append(x)
    
    keys = list(y_x.keys())
    n_keys = len(keys)
    
    check(0, y_x[keys[0]][0], 0, 100000)
    root_node = node = idx[(y_x[keys[0]][0], keys[0])]
    # print(root_node)
    pre(root_node)
    post(root_node)
    # print(answer)
    return answer