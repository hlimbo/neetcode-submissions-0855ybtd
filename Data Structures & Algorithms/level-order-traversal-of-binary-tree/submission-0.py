# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# apply bfs by using a queue to store the nodes as you visit them from left to right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque()
        queue.append(root)

        ans = []
        while len(queue) > 0:

            nodesPerLevel = len(queue)
            level = []
            while nodesPerLevel > 0:
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                nodesPerLevel -= 1

            ans.append(level)

        return ans