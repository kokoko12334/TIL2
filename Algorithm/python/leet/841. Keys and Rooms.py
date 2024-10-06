

class Solution:
    def canVisitAllRooms(self, rooms) -> bool:
        

        stack = [rooms[0]]
        
        n = len(rooms)
        visited = [0]*n
        visited[0] = 1
        while stack:
            r = stack.pop()
            print(r)
            for i in r:
                print(visited[i])
                if visited[i] == 0:
                        print(visited[i])
                        stack.append(rooms[i])
                        visited[i] = 1

        print(visited)
        answer = True
        for i in visited:
             if i == 0:
                  answer = False
                  break
        return answer


a = Solution()

a.canVisitAllRooms(rooms = [[1],[2],[3],[]])