from collections import defaultdict, deque
def solution(nodes, edges):
    #[0, 1] => 홀, 역홀
    g = defaultdict(list)
    
    for edge in edges:
        a, b = edge
        g[a].append(b)
        g[b].append(a)
    
    answer = [0, 0]
    def check(start):
        nonlocal seen
        stack = [start]
        seen.add(start)
        root = 0
        noroot = 0
        cnt = 0
        while stack:
            cnt += 1
            num = stack.pop()
            child_cnt = len(g[num])
            
            if num%2 == 0:
                if child_cnt%2 == 0:
                    noroot += 1
                else:
                    root += 1
            else:
                if child_cnt%2 == 0:
                    root += 1
                else:
                    noroot += 1
            
            for next_node in g[num]:
                if next_node not in seen:
                    seen.add(next_node)
                    stack.append(next_node)
        
        if cnt == 1:
            if start%2 == 0:
                answer[0] += 1
            else:
                answer[1] += 1
        elif cnt == 2:
            if root == 1:
                answer[0] += 1
                answer[1] += 1
        else:
            if root == 1:
                answer[1] += 1
            elif noroot == 1:
                answer[0] += 1
        
        return
        
        
        
    
    seen = set()
    for i in range(len(nodes)):
        if nodes[i] in seen:
            continue
        
        check(nodes[i])
    
    
            
        
    return answer