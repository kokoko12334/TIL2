from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        lst = ListNode()
        p = lst
        add_num = 0
        p1 = l1
        p2 = l2
        while True:
            num1 = 0
            num2 = 0
            if p1 != None:
                num1 = p1.val
            if p2 != None:
                num2 = p2.val
            result = num1 + num2 + add_num
            if result >= 10:
                this_val = result - 10
                next_add_num = 1
            else:
                this_val = result
                next_add_num = 0
            
            p.val = this_val
            add_num = next_add_num
            if p1 != None:
                p1 = p1.next
            if p2 != None:
                p2 = p2.next
            if p1 == None and p2 == None and add_num == 0:
                break
            p.next = ListNode()
            p = p.next

        return lst



