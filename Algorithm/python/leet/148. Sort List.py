# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        node = head
        arr = []
        while node != None:
            arr.append(node.val)
            node = node.next
            
        def merge_sort(arr):
            
            if len(arr) > 1:
                mid = len(arr) // 2
                left = arr[:mid]
                right = arr[mid:]

                merge_sort(left)
                merge_sort(right)

                i = 0
                j = 0
                k = 0
                while i < len(left) and j < len(right):
                    if left[i] < right[j]:
                        arr[k] = left[i]
                        i += 1
                    else:
                        arr[k] = right[j]
                        j += 1
                    k += 1
                
                while i < len(left):
                    arr[k] = left[i]
                    k += 1
                    i += 1
                
                while j < len(right):
                    arr[k] = right[j]
                    k += 1
                    j += 1
        merge_sort(arr)
        
        if head:
            head = ListNode()
            node = head
            idx = 0

            while idx < len(arr):
                node.val = arr[idx]
                idx += 1
                if idx < len(arr):
                    node.next = ListNode()
                    node = node.next
                else:
                    break
            
        return head