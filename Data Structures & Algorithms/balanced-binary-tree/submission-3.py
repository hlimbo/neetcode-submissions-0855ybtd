# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# height = max number of edges of a tree

'''
To do this recursively:

Base Case:
    if root is Null or None:
        return -1 as we are counting number of edges not number of nodes

To compute height recursively,
    *  1 + max(self.recur(root.left), self.recur(root.right))
if abs(height of left subtree - height of right subtree) < 2 => return True; otherwise return False

'''

class Solution:
    # counts the max number of edges of a tree based on which side of the tree has the tallest edge
    def getHeight(self, root: Optional[TreeNode]) -> int:
        # accounts for number of edges and not nodes
        if root is None:
            return -1

        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Assume: a null root is a balanced tree
        if root is None:
            return True

        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        isTreeBalanced = abs(leftHeight - rightHeight) <= 1
        return isTreeBalanced and self.isBalanced(root.left) and self.isBalanced(root.right)
        
