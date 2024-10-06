

class Solution:
    def asteroidCollision(self, asteroids):

        
        stack = [asteroids[0]]
        n = len(asteroids)
        for i in range(1,n):
            v = asteroids[i]
            
            while True:
                if stack:
                    top = stack[-1]

                    if top > 0:
                        if v < 0:
                            if abs(top) < abs(v):
                                stack.pop()

                            elif abs(top) == abs(v):
                                stack.pop()
                                break
                            else:
                                break
                        else:
                            stack.append(v)
                            break


                    else:
                        stack.append(v)
                        break
                else:
                    stack.append(v)
                    break
        answer = stack
        return answer
    

a = Solution()

a.asteroidCollision(asteroids = [1,-2,-2,-2])