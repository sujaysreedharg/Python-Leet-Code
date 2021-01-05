#Recursive:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left,root.right = root.right,root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root
       
       
 #Iterative-uh:
 
 from queue import Queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            q= Queue()
            q.put(root)
            while q.qsize() > 0:
                node= q.get()
                node.left, node.right = node.right, node.left
                if node.left:
                    q.put(node.left)
                    
                if node.right:
                    q.put(node.right)
        return root
For both recursive and iterative
 Time -> O(n)
 Space -> O(n)
