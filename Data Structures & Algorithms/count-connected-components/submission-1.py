'''
INPUTS
* n nodes represented as an integer
* array of edges where edges[i] = [ai, bi]

Task:
* return number of connected components in the graph

Approach is to use disjoint set or union find but I don't remember how to do that algorithm

How do I know if a node is disconnected from all other nodes?
    * there is no direct or indirect connection to that node
        * direct connection ==> Its defined as an edge in the inputs
        * indirect connection 
        ==> I can reach the target node by taking an arbitrary number of nodes in betweeen to reach it

I also know that from my inputs I'm given the number of nodes in the graph
* use that information to figure out how many i have left to process

- I know its 1 graph component if all nodes can reach other
- its 2 or more graphs if you can't reach at least 1 node

what I could do is convert the list of edges into an adjacency list
* key - node I'm coming from
* value - all the nodes that are directly connected to key node (list of nodes)

Use BFS to explore all nodes that are connected starting with the first edge
and add it to a visited set
* BFS stops once all the nodes I process in the deque or queue are empty
* if the number of nodes i processed is < n, and I finish my BFS, then there has to be at least
 one more connected set of components to process

 Answer would be the the number of visited sets I get from all the BFS traversals I do

Questions
* is it an undirected or directed graph? undirected from the visual examples it seems
* are there cycles in this graph? maybe
'''

class Solution:
    # return number of nodes processed
    def bfsTraversal(self, startNode: int, adjList: Dict[int, List[int]]) -> set:
        visitedSet = set()
        nodeQueue = deque()
        nodeQueue.append(startNode)

        while len(nodeQueue) > 0:
            node = nodeQueue.popleft()
            if node in visitedSet:
                continue
            
            visitedSet.add(node)

            neighbors = adjList[node]
            for neighbor in neighbors:
                nodeQueue.append(neighbor)


        return visitedSet

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # convert edges to adj list
        adjList = {}
        for node in range(n):
            adjList[node] = []

        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        processedNodes = set()
        islandsCount = 0

        for node in range(n):
            # skip ones visited from previous bfs traversals
            if node in processedNodes:
                continue

            currSet = self.bfsTraversal(node, adjList)
            for visitedNode in currSet:
                processedNodes.add(visitedNode)
            islandsCount += 1

            # visited all nodes in the potentially disconnected graph
            if len(processedNodes) == n:
                break

        return islandsCount
        