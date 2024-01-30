class Solution:
    def findCircleNum(self, isConnected) -> int:

        answer = 0
        n = len(isConnected)
        seen = [-1]*n

        for i in range(n):
            
            stack = [i]
            if seen[i] == -1:
                seen[i] = i

            while stack:
                node = stack.pop()
                for j in range(n):
                    
                    if isConnected[node][j] == 1 and seen[j] == -1:
                        stack.append(j)
                        seen[j] = i

        answer = len(set(seen))
        return answer

#유니온파인드
# class Solution:

#     def find(self,x,parent):

#         if x != parent[x]:
#             parent[x] = self.find(parent[x],parent)

#         return parent[x]

#     def union(self, x,y, parent, rank):
#         xroot = self.find(x, parent)
#         yroot = self.find(y, parent)

#         if xroot == yroot:
#             return
        
#         if rank[xroot] < rank[yroot]:
#             parent[xroot] = yroot
#         elif rank[xroot] > rank[yroot]:
#             parent[yroot] = xroot
#         else:
#             parent[yroot] = xroot
#             rank[xroot] += 1

#     def findCircleNum(self, isConnected) -> int:

#         n = len(isConnected)
#         parent = [i for i in range(n)]
#         rank = [0]*n

#         for i in range(n):
#             for j in range(n):
#                 if isConnected[i][j] == 1:
#                     self.union(i,j,parent,rank)
        
#         for i in range(n):
#             self.find(i,parent)
        
#         answer = len(set(parent))
        
#         return answer

a = Solution()

a.findCircleNum(isConnected = [[1,1,0,0,0,0,0,1,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,1,1,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,1,1,0,0,0,0],[0,0,0,1,0,1,0,0,0,0,1,0,0,0,0],[0,0,0,1,0,0,1,0,1,0,0,0,0,1,0],[1,0,0,0,0,0,0,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,1,0,0,0,0,1,0],[0,0,0,0,1,0,0,0,0,1,0,1,0,0,1],[0,0,0,0,1,1,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,1,0,1,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,1,0,0,0,0,1]])


