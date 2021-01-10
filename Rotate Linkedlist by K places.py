# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if not head or k==0:
            return head

        count=1
        last=head
        while last.next:

            last=last.next
            count+=1
        last.next= head
        curr=head

        for _ in range(count - (k % count)-1):
            curr=curr.next

        result= curr.next
        curr.next=None
        return result
