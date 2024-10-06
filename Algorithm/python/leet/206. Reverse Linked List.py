# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        
        

        if head != None:
            pre_node = ListNode(head.val,None)
            node = head.next

            while node!= None:
                next_node = node.next
                
                node.next = pre_node
                
                pre_node = node
                
                node = next_node

            
            
            return pre_node
        else:
            return None
        

