# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
            
        stack1=[root]
        stack2=[]
        level=[]
        result=[]
        while stack1 or stack2:
            while stack1:
                root= stack1.pop()
                level.append(root.val)
                if root.left is not None:
                    stack2.append(root.left)
                if root.right is not None:
                    stack2.append(root.right)
            result.append(level)
            level=[]
            while stack2:
                root=stack2.pop()
                level.append(root.val)
                if root.right is not None:
                    stack1.append(root.right)
                if root.left is not None:
                    stack1.append(root.left)
            if level!=[]:
                result.append(level)
                level=[]
        return result
        
        
        
        Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]




