Recursive:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pval=p.val 
        qval= q.val
        parentval = root.val
        if pval > parentval and qval> parentval:
            return self.lowestCommonAncestor(root.right,p,q)
        elif pval < parentval and qval < parentval:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return root
            
Time Complexity: O(N), where N is the number of nodes in the BST. In the worst case we might be visiting all the nodes of the BST.

Space Complexity: O(N). This is because the maximum amount of space utilized by the recursion stack would be N since the height of a skewed BST could be N.


Iterative:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pval=p.val 
        qval= q.val
        
        while root:
            parentval=root.val
            if pval> parentval and qval>parentval:
                root=root.right
            elif pval < parentval and qval< parentval:
                root=root.left
            else:
                return root
                
                
 Time Complexity : O(N) where N is the number of nodes in the BST. In the worst case we might be visiting all the nodes of the BST.

Space Complexity : O(1).


