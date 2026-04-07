'''
Constraints:
* can form a path for a word
    * horizontally OR vertically
* same cell cannot be used more than once

Task:
* return true if word can be found in the 2d grid of characters called board; false otherwise


Boundary condition
* if r >= len(board) or c >= len(board[r]) or r < 0 or c < 0: --> out of bounds stop


High Level Approach:
* for each letter in the grid
    * use DFS to scan for a potential word match
        * DFS implementation 
            if char from word does not match char on current grid state:
                return false --> path yields a dead-end
            
            --> if any of these decisions below results in a match, return true
            1 move left
            2 move right
            3 move down
            4 move up
        base case:
            if number of matching characters matches length of word to be looked for return true

Time Complexity O(N * M * L^4)
* N = number of rows
* M = number of cols
* L = number of characters in word
* 4 = number of choices to move towards when scanning for letters that match the word

A B C E
S F E S
A D E E

ABCESEEEFS


'''

class Solution:
    def dfsHelper(self, board: List[List[str]], word: str, r: int, c: int, wordIndex: int , visitedIndices: set) -> bool:
        # base case: match found
        if wordIndex == len(word):
            return True

        # out of bounds
        isOutOfBounds = r >= len(board) or c >= len(board[r]) or r < 0 or c < 0
        if isOutOfBounds:
            return False

        # character for this particular path did not match
        if word[wordIndex] != board[r][c]:
            return False 

        # if revisiting a character on board, skip it
        if (r,c) in visitedIndices:
            return False
        
        visitedIndices.add((r,c))

        # scan through 4 different possibilities... if one of them results in a match, return True
        isFoundScanningLeft = self.dfsHelper(board, word, r, c-1, wordIndex+1, visitedIndices)

        # backtrack
        if not isFoundScanningLeft and (r,c-1) in visitedIndices:
            visitedIndices.remove((r,c-1))

        isFoundScanningRight = self.dfsHelper(board, word, r, c+1, wordIndex+1, visitedIndices)
        
        if not isFoundScanningRight and (r,c+1) in visitedIndices:
            visitedIndices.remove((r,c+1))

        isFoundScanningTop = self.dfsHelper(board, word, r-1, c, wordIndex+1, visitedIndices)
        
        if not isFoundScanningTop and (r-1,c) in visitedIndices:
            visitedIndices.remove((r-1,c))

        isFoundScanningBottom = self.dfsHelper(board, word, r+1, c, wordIndex+1, visitedIndices)

        if not isFoundScanningBottom and (r+1,c) in visitedIndices:
            visitedIndices.remove((r+1,c))

        return isFoundScanningLeft or isFoundScanningRight or isFoundScanningTop or isFoundScanningBottom


    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(word) > len(board) * len(board[0]):
            return False

        for r in range(len(board)):
            for c in range(len(board[r])):
                visitedIndices = set()
                if self.dfsHelper(board, word, r, c, 0, visitedIndices):
                    return True
        
        return False
        