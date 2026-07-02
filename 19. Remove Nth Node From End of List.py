# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=left=ListNode(0)
        dummy.next=left.next=head
        for _ in range(n):
            head=head.next
        while head!=None:
            head=head.next
            left=left.next
        left.next=left.next.next
        return dummy.next
