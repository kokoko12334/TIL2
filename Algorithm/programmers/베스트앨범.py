from collections import defaultdict
def solution(genres, plays):
    
    g_cnt = defaultdict(int)
    g_list = defaultdict(list)
    
    n = len(plays)
    for i in range(n):
        gen = genres[i]
        play = plays[i]
        g_cnt[gen] += play
        g_list[gen].append((play,i))
    
    g_cnt_arr = sorted([(v, k) for k, v in g_cnt.items()], reverse=True)
    
    answer = []
    for i in range(len(g_cnt_arr)):
        genre = g_cnt_arr[i][1]
        arr = g_list[genre]
        arr.sort(key=lambda x: (-x[0], x[1]))
        if len(arr) >= 2:
            answer.append(arr[0][1])
            answer.append(arr[1][1])
        else:
            answer.append(arr[0][1])
        
    
    return answer