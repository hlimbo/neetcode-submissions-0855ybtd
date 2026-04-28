"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        originalToClonedNodesMap = {}
        
        def dfs(node: Optional['Node']) -> Optional['Node']:
            if node is None:
                return None
            if node in originalToClonedNodesMap:
                return originalToClonedNodesMap[node]
            
            # create a new copy if one does not exist yet
            originalToClonedNodesMap[node] = Node(node.val)
            newNode = originalToClonedNodesMap[node]
            
            for neighbor in node.neighbors:
                neighborCopy = dfs(neighbor)
                newNode.neighbors.append(neighborCopy)

            return newNode

        return dfs(node)