"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        clone= Node(0)
        clonehead= clone
        currentnode= head
        hashmap ={}
        hashmap[None]=None
        while currentnode:
            clone.next = Node(currentnode.val)
            clone = clone.next
            hashmap[currentnode]=clone
            currentnode= currentnode.next
        currentnode =head
        clone = clonehead.next
        while currentnode:
            clone.random = hashmap[currentnode.random]
            clone= clone.next
            currentnode =currentnode.next
        return clonehead.next
        
        
        
        se a hashtable to facilitate the cloning.

Complexities

Time: O( n )

We will perform linear time traversals that keep our asymptotic behavior linear.

Space: O( n )

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.
 

Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
Example 4:

Input: head = []
Output: []
Explanation: Given linked list is empty (null pointer), so return null.


