# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Count the depth of all subtrees within the tree to obtain the diameter? will that work for all cases?


1. diameter = depth of left subtree + depth of right subtree + (root node count 1)
2. depth of root node tree

max diameter = max(depth of root node tree, diameter, depth of left subtree, depth of right subtree)

need the depth of the current subtree and diameter of current subtree

'''

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depthHelper(rootNode) -> int:
            if not rootNode:
                return 0
            return 1 + max(depthHelper(rootNode.left), depthHelper(rootNode.right))

        if not root:
            return 0

        leftDepth = depthHelper(root.left)
        rightDepth = depthHelper(root.right)
        diameter = leftDepth + rightDepth

        leftResult = self.diameterOfBinaryTree(root.left)
        rightResult = self.diameterOfBinaryTree(root.right)

        maxDiameter = max(diameter, max(leftResult, rightResult))
        return maxDiameter