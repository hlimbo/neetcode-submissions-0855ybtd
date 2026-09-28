'''
Task:
* given a weighted directed graph and a started vertex, return shortest distance from starting vertex to every vertex in graph

Inputs:
- n = number of vertices in graph where 2 <= n <= 100
- edges = list of tuples where each tuple = (u, v, w)
    - u = source vertex
    - v = destination vertex
    - w = edge weight (1 <= w <= 10)
- src - src vertex from which to start the algorithm (0 <= src < n)

Output:
* dictionary
    - key = destination node
    - value = shortest distance cost to reach destination node

Ingredients
- min-heap -> from collections import heapq
    - used to decide which node to process next
- set 
    - used to determine which nodes are already processed so we don't process the same node if it is added as a direct neighbor from a previous step
- dictionary - keep track of the destination node keys and the shortest distances to reach them as values

Pseudocode:
    - initialize  dictionary named distanceMap
        - for each node in nodes
            - set its distance to float('inf') to mark that we haven't processed nodes yet
    - iterate through list of edges to find the src node
        - if not found in the edges list, return -1 as it would not be possible to find all shortest distances from src if it does not exist in the graph
    - create dictionary named edgeMap
        - outer key = source node
        - inner key = dest node
        - value = edge weight cost
    - create dictionary named neighborMap
        - key = node
        - value = list of nodes directly connected to key node
    - store source node in min heap pq
        - tuple (distance cost to reach dest node from source node, source node, dest node)
        - for this case distance cost to reach source will be 0 because this is where we start
    
    - while min heap pq length > 0
        - distance_cost, i_node, dest_node = remove node from min heap with lowest distance cost
        if visitedSet has dest_node
            skip
        
        visitedSet add dest_node

        for neighbor_node in neighborMap[dest_node]:
            -- incorrect -- this should be distanceMap[neighbor_node] and be appended to min heap AFTER total_distance check is done...
            add (edgeMap[dest_node][neighbor_node], dest_node, neighbor_node) to min heap

            total_distance = distance_cost + edgeMap[dest_node][neighbor_node]
            if total_distance < distanceMap[neighbor_node]:
                distanceMap[neighbor_node] = total_distance

dry run

distanceMap
    0: inf
    1: inf
    2: inf
    3: inf
    4: inf

edgeMap:
    0-0: 0 (special case: starting node)
    0-1: 10
    0-2: 3
    2-1: 4
    1-1: 0
    1-3: 2
    2-2: 0
    2-1: 4
    2-3: 8
    2-4: 2
    3-3: 0
    3-4: 5
    4-4: 0

neighborMap:
    0: [0,1,2]
    1: [1,3]
    2: [1,2,3,4]
    3: [3,4]
    4: [4]

visitedSet:
    0


(0, 0, 0)

'''
import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        distanceMap = {}
        # adjMap - key = node, value list of tuples where each tuple (dest_node, weight)
        adjMap = {}
        visitedSet = set()
        minHeap = []

        for node in range(n):
            distanceMap[node] = float('inf')

        distanceMap[src] = 0
        
        # create edge map and neighbor map
        for edge in edges:
            src_node = edge[0]
            dst_node = edge[1]
            weight = edge[2]

            if src_node not in adjMap:
                adjMap[src_node] = []
            adjMap[src_node].append((dst_node, weight))

        for node in range(n):
            if node not in adjMap:
                adjMap[node] = []

        # cost, src node, dest node
        starting_node = (0, src, src)
        heapq.heappush(minHeap, starting_node)

        print("starting_node: ", starting_node)
        print(adjMap)

        while len(minHeap) > 0:
            distance_cost, inter_node, dst_node = heapq.heappop(minHeap)
            if dst_node in visitedSet:
                continue

            visitedSet.add(dst_node)

            # check neighbors
            for neighbor, edge_cost in adjMap[dst_node]:
                cost_to_reach_neighbor = distance_cost + edge_cost

                if cost_to_reach_neighbor < distanceMap[neighbor]:
                    distanceMap[neighbor] = cost_to_reach_neighbor
                    heapq.heappush(minHeap, (distanceMap[neighbor], dst_node, neighbor))

        for node in distanceMap:
            # unreachable node set to distance -1
            if distanceMap[node] == float('inf'):
                distanceMap[node] = -1

        return distanceMap


