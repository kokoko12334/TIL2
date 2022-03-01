t = int(input())
lst = [input() for _ in range(t)]
#모든 원소가 같은지 확인
def all(str):
    if len(set(str))==1:
        return True
    else:
        return False 
#세로 비교형으로 변형
def check(lst):            

    check_box = list(zip(*lst))
    check_box = [list(check_box[i]) for i in range(len(check_box))]   
    return check_box


check_box = check(lst)

for i in range(len(check_box)):
    if all(check_box[i]):
        continue
    else:
        for j in range(len(check_box[i])):
            check_box[i][j] = '?'

lst = check(check_box)
print(''.join(lst[0]))



##############################

n = int(input())
files = [input() for _ in range(n)]
pattern = ""

for columns in zip(*files):
    pattern += "?" if columns.count(columns[0]) < n else columns[0]

print(pattern)








