class Solution:
    def largestAltitude(self, gain) -> int:
        
        arr = [0]
        for i in range(len(gain)):
            arr.append(arr[i] + gain[i])
        
        
        answer = max(arr)
        return answer