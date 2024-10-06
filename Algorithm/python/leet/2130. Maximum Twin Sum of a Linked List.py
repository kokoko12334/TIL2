# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head) -> int:

        node = head
        idx = 0
        lst = []
        while node != None:
            lst.append(node.val)
            node = node.next
            idx += 1
        
        n = idx//2

        answer = 0
    
        for i in range(n):
            
            result = lst[i] + lst[idx-1-i]
            answer = max(answer, result)


        return answer