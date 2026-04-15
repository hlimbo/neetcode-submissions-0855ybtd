'''
Knowns
* 1 = land
* 0 = water

An island is a set of 1s uniquely identifiable by their position (row, col)
* 1s must be connected to one another
* if there is one or more 1 in between two 1's, then those 1's are indirectly connected
* a land can be connected to another land horizontally or vertically


Questions
1. can 2 lands be connected diagonally

0  1  0
0  0  1

^ 2 islands because the north 1 is diagonally away from the southeast 1


High Level Approaches
1. BFS
2. Disjoint Set or Union Find
    - give each land a rank
    - parent, child array structure where a[child] = parent (read as child has a parent set to parent)


Deep Dive: BFS
* total island count = 0
* for each row
    * for each col
        * if grid[row][col] == land
            - if (row, col) is in global visited set --> go to next row,col combination
            - otherwise:
                - run bfs algorithm to find all lands connected to what was matched
                - add lands from local visited set to global visited set
                - increase total island count by 1

BFS Algorithm
    - add land to deque
    - while deque has 1 or more lands in them
        - remove land from deque
        - add land to visited set
        - visit north, south, east, west adjacent spots of land
            - filter out adjacent spots that are out of bounds
            - filter out adjacent spots that are water spots
            - filter out adjacent spots that were already marked as visited
    
    - check if local visited > 0 ==> return 1 as we found a new island
    - if local visited == 0 ==> return 0 as we found no new island
    - return a tuple containing set of visited land locations and a number that 
    - represents if we found a new island or not


'''

LAND = "1"
WATER = "0"

class Solution:
    def bfs(self, r: int, c: int, grid: List[List[str]]) -> (set, int):
        localSet = set()
        islandsVisited = 0
        cellDeque = deque()
        cellDeque.append((r,c))

        dirs = [
            (0, -1),
            (0, 1),
            (1, 0),
            (-1, 0)
        ]

        while len(cellDeque) > 0:
            row, col = cellDeque.popleft()
            localSet.add((row, col))

            for direction in dirs:
                adjCell = (row + direction[0], col + direction[1])
                isOutOfBounds = adjCell[0] >= len(grid) or adjCell[0] < 0 or adjCell[1] >= len(grid[0]) or adjCell[1] < 0
                if isOutOfBounds or grid[adjCell[0]][adjCell[1]] == WATER or adjCell in localSet:
                    continue

                cellDeque.append(adjCell)



        if len(localSet) > 0:
            islandsVisited = 1

        return (localSet, islandsVisited)

    def numIslands(self, grid: List[List[str]]) -> int:
        totalIslandCount = 0
        globalVisitedSet = set()

        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == LAND and (r,c) not in globalVisitedSet:
                    localSet, islandsVisited = self.bfs(r, c, grid)

                    for position in localSet:
                        globalVisitedSet.add(position)

                    totalIslandCount += islandsVisited

        return totalIslandCount
        