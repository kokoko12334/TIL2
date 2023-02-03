
#유니온-> 최종 부모노드를 확인하는 작업(어느 그룹의 그래프에 속하는지 ) 더 낮은 값을 부모노드로
#파인드 -> 최종 부모노드들이 같은지 확인(두개를 골랐을 때 같은 그래프에 속하는지)
#인덱스가 번호, 인덱스의 값이 부모노드를 말함

class Graph:
    def __init__(self, num):
        self.num = num

        parent = [0]*(self.num+1)
        for i in range(1,self.num+1):
            parent[i] = i
        self.parent = parent
    

    def __call__(self):
        return self.parent

    def getparent(self,x):               #부모노드를 찾는 과정(3->2->1)
        if self.parent[x] == x:
            return x
        else:
            return self.getparent(self.parent[x])    

    def unionparent(self, a,b):
        a = self.getparent(a)
        b = self.getparent(b)
        if a < b:
            self.parent[b] = a 
        else:
            self.parent[a] = b

    def findparent(self, a, b):
        a = self.getparent(a)
        b = self.getparent(b)
        if a == b:
            return 1
        else:
            return 0    
 
class Edge:
    def __init__(self, a,b, value):
        self.node = [0,0]
        self.node[0] = a
        self.node[1] = b
        self.v = value

a = Graph(10)

a.unionparent(2,3)
a.unionparent(1,2)

a.unionparent(3,4)


a.unionparent(5,6)

a.unionparent(7,8)
a.unionparent(8,9)
a.unionparent(9,10)
a()


a.findparent(1,3)   #같은 집합인지 (연결 되어있는지)




#크루스칼(Kruskal)알고리즘: 가장 적은 비용으로 모든 노드를 연결
#  => 최소 비용 신장 트리를 만들기 위한 알고리즘

values = []

values.append(Edge(1, 7, 12))
values.append(Edge(1, 4, 28))
values.append(Edge(1, 2, 67))
values.append(Edge(1, 5, 17))
values.append(Edge(2, 4, 24))
values.append(Edge(2, 5, 62))
values.append(Edge(3, 5, 20))
values.append(Edge(3, 6, 37))
values.append(Edge(4, 7, 13))
values.append(Edge(5, 6, 45))
values.append(Edge(5, 7, 73))


values = sorted(values, key = lambda x: x.v) #간선의 값을 기준으로 정렬

for i in values:
    print(i.v)

a = Graph(7)       #초기에는 각자 자기를 가리키는 그래프를 생성

total = 0
cycle = False 
for i in values:
    if not a.findparent(i.node[0], i.node[1]):   #부모노드가 같지 않다면
        total += i.v                             #더함
        a.unionparent(i.node[0], i.node[1])    #그다음 연결
    else:
        cycle = True


print(total)

if cycle:
    print("싸이클 존재")


d  = {1:1, 2:2}



list(d.keys())[0]
a = {1,2,3}

b = {2,3}

int('123'[0])
(a-b)[0]





total =0

total += 0



91011


result = []

result.append(None)

