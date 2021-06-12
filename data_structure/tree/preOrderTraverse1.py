# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
a = []

def preOrderTraverse1(root):
    if root != None:
        preOrderTraverse1(root.left)
        a.append(root.val)
        preOrderTraverse1(root.right)
