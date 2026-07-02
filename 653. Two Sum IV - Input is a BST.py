# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None:
            return False
        def check(root,val,currNode):
            if root is None:
                return False
            if val > root.val:
                return check(root.right,val,currNode)
            elif val < root.val:
                return check(root.left,val,currNode)
            elif root.val==val:
                return root!=currNode
            return False
        def dfs(root,currNode,k):
            if currNode is None:
                return False
            if check(root,k-currNode.val,currNode):
                return True
            return dfs(root,currNode.left,k) or dfs(root,currNode.right,k)
        return dfs(root,root,k)
            
