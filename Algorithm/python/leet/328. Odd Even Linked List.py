import copy
class Solution:
    def oddEvenList(self, head):
        

        if head != None:
            node = head
            head2 = copy.deepcopy(head).next
            node1 = head2


            while node != None and node.next != None:


                node.next = node.next.next
                if node.next != None:
                    node = node.next




            while node1 != None and node1.next != None:
            
                node1.next = node1.next.next

                if node1.next != None:
                    node1 = node1.next


            node.next = head2


            return head

        else:
            
            return None