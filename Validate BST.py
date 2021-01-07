# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.bsthelper(root,float("-inf"),float("inf"))
    def bsthelper(self,root, minvalue,maxvalue):
        if root is None:
            return True
        if root.val <= minvalue or root.val >= maxvalue:
            return False
        validateleftsubtree = self.bsthelper(root.left,minvalue,root.val)
        return validateleftsubtree and self.bsthelper(root.right,root.val,maxvalue)
        
        
        
        Time -> O(n)
        Space -> O(d) 
        
