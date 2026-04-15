'''
Applying Union Find to this problem


When to use it?
* counting the number of disjoint sets in a graph (e.g. counting the number of forests in a graph)
* match 3 game, count the number of nodes that are touching each other which share the same color
    * if there is a case where 2 or more nodes match in color in 2 separate areas, then both should be computed at the same time

Textbook Union Find
1. You have a parents array where parent[child_index] = parent_value
    - this is read as the child of parent IS EQUAL TO parent_value
2. You have a ranks array where ranks[node_index] = number_of_nodes_connected_with_each_other
    - e.g. ranks[3] = 5 (5 nodes are connected to node 3)

Union Find has 2 functions
1. find(x) -> returns some representation of the set to which x belongs
2. union(x,y) -> merge the sets containing x and y


To apply it to this problem, we know we use a 2d array but text book union find uses 1d array...
Data Structure Design:

initialize parent 2d array as:
* parent = new int[row_count][col_count]
for row in rows:
    for col in cols:
        // node in row, col parent is itself
        parent[row][col] = (row, col)

count the number of nodes connected in graph
* ranks = new int[row_count][col_count]
for row in rows:
    for col in cols:
        // count itself as 1 -- base case
        ranks[row][col] = 1


'''

LAND = "1"
WATER = "0"

class UnionFind:
    def __init__(self, row_count: int, col_count: int, grid: List[List[str]]):
        # initialize all nodes to be parents to themselves
        self.parent = [[(r,c) for c in range(col_count)] for r in range(row_count)]
        # set size of all nodes that are lands to be 1
        self.ranks = [[1 if grid[r][c] == LAND else 0 for c in range(col_count)] for r in range(row_count)]

    # returns root node
    def find(self, row: int, col: int) -> (int, int):
        root = (row, col)
        while self.parent[root[0]][root[1]] != root:
            root = self.parent[root[0]][root[1]]
        
        return root

    # returns True if can merge landCell1 and landCell2 together
    # otherwise it returns False
    def union(self, landCell1: (int, int), landCell2: (int, int)) -> bool:
        rootLandCell1 = self.find(landCell1[0], landCell1[1])
        rootLandCell2 = self.find(landCell2[0], landCell2[1])

        # the 2 land cells are already connected with one another
        if rootLandCell1 == rootLandCell2:
            return False

        # add smaller tree to the bigger tree to minimize the tree height (tries to keep the tree as balanced as possible)
        if self.ranks[rootLandCell2[0]][rootLandCell2[1]] > self.ranks[rootLandCell1[0]][rootLandCell1[1]]:
            self.parent[rootLandCell1[0]][rootLandCell1[1]] = rootLandCell2
            self.ranks[rootLandCell2[0]][rootLandCell2[1]] += self.ranks[rootLandCell1[0]][rootLandCell1[1]]
        else:
            self.parent[rootLandCell2[0]][rootLandCell2[1]] = rootLandCell1
            self.ranks[rootLandCell1[0]][rootLandCell1[1]] += self.ranks[rootLandCell2[0]][rootLandCell2[1]]

        return True

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rowCount = len(grid)
        colCount = len(grid[0])

        # assume number of islands is the number of 1s found in the grid at the beginning
        islandsCount = 0
        landPositions = []
        for row in range(rowCount):
            for col in range(colCount):
                if grid[row][col] == LAND:
                    landPositions.append((row, col))
                    islandsCount += 1

        #print("Initial Islands count: ", islandsCount)
        unionIslandFinder = UnionFind(rowCount, colCount, grid)

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        
        # build unique land edges
        # insight: check if the current land cell is surrounded by any land cells
        # also account for water cells or out of bounds adjacent areas
        uniqueEdges = set()
        #print("land positions: ", landPositions)
        for landPosition in landPositions:
            neighbors = []
            for direction in directions:
                possibleNeighbor = (landPosition[0] + direction[0], landPosition[1] + direction[1])
                
                # skip the union if not land or out of bounds
                isOutOfBounds = possibleNeighbor[0] >= rowCount or possibleNeighbor[1] >= colCount or possibleNeighbor[0] < 0 or possibleNeighbor[1] < 0
                if isOutOfBounds or grid[possibleNeighbor[0]][possibleNeighbor[1]] == WATER:
                    continue
                
                neighbors.append(possibleNeighbor)
            
            for neighbor in neighbors:
                potentialEdge1 = (landPosition, neighbor)
                potentialEdge2 = (neighbor, landPosition)
                if potentialEdge1 in uniqueEdges or potentialEdge2 in uniqueEdges:
                    continue
                
                uniqueEdges.add(potentialEdge1)

        for landPosition1, landPosition2 in uniqueEdges:
            areLandsConnected = unionIslandFinder.union(landPosition1, landPosition2)
            if areLandsConnected:
                islandsCount = max(1, islandsCount - 1)
        
        return islandsCount