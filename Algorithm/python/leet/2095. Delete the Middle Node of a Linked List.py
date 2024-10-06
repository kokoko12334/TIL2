class Solution:
    def deleteMiddle(self, head):
        c=1
        temp=head
        while temp.next!=None:
            temp=temp.next
            c+=1
        m=c//2
        if m==0:
            return None
        c,temp=1,head
        while c!=m:
            temp=temp.next
            c+=1
        if temp.next.next==None:
            temp.next=None
        else:
            temp.next=temp.next.next
        return head