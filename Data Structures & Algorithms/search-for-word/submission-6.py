'''
Inputs
* 2d word search grid
* word as string to find

Output
* return true if word is found
* return false otherwise

* A word can be formed if the path follows a horizontally or vertically neighboring cells
* No diagonals
* can't use the same cell more than once to form the word

Test Cases
* edge cases
    * if the length of the word is bigger than the size of the grid, the word cannot be found
    * if searching leads to a dead-end before the word is found, then that path yields false
    * word to be found can form a spiral
        GRID
        a t s i r
        e r c d t
        i y a r s
        x x r d i
        WORD TO FIND = cardistry

Brainstorming
* scan through each character on the grid row by row / col by col
    * if first letter from the word matches what is scene in grid[row][col]
        * start dfs procedure

DFS PROCEDURE
    * STATE
        - word_match_index
        - grid row and col indices
        - visited letters set
        - grid
        - word
    * OUTPUT
        * TRUE - if all letters matched the word found
        * FALSE - if a letter earlier in the DFS doesn't match
    * RECURSIVE STATE
        * try for left, right, top, down neighbors
    * BASE CASE
        * if row, col indices are out of bounds
            => return false
        * if current letter index of word does not match current character on grid
            => return false
        * if last letter index of word matches current character on grid
            => return true
    * BACKTRACK
        - in the event one of the false base cases are met
            - backtrack is applied by removing the last letter that was visited
            - why? b/c we want to reconsider that letter for another DFS path

* ANOTHER WAY I CAN DO THIS IS MAYBE USE UNION FIND?
    * build a list of directly connected edges (treat it like a directed graph)
    * start from the first letter and last letter and see if an indirect connection can
    be made by finding letters in between
    * example: cardistry
        * start with c
        * end with y
        * see if there is a path that exists that uses a,r,d,i,s,t,r in that order!

'''


class Solution:
    def dfs(self, board: List[List[str]], word: str, row: int, col: int, wordIndex: int, visitedCoords: set) -> bool:
        rowCount = len(board)
        colCount = len(board[0])
        
        # print("rowCount and colCount: ", (rowCount, colCount))

        isOutOfBounds = row >= rowCount or col >= colCount or row < 0 or col < 0
        if isOutOfBounds:
            return False
            
        # print("at ", (row, col))
        currChar = board[row][col]
        #print("curr char: ", currChar)
        if currChar != word[wordIndex]:
            # print("did not match: ", currChar, "!=", word[wordIndex])
            # print("row, col coord: ", (row, col))
            # print("word index: ", wordIndex)
            return False

        coord = (row, col)
        if coord in visitedCoords:
            # print("already visited: ", coord)
            return False
        if wordIndex == len(word) - 1 and word[wordIndex] == currChar:
            return True

        visitedCoords.add((row, col))
        isWordFound = self.dfs(board, word, row+1, col, wordIndex+1, visitedCoords) or self.dfs(board, word, row-1, col, wordIndex+1, visitedCoords) or self.dfs(board, word, row, col-1, wordIndex+1, visitedCoords) or self.dfs(board, word, row, col+1, wordIndex+1, visitedCoords)
        
        # backtrack in the event word is not found to reconsider the current letter on grid
        # as part of the solution
        if not isWordFound:
            visitedCoords.remove((row, col))

        return isWordFound

    def exist(self, board: List[List[str]], word: str) -> bool:
        assert len(board) > 0 and len(board[0]) > 0 and len(board[0][0]) > 0
        
        # print ("number of columns in 1 row: ", len(board[0][0]))
        rowCount = len(board)
        colCount = len(board[0])
        # print("row and col count: ", (rowCount, colCount))
        for row in range(rowCount):
            for col in range(colCount):
                visitedCoords = set()
                # print("starting with: ", (row, col))
                isWordFound = self.dfs(board, word, row, col, 0, visitedCoords)
                if isWordFound:
                    return True
        
        return False