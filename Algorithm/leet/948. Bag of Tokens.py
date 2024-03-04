from typing import List

class Solution:
    
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        tokens.sort()
        tokens.append(power)

        l = 0
        r = len(tokens) - 1
        score = 0
        power = 0
        while l < r:
            
            l_v = tokens[l]
            r_v = tokens[r] + power
            # print(f"r_idx:{r},r_value:{r_v},l_idx:{l},l_value:{l_v},score:{score}")
            if r_v >= l_v:
                score += 1
                tokens[r] -= l_v
                l += 1
            elif score > 0 and r_v < l_v:
                power += tokens[r]
                if len(tokens[l:r]) > 1:
                    score -= 1
                r -= 1
                
            else:
                break
        
        

        return score    