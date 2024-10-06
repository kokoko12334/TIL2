from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        n = len(words)

        idx = 0
        answer = []
        while idx < n:
            arr = [words[idx]]
            avail = maxWidth - len(words[idx])
            
            while idx+1 < n and len(words[idx+1]) + 1 <= avail:
                idx += 1
                # print(f"{words[idx]}, avail:{avail}, len:{len(words[idx])+1}")
                arr.append(words[idx])
                avail -= len(words[idx]) + 1
            
            arr_n = len(arr)
            avail += arr_n - 1
            string = [arr[0]]
            if arr_n > 1:
                quo = avail // (arr_n - 1)
                res = avail % (arr_n - 1)
                
                if res:
                    for i in range(1, arr_n):
                        if i <= res:
                            string.append(" " * (quo + 1))
                            string.append(arr[i])
                        else:
                            string.append(" " * quo)
                            string.append(arr[i])
                else:
                    for i in range(1, arr_n):
                            string.append(" " * quo)
                            string.append(arr[i])
            else:
                string.append(" " * (maxWidth - len(arr[0])))
            # print(string)
            answer.append("".join(string))
        
            idx += 1

        last = answer[-1].split(" ")
        last_arr = []
        for i in range(len(last)):
            if last[i]:
                last_arr.append(last[i])
        last_string = " ".join(last_arr)
        last_string += " " * (maxWidth -len(last_string))
        answer[-1] = last_string

        return answer