

lst = [list(map(int, input().split())) for _ in range(5)]
  
score = [sum(i) for i in lst]

print(score.index(max(score))+1, max(score))





