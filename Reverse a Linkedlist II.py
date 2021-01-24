# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None
        
        curr = head
        prev=None
        while m>1:
            prev = curr
            curr=curr.next
            m-=1
            n-=1
        tail = curr
        con=prev
        
        while n>0:
            nextnode=curr.next
            curr.next=prev
            prev=curr
            curr=nextnode
            n-=1
        if con:
            con.next=prev
        else:
            head=prev
        tail.next=curr
        return head
