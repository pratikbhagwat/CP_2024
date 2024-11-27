from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        arrayOfNodes =[]
        self.preOrderTraverseAndStore(root,arrayOfNodes)

        for index, node in enumerate(arrayOfNodes):
            if index == len(arrayOfNodes)-1:
                node.left=None
                node.right=None
            else:
                node.left=None
                node.right=arrayOfNodes[index+1]

        return root


    def preOrderTraverseAndStore(self, node, array):

        if node:
            array.append(node)
            self.preOrderTraverseAndStore(node.left, array)
            self.preOrderTraverseAndStore(node.right, array)

    def flattenOof1(self, root):

        stack = []

        node = root

        while node:
            if node.right and node.left:
                stack.append(node.right)
                node.right=node.left
                node.left = None
            elif node.left and node.right == None:
                node.right = node.left
                node.left=None
            elif node.left == None and node.right:
                pass
            elif node.right == None and node.left==None:
                if len(stack)!=0:
                    node.right=stack.pop()



            node=node.right

        return root







