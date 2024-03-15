
def deliver(idx,deliveries,cap):
    stack = []
    
    while cap > 0 and idx >=0:
        d = deliveries[idx]
        if d:
            if cap >= d:
                cap -= d
                stack.append(idx)
                deliveries[idx] = 0
                idx -= 1
            else:
                
                deliveries[idx] -= cap
                cap = 0
                stack.append(idx)
        else:
            idx -= 1
    if stack:
        dis = stack[0] + 1
        next_idx = idx
        return dis, next_idx, deliveries
    return 0,idx,deliveries

def pickup(idx,pickups,cap):
    stack = []
    while cap > 0 and idx >=0:
        d = pickups[idx]
        if d:
            if cap >= d:
                cap -= d
                stack.append(idx)
                pickups[idx] = 0
                idx -= 1
            else:
                
                pickups[idx] -= cap
                cap = 0
                stack.append(idx)
        else:
            idx -= 1
    if stack:        
        dis = stack[0] + 1
        next_idx = idx
        return dis,next_idx, pickups
    return 0,idx,pickups
    
def solution(cap, n, deliveries, pickups):
    
    idx_d = n-1
    idx_p = n-1
    answer_lst = []
    while True:
        dis_d = 0
        dis_p = 0
        if idx_d >= 0:
            dis_d,idx_d,deliveries = deliver(idx_d,deliveries,cap)
        if idx_p >= 0:
            dis_p,idx_p,pickups = pickup(idx_p,pickups,cap)
        # print(f"dis_d:{dis_d}, idx_d:{idx_d}")
        # print(f"del:{deliveries}")
        # print(f"dis_p:{dis_p}, idx_p:{idx_p}")
        # print(f"picks:{pickups}")
        cost = max(dis_d, dis_p)
        # print(dis_d,dis_p)
        answer_lst.append(cost)
        answer_lst.append(cost)
        if idx_d < 0 and idx_p < 0:
            break
    
    answer = sum(answer_lst)
    # print(answer_lst)
    return answer
