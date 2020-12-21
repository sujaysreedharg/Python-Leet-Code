import heapq as heap

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        priorityqueue = []
        dummy = ListNode()
        for l in lists:
            while l:
                heap.heappush(priorityqueue,l.val)
                l= l.next
        l = dummy
        while priorityqueue:
            l.next = ListNode(val=heap.heappop(priorityqueue))
            l = l.next
        return dummy.next
        
        
        
        
        
Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
        
        
        
        



Runtime: O(n*log(n)) - each heappush and heappop runs in O(log(n)) time; we call both functions for every element.
Space: O(n) - to accommodate the heap with n elements.
