'''
inputs:
* n nodes
* labeled 0 to n - 1
* list of undirected edges where each edge is a pair of nodes

task:
* write a function to check whether these edges make up a valid tree

output:
* bool
    - true if valid tree
    - false if invalid tree


Questions
* Is this for an n-ary tree? binary tree?
* undirected means that you can either go from node a to b or vice
versa assuming a,b form an edge?
* If you have many nodes but 0 edges, I assume it wouldn't count
as a tree because no nodes are connected to any other nodes? Is this
the right assumption to have?
* is it possible to have cycles for this graph?


Possible Approach:
* Using BFS
* why?
* if these 2 things are true, then it should solve it for majority of the cases

1. if you cannot visit all the nodes at most 1 time, then it is not a valid tree
2. if you visit a node more than once, then it is not a valid tree

Steps
* convert edges into an adjacency map where key is node and value is set of nodes key node can go towards
* start with the 0th node and store in a queue to begin the bfs node search
* run bfs to visit each node and as each node is visited store it in a visited set
    - remove node pending from queue
    - if node is already visited:
        return false
    otherwise
        add node to visited set
        for every neighbor from adjacency map[node]
            add neighbor to queue

* if visited nodes count matches n --> return true (signifies that each node is visited exactly 1 time)
* otherwise return false

The BFS in this scenario I described does not work because there is a
chance you visit the same node more than once due to the undirected edge
relationship

Challenges
* because its an undirected graph, how do I make sure that
I don't accidentally backtrack to the node I just seen from the last bfs iteration?
* store it in a lastNodeVisited variable to ensure we don't mark a node we saw last time
as it being an invalid tree... we only want to visit all nodes EXCEPT for the one we last visited
'''

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:        
        adjMap = {}
        for i in range(n):
            adjMap[i] = set()
        
        for edge in edges:
            incoming,outgoing = edge
            adjMap[incoming].add(outgoing)
            adjMap[outgoing].add(incoming)

            # no self loops
            if incoming == outgoing:
                return False

        nodeQueue = deque()
        # visit any node here -- start with 0th node for convenience
        nodeQueue.append(0)
        nodesVisitedSet = set()

        while len(nodeQueue) > 0:
            currNode = nodeQueue.popleft()
            # check for cycles
            if currNode in nodesVisitedSet:
                return False

            nodesVisitedSet.add(currNode)

            neighbors = adjMap[currNode]
            for neighbor in neighbors:
                # remove connections from neighbors that can backtrack back to this node
                # because we don't want to say its an invalid tree as the edges are undirected
                if currNode in adjMap[neighbor]: 
                    adjMap[neighbor].remove(currNode)
                nodeQueue.append(neighbor)

        return len(nodesVisitedSet) == n