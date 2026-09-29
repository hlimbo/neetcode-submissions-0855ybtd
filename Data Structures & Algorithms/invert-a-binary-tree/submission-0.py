# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(node) -> Optional[TreeNode]:
            if not node:
                return None
            
            newLeft = helper(node.right)
            newRight = helper(node.left)

            node.left = newLeft
            node.right = newRight
            return node

        return helper(root)