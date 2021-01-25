# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root ==None:
            return None
        return self.dfs(root,targetSum)
    def dfs(self,root,currtarget):
        if root: 
            print(root.val,currtarget)
        else:
            print("rrotgaali")
        if root==None:
            return False
        if currtarget-root.val==0 and root.left==None and root.right==None:
            return True
        if root:
            if (self.dfs(root.left,currtarget-root.val) or self.dfs(root.right,currtarget-root.val)):
                return True
        return False
