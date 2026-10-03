'''
inputs:
    - weighted directed graph
    - n = number of vertices in graph (2 <= n <= 100)
    - each vertex is labeled 0 to n - 1
    - edges - list of tuples
        - tuple (u, v, w) 
        - u - source vertex
        - v - destination vertex
        - w - weight of edge (1 <= w <= 10)

If a vertex is unreachable from source vertex, unreachable vertex distance value will be -1

task:
    * given a starting vertex, return shortest distance from starting vertex to every vertex in the graph

Output:
    * dictionary
        - key - destination node
        - value - shortest distance from src node to destination node


Steps
    1. create short distances dictionary
        - for each node in graph, initialize its key value pair as node => float('inf')
            - the exception here is the source node is set to be 0 as we are starting here
    2. create adjacency list
        - key = node
        - value = list of tuples (u,w)
            - u is destination node
            - w is weight to go from source node to u node
    3. create a min priority queue of tuples
        - (weight, current_node)
    4. create a visited set of nodes
        why? so that when we end up seeing a node but ends up having a higher cost to travel, we skip it as Dijkstra's is a greedy algorithm as its aim is to minimize the total cost to travel from one point to the next
    5. add starting node (0, src_node) to min priority queue

    loop:
        while min priority queue count > 0
            - remove first item from min priority queue
            - first item contains current node and total weight to reach current node named total_weight
            if current node is in visited
                continue
            - add current node to visited

            for each neighboring node of the current node
                - neighbor, weight = adjList[currNode]
                - total_weight to reach neighboring node = total_weight + weight
                if total weight to reach neighboring node < distances dictionary[neighboring node]
                    add neighboring node to min priority queue
                    distances dictionary[neighboring node] = total_weight to reach neighboring node

    return distances dictionary 
        
'''


class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # key = node
        # value = shortest distance to node
        shortestDistances = {}
        adjList = {}
        prioQueue = []
        visited = set()

        for i in range(n):
            shortestDistances[i] = float('inf')
            adjList[i] = []
        
        # distance to self is 0
        shortestDistances[src] = 0

        for edge in edges:
            e1, e2, weight = edge
            if e1 not in adjList:
                adjList[e1] = []
            adjList[e1].append((e2, weight))

        # add starting node to min priority queue to start the algorithm loop
        starting_node = (0, src)
        heapq.heappush(prioQueue, starting_node)

        # print(f'shortest distances: {shortestDistances}')
        # print(f'adjList: {adjList}')

        while len(prioQueue) > 0:
            cost_to_reach_node, node = heapq.heappop(prioQueue)
            if node in visited:
                continue
            
            visited.add(node)

            for neighbor_node in adjList[node]:
                neighbor, weight = neighbor_node
                total_cost = cost_to_reach_node + weight
                if total_cost < shortestDistances[neighbor]:
                    heapq.heappush(prioQueue, (total_cost, neighbor))
                    shortestDistances[neighbor] = total_cost

        for i in range(n):
            if shortestDistances[i] == float('inf'):
                shortestDistances[i] = -1

        return shortestDistances


