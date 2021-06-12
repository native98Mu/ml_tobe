class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def printTree(self):
        print(self.val)



class BinaryTree(object):
    def __init__(self):
        self._root = None
    def insert(self, item):
        node = TreeNode(item)
        if self.val:
            if item < self.val:
                if self.left is None:
                    self.left = node
root = BinaryTree()
root.insert(6)
root.insert(3)
print(root)

def inOrderTraverse1(root):
    if root != None:
        inOrderTraverse1(root.left)
        inOrderTraverse1(root.right)
# class Node:
#     def __init__(self, data):
#         self.left = None
#         self.right = None
#         self.data = data

#     def insert(self, data):
#     # 将新值与父节点进行比较
#         if self.data:  # 非空
#             if data < self.data:            #新值较小，放左边
#                 if self.left is None:       #若空，则新建插入节点
#                     self.left = Node(data)
#                 else:                       #否则，递归往下查找
#                     self.left.insert(data)
#             elif data > self.data:          #新值较大，放右边
#                 if self.right is None:      #若空，则新建插入节点
#                     self.right = Node(data)
#                 else:                       #否则，递归往下查找
#                     self.right.insert(data)
#         else:
#             self.data = data                

#     # 打印这棵树，中序遍历
#     def PrintTree(self):
#         if self.left:
#             self.left.PrintTree()
#         print(self.data),
#         if self.right:
#             self.right.PrintTree()

# # 使用insert方法添加节点
# root = Node(12)
# root.insert(6)
# root.insert(7)
# root.insert(3)

# root.PrintTree()
                    



    


