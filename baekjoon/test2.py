class Solution:

    def sliding_window(self,answer,arr):
        n = len(arr)
        size = 2
        l = 0
        r = size - 1
        result = arr[r] - arr[l]
        answer = max(answer, result)
        l += 1
        r += 1 

        while r < n:
            front = arr[l-1]
            rear = arr[r]
            result += front
            result = rear - result
            answer = max(answer, result)
            l += 1
            r += 1 
        
        return answer


    def lengthOfLongestSubstring(self, s: str) -> int:


        
        hash_map = {}


        for i in range(len(s)):
            string = s[i]
            if string not in hash_map:
                hash_map[string] = [i]
            else:
                hash_map[string].append(i)

        answer = 0
        for arr in hash_map.values():
            if len(arr) >= 2:
                answer = max(answer, self.sliding_window(answer,arr))

        
        return answer



a = Solution()

print(a.lengthOfLongestSubstring("abcabcbb"))