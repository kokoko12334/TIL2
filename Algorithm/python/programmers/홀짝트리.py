from collections import defaultdict, deque
def solution(nodes, edges):
    
    g = defaultdict(list)
    
    for edge in edges:
        a, b = edge
        g[a].append(b)
        g[b].append(a)
    
    
    
    
    def bfs(node, type_):
        nonlocal seen_0, seen_1
        q = deque()
        tmp_seen = set()
        tmp_seen.add(node)
        
        for child in g[node]:
            q.append(child)
            tmp_seen.add(child)
        
        while q:
            current_node = q.popleft()
            current_node_res = current_node % 2
            child_nodes = [i for i in g[current_node] if i not in tmp_seen]
            child_res = len(child_nodes) % 2
            # print(f"{current_node}의 자식들:{child_nodes}, 수: {child_res}")
            if type_ == 0:
                if current_node_res == child_res:
                    for next_node in child_nodes:
                        if next_node in tmp_seen:
                            continue
                        q.append(next_node)
                        tmp_seen.add(next_node)
                else:
                    # print("중단")
                    return False
            else:
                if current_node_res != child_res:
                    for next_node in child_nodes:
                        if next_node in tmp_seen:
                            continue
                        q.append(next_node)
                        tmp_seen.add(next_node)
                else:
                    # print("중단")
                    return False
        
        if type_ == 0:
            for ele in tmp_seen:
                seen_0.add(ele)
        else:
            for ele in tmp_seen:
                seen_1.add(ele)
        
        return True
    
    # 0: 홀 
    # 1: 역홀
    answer = [0, 0]
    n = len(nodes)
    seen_0 = set()
    seen_1 = set()
    for i in range(n):
        node = nodes[i]
        
        node_res = node % 2
        child_res = len(g[node]) % 2
        if node_res == child_res:
            type_ = 0
        else:
            type_ = 1
        
        if type_ == 0 and node in seen_0:
            continue
        elif type_ == 1 and node in seen_1:
            continue
        
        # print(f"#####{node} 루트노드 수행 -> {type_}########")
        if bfs(node, type_):
            answer[type_] += 1
            # print(f"{type_} += 1")
            
        
    return answer