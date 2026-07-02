# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue=deque()
        queue.append(root)
        result=[]
        
        while queue:
            level=[]
            size = len(queue)
            for i in range(size):
                value=queue.popleft()
                level.append(value.val)
                if value.left:
                    queue.append(value.left)
                if value.right:
                    queue.append(value.right)
            result.append(level)
        return result
        
        
