class Solution:
    def countAndSay(self, n: int) -> str:

        if n == 1:
            return '1'
        
        string = self.countAndSay(n-1)
        arr = []
        s = ""
        cnt = 1
        for i in range(len(string)):
            if string[i] == s:
                cnt += 1
            else:
                arr.append(str(cnt))
                arr.append(s)
                s = string[i]
                cnt = 1
        arr.append(str(cnt))
        arr.append(s)
        result = "".join(arr[2:])
        return result