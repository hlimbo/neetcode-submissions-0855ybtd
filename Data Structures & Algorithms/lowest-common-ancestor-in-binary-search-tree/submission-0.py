# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
BST
        left descendant nodes < node < right descendant nodes

- all values are unique

Task
* find the Lowest Common Ancestor (LCA) of 2 nodes p and q

A common ancestor of nodes p and q is a node up the tree that both connect back to p and q


One way to do it is to
* start at the root node
    * look for p using DFS
    * look for q using DFS
    * if p and q can be found, then the node we are on is a common ancestor
* go down again by visiting the left node
    * look for p using DFS
    * look for q using DFS
        * if p and q are found, then this node is the newest lca
* go down again by visiting the right node
    * look for p using DFS
    * look for q using DFS
        * if p and q are found, then this node is the newest lca
* N^2 time complexity...

* try a more efficient approach since we know that in a BST
    * left descendant nodes < node < right descendant nodes

* if p.val <= node <= q.val OR q.val <= node <= p.val (this would be the lowest common ancestor)

* if p.val > node and q.val > node
    * lowest common ancestor is on right side of tree

* if p.val < node and q.val < node
    * lowest common ancestor is on left side of tree

this gets cut down to a O(LogN) search

'''

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            # something went wrong here....
            return None
        
        if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
            return root

        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)