'''
Legend
* L = land = INF (passable)
* W = water = -1 (cannot pass through)
* C = chest = 0 (target)

Contraints
- grid can be traversed up, down, left, or right
- can only modify the grid in-place

Task
- fill each land cell with distance to its nearest treasure chest (give it a number)
    - if land cell cannot reach a treasure chest, then the value should remain INF


Brainstorming
* locate all the positions in the grid of where the treasure chests are
* start where the chests are and backtrack in the 4 cardinal directions to obtain the value
    * BFS starting backwards from where all the chests are located and incrementing the number by 1
        from chest location to its adjacent location
            if the current distance > chest location + cost to get to current position
                current distance = chest location + cost to get to current position
    * keep track of which cells you visited per treasure to ensure you don't visit the same treasure more than once

                      1
             L   -1   C  -1
                  L   1   L
'''

from queue import Queue

LAND = 2147483647
WATER = -1
CHEST = 0

class Solution:
    def backtrackFromTreasures(self, grid: List[List[int]], treasureLocations: List[(int, int)]) -> None:
        bfsQueue = deque()
        visited = set()
        
        for treasureLocation in treasureLocations:
            bfsQueue.append(treasureLocation)

        directions = [
            (0,1),   # right
            (0,-1),  # left
            (1,0),   # bottom
            (-1, 0), # top
        ]


        while len(bfsQueue) > 0:
            r,c = bfsQueue.popleft()
            visited.add((r,c))
            distance = grid[r][c]

            for direction in directions:
                newRow, newCol = r + direction[0], c + direction[1]
                isOutOfBounds = newRow >= len(grid) or newCol >= len(grid[newRow]) or newRow < 0 or newCol < 0
                if isOutOfBounds:
                    continue
                
                if grid[newRow][newCol] == WATER:
                    continue

                grid[newRow][newCol] = min(1 + distance, grid[newRow][newCol])

                newPosition = (newRow, newCol)
                if newPosition not in visited:
                    bfsQueue.append(newPosition)


    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        treasureLocations = []
        # find treasure locations
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == CHEST:
                    treasureLocations.append((r,c))

        self.backtrackFromTreasures(grid, treasureLocations)

