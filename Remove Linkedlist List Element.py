# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return None
        currentnode= ListNode(-1)
        currentnode.next = head
        head = currentnode
        while currentnode.next!= None:
            if currentnode.next.val == val:
                currentnode.next= currentnode.next.next
            else:   currentnode= currentnode.next
        return head.next
        
        
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
