# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode):
        arr =[]
        while(head!= None):
            arr.append(head.val)
            head = head.next
        return arr == arr[::-1]
            
            
            Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
