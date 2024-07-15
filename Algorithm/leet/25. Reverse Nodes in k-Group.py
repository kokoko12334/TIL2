
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):

        def reverseLinkedList(head, k):
            prev = None
            curr = head
            while k > 0 and curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                k -= 1
            return prev
        
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        while True:
            # Check if there are at least k nodes left
            start = prev_group_end.next
            end = prev_group_end
            for _ in range(k):
                if end.next:
                    end = end.next
                else:
                    return dummy.next  # No more nodes to reverse
            
            # Save the next group's start
            next_group_start = end.next
            
            # Reverse the current group
            end.next = None  # Disconnect the end of the current group
            prev_group_end.next = reverseLinkedList(start, k)
            
            # Reconnect the reversed group
            start.next = next_group_start
            
            # Update prev_group_end for the next iteration
            prev_group_end = start
        
        return dummy.next