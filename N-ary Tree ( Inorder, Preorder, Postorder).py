"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res=[]
        if not root:
            return res
        def dfs(node):
            if not node:
                return None
            res.append(node.val)
            children=node.children
            for i in range(len(children)):
                dfs(children[i])
        dfs(root)
        return res
        
        
        
 """
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res=[]
        if not root:
            return res
        def dfs(node):
            if not node:
                return None
            
            children=node.children
            for i in range(len(children)):
                dfs(children[i])
            res.append(node.val)                
        dfs(root)
        return res
        
        
        
        
      INORDER:
      class Solution:
    def inorder(self, root: 'Node') -> List[int]:
        res=[]
        if not root:
            return res
        def dfs(node):
            if not node:
                return None
            
            children=node.children
            for i in range(len(children)-1):
                dfs(children[i])
            res.append(node.val)   
            dfs(children[len(children)-1])
        dfs(root)
        return res
