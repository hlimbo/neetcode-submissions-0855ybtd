'''
Union Find
- Find function(a: cellPosition) -> (int, int)
    - returns the root node of the given cell
- merge function(a: cellPosition, b: cellPosition) -> bool
    - returns true if 2 cells can be combined together to form a bigger island
    - returns false if 2 cells cannot be connected or already connected

'''

WATER = 0
LAND = 1

class UnionFind:
    def __init__(self, rowLength: int, colLength: int, grid: List[List[int]]):
        # initialize each cell to be a parent of itself
        self.parent = [[(row, col) for col in range(colLength)] for row in range(rowLength)]
        # initialize each cell to be value 1 if it is a land; otherwise 0 if its water
        self.ranks = [[0 if grid[row][col] == WATER else 1 for col in range(colLength)] for row in range(rowLength)]

    # returns root cell
    def find(self, landCell: (int, int)) -> (int, int):
        root = landCell
        while root != self.parent[root[0]][root[1]]:
            root = self.parent[root[0]][root[1]]

        return root

    def merge(self, landCellA: (int, int), landCellB: (int, int)) -> int:
        rootA = self.find(landCellA)
        rootB = self.find(landCellB)

        # already connected
        if rootA == rootB:
            return self.ranks[rootA[0]][rootA[1]]

        # use rank as rank represents the number of lands connected in an island to determine
        # which set of lands should be merged with (e.g. should it merge with landCellA or landCellB?)
        mergedSize = 0
        if self.ranks[rootA[0]][rootA[1]] > self.ranks[rootB[0]][rootB[1]]:
            self.parent[rootB[0]][rootB[1]] = rootA
            self.ranks[rootA[0]][rootA[1]] += self.ranks[rootB[0]][rootB[1]]
            mergedSize = self.ranks[rootA[0]][rootA[1]]
        else:
            self.parent[rootA[0]][rootA[1]] = rootB
            self.ranks[rootB[0]][rootB[1]] += self.ranks[rootA[0]][rootA[1]]
            mergedSize = self.ranks[rootB[0]][rootB[1]]

        return mergedSize

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rowLength = len(grid)
        colLength = len(grid[0])
        unionFind = UnionFind(rowLength, colLength, grid)

        maxArea = 0
        lands = []
        for row in range(rowLength):
            for col in range(colLength):
                if grid[row][col] == LAND:
                    lands.append((row, col))
                    maxArea = 1

        directions = [
            (0,1),
            (0,-1),
            (1, 0),
            (-1, 0)
        ]

        uniqueLandEdges = set()
        for land in lands:
            possibleNeighbors = [(land[0] + direction[0], land[1] + direction[1]) for direction in directions]
            for possibleNeighbor in possibleNeighbors:
                isInBoundsAndLand = possibleNeighbor[0] >= 0 and possibleNeighbor[1] >= 0 and possibleNeighbor[0] < rowLength and possibleNeighbor[1] < colLength and grid[possibleNeighbor[0]][possibleNeighbor[1]] == LAND
                if not isInBoundsAndLand:
                    continue

                landEdge1 = (land, possibleNeighbor)
                landEdge2 = (possibleNeighbor, land)
                if landEdge1 not in uniqueLandEdges and landEdge2 not in uniqueLandEdges:
                    uniqueLandEdges.add(landEdge1)
        
        print("unique land edges: ", len(uniqueLandEdges))
        for landEdge1, landEdge2 in uniqueLandEdges:
            currSize = unionFind.merge(landEdge1, landEdge2)
            maxArea = max(maxArea, currSize)

        return maxArea