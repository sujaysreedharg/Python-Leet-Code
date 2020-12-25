# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        head = dummy
        while (l1!=None and l2!=None):

            if l1.val <= l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next =l2
                l2 = l2.next
            dummy =dummy.next
        dummy.next = l1 or l2
        return head.next
        
        
        
        O(m+n) -> Time
        O(1) -> Space
        
        
        Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]

        
