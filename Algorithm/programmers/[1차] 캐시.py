from collections import deque           
def solution(cacheSize, cities):
    answer = 0
    n = len(cities)
    cache = deque()
    for i in range(n):
        city = cities[i].upper()
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                
                if cache:
                    cache.popleft()
                    cache.append(city)
            answer += 5
        
    return answer