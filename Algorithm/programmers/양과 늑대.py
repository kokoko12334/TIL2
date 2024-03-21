def solution(info, edges):
    seen = [0] * len(info)
    answer = []
    
    def dfs(sheep, wolf):
        # print(f"sheep:{sheep}, wolf:{wolf}, answer:{answer}")
        if sheep > wolf:
            answer.append(sheep)
        else:
            return 
        
        for p, c in edges:
            if seen[p] and not seen[c]:
                seen[c] = 1
                if info[c] == 0:
                    dfs(sheep+1, wolf)
                else:
                    dfs(sheep, wolf+1)
                seen[c] = 0

    seen[0] = 1
    dfs(1, 0)
    return max(answer)