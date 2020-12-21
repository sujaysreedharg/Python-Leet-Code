 RECURSIVE BT:

class TreeNode:
  def __init__(self, val=0, left=None, right=None):        
    self.val = val
    self.left = left
    self.right = right

def inorderTraversal(root):
  arr=[]
  print(traverse(root,arr))
def traverse(root,arr):
  if root == None:
    return
  traverse(root.left,arr)
  arr.append((root.val))
  traverse(root.right,arr)
  return arr

def preorderTraversal(root):
  arr=[]
  print(pretraverse(root,arr))
def pretraverse(root,arr):
  if root == None:
    return
  arr.append((root.val))
  pretraverse(root.left,arr)
  pretraverse(root.right,arr)
  return arr

def postorderTraversal(root):
  arr=[]
  print(posttraverse(root,arr))
def posttraverse(root,arr):
  if root == None:
    return
  posttraverse(root.left,arr)
  posttraverse(root.right,arr)
  arr.append((root.val))
  return arr
root= TreeNode(12)
root.left = TreeNode(6)
root.right = TreeNode(3)

inorderTraversal(root)
preorderTraversal(root)
postorderTraversal(root)

 O (n) where n is the number of nodes in the tree
 O(h) -> Space where h is the height of the tree

ITERATIVE BT:


class TreeNode:
  def __init__(self, val=0, left=None, right=None):        
    self.val = val
    self.left = left
    self.right = right

def inorderTraversal(root):
  stack=[]
  result=[]
  node= root
  while True:
    while node!=None:
      stack.append(node)
      node=node.left
    if not stack:
      break
    node=stack.pop()
    result.append(node.val)
    node=node.right
  print(result)
def preorderTraversal( root):
  stack=[root]
  result=[]
  while stack:
    root = stack.pop()
    result.append(root.val)
    if root.right!= None:
      stack.append(root.right)
    if root.left!=None:
      stack.append(root.left)
  print(result)
def postorderTraversal( root):
  stack1=[root]
  stack2=[]
  result=[]
  while stack1:
    popped=stack1.pop()
    stack2.append(popped.val)
    if popped.left:
      stack1.append(popped.left)
    if popped.right:
      stack1.append(popped.right)
  while stack2:
    node= stack2.pop()
    result.append(node)
  print(result)
root= TreeNode(12)
root.left = TreeNode(6)
root.right = TreeNode(3)

inorderTraversal(root)
preorderTraversal(root)
postorderTraversal(root)



